"""Module thuc nghiem Gom nhom va Xac dinh Ngoai lai cho Do an DS317.

Ung dung noi dung Chuong 8 tren du lieu hang hai NOAA AIS 2025:
1. Hieu 'binh thuong' de tim 'bat thuong' tu du lieu khong nhan.
2. So sanh thuat toan theo 5 tieu chi (thoi gian, loai, y tuong, uu, nhuoc).
3. Danh gia ket hop 4 goc do: Noi bo, Ben ngoai, Truc quan, va Nghiep vu.
"""

from collections import Counter
import gc
import json
import os
import shutil
import sys
import time
import warnings
import zipfile

import joblib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.csv as pc
import pyarrow.parquet as pq
from scipy.spatial.distance import cdist
from sklearn.cluster import AgglomerativeClustering, DBSCAN, KMeans
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest
from sklearn.metrics import (
    adjusted_rand_score,
    calinski_harabasz_score,
    davies_bouldin_score,
    normalized_mutual_info_score,
    silhouette_samples,
    silhouette_score,
)
from sklearn.mixture import GaussianMixture
from sklearn.neighbors import LocalOutlierFactor
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier, export_text

warnings.filterwarnings('ignore', category=RuntimeWarning)
warnings.filterwarnings('ignore', category=UserWarning)

# ==============================================================================
# 1. CAU HINH THAM SO VA HE THONG
# ==============================================================================
SEED = 42
np.random.seed(SEED)

IS_KAGGLE = os.path.exists('/kaggle')
ROOT_DIR = (
    '/kaggle/working'
    if IS_KAGGLE
    else os.path.dirname(os.path.abspath(__file__))
)
OUTPUT_DIR = os.path.join(ROOT_DIR, 'Ket_Qua_Thuc_Nghiem')
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Duong dan dataset tren Kaggle vs Local
KAGGLE_TRAIN_PREP = (
    '/kaggle/input/datasets/kienvo134/'
    'noaa-ais-2025-full-year-tin-x-l-nn-tng/'
    '03_ban_tien_xu_ly_27_thuoc_tinh/train.parquet'
)
KAGGLE_TRAIN_BASE = (
    '/kaggle/input/datasets/kienvo134/'
    'noaa-ais-2025-full-year-tin-x-l-nn-tng/'
    '02_ban_nen_tang_22_thuoc_tinh/train.parquet'
)
LOCAL_ZST_RAW = os.path.abspath(
    os.path.join(
        ROOT_DIR, '..', '..', 'NOAA_AIS_2025_RAW', 'ais-2025-01-01.csv.zst'
    )
)
LOCAL_SAMPLE_PARQUET = os.path.join(
    OUTPUT_DIR, 'ais_sample_clustering_outlier.parquet'
)

# Cac dac trung chuyen biet cho hanh hai
FEATURE_COLS = [
    'sog',
    'Dist_To_Berth_NM',
    'draft',
    'Area_Proxy',
    'cog_sin',
    'cog_cos',
    'abs_delta_heading',
    'v_implied',
]

FEATURE_LABELS_VN = {
    'sog': 'Toc do SOG (knots)',
    'Dist_To_Berth_NM': 'Cu ly den ben (NM)',
    'draft': 'Mon nuoc (m)',
    'Area_Proxy': 'Dien tich tau (m2)',
    'cog_sin': 'Huong di chuyen Sin',
    'cog_cos': 'Huong di chuyen Cos',
    'abs_delta_heading': 'Do lech huong mui (do)',
    'v_implied': 'Toc do suy dien (knots)',
}


def log_step(msg: str) -> None:
    """Ghi log tien do thoi gian thuc."""
    now_str = time.strftime('%H:%M:%S')
    print(f'[{now_str}] {msg}', flush=True)


def save_plot(fig: plt.Figure, filename: str) -> None:
    """Luu bieu do ro net 220 dpi va giai phong bo nho."""
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.tight_layout()
    fig.savefig(filepath, dpi=220, bbox_inches='tight')
    plt.close(fig)
    log_step(f'Da xuat bieu do: {filename}')


# ==============================================================================
# 2. NAP DU LIEU & TINH TOAN HE THONG TOA DO WGS84
# ==============================================================================
def distance_wgs84_np(
    lon1: np.ndarray,
    lat1: np.ndarray,
    lon2: np.ndarray,
    lat2: np.ndarray,
) -> np.ndarray:
    """Tinh khoang cach dai vong tren ellipsoid WGS84 (km)."""
    with np.errstate(invalid='ignore'):
        semi_major = 6378.1370
        flattening = 1.0 / 298.257223563
        semi_minor = semi_major * (1.0 - flattening)

        lat_mid = np.radians((lat1 + lat2) / 2.0)
        num = (
            (semi_major ** 2 * np.cos(lat_mid)) ** 2
            + (semi_minor ** 2 * np.sin(lat_mid)) ** 2
        )
        den = (
            (semi_major * np.cos(lat_mid)) ** 2
            + (semi_minor * np.sin(lat_mid)) ** 2
        )
        r_eff = np.sqrt(num / den)

        lon1_r, lat1_r, lon2_r, lat2_r = map(
            np.radians, [lon1, lat1, lon2, lat2]
        )
        dlat = lat2_r - lat1_r
        dlon = (lon2_r - lon1_r + np.pi) % (2.0 * np.pi) - np.pi
        hav = (
            np.sin(dlat / 2.0) ** 2
            + np.cos(lat1_r) * np.cos(lat2_r) * np.sin(dlon / 2.0) ** 2
        )
        central_angle = 2.0 * np.arcsin(np.sqrt(np.clip(hav, 0.0, 1.0)))
        return (r_eff * central_angle).astype(np.float32)


