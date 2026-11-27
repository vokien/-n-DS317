"""Kiem dinh y nghia thong ke Wilcoxon signed-rank va Diebold-Mariano.

Module nay thuc hien kiem dinh cap doi phi tham so (Wilcoxon signed-rank)
va kiem dinh do chinh xac du bao Diebold-Mariano (hieu chinh
Harvey-Leybourne-Newbold 1997 voi phuong sai dai han Newey-West HAC)
giua hai mo hinh/bien the theo tung Fold va phan tang (All, LE_168h,
GT_168h). Ho tro tu dong nap du lieu that tu detailed_predictions/ hoac
chay thu nghiem tren du lieu demo/mock.
"""

# 1. Thu vien chuan
import argparse
from pathlib import Path
import sys
from typing import Any

# 2. Thu vien ben thu ba
import numpy as np
import pandas as pd
from scipy import stats


STRATUM_LIMIT_HOURS = 168.0
DEFAULT_ASYM_WEIGHT = 2.5
DEFAULT_MAX_WILCOXON = 200_000


def compute_loss_series(
    err_base: np.ndarray,
    err_cand: np.ndarray,
    loss_type: str = "abs",
    asym_weight: float = DEFAULT_ASYM_WEIGHT,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Tinh chuoi mat mat cua baseline, ung vien va hieu so d = L_c - L_b.

    Args:
        err_base (np.ndarray): Sai so du bao (y_pred - y_true) baseline.
        err_cand (np.ndarray): Sai so du bao (y_pred - y_true) ung vien.
        loss_type (str): Loai ham mat mat ('abs', 'squared', 'asym').
        asym_weight (float): Trong so phat du bao som (err < 0) cho
            che do 'asym'.

    Returns:
        tuple[np.ndarray, np.ndarray, np.ndarray]: Bo ba (loss_base,
            loss_cand, diff) trong do diff < 0 nghia la ung vien tot hon.
    """
    e_b = np.asarray(err_base, dtype=np.float64)
    e_c = np.asarray(err_cand, dtype=np.float64)

    if loss_type == "abs":
        l_b = np.abs(e_b)
        l_c = np.abs(e_c)
    elif loss_type == "squared":
        l_b = e_b ** 2
        l_c = e_c ** 2
    elif loss_type == "asym":
        w_b = np.where(e_b < 0.0, asym_weight, 1.0)
        w_c = np.where(e_c < 0.0, asym_weight, 1.0)
        l_b = w_b * (e_b ** 2)
        l_c = w_c * (e_c ** 2)
    else:
        raise ValueError(f"Khong ho tro loss_type={loss_type!r}")

    diff = l_c - l_b
    return l_b, l_c, diff


def wilcoxon_signed_rank_test(
    err_base: np.ndarray,
    err_cand: np.ndarray,
    loss_type: str = "abs",
    asym_weight: float = DEFAULT_ASYM_WEIGHT,
    max_samples: int = DEFAULT_MAX_WILCOXON,
    seed: int = 42,
) -> dict[str, Any]:
    """Thuc hien kiem dinh Wilcoxon signed-rank hai phia tren cap sai so.

    Args:
        err_base (np.ndarray): Sai so (y_pred - y_true) cua baseline.
        err_cand (np.ndarray): Sai so (y_pred - y_true) cua ung vien.
        loss_type (str): Ham mat mat ('abs', 'squared', 'asym').
        asym_weight (float): He so phat du bao som cho che do 'asym'.
        max_samples (int): Nguong lay mau ngau nhien neu N qua lon.
        seed (int): Hat giong ngau nhien co dinh khi lay mau con.

    Returns:
        dict[str, Any]: Tu dien gom n_total, n_tested, n_nonzero,
            w_stat, p_value, mean_diff, median_diff.
    """
    _, _, diff = compute_loss_series(
        err_base=err_base,
        err_cand=err_cand,
        loss_type=loss_type,
        asym_weight=asym_weight,
    )
    valid = np.isfinite(diff)
    diff = diff[valid]
    n_total = int(len(diff))

    if n_total == 0:
        return {
            "n_total": 0,
            "n_tested": 0,
            "n_nonzero": 0,
            "w_stat": np.nan,
            "p_value": np.nan,
            "mean_diff": np.nan,
            "median_diff": np.nan,
        }

    if max_samples > 0 and n_total > max_samples:
        rng = np.random.default_rng(seed)
        idx = rng.choice(n_total, size=max_samples, replace=False)
        sample_diff = diff[idx]
    else:
        sample_diff = diff

    nonzero = sample_diff[sample_diff != 0.0]
    n_nonzero = int(len(nonzero))
    if n_nonzero == 0:
        return {
            "n_total": n_total,
            "n_tested": int(len(sample_diff)),
            "n_nonzero": 0,
            "w_stat": 0.0,
            "p_value": 1.0,
            "mean_diff": float(np.mean(diff)),
            "median_diff": float(np.median(diff)),
        }

    res = stats.wilcoxon(
        sample_diff,
        zero_method="wilcox",
        alternative="two-sided",
    )
    return {
        "n_total": n_total,
        "n_tested": int(len(sample_diff)),
        "n_nonzero": n_nonzero,
        "w_stat": float(res.statistic),
        "p_value": float(res.pvalue),
        "mean_diff": float(np.mean(diff)),
        "median_diff": float(np.median(diff)),
    }


def diebold_mariano_test(
    err_base: np.ndarray,
    err_cand: np.ndarray,
    horizon: int = 1,
    loss_type: str = "abs",
    asym_weight: float = DEFAULT_ASYM_WEIGHT,
) -> dict[str, Any]:
    """Thuc hien kiem dinh Diebold-Mariano voi hieu chinh HLN (1997).

    Su dung uoc luong phuong sai dai han Newey-West HAC voi do tre
    (horizon - 1) va phan phoi Student-t (df = T - 1).

    Args:
        err_base (np.ndarray): Sai so (y_pred - y_true) cua baseline.
        err_cand (np.ndarray): Sai so (y_pred - y_true) cua ung vien.
        horizon (int): Chan troi du bao h (>= 1) cho HAC Bartlett lag.
        loss_type (str): Ham mat mat ('abs', 'squared', 'asym').
        asym_weight (float): He so phat du bao som cho che do 'asym'.

    Returns:
        dict[str, Any]: Tu dien gom n_obs, dm_stat, p_value, mean_diff,
            hac_se.
    """
    _, _, diff = compute_loss_series(
        err_base=err_base,
        err_cand=err_cand,
        loss_type=loss_type,
        asym_weight=asym_weight,
    )
    diff = diff[np.isfinite(diff)]
    n_obs = int(len(diff))
    if n_obs < 3:
        return {
            "n_obs": n_obs,
            "dm_stat": np.nan,
            "p_value": np.nan,
            "mean_diff": np.nan,
            "hac_se": np.nan,
        }

    d_mean = float(np.mean(diff))
    d_centered = diff - d_mean
    gamma_0 = float(np.dot(d_centered, d_centered) / n_obs)

    long_run_var = gamma_0
    max_lag = max(0, int(horizon) - 1)
    for lag in range(1, max_lag + 1):
        if lag >= n_obs:
            break
        gamma_k = float(
            np.dot(d_centered[lag:], d_centered[:-lag]) / n_obs
        )
        weight = 1.0 - (lag / (max_lag + 1.0))
        long_run_var += 2.0 * weight * gamma_k

    if long_run_var <= 0.0:
        long_run_var = gamma_0

    var_mean = long_run_var / n_obs
    if var_mean <= 1e-18:
        return {
            "n_obs": n_obs,
            "dm_stat": 0.0,
            "p_value": 1.0,
            "mean_diff": d_mean,
            "hac_se": 0.0,
        }

    hac_se = float(np.sqrt(var_mean))
    dm_raw = d_mean / hac_se

    # Hieu chinh mau huu han Harvey-Leybourne-Newbold (1997)
    h_eff = max(1, int(horizon))
    hln_factor = np.sqrt(
        max(
            1e-12,
            (n_obs + 1.0 - 2.0 * h_eff + h_eff * (h_eff - 1.0) / n_obs)
            / n_obs,
        )
    )
    dm_hln = float(dm_raw * hln_factor)
    p_value = float(2.0 * stats.t.sf(abs(dm_hln), df=n_obs - 1))

    return {
        "n_obs": n_obs,
        "dm_stat": dm_hln,
        "p_value": p_value,
        "mean_diff": d_mean,
        "hac_se": hac_se,
    }


def evaluate_pair_stratified(
    y_true: np.ndarray,
    y_pred_base: np.ndarray,
    y_pred_cand: np.ndarray,
    fold_label: str,
    model_name: str,
    loss_type: str = "abs",
    horizon: int = 1,
    asym_weight: float = DEFAULT_ASYM_WEIGHT,
    max_wilcoxon: int = DEFAULT_MAX_WILCOXON,
    seed: int = 42,
) -> list[dict[str, Any]]:
    """Kiem dinh cap mo hinh tren 3 tang All, LE_168h va GT_168h.

    Args:
        y_true (np.ndarray): Nhan thuc te Target_Hours.
        y_pred_base (np.ndarray): Gia tri du bao cua mo hinh baseline.
        y_pred_cand (np.ndarray): Gia tri du bao cua mo hinh ung vien.
        fold_label (str): Nhan Fold (vd: 'Fold_1', 'Fold_2', 'Fold_3').
        model_name (str): Ten mo hinh (vd: 'XGBoost', 'CatBoost').
        loss_type (str): Ham mat mat ('abs', 'squared', 'asym').
        horizon (int): Chan troi h cho kiem dinh Diebold-Mariano.
        asym_weight (float): Trong so cho ham mat mat bat doi xung.
        max_wilcoxon (int): So mau toi da cho Wilcoxon signed-rank.
        seed (int): Hat giong ngau nhien co dinh.

    Returns:
        list[dict[str, Any]]: Danh sach dong ket qua theo tung tang.
    """
    yt = np.asarray(y_true, dtype=np.float64)
    yb = np.asarray(y_pred_base, dtype=np.float64)
    yc = np.asarray(y_pred_cand, dtype=np.float64)

    masks = {
        "All": np.ones(len(yt), dtype=bool),
        "LE_168h": yt <= STRATUM_LIMIT_HOURS,
        "GT_168h": yt > STRATUM_LIMIT_HOURS,
    }

    rows: list[dict[str, Any]] = []
    for stratum, mask in masks.items():
        if not np.any(mask):
            continue
        err_b = yb[mask] - yt[mask]
        err_c = yc[mask] - yt[mask]

        mae_b = float(np.mean(np.abs(err_b)))
        mae_c = float(np.mean(np.abs(err_c)))

        w_res = wilcoxon_signed_rank_test(
            err_base=err_b,
            err_cand=err_c,
            loss_type=loss_type,
            asym_weight=asym_weight,
            max_samples=max_wilcoxon,
            seed=seed,
        )
        dm_res = diebold_mariano_test(
            err_base=err_b,
            err_cand=err_c,
            horizon=horizon,
            loss_type=loss_type,
            asym_weight=asym_weight,
        )

        rows.append(
            {
                "Fold": fold_label,
                "Model": model_name,
                "Stratum": stratum,
                "Loss_Type": loss_type,
                "N_Obs": int(dm_res["n_obs"]),
                "MAE_Base": round(mae_b, 4),
                "MAE_Cand": round(mae_c, 4),
                "Delta_MAE": round(mae_c - mae_b, 4),
                "Mean_Loss_Diff": round(float(dm_res["mean_diff"]), 4),
                "Wilcoxon_N_Tested": int(w_res["n_tested"]),
                "Wilcoxon_Stat": w_res["w_stat"],
                "Wilcoxon_p": w_res["p_value"],
                "DM_Stat": round(float(dm_res["dm_stat"]), 4),
                "DM_p": dm_res["p_value"],
                "Sig_0_05": bool(
                    w_res["p_value"] < 0.05 and dm_res["p_value"] < 0.05
                ),
                "Sig_0_01": bool(
                    w_res["p_value"] < 0.01 and dm_res["p_value"] < 0.01
                ),
            }
        )
    return rows


def load_prediction_pair(
    pred_dir: Path,
    base_slug: str,
    cand_slug: str,
    model_name: str,
    fold_num: str,
) -> pd.DataFrame | None:
    """Nap cap file du doan that tu detailed_predictions/ va ghep eval_meta.

    Args:
        pred_dir (Path): Thu muc chua eval_meta_fold*.parquet va pred_*.
        base_slug (str): Tien to thi nghiem baseline (vd: '00_baseline_b0').
        cand_slug (str): Tien to thi nghiem ung vien.
        model_name (str): Ten mo hinh can doi chieu.
        fold_num (str): So thu tu Fold ('1', '2', '3').

    Returns:
        pd.DataFrame | None: DataFrame gom y_true, y_pred_base, y_pred_cand
            hoac None neu khong tim thay du file.
    """
    meta_path = pred_dir / f"eval_meta_fold{fold_num}.parquet"
    if not meta_path.is_file():
        return None

    def _read_pred(slug: str) -> pd.DataFrame | None:
        stem = f"pred_{slug}_{model_name}_fold{fold_num}"
        p_pq = pred_dir / f"{stem}.parquet"
        p_gz = pred_dir / f"{stem}.csv.gz"
        if p_pq.is_file():
            return pd.read_parquet(p_pq)
        if p_gz.is_file():
            return pd.read_csv(p_gz)
        return None

    df_b = _read_pred(base_slug)
    df_c = _read_pred(cand_slug)
    if df_b is None or df_c is None:
        return None

    df_meta = pd.read_parquet(meta_path, columns=["row_id", "y_true"])

    if "row_id" in df_b.columns:
        base_m = df_meta.merge(
            df_b[["row_id", "y_pred"]].rename(
                columns={"y_pred": "y_pred_base"}
            ),
            on="row_id",
        )
    else:
        base_m = df_meta.copy()
        base_m["y_pred_base"] = df_b["y_pred"].to_numpy(dtype=np.float32)

    if "row_id" in df_c.columns:
        merged = base_m.merge(
            df_c[["row_id", "y_pred"]].rename(
                columns={"y_pred": "y_pred_cand"}
            ),
            on="row_id",
        )
    else:
        merged = base_m
        merged["y_pred_cand"] = df_c["y_pred"].to_numpy(dtype=np.float32)

    return merged


def generate_demo_predictions(
    n_rows: int = 3000,
    seed: int = 42,
) -> dict[tuple[str, str], pd.DataFrame]:
    """Tao du lieu du doan gia lap chi dung cho kiem thu offline (--demo).

    Args:
        n_rows (int): So dong gia lap moi cap (Fold, Model).
        seed (int): Hat giong ngau nhien co dinh.

    Returns:
        dict[tuple[str, str], pd.DataFrame]: Anh xa (Fold, Model) sang
            DataFrame chua y_true, y_pred_base, y_pred_cand.
    """
    rng = np.random.default_rng(seed)
    folds = ("Fold_1", "Fold_2", "Fold_3")
    models = ("LightGBM", "XGBoost", "CatBoost")
    demo_map: dict[tuple[str, str], pd.DataFrame] = {}

    for f_idx, fold_label in enumerate(folds):
        n_short = int(n_rows * 0.786)
        n_long = n_rows - n_short
        y_short = rng.uniform(1.0, 168.0, size=n_short)
        y_long = rng.uniform(169.0, 900.0, size=n_long)
        y_true = np.concatenate([y_short, y_long])
        rng.shuffle(y_true)

        for m_idx, model_name in enumerate(models):
            noise_scale = np.where(
                y_true <= STRATUM_LIMIT_HOURS, 28.0, 220.0
            )
            err_b = rng.normal(
                loc=-5.0, scale=noise_scale + f_idx + m_idx
            )
            err_c = rng.normal(
                loc=-2.5, scale=(noise_scale * 0.88) + f_idx + m_idx
            )
            demo_map[(fold_label, model_name)] = pd.DataFrame(
                {
                    "y_true": y_true,
                    "y_pred_base": np.maximum(0.0, y_true + err_b),
                    "y_pred_cand": np.maximum(0.0, y_true + err_c),
                }
            )
    return demo_map


def has_real_predictions(pred_dir: Path) -> bool:
    """Kiem tra thu muc co chua it nhat mot file eval_meta_fold*.parquet.

    Args:
        pred_dir (Path): Thu muc detailed_predictions can kiem tra.

    Returns:
        bool: True neu ton tai file metadata thuc te.
    """
    if not pred_dir.is_dir():
        return False
    return any(pred_dir.glob("eval_meta_fold*.parquet"))


def run_statistical_suite(
    pred_dir: Path,
    base_slug: str,
    cand_slug: str,
    models: list[str],
    folds: list[str],
    loss_type: str = "abs",
    horizon: int = 1,
    asym_weight: float = DEFAULT_ASYM_WEIGHT,
    max_wilcoxon: int = DEFAULT_MAX_WILCOXON,
    force_demo: bool = False,
    output_csv: Path | None = None,
) -> pd.DataFrame:
    """Chay bo kiem dinh Wilcoxon & Diebold-Mariano cho nhieu Fold/Model.

    Args:
        pred_dir (Path): Thu muc chua detailed_predictions/.
        base_slug (str): Tien to thi nghiem baseline.
        cand_slug (str): Tien to thi nghiem ung vien.
        models (list[str]): Danh sach ten mo hinh can kiem dinh.
        folds (list[str]): Danh sach so fold ('1', '2', '3').
        loss_type (str): Ham mat mat ('abs', 'squared', 'asym').
        horizon (int): Do tre Newey-West HAC (h >= 1).
        asym_weight (float): Trong so phat som cho che do 'asym'.
        max_wilcoxon (int): Nguong lay mau cho Wilcoxon signed-rank.
        force_demo (bool): Ep chay du lieu gia lap de kiem thu offline.
        output_csv (Path | None): Duong dan luu ket qua CSV neu can.

    Returns:
        pd.DataFrame: Bang tong hop ket qua kiem dinh theo Fold/Model/Tang.
    """
    all_rows: list[dict[str, Any]] = []
    use_demo = force_demo or (not has_real_predictions(pred_dir))

    if use_demo:
        print(
            "[DEMO MODE] Chua co eval_meta_fold*.parquet trong "
            f"{pred_dir}. Dang chay kiem thu tren du lieu gia lap."
        )
        demo_data = generate_demo_predictions()
        for (fold_label, model_name), df_pair in demo_data.items():
            all_rows.extend(
                evaluate_pair_stratified(
                    y_true=df_pair["y_true"].to_numpy(),
                    y_pred_base=df_pair["y_pred_base"].to_numpy(),
                    y_pred_cand=df_pair["y_pred_cand"].to_numpy(),
                    fold_label=fold_label,
                    model_name=model_name,
                    loss_type=loss_type,
                    horizon=horizon,
                    asym_weight=asym_weight,
                    max_wilcoxon=max_wilcoxon,
                )
            )
    else:
        print(f"[REAL MODE] Dang nap du doan tu: {pred_dir}")
        for fold_num in folds:
            fold_label = f"Fold_{fold_num}"
            for model_name in models:
                df_pair = load_prediction_pair(
                    pred_dir=pred_dir,
                    base_slug=base_slug,
                    cand_slug=cand_slug,
                    model_name=model_name,
                    fold_num=fold_num,
                )
                if df_pair is None:
                    continue
                all_rows.extend(
                    evaluate_pair_stratified(
                        y_true=df_pair["y_true"].to_numpy(),
                        y_pred_base=df_pair["y_pred_base"].to_numpy(),
                        y_pred_cand=df_pair["y_pred_cand"].to_numpy(),
                        fold_label=fold_label,
                        model_name=model_name,
                        loss_type=loss_type,
                        horizon=horizon,
                        asym_weight=asym_weight,
                        max_wilcoxon=max_wilcoxon,
                    )
                )

    df_out = pd.DataFrame(all_rows)
    if output_csv is not None and not df_out.empty:
        output_csv.parent.mkdir(parents=True, exist_ok=True)
        df_out.to_csv(output_csv, index=False)
        print(f"[SAVED] Da ghi ket qua kiem dinh: {output_csv}")

    return df_out


def parse_args(argv: list[str]) -> argparse.Namespace:
    """Phan tich tham so dong lenh cho script kiem dinh thong ke.

    Args:
        argv (list[str]): Danh sach doi so dong lenh.

    Returns:
        argparse.Namespace: Doi tuong tham so da phan tich.
    """
    repo_root = Path(__file__).resolve().parents[2]
    default_pred_dir = (
        repo_root
        / "05_Output_Cac_Notebook"
        / "07_Runner_Song_Song_1_Baseline_M1_M2_M3"
        / "detailed_predictions"
    )

    parser = argparse.ArgumentParser(
        description=(
            "Kiem dinh Wilcoxon signed-rank va Diebold-Mariano "
            "cho ket qua du bao ETA DS317."
        )
    )
    parser.add_argument(
        "--pred-dir",
        type=Path,
        default=default_pred_dir,
        help="Thu muc chua eval_meta_fold*.parquet va pred_*.parquet.",
    )
    parser.add_argument(
        "--base-slug",
        default="00_baseline_b0",
        help="Slug thi nghiem baseline (mac dinh: 00_baseline_b0).",
    )
    parser.add_argument(
        "--cand-slug",
        default="m3_features_exp1_g1",
        help="Slug thi nghiem ung vien can so sanh.",
    )
    parser.add_argument(
        "--models",
        nargs="+",
        default=[
            "LightGBM",
            "XGBoost",
            "CatBoost",
            "Bi-LSTM",
            "PatchTST",
            "TFT",
            "ST-GNN",
        ],
        help="Danh sach mo hinh can kiem dinh.",
    )
    parser.add_argument(
        "--folds",
        nargs="+",
        default=["1", "2", "3"],
        help="Danh sach Fold can kiem dinh.",
    )
    parser.add_argument(
        "--loss-type",
        choices=("abs", "squared", "asym"),
        default="abs",
        help="Ham mat mat kiem dinh (abs, squared, asym).",
    )
    parser.add_argument(
        "--horizon",
        type=int,
        default=1,
        help="Do tre chan troi h (>= 1) cho Diebold-Mariano HAC.",
    )
    parser.add_argument(
        "--asym-weight",
        type=float,
        default=DEFAULT_ASYM_WEIGHT,
        help="Trong so phat som cho loss_type=asym.",
    )
    parser.add_argument(
        "--max-wilcoxon",
        type=int,
        default=DEFAULT_MAX_WILCOXON,
        help="So mau toi da cho Wilcoxon signed-rank.",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Ep chay thu nghiem tren du lieu gia lap.",
    )
    parser.add_argument(
        "--output-csv",
        type=Path,
        default=None,
        help="Duong dan file CSV xuat ket qua kiem dinh.",
    )
    return parser.parse_args(argv)


def main() -> int:
    """Diem vao chinh cua script kiem dinh Wilcoxon & Diebold-Mariano.

    Returns:
        int: Ma thoat (0 neu chay thanh cong).
    """
    args = parse_args(sys.argv[1:])
    df_res = run_statistical_suite(
        pred_dir=args.pred_dir,
        base_slug=args.base_slug,
        cand_slug=args.cand_slug,
        models=args.models,
        folds=args.folds,
        loss_type=args.loss_type,
        horizon=args.horizon,
        asym_weight=args.asym_weight,
        max_wilcoxon=args.max_wilcoxon,
        force_demo=args.demo,
        output_csv=args.output_csv,
    )
    if df_res.empty:
        print("[WARN] Khong co cap du lieu hop le de kiem dinh.")
        return 1

    preview_cols = [
        "Fold",
        "Model",
        "Stratum",
        "N_Obs",
        "MAE_Base",
        "MAE_Cand",
        "Delta_MAE",
        "Wilcoxon_p",
        "DM_Stat",
        "DM_p",
        "Sig_0_01",
    ]
    print(df_res[preview_cols].head(12).to_string(index=False))
    print(f"Tong so dong kiem dinh: {len(df_res)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