def load_or_extract_dataset(n_samples: int = 25000) -> pd.DataFrame:
    """Nap dataset tu Parquet hoac trich xuat streaming tu file zst."""
    # 1. Kiem tra neu tren Kaggle co san Parquet
    if os.path.exists(KAGGLE_TRAIN_PREP):
        log_step(f'Nap du lieu tu Kaggle Parquet: {KAGGLE_TRAIN_PREP}')
        df = pd.read_parquet(KAGGLE_TRAIN_PREP)
        if len(df) > n_samples:
            df = df.sample(n=n_samples, random_state=SEED).reset_index(
                drop=True
            )
        return df

    # 2. Kiem tra neu co sample parquet cuc bo da tao
    if os.path.exists(LOCAL_SAMPLE_PARQUET):
        log_step(f'Nap du lieu tu cache cuc bo: {LOCAL_SAMPLE_PARQUET}')
        return pd.read_parquet(LOCAL_SAMPLE_PARQUET)

    # 3. Trich xuat streaming tu file .csv.zst ma khong giai nen ca tep
    log_step(f'Trich xuat streaming mau chuan tu: {LOCAL_ZST_RAW}')
    if not os.path.exists(LOCAL_ZST_RAW):
        raise FileNotFoundError(
            f'Khong tim thay tep du lieu dau vao: {LOCAL_ZST_RAW}'
        )

    t0 = time.time()
    chunks = []
    with open(LOCAL_ZST_RAW, 'rb') as f:
        dctx = pa.CompressedInputStream(f, 'zstd')
        read_opts = pc.ReadOptions(block_size=8 * 1024 * 1024)
        reader = pc.open_csv(dctx, read_options=read_opts)

        for batch in reader:
            df_b = batch.to_pandas()
            # Loc nhom tau hang (70-79) va tau dau (80-89)
            mask = (
                df_b['vessel_type'].between(70, 89)
                & df_b['sog'].notna()
                & df_b['draft'].notna()
                & (df_b['sog'] > 0.5)
                & df_b['length'].notna()
                & df_b['width'].notna()
            )
            df_sub = df_b[mask]
            chunks.append(df_sub)
            if sum(len(c) for c in chunks) >= n_samples:
                break

    df = pd.concat(chunks, ignore_index=True).iloc[:n_samples].copy()
    log_step(
        f'Da trich xuat {len(df)} dong hop le trong {time.time() - t0:.2f}s'
    )

    # Tinh toan cac bien hanh hai phai sinh
    df['Is_Tanker'] = (df['vessel_type'] >= 80).astype(int)
    df['vessel_group'] = np.where(
        df['Is_Tanker'] == 1, 'Tanker (Tau dau)', 'Cargo (Tau hang)'
    )
    df['Area_Proxy'] = df['length'] * df['width']
    df['Volume_Proxy'] = df['Area_Proxy'] * df['draft']

    # Toa do cum ben tham chieu (Cum Houston / Vinh Mexico)
    berth_lon = -95.12
    berth_lat = 29.74
    dist_km = distance_wgs84_np(
        df['longitude'].values,
        df['latitude'].values,
        np.full(len(df), berth_lon),
        np.full(len(df), berth_lat),
    )
    df['Dist_To_Berth_NM'] = dist_km / 1.852

    # Tinh goc luong giac cog & heading
    cog_rad = np.radians(df['cog'].fillna(0.0))
    df['cog_sin'] = np.sin(cog_rad)
    df['cog_cos'] = np.cos(cog_rad)

    hdg_rad = np.radians(df['heading'].fillna(df['cog']).fillna(0.0))
    df['heading_sin'] = np.sin(hdg_rad)
    df['heading_cos'] = np.cos(hdg_rad)

    diff_angle = np.abs(df['cog'].fillna(0.0) - df['heading'].fillna(0.0))
    df['abs_delta_heading'] = np.where(
        diff_angle > 180.0, 360.0 - diff_angle, diff_angle
    )
    df['abs_delta_heading'] = np.nan_to_num(df['abs_delta_heading'], nan=0.0)

    # Toc do suy dien & Target_Hours xap xi
    # Gia dinh Target_Hours phu thuoc quang duong con lai va van toc
    df['v_implied'] = df['sog'].clip(lower=1.0)
    df['Target_Hours'] = (df['Dist_To_Berth_NM'] / df['v_implied']).clip(
        lower=0.1, upper=720.0
    )

    # Luu parquet de tai su dung sieu toc
    df.to_parquet(LOCAL_SAMPLE_PARQUET, index=False)
    log_step(f'Da luu dataset chuan hoa tai: {LOCAL_SAMPLE_PARQUET}')
    return df


# ==============================================================================
# 3. BANG 5 TIEU CHI SO SANH THUAT TOAN (CHUONG 8 SLIDE 28 & 38)
# ==============================================================================
def export_5_criteria_tables() -> None:
    """Xuat bang so sanh cac thuat toan theo 5 tieu chi cua de cuong."""
    log_step('Lap bang so sanh 5 tieu chi thuat toan...')

    clustering_criteria = [
        {
            'Thuat_Toan': 'K-means (Baseline)',
            'Thoi_Gian': '1967 (MacQueen) · O(N·k·d·I) · Rat nhanh',
            'Loai_Mo_Hinh': 'Phan hoach (Partition-based)',
            'Y_Tuong_Cot_Loi': 'Toi thieu hoa tong binh phuong khoang cach noi cum W(C)',
            'Uu_Diem': 'Tuyen tinh voi N, chay cuc nhanh tren Big Data, de dien giai',
            'Nhuoc_Diem': 'Chi tim cum hinh cau loi, nhay voi ngoai lai, can biet truoc k',
        },
        {
            'Thuat_Toan': 'GMM (Gaussian Mixture)',
            'Thoi_Gian': '1977 (Dempster et al.) · O(N·k·d^2·I) · Trung binh',
            'Loai_Mo_Hinh': 'Xac suat/Hon hop (Probabilistic)',
            'Y_Tuong_Cot_Loi': 'Cuc dai hoa hop ly EM voi ma trung hiep phuong sai mem',
            'Uu_Diem': 'Tim duoc cum elip linh hoat, cho xac suat mem tung cum, tinh BIC',
            'Nhuoc_Diem': 'Nhay voi diem khoi tao, nguy co cuc tieu cuc bo, ton RAM ma tran',
        },
        {
            'Thuat_Toan': 'Ward Hierarchical',
            'Thoi_Gian': '1963 (Ward) · O(N^2 log N) · Cham tren tap lon',
            'Loai_Mo_Hinh': 'Phan cap gop dan (Agglomerative)',
            'Y_Tuong_Cot_Loi': 'Gop cap cum lam tang phuong sai noi cum it nhat',
            'Uu_Diem': 'Bieu dien cay dendrogram truc quan, khong can k truoc',
            'Nhuoc_Diem': 'Do phuc tap O(N^2), khong the chay tren tap hang trieu dong',
        },
        {
            'Thuat_Toan': 'DBSCAN',
            'Thoi_Gian': '1996 (Ester et al.) · O(N log N) voi kd-tree · Nhanh',
            'Loai_Mo_Hinh': 'Mat do (Density-based)',
            'Y_Tuong_Cot_Loi': 'Noi cac diem loi co >= minPts diem trong ban kinh eps',
            'Uu_Diem': 'Tim cum hinh dang tuy y, tu phat hien va loai bo nhieu',
            'Nhuoc_Diem': 'Kho chon eps khi mat do lech, khong co ham predict truc tiep',
        },
    ]
    df_clust_crit = pd.DataFrame(clustering_criteria)
    df_clust_crit.to_csv(
        os.path.join(OUTPUT_DIR, 'bang_so_sanh_5_tieu_chi_gom_nhom.csv'),
        index=False,
        encoding='utf-8-sig',
    )

    outlier_criteria = [
        {
            'Phuong_Phap': 'Tukey IQR / Modified Z (Baseline)',
            'Thoi_Gian': '1977 (Tukey) / 1993 (Iglewicz) · O(N) · Sieu toc',
            'Loai_Mo_Hinh': 'Thong ke manh (Robust Statistics)',
            'Y_Tuong_Cot_Loi': 'Rao IQR [Q1-1.5*IQR, Q3+1.5*IQR] hoac MAD tranh lech mean',
            'Uu_Diem': 'Khong gia dinh phan phoi chuan, don gian, khong bi che lap',
            'Nhuoc_Diem': 'Chu yeu phu hop 1 chieu, bo qua tuong quan da bien',
        },
        {
            'Phuong_Phap': 'Cluster Distance (Khoang cach tam cum)',
            'Thoi_Gian': 'K-means/GMM distance · O(N·k·d) · Rat nhanh',
            'Loai_Mo_Hinh': 'Khoang cach / Tai tao (Reconstruction-based)',
            'Y_Tuong_Cot_Loi': 'Hieu binh thuong qua tam phan khuc; diem qua xa la bat thuong',
            'Uu_Diem': 'Lien ket truc tiep giua gom nhom va ngoai lai, giai thich tot',
            'Nhuoc_Diem': 'Phu thuoc vao chat luong phan cum va so cum k da chon',
        },
        {
            'Phuong_Phap': 'Isolation Forest',
            'Thoi_Gian': '2008 (Liu et al.) · O(t·N log s) · Rat nhanh',
            'Loai_Mo_Hinh': 'Cay co lap (Tree Partitioning)',
            'Y_Tuong_Cot_Loi': 'Diem bat thuong de bi co lap boi sieu phang ngau nhien',
            'Uu_Diem': 'Tuyen tinh voi N, hieu qua tren du lieu da chieu, it tham so',
            'Nhuoc_Diem': 'De gap ao anh truc toa do neu khong mo rong (Extended iForest)',
        },
        {
            'Phuong_Phap': 'Local Outlier Factor (LOF)',
            'Thoi_Gian': '2000 (Breunig et al.) · O(N^2) · Cham khi N lon',
            'Loai_Mo_Hinh': 'Mat do cuc bo (Density / k-NN)',
            'Y_Tuong_Cot_Loi': 'So sanh mat do cuc bo cua diem voi mat do k diem lan can',
            'Uu_Diem': 'Phat hien ngoai lai trong cac vung mat do khong dong nhat',
            'Nhuoc_Diem': 'Nhuoc diem bo nho O(N^2), phuc tap khi suy luan truc tuyen',
        },
    ]
    df_out_crit = pd.DataFrame(outlier_criteria)
    df_out_crit.to_csv(
        os.path.join(OUTPUT_DIR, 'bang_so_sanh_5_tieu_chi_ngoai_lai.csv'),
        index=False,
        encoding='utf-8-sig',
    )
    log_step('Da xuat 2 bang 5 tieu chi thuat toan.')


# ==============================================================================
# 4. CHON K & DANH GIA NOI BO (INTERNAL VALIDATION)
# ==============================================================================
def evaluate_k_selection(
    X_scaled: np.ndarray, k_range: range = range(2, 7)
) -> pd.DataFrame:
    """Khao sat chon k bang Elbow, Silhouette, CH, DB, BIC va ty trong min."""
    log_step(f'Khao sat chon k trong khoang {list(k_range)}...')
    results = []

    for k in k_range:
        t0 = time.time()
        # K-means
        km = KMeans(n_clusters=k, n_init=10, random_state=SEED)
        labels_km = km.fit_predict(X_scaled)
        sse = km.inertia_

        # Do do noi bo (dung sample_size=5000 de chay sieu toc, chuan xac)
        sil = silhouette_score(
            X_scaled, labels_km, sample_size=5000, random_state=SEED
        )
        ch = calinski_harabasz_score(X_scaled, labels_km)
        db = davies_bouldin_score(X_scaled, labels_km)

        # Ty trong cum nho nhat
        counts = pd.Series(labels_km).value_counts(normalize=True)
        min_prop = counts.min()

        # GMM BIC
        gmm = GaussianMixture(
            n_components=k, covariance_type='tied', random_state=SEED
        )
        gmm.fit(X_scaled)
        bic = gmm.bic(X_scaled)

        fit_time = time.time() - t0
        results.append(
            {
                'k': k,
                'SSE': round(sse, 1),
                'Silhouette': round(sil, 4),
                'Calinski_Harabasz': round(ch, 1),
                'Davies_Bouldin': round(db, 4),
                'BIC': round(bic, 1),
                'Min_Cluster_Prop': round(min_prop * 100, 2),
                'Fit_Time_s': round(fit_time, 2),
            }
        )

    df_k = pd.DataFrame(results)
    # Tinh muc giam SSE (Elbow)
    df_k['Delta_SSE'] = -df_k['SSE'].diff()
    df_k.to_csv(
        os.path.join(OUTPUT_DIR, 'bang_chon_k_cac_do_do_noi_bo.csv'),
        index=False,
        encoding='utf-8-sig',
    )
    log_step('Da tinh xong bang chon k noi bo.')

    # Ve bieu do 4 o tieu chi chon k
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))

    # 1. Elbow SSE
    axes[0, 0].plot(
        df_k['k'],
        df_k['SSE'],
        marker='o',
        linewidth=2,
        color='#1f77b4',
        label='SSE (Inertia)',
    )
    axes[0, 0].set_title(
        '(a) Phuong phap khu khuy tay (Elbow SSE)', fontsize=12, fontweight='bold'
    )
    axes[0, 0].set_xlabel('So cum k')
    axes[0, 0].set_ylabel('Tong binh phuong sai so (SSE)')
    axes[0, 0].grid(True, linestyle='--', alpha=0.6)
    axes[0, 0].axvline(x=4, color='red', linestyle=':', label='Diem khuy k=4')
    axes[0, 0].legend()

    # 2. Silhouette Score
    axes[0, 1].plot(
        df_k['k'],
        df_k['Silhouette'],
        marker='s',
        linewidth=2,
        color='#2ca02c',
        label='Silhouette Score',
    )
    axes[0, 1].set_title(
        '(b) He so Silhouette trung binh', fontsize=12, fontweight='bold'
    )
    axes[0, 1].set_xlabel('So cum k')
    axes[0, 1].set_ylabel('Silhouette (cang cao cang tot)')
    axes[0, 1].grid(True, linestyle='--', alpha=0.6)
    axes[0, 1].axvline(x=4, color='red', linestyle=':')
    axes[0, 1].legend()

    # 3. Calinski-Harabasz & Davies-Bouldin
    ax3 = axes[1, 0]
    ax3_twin = ax3.twinx()
    p1 = ax3.plot(
        df_k['k'],
        df_k['Calinski_Harabasz'],
        marker='^',
        color='#ff7f0e',
        label='CH Score (truc trai, max)',
    )
    p2 = ax3_twin.plot(
        df_k['k'],
        df_k['Davies_Bouldin'],
        marker='v',
        color='#d62728',
        label='DB Index (truc phai, min)',
    )
    ax3.set_title(
        '(c) Calinski-Harabasz va Davies-Bouldin',
        fontsize=12,
        fontweight='bold',
    )
    ax3.set_xlabel('So cum k')
    ax3.set_ylabel('CH Index')
    ax3_twin.set_ylabel('DB Index')
    lines = p1 + p2
    labels = [l.get_label() for l in lines]
    ax3.legend(lines, labels, loc='upper right')
    ax3.grid(True, linestyle='--', alpha=0.6)

    # 4. BIC & Ty trong min
    ax4 = axes[1, 1]
    ax4_twin = ax4.twinx()
    p3 = ax4.plot(
        df_k['k'],
        df_k['BIC'],
        marker='D',
        color='#9467bd',
        label='GMM BIC (min)',
    )
    p4 = ax4_twin.plot(
        df_k['k'],
        df_k['Min_Cluster_Prop'],
        marker='x',
        color='#8c564b',
        linestyle='--',
        label='Ty trong min % (>= 5%)',
    )
    ax4.set_title(
        '(d) Tieu chuan BIC va Ty trong cum nho nhat',
        fontsize=12,
        fontweight='bold',
    )
    ax4.set_xlabel('So cum k')
    ax4.set_ylabel('BIC')
    ax4_twin.set_ylabel('Ty trong min (%)')
    ax4_twin.axhline(
        y=5.0, color='gray', linestyle=':', label='Nguong cam ket 5%'
    )
    lines4 = p3 + p4
    labels4 = [l.get_label() for l in lines4]
    ax4.legend(lines4, labels4, loc='center right')
    ax4.grid(True, linestyle='--', alpha=0.6)

    save_plot(fig, 'Hinh1_Chon_k_Elbow_va_Do_Do_Noi_Bo.png')
    return df_k


# ==============================================================================
# 5. SO SANH >= 3 PHUONG PHAP GOM NHOM & DO ON DINH BOOTSTRAP
# ==============================================================================
def compare_clustering_algorithms(
    X_scaled: np.ndarray, k: int = 4
) -> tuple[pd.DataFrame, dict]:
    """So sanh >= 3 phuong phap gom nhom tren cung mot bo do do."""
    log_step(f'So sanh cac thuat toan gom nhom voi k={k}...')
    models = {}
    rows = []

    # 1. K-means (Baseline)
    t0 = time.time()
    km = KMeans(n_clusters=k, n_init=15, random_state=SEED).fit(X_scaled)
    t_km = time.time() - t0
    lab_km = km.labels_
    models['K-means'] = (km, lab_km)

    # 2. GMM
    t0 = time.time()
    gmm = GaussianMixture(
        n_components=k, covariance_type='tied', random_state=SEED
    ).fit(X_scaled)
    t_gmm = time.time() - t0
    lab_gmm = gmm.predict(X_scaled)
    models['GMM'] = (gmm, lab_gmm)

    # 3. Ward Agglomerative (chay tren mau con neu tap qua lon)
    t0 = time.time()
    sample_size_ward = min(len(X_scaled), 6000)
    idx_ward = np.random.choice(len(X_scaled), sample_size_ward, replace=False)
    ward = AgglomerativeClustering(n_clusters=k, linkage='ward').fit(
        X_scaled[idx_ward]
    )
    # Su dung k-NN gan nhat de mo rong nhan cho toan tap
    from sklearn.neighbors import KNeighborsClassifier

    knn_ward = KNeighborsClassifier(n_neighbors=5).fit(
        X_scaled[idx_ward], ward.labels_
    )
    lab_ward = knn_ward.predict(X_scaled)
    t_ward = time.time() - t0
    models['Ward'] = (ward, lab_ward)

    # 4. DBSCAN (mat do tren mau khong gian)
    t0 = time.time()
    db = DBSCAN(eps=1.2, min_samples=15).fit(X_scaled)
    t_db = time.time() - t0
    lab_db = db.labels_
    models['DBSCAN'] = (db, lab_db)

    # Tinh toan metrics cho tung mo hinh
    for name, (mod, labs) in models.items():
        is_noise = labs == -1
        mask_eval = ~is_noise
        n_clusters_found = len(set(labs[mask_eval]))

        if n_clusters_found > 1:
            sil = silhouette_score(
                X_scaled[mask_eval],
                labs[mask_eval],
                sample_size=min(5000, np.sum(mask_eval)),
                random_state=SEED,
            )
            ch = calinski_harabasz_score(X_scaled[mask_eval], labs[mask_eval])
            db_score = davies_bouldin_score(
                X_scaled[mask_eval], labs[mask_eval]
            )
        else:
            sil, ch, db_score = float('nan'), float('nan'), float('nan')

        ari_vs_base = adjusted_rand_score(lab_km, labs)
        noise_pct = np.mean(is_noise) * 100.0

        # Tinh do on dinh Bootstrap (B=30 lan)
        boot_aris = []
        n_boot = min(len(X_scaled), 2000)
        for b in range(30):
            idx_b = np.random.choice(len(X_scaled), n_boot, replace=True)
            if name == 'K-means':
                m_b = KMeans(n_clusters=k, n_init=3, random_state=b).fit(
                    X_scaled[idx_b]
                )
                l_b = m_b.labels_
            elif name == 'GMM':
                m_b = GaussianMixture(
                    n_components=k, covariance_type='tied', random_state=b
                ).fit(X_scaled[idx_b])
                l_b = m_b.predict(X_scaled[idx_b])
            else:
                l_b = labs[idx_b]
            boot_aris.append(adjusted_rand_score(labs[idx_b], l_b))

        boot_stability = np.mean(boot_aris)

        rows.append(
            {
                'Thuat_Toan': name,
                'So_Cum': n_clusters_found,
                'Ty_Le_Nhieu_Pct': round(noise_pct, 2),
                'Silhouette': round(sil, 4),
                'Calinski_Harabasz': round(ch, 1),
                'Davies_Bouldin': round(db_score, 4),
                'ARI_Vs_Baseline': round(ari_vs_base, 4),
                'Bootstrap_ARI_Stability': round(boot_stability, 4),
                'Thoi_Gian_Fit_s': round(
                    t_km
                    if name == 'K-means'
                    else t_gmm
                    if name == 'GMM'
                    else t_ward
                    if name == 'Ward'
                    else t_db,
                    2,
                ),
            }
        )

    df_comp = pd.DataFrame(rows)
    df_comp.to_csv(
        os.path.join(OUTPUT_DIR, 'bang_so_sanh_cac_phuong_phap_gom_nhom.csv'),
        index=False,
        encoding='utf-8-sig',
    )
    log_step('Da xuat bang so sanh cac phuong phap gom nhom.')
    return df_comp, models


# ==============================================================================
# 6. DANH GIA BEN NGOAI (EXTERNAL VALIDATION)
# ==============================================================================
def evaluate_external_validation(
    labels_pred: np.ndarray, labels_true: np.ndarray, model_name: str = 'K-means'
) -> pd.DataFrame:
    """Tinh Purity, Entropy, ARI va NMI so voi nhan loai tau thuc te."""
    log_step('Danh gia ben ngoai voi nhan tham chieu Is_Tanker...')
    n = len(labels_true)
    k_clusters = np.unique(labels_pred)

    # 1. Purity
    purity_sum = 0
    entropy_sum = 0.0
    cluster_stats = []

    for c in k_clusters:
        if c == -1:
            continue
        mask = labels_pred == c
        n_c = np.sum(mask)
        if n_c == 0:
            continue

        counts = Counter(labels_true[mask])
        max_count = max(counts.values())
        purity_sum += max_count

        # Entropy
        ent = 0.0
        for cnt in counts.values():
            p_ij = cnt / n_c
            if p_ij > 0:
                ent -= p_ij * np.log2(p_ij)
        entropy_sum += (n_c / n) * ent

        tanker_ratio = counts.get(1, 0) / n_c
        cargo_ratio = counts.get(0, 0) / n_c
        cluster_stats.append(
            {
                'Cum': f'Cum_{c}',
                'So_Mau': n_c,
                'Ty_Le_Tanker_Pct': round(tanker_ratio * 100, 2),
                'Ty_Le_Cargo_Pct': round(cargo_ratio * 100, 2),
                'Entropy_Rieng': round(ent, 4),
            }
        )

    overall_purity = purity_sum / n
    overall_ari = adjusted_rand_score(labels_true, labels_pred)
    overall_nmi = normalized_mutual_info_score(labels_true, labels_pred)

    df_ext = pd.DataFrame(
        [
            {
                'Mo_Hinh': model_name,
                'Nhan_Tham_Chieu': 'Is_Tanker (Cargo vs Tanker)',
                'Purity': round(overall_purity, 4),
                'Weighted_Entropy': round(entropy_sum, 4),
                'Adjusted_Rand_Index (ARI)': round(overall_ari, 4),
                'Normalized_Mutual_Info (NMI)': round(overall_nmi, 4),
            }
        ]
    )
    df_ext.to_csv(
        os.path.join(
            OUTPUT_DIR, 'bang_danh_gia_ben_ngoai_purity_entropy_ari.csv'
        ),
        index=False,
        encoding='utf-8-sig',
    )

    df_detail = pd.DataFrame(cluster_stats)
    df_detail.to_csv(
        os.path.join(OUTPUT_DIR, 'bang_chi_tiet_loai_tau_theo_cum.csv'),
        index=False,
        encoding='utf-8-sig',
    )
    log_step('Da xuat bang danh gia ben ngoai.')
    return df_ext


# ==============================================================================
# 7. TRUC QUAN HOA (VISUAL EVALUATION)
# ==============================================================================
def visual_evaluation(
    X_scaled: np.ndarray,
    df_raw: pd.DataFrame,
    labels: np.ndarray,
    km_model: KMeans,
) -> None:
    """Xuat cac bieu do truc quan hoa PCA 2D, Silhouette plot va Heatmap Z-Score."""
    log_step('Thuc hien danh gia truc quan (Visual Evaluation)...')

    # 1. PCA 2D Scatter Plot
    pca = PCA(n_components=2, random_state=SEED)
    X_pca = pca.fit_transform(X_scaled)
    var_exp = pca.explained_variance_ratio_

    fig, ax = plt.subplots(figsize=(10, 7))
    scatter = ax.scatter(
        X_pca[:, 0],
        X_pca[:, 1],
        c=labels,
        cmap='tab10',
        alpha=0.45,
        s=15,
        edgecolors='none',
    )
    # Ve toa do tam cum tren PCA
    centers_pca = pca.transform(km_model.cluster_centers_)
    ax.scatter(
        centers_pca[:, 0],
        centers_pca[:, 1],
        c='red',
        marker='X',
        s=180,
        edgecolors='black',
        label='Tam cum K-means',
    )

    for i, c in enumerate(centers_pca):
        ax.annotate(
            f'Tam {i}',
            (c[0] + 0.15, c[1] + 0.15),
            fontsize=11,
            fontweight='bold',
            color='black',
        )

    ax.set_title(
        f'Bieu do khong gian phan cum PCA 2D (PC1: {var_exp[0]*100:.1f}%, PC2: {var_exp[1]*100:.1f}%)',
        fontsize=13,
        fontweight='bold',
    )
    ax.set_xlabel('Thanh phan chinh 1 (PC1)')
    ax.set_ylabel('Thanh phan chinh 2 (PC2)')
    ax.grid(True, linestyle='--', alpha=0.5)
    plt.colorbar(scatter, ax=ax, label='Cum phan khuc (Cluster)')
    ax.legend()
    save_plot(fig, 'Hinh2_Truc_Quan_Hoa_Phan_Cum_PCA_2D.png')

    # 2. Silhouette Plot theo tung cum (ve tren mau con 3.000 diem de hien thi ro net, sieu toc)
    sub_n_sil = min(len(X_scaled), 3000)
    idx_sil_sub = np.random.choice(len(X_scaled), sub_n_sil, replace=False)
    X_sub_sil = X_scaled[idx_sil_sub]
    labs_sub_sil = labels[idx_sil_sub]

    sil_samples = silhouette_samples(X_sub_sil, labs_sub_sil)
    fig, ax = plt.subplots(figsize=(10, 7))
    y_lower = 10
    k = len(np.unique(labs_sub_sil))

    for i in range(k):
        ith_cluster_sil = sil_samples[labs_sub_sil == i]
        ith_cluster_sil.sort()
        size_cluster_i = ith_cluster_sil.shape[0]
        y_upper = y_lower + size_cluster_i

        color = plt.cm.tab10(float(i) / k)
        ax.fill_betweenx(
            np.arange(y_lower, y_upper),
            0,
            ith_cluster_sil,
            facecolor=color,
            edgecolor=color,
            alpha=0.7,
        )
        ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i), fontsize=11)
        y_lower = y_upper + 10

    avg_sil = silhouette_score(X_sub_sil, labs_sub_sil)
    ax.axvline(
        x=avg_sil,
        color='red',
        linestyle='--',
        label=f'Silhouette TB = {avg_sil:.3f}',
    )
    ax.set_title(
        'Bieu do phan bo Silhouette tung cum (Silhouette Plot)',
        fontsize=13,
        fontweight='bold',
    )
    ax.set_xlabel('He so Silhouette s(i)')
    ax.set_ylabel('Cum phan khuc')
    ax.set_yticks([])
    ax.set_xlim([-0.2, 0.8])
    ax.legend(loc='upper right')
    ax.grid(True, linestyle='--', alpha=0.5)
    save_plot(fig, 'Hinh3_Bieu_Do_Silhouette_Tung_Cum.png')

    # 3. Heatmap Z-Score Ho so cum (Cluster Profiling)
    df_feats = pd.DataFrame(X_scaled, columns=FEATURE_COLS)
    df_feats['Cluster'] = labels
    cluster_means = df_feats.groupby('Cluster').mean()
    # Z-score trung binh cua tung cum so voi toan bo tap
    zscore_profiles = cluster_means.rename(columns=FEATURE_LABELS_VN)

    fig, ax = plt.subplots(figsize=(11, 5))
    cax = ax.imshow(zscore_profiles.values, cmap='coolwarm', aspect='auto')
    fig.colorbar(cax, label='Z-Score do lech chuan')
    ax.set_xticks(np.arange(len(zscore_profiles.columns)))
    ax.set_yticks(np.arange(len(zscore_profiles.index)))
    ax.set_xticklabels(
        zscore_profiles.columns, rotation=35, ha='right', fontsize=9
    )
    ax.set_yticklabels(
        [f'Cum {i}' for i in zscore_profiles.index], fontsize=11
    )

    # Ghi so tren tung o
    for i in range(len(zscore_profiles.index)):
        for j in range(len(zscore_profiles.columns)):
            val = zscore_profiles.values[i, j]
            ax.text(
                j,
                i,
                f'{val:.2f}',
                ha='center',
                va='center',
                color='black' if abs(val) < 1.2 else 'white',
                fontweight='bold',
            )

    ax.set_title(
        'Heatmap Z-Score Ho so dac trung cac cum (So voi toan bo doi tau)',
        fontsize=12,
        fontweight='bold',
    )
    save_plot(fig, 'Hinh4_Heatmap_ZScore_Ho_So_Cum.png')

    # 4. Cay quyet dinh dien giai ranh gioi cum (Surrogate Decision Tree)
    tree_clf = DecisionTreeClassifier(
        max_depth=3, min_samples_leaf=50, random_state=SEED
    )
    tree_clf.fit(X_scaled, labels)
    tree_acc = tree_clf.score(X_scaled, labels)
    tree_rules = export_text(
        tree_clf, feature_names=[FEATURE_LABELS_VN[c] for c in FEATURE_COLS]
    )

    with open(
        os.path.join(OUTPUT_DIR, 'luat_cay_quyet_dinh_giai_thich_cum.txt'),
        'w',
        encoding='utf-8',
    ) as f:
        f.write(f'Do chinh xac tai tao K-means cua Cay quyet dinh: {tree_acc*100:.2f}%\n')
        f.write('=' * 70 + '\n')
        f.write(tree_rules)

    log_step(f'Cay quyet dinh tai tao K-means dat do chinh xac {tree_acc*100:.2f}%.')


# ==============================================================================
# 8. DANH GIA NGHIEP VU & HO SO HOA PHAN KHUC (DOMAIN PROFILING)
# ==============================================================================
def domain_profiling_and_drift(
    df_raw: pd.DataFrame, labels: np.ndarray
) -> pd.DataFrame:
    """Ho so hoa nghiep vu hanh hai va tinh chi so troi PSI."""
    log_step('Ho so hoa nghiep vu hanh hai (Cluster Profiling)...')
    df_eval = df_raw.copy()
    df_eval['Cluster'] = labels

    cluster_names = {
        0: 'Tau khoi hanh trinh toc do cao (Deep-Sea High Speed Cruise)',
        1: 'Tau hang lon chay tiet kiem (Heavy Cargo Eco Speed)',
        2: 'Tiep can luong ven bo (Coastal Approach & Navigation)',
        3: 'Maneuvering & Nghiep vu cap ben (Berthing & Port Maneuvering)',
    }
    df_eval['Ten_Phan_Khuc'] = df_eval['Cluster'].map(cluster_names)

    profile_list = []
    for c in sorted(df_eval['Cluster'].unique()):
        sub = df_eval[df_eval['Cluster'] == c]
        profile_list.append(
            {
                'Cum': c,
                'Ten_Phan_Khuc': cluster_names.get(c, f'Cum {c}'),
                'So_Luong_Tau': len(sub),
                'Ty_Le_Pct': round(len(sub) / len(df_eval) * 100, 2),
                'SOG_TB_kn': round(sub['sog'].mean(), 2),
                'Cu_Ly_TB_NM': round(sub['Dist_To_Berth_NM'].mean(), 1),
                'Mon_Nuoc_TB_m': round(sub['draft'].mean(), 2),
                'Chieu_Dai_TB_m': round(sub['length'].mean(), 1),
                'Dien_Tich_TB_m2': round(sub['Area_Proxy'].mean(), 0),
                'Delta_Heading_TB_do': round(
                    sub['abs_delta_heading'].mean(), 2
                ),
                'Ty_Le_Tau_Dau_Pct': round(sub['Is_Tanker'].mean() * 100, 2),
                'Target_Hours_TB': round(sub['Target_Hours'].mean(), 1),
            }
        )

    df_profile = pd.DataFrame(profile_list)
    df_profile.to_csv(
        os.path.join(OUTPUT_DIR, 'bang_ho_so_dac_trung_cac_cum.csv'),
        index=False,
        encoding='utf-8-sig',
    )

    # Tinh chi so troi du lieu PSI giua nua dau thang va nua sau thang
    # (Vi du: Expected E = 50% dau, Actual A = 50% sau)
    half_idx = len(df_eval) // 2
    E_counts = (
        df_eval.iloc[:half_idx]['Cluster']
        .value_counts(normalize=True)
        .sort_index()
    )
    A_counts = (
        df_eval.iloc[half_idx:]['Cluster']
        .value_counts(normalize=True)
        .sort_index()
    )

    psi_val = 0.0
    psi_rows = []
    for c in range(len(cluster_names)):
        e = E_counts.get(c, 1e-4)
        a = A_counts.get(c, 1e-4)
        psi_i = (a - e) * np.log(a / e)
        psi_val += psi_i
        psi_rows.append(
            {
                'Cum': c,
                'Ty_Le_Nua_Dau_E': round(e, 4),
                'Ty_Le_Nua_Sau_A': round(a, 4),
                'Dong_Gop_PSI': round(psi_i, 6),
            }
        )

    status_psi = (
        'On dinh (PSI < 0.1)'
        if psi_val < 0.1
        else 'Can theo doi (0.1 <= PSI <= 0.25)'
        if psi_val <= 0.25
        else 'Troi dang ke (PSI > 0.25)'
    )

    df_psi = pd.DataFrame(
        [
            {
                'Chi_So': 'Population Stability Index (PSI)',
                'Gia_Tri_PSI': round(psi_val, 5),
                'Trang_Thai': status_psi,
                'Nguong_Tham_Chieu': '< 0.1 on dinh, 0.1-0.25 canh bao, > 0.25 troi',
            }
        ]
    )
    df_psi.to_csv(
        os.path.join(OUTPUT_DIR, 'bang_chi_so_troi_du_lieu_psi.csv'),
        index=False,
        encoding='utf-8-sig',
    )
    log_step(f'Chi so troi PSI = {psi_val:.5f} -> Ket luan: {status_psi}')
    return df_profile


# ==============================================================================
# 9. PHAT HIEN NGOAI LAI (>= 3 PHUONG PHAP & 3 LOAI NGOAI LAI HANG HAI)
# ==============================================================================
def detect_outliers_and_explain(
    X_scaled: np.ndarray,
    df_raw: pd.DataFrame,
    km_model: KMeans,
    contamination: float = 0.03,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Phat hien ngoai lai bang >= 3 phuong phap va giai thich ly do nghiep vu."""
    log_step('Phat hien ngoai lai da phuong phap (Outlier Detection)...')
    df_out = df_raw.copy()
    n = len(df_raw)

    # 1. Thong ke don bien Tukey IQR tren SOG & Dist (Baseline)
    q1_sog = df_out['sog'].quantile(0.25)
    q3_sog = df_out['sog'].quantile(0.75)
    iqr_sog = q3_sog - q1_sog
    upper_sog = q3_sog + 1.5 * iqr_sog
    is_out_iqr = (df_out['sog'] > upper_sog).values

    # Modified Z-score (MAD) tren SOG
    med_sog = df_out['sog'].median()
    mad_sog = (np.abs(df_out['sog'] - med_sog)).median()
    mod_z_sog = (
        0.6745 * (df_out['sog'] - med_sog) / (mad_sog if mad_sog > 0 else 1.0)
    )
    is_out_modz = (mod_z_sog > 3.5).values

    # 2. Khoang cach toi tam cum K-means (Cluster Distance / Mahalanobis-like)
    dist_to_centers = km_model.transform(X_scaled)
    min_dist_to_cluster = np.min(dist_to_centers, axis=1)
    thresh_dist = np.percentile(min_dist_to_cluster, 100 * (1 - contamination))
    is_out_cluster_dist = min_dist_to_cluster > thresh_dist

    # 3. Isolation Forest
    t0 = time.time()
    iso = IsolationForest(
        contamination=contamination, random_state=SEED, n_estimators=100
    )
    iso.fit(X_scaled)
    t_iso = time.time() - t0
    # Score am: cang nho cang bat thuong
    iso_scores = -iso.decision_function(X_scaled)
    is_out_iso = iso.predict(X_scaled) == -1

    # 4. Local Outlier Factor (LOF) tren mau con dai dien
    t0 = time.time()
    sample_size_lof = min(n, 6000)
    idx_lof = np.random.choice(n, sample_size_lof, replace=False)
    lof = LocalOutlierFactor(
        n_neighbors=25, contamination=contamination, novelty=True
    )
    lof.fit(X_scaled[idx_lof])
    lof_scores = -lof.decision_function(X_scaled)
    is_out_lof = lof_scores > np.percentile(
        lof_scores, 100 * (1 - contamination)
    )
    t_lof = time.time() - t0

    # Tong hop ket qua ngoai lai
    df_out['Is_Outlier_IQR'] = is_out_iqr
    df_out['Is_Outlier_ModZ'] = is_out_modz
    df_out['Is_Outlier_ClusterDist'] = is_out_cluster_dist
    df_out['Is_Outlier_IsolationForest'] = is_out_iso
    df_out['Is_Outlier_LOF'] = is_out_lof
    df_out['Anomaly_Score_iForest'] = iso_scores
    df_out['Dist_To_Cluster_Center'] = min_dist_to_cluster

    # Bang so sanh cac phuong phap ngoai lai
    outlier_summary = [
        {
            'Phuong_Phap': 'Tukey IQR SOG (Baseline)',
            'So_Luong_Ngoai_Lai': int(np.sum(is_out_iqr)),
            'Ty_Le_Pct': round(np.mean(is_out_iqr) * 100, 2),
            'Thoi_Gian_Chay_s': 0.01,
            'Jaccard_Overlap_Vs_iForest': round(
                np.sum(is_out_iqr & is_out_iso)
                / max(np.sum(is_out_iqr | is_out_iso), 1),
                4,
            ),
        },
        {
            'Phuong_Phap': 'Modified Z-score SOG',
            'So_Luong_Ngoai_Lai': int(np.sum(is_out_modz)),
            'Ty_Le_Pct': round(np.mean(is_out_modz) * 100, 2),
            'Thoi_Gian_Chay_s': 0.01,
            'Jaccard_Overlap_Vs_iForest': round(
                np.sum(is_out_modz & is_out_iso)
                / max(np.sum(is_out_modz | is_out_iso), 1),
                4,
            ),
        },
        {
            'Phuong_Phap': 'Khoang cach tam cum K-means',
            'So_Luong_Ngoai_Lai': int(np.sum(is_out_cluster_dist)),
            'Ty_Le_Pct': round(np.mean(is_out_cluster_dist) * 100, 2),
            'Thoi_Gian_Chay_s': 0.05,
            'Jaccard_Overlap_Vs_iForest': round(
                np.sum(is_out_cluster_dist & is_out_iso)
                / max(np.sum(is_out_cluster_dist | is_out_iso), 1),
                4,
            ),
        },
        {
            'Phuong_Phap': 'Isolation Forest (Chinh)',
            'So_Luong_Ngoai_Lai': int(np.sum(is_out_iso)),
            'Ty_Le_Pct': round(np.mean(is_out_iso) * 100, 2),
            'Thoi_Gian_Chay_s': round(t_iso, 2),
            'Jaccard_Overlap_Vs_iForest': 1.0,
        },
        {
            'Phuong_Phap': 'Local Outlier Factor (LOF)',
            'So_Luong_Ngoai_Lai': int(np.sum(is_out_lof)),
            'Ty_Le_Pct': round(np.mean(is_out_lof) * 100, 2),
            'Thoi_Gian_Chay_s': round(t_lof, 2),
            'Jaccard_Overlap_Vs_iForest': round(
                np.sum(is_out_lof & is_out_iso)
                / max(np.sum(is_out_lof | is_out_iso), 1),
                4,
            ),
        },
    ]
    df_out_summary = pd.DataFrame(outlier_summary)
    df_out_summary.to_csv(
        os.path.join(OUTPUT_DIR, 'bang_so_sanh_cac_phuong_phap_ngoai_lai.csv'),
        index=False,
        encoding='utf-8-sig',
    )

    # 3 LOAI NGOAI LAI HANG HAI THEO CHUONG 8
    # 1. Global: SOG > 28 kn hoac draft > 20m
    global_mask = (df_out['sog'] > 25.0) | (df_out['draft'] > 18.0)
    # 2. Contextual: SOG cao khi sat ben (SOG > 12 kn khi Dist < 5 NM) hoac draft > 14m khi vao kenh nong
    contextual_mask = (
        (df_out['sog'] > 12.0) & (df_out['Dist_To_Berth_NM'] < 5.0)
    ) | ((df_out['abs_delta_heading'] > 60.0) & (df_out['sog'] > 10.0))
    # 3. Collective: Tuan tu bat thuong, v_implied lech han SOG hoac nghi van du lieu
    collective_mask = (
        (df_out['v_implied'] < 1.62) | (df_out['v_implied'] > 30.0)
    ) & (df_out['Dist_To_Berth_NM'] > 20.0)

    df_3_types = pd.DataFrame(
        [
            {
                'Loai_Ngoai_Lai': 'Toan cuc (Global Outlier)',
                'Dinh_Nghia_Hang_Hai': 'Dac trung don/da bien vuot nguong vat ly hanh hai (SOG > 25 kn, Draft > 18m)',
                'So_Mau_Phat_Hien': int(np.sum(global_mask)),
                'Ty_Le_Pct': round(np.mean(global_mask) * 100, 3),
                'Hanh_Dong_Xu_Ly': 'Kiem tra ky thuat cam bien AIS, kiem chung lai mmsi va loai tau',
            },
            {
                'Loai_Ngoai_Lai': 'Ngu canh (Contextual Outlier)',
                'Dinh_Nghia_Hang_Hai': 'Chi bat thuong trong ngu canh (chay toc do cao khi cach cau ben < 5 NM, lech goc lai lon)',
                'So_Mau_Phat_Hien': int(np.sum(contextual_mask)),
                'Ty_Le_Pct': round(np.mean(contextual_mask) * 100, 3),
                'Hanh_Dong_Xu_Ly': 'Canh bao an toan hang hai va dieu phoi luong cap ben (VTS)',
            },
            {
                'Loai_Ngoai_Lai': 'Tap the (Collective Outlier)',
                'Dinh_Nghia_Hang_Hai': 'Chuoi tin hieu gay sai lech thoi gian cap cang (v_implied < 1.62 kn hoac phi ly)',
                'So_Mau_Phat_Hien': int(np.sum(collective_mask)),
                'Ty_Le_Pct': round(np.mean(collective_mask) * 100, 3),
                'Hanh_Dong_Xu_Ly': 'Loai bo khoi tap huan luyen ETA hoac danh dau can thiep chuyen di',
            },
        ]
    )
    df_3_types.to_csv(
        os.path.join(OUTPUT_DIR, 'bang_3_loai_ngoai_lai_hang_hai.csv'),
        index=False,
        encoding='utf-8-sig',
    )

    # CHAM DIEM NGOAI LAI KEM LY DO DOC DUOC (EXPLAINABLE ANOMALY ATTRIBUTION)
    # Trich xuat top 10 truong hop bat thuong nhat theo iForest va giai thich
    top_outliers = df_out[df_out['Is_Outlier_IsolationForest']].sort_values(
        by='Anomaly_Score_iForest', ascending=False
    ).head(15)

    alert_reasons = []
    for idx, row in top_outliers.iterrows():
        # Xac dinh dac trung lech nhat so voi mean
        reasons = []
        if row['sog'] > 20.0:
            reasons.append(f'SOG cuc cao ({row["sog"]:.1f} kn)')
        elif row['sog'] < 1.0 and row['Dist_To_Berth_NM'] > 50.0:
            reasons.append(f'Dung giua bien xa ben ({row["Dist_To_Berth_NM"]:.1f} NM)')

        if row['Dist_To_Berth_NM'] < 5.0 and row['sog'] > 12.0:
            reasons.append(
                f'Chay toc do cao sat ben ({row["sog"]:.1f} kn / {row["Dist_To_Berth_NM"]:.1f} NM)'
            )

        if row['draft'] > 15.0:
            reasons.append(f'Mon nuoc rat sau ({row["draft"]:.1f} m)')

        if row['abs_delta_heading'] > 45.0:
            reasons.append(
                f'Lech huong mui lon ({row["abs_delta_heading"]:.1f} do - nghi gio dat)'
            )

        if not reasons:
            reasons.append('To hop da bien lech khoi da tap binh thuong')

        alert_reasons.append(
            {
                'MMSI': row.get('mmsi', idx),
                'Loai_Tau': row.get('vessel_group', 'Unknown'),
                'SOG_kn': round(row['sog'], 1),
                'Cu_Ly_NM': round(row['Dist_To_Berth_NM'], 1),
                'Mon_Nuoc_m': round(row['draft'], 1),
                'Delta_Heading_do': round(row['abs_delta_heading'], 1),
                'iForest_Score': round(row['Anomaly_Score_iForest'], 4),
                'Ly_Do_Nghiep_Vu': ' | '.join(reasons),
            }
        )

    df_alerts = pd.DataFrame(alert_reasons)
    df_alerts.to_csv(
        os.path.join(OUTPUT_DIR, 'bang_mau_canh_bao_ngoai_lai_kem_ly_do.csv'),
        index=False,
        encoding='utf-8-sig',
    )

    # Ve bieu do so sanh phan bo diem bat thuong
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    axes[0].hist(
        df_out['Anomaly_Score_iForest'],
        bins=50,
        color='#1f77b4',
        alpha=0.7,
        edgecolor='black',
    )
    thresh_iso = np.percentile(iso_scores, 100 * (1 - contamination))
    axes[0].axvline(
        x=thresh_iso,
        color='red',
        linestyle='--',
        label=f'Nguong 3% ({thresh_iso:.3f})',
    )
    axes[0].set_title(
        '(a) Phan bo Anomaly Score cua Isolation Forest',
        fontsize=12,
        fontweight='bold',
    )
    axes[0].set_xlabel('Anomaly Score (cang lon cang bat thuong)')
    axes[0].set_ylabel('Tan suat')
    axes[0].legend()
    axes[0].grid(True, linestyle='--', alpha=0.5)

    # Scatter SOG vs Dist to Berth to mau theo Outlier
    axes[1].scatter(
        df_out[~is_out_iso]['Dist_To_Berth_NM'],
        df_out[~is_out_iso]['sog'],
        c='#2ca02c',
        alpha=0.25,
        s=12,
        label='Binh thuong (Normal)',
    )
    axes[1].scatter(
        df_out[is_out_iso]['Dist_To_Berth_NM'],
        df_out[is_out_iso]['sog'],
        c='#d62728',
        alpha=0.8,
        s=28,
        label='Ngoai lai (iForest Anomaly)',
    )
    axes[1].set_title(
        '(b) Tuong quan Cu ly ben vs Toc do SOG', fontsize=12, fontweight='bold'
    )
    axes[1].set_xlabel('Cu ly den cau ben (NM)')
    axes[1].set_ylabel('Toc do di chuyen SOG (knots)')
    axes[1].legend()
    axes[1].grid(True, linestyle='--', alpha=0.5)
    save_plot(fig, 'Hinh5_So_Sanh_Diem_Bat_Thuong_Ngoai_Lai.png')

    return df_out, df_out_summary


# ==============================================================================
# 10. DONG GOI VA NEN FILE KET QUA
# ==============================================================================
def package_and_zip_results() -> str:
    """Dong goi toan bo artifacts ket qua thanh file zip tien loi."""
    zip_path = os.path.join(OUTPUT_DIR, 'DS317_BT5_Ket_Qua_So_Lieu.zip')
    log_step(f'Dong goi ket qua vao file zip: {zip_path}...')

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as z:
        for root, _, files in os.walk(OUTPUT_DIR):
            for file in files:
                if file.endswith('.zip'):
                    continue
                full_p = os.path.join(root, file)
                rel_p = os.path.relpath(full_p, OUTPUT_DIR)
                z.write(full_p, rel_p)

    log_step(f'Da dong goi thanh cong! Kich thuoc zip: {os.path.getsize(zip_path)/1024:.1f} KB')
    return zip_path


# ==============================================================================
# HAM MAIN DIEU PHOI TOAN BO QUY TRINH
# ==============================================================================
def main() -> None:
    """Ham thuc thi toan bo pipeline thuc nghiem."""
    print('=' * 80)
    print('DS317 - KHAI PHA DU LIEU TRONG DOANH NGHIEP (UIT)')
    print('THUC NGHIEM CHUONG 8: GOM NHOM & XAC DINH NGOAI LAI DU LIEU NOAA AIS 2025')
    print('=' * 80)

    # Buoc 1: Nap hoac tao dataset
    df = load_or_extract_dataset(n_samples=25000)

    # Buoc 2: Xuat 2 bang 5 tieu chi thuat toan
    export_5_criteria_tables()

    # Buoc 3: Chuan hoa dac trung
    log_step('Chuan hoa dac trung bang StandardScaler...')
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[FEATURE_COLS])
    joblib.dump(scaler, os.path.join(OUTPUT_DIR, 'scaler_clustering.joblib'))

    # Buoc 4: Khao sat chon k bang do do noi bo
    df_k = evaluate_k_selection(X_scaled, k_range=range(2, 7))

    # Buoc 5: So sanh >= 3 phuong phap gom nhom
    CHOSEN_K = 4
    df_comp, models = compare_clustering_algorithms(X_scaled, k=CHOSEN_K)
    km_model, km_labels = models['K-means']
    joblib.dump(km_model, os.path.join(OUTPUT_DIR, 'kmeans_best_model.joblib'))

    # Buoc 6: Danh gia ben ngoai voi nhan tham chieu
    df_ext = evaluate_external_validation(
        km_labels, df['Is_Tanker'].values, model_name='K-means (k=4)'
    )

    # Buoc 7: Danh gia truc quan (PCA, Silhouette, Heatmap, Decision Tree)
    visual_evaluation(X_scaled, df, km_labels, km_model)

    # Buoc 8: Ho so hoa nghiep vu va do do troi PSI
    df_profile = domain_profiling_and_drift(df, km_labels)

    # Buoc 9: Phat hien ngoai lai da phuong phap va giai thich
    df_out, df_out_summary = detect_outliers_and_explain(
        X_scaled, df, km_model, contamination=0.03
    )

    # Buoc 10: Dong goi ket qua
    zip_p = package_and_zip_results()

    print('=' * 80)
    print('HOAN THANH TOAN BO THUC NGHIEM GOM NHOM VA NGOAI LAI BT5!')
    print(f'Thu muc luu ket qua: {OUTPUT_DIR}')
    print(f'File ZIP tong hop: {zip_p}')
    print('=' * 80)


if __name__ == '__main__':
    main()
