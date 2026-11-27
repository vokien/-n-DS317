# Kho Lưu Trữ Output Tập Trung Các Notebook (`05_Output_Cac_Notebook/`)

Thư mục này tập trung toàn bộ kết quả đầu ra từ các notebook trong [`02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/) để nhóm quản lý tập trung, đối chiếu số liệu báo cáo và đồng bộ sang [`DS317_R11_Nhom03_HoSoNopDoAn/`](../DS317_R11_Nhom03_HoSoNopDoAn/README.md) bằng script [`dong_bo_ho_so_nop.py`](dong_bo_ho_so_nop.py).

---

## 1. Nguyên Tắc Chuẩn Hóa Phân Loại "Số Liệu" và "Tham Số"

Để đảm bảo tính khoa học, khả năng tái lập thực nghiệm và sự minh bạch trong toàn bộ đồ án, các file đầu ra được phân định rành mạch thành 4 nhóm chuẩn hóa:

1. **Số Liệu Kết Quả Thực Nghiệm (`results/`):**
   - Chứa các bảng số liệu đo lường chất lượng dữ liệu, đánh giá mô hình, độ lỗi thực nghiệm, kiểm định giả thuyết (`*_summary.csv`, `*_folds.csv`, `*_horizons.csv`, `*_comparison.csv`).
   - Được định dạng dạng bảng chữ nhật, chuẩn UTF-8, sẵn sàng cho việc phân tích và vẽ biểu đồ.

2. **Tham Số & Cấu Hình Mô Hình (`parameters/`):**
   - Chứa toàn bộ siêu tham số (hyperparameters), danh sách đặc trưng đầu vào (`feature_cols`), chế độ nhãn mục tiêu (`target_mode`), hệ số mất mát bất đối xứng (`asym_alpha`), khoảng tin cậy conformal (`conformal_q90`), giá trị trung vị điền khuyết (`fit_medians`), và tham số chuẩn hóa (`scaler_mean`, `scaler_std`).
   - Định dạng chi tiết qua các file `*_meta.json` tương ứng cho từng biến thể, từng mô hình, từng fold và bảng tra cứu tập trung `parameters_summary.csv`.

3. **Trọng Số Mô Hình Huấn Luyện (`saved_models/`):**
   - Chứa các file nhị phân lưu trữ trạng thái trọng số mô hình đã huấn luyện: PyTorch state dict (`.pt`), CatBoost model (`.cbm`), LightGBM/XGBoost (`.txt`, `.json`), scikit-learn Ridge/Scaler (`.joblib`), kèm gói nén lưu trữ tương ứng (`.zip`).

4. **Dự Đoán Chi Tiết Cấp Hành Trình (`detailed_predictions/`):**
   - Chứa các bảng dự đoán chi tiết từng dòng dữ liệu và từng chuyến đi (`.parquet`) phục vụ kiểm toán sâu sai số theo khoảng cách và thời gian.

---

## 2. Bảng Ánh Xạ Thư Mục Đích Theo Từng Notebook

| STT | Thư mục trong `05_Output_Cac_Notebook/` | Notebook nguồn tương ứng | Hiện trạng & Phân loại cấu trúc chuẩn hóa |
| :-: | :--- | :--- | :--- |
| 1 | `01_DS317_01_Pipeline_Tien_Xu_Ly/` | [`DS317_01_Pipeline_Tien_Xu_Ly_Du_Lieu.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_01_Pipeline_Tien_Xu_Ly_Du_Lieu.ipynb) | Phân tầng theo 3 phiên bản dữ liệu `01_ban_tho_18_thuoc_tinh/`, `02_ban_nen_tang_22_thuoc_tinh/`, `03_ban_tien_xu_ly_27_thuoc_tinh/` (`q1..q4.parquet` bị `.gitignore` quản lý) và `artifacts/` (metadata cấu hình pipeline). |
| 2 | `02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/` | [`DS317_02_Kham_Pha_Kiem_Ke_Chat_Luong.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_02_Kham_Pha_Kiem_Ke_Chat_Luong.ipynb) | **29 files (0.59 MB)** giải nén từ `ds317_02_eda_dama_results.zip`: <br>- **Số liệu**: `DAMA/` (5 csv), `DICTIONARY/` (7 csv), `EDA/` (2 csv), `CORRELATION/` (2 csv), `VALIDATION/` (4 csv), `COMMON/` (1 csv). <br>- **Biểu đồ**: `CHARTS/` (6 png). <br>- **Cấu hình**: `run_manifest.json`, `README_results.txt`. |
| 3 | `03_DS317_03_Kiem_Chung_Dac_Trung/` | [`DS317_03_Kiem_Chung_Lua_Chon_Dac_Trung.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_03_Kiem_Chung_Lua_Chon_Dac_Trung.ipynb) | Khung thư mục phân tầng kiểm chứng `AUDIT/`, `COMMON/`, `RAW2/`, `TASK03/`. |
| 4 | `04_DS317_04_Baseline_Ridge/` | [`DS317_04_Huan_Luyen_Mo_Hinh_Co_So_Baseline.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_04_Huan_Luyen_Mo_Hinh_Co_So_Baseline.ipynb) | **5 files chuẩn hóa**: <br>- `results/`: `benchmark_results_raw_complete_case.csv` (số liệu thực nghiệm) <br>- `parameters/`: `raw_baseline_metadata.json`, `scaler_readable.csv` (tham số cấu hình) <br>- `saved_models/`: `ridge_raw_cc_model.joblib`, `scaler_raw_cc.joblib` (trọng số mô hình). |
| 5 | `05_DS317_05_Thoi_Tiet_RTMA_2025/` | [`DS317_05_Tich_Hop_Thoi_Tiet_RTMA_2025.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_05_Tich_Hop_Thoi_Tiet_RTMA_2025.ipynb) | Khung lưu trữ báo cáo kiểm tra ghép nối không gian/thời gian RTMA, schema đặc trưng và thống kê (`weather_rtma_2025_sidecar/` bị `.gitignore` quản lý). |
| 6 | `06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/` | [`DS317_Tong_Hop_Xuat_So_Lieu_BTVN.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_Tong_Hop_Xuat_So_Lieu_BTVN.ipynb) | **102 files (2.34 MB)** kiểm kê dữ liệu đầy đủ: <br>- **Số liệu**: 60 CSV (`BENCHMARK_3_VERSIONS/`, `DAMA/`, `RAW18_SPLIT/`, `RAW_PRE_SPLIT/`, `TASK03_NO_DEST/`, `TASK03_WITH_DEST/`, `IMPUTE_BENCHMARK/`). <br>- **Tham số**: 9 JSON/CSV (metadata 3 phiên bản, ship scope, full summary). <br>- **Trọng số**: 8 joblib (Ridge models & Scalers). <br>- **Biểu đồ**: 24 PNG (`Hinh_Anh_Bieu_Do/`). <br>- **Báo cáo**: `REPORTS/Muc_6_5_6_6.md`, `run_manifest.json`. |
| 7 | `07_Runner_Song_Song_1_Baseline_M1_M2_M3/` | [`DS317_Runner_Song_Song_1_Baseline_M1_M2_M3.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/02_Runner_Song_Song_Chinh_Thuc_v2/DS317_Runner_Song_Song_1_Baseline_M1_M2_M3.ipynb) | **316 files (1.48 MB)** phân định rõ: <br>- `results/`: **42 file CSV** số liệu thực nghiệm (`00_baseline_*`, `m1_*`, `m2_*`, `m3_*`, `runner1_master_*`). <br>- `parameters/`: **274 file** tham số cấu hình (273 file `*_meta.json` chi tiết + `parameters_summary.csv` tổng hợp 13 biến thể x 7 model x 3 fold). <br>- `saved_models/`: lưu trữ trọng số (gói `runner1_saved_models.zip` 72.98 MB chứa 273 file trọng số `.pt`, `.cbm`, `.txt`, `.json`). <br>- `detailed_predictions/`: khung lưu file dự đoán `.parquet`. |
| 8 | `08_Runner_Song_Song_2_M4_M5_M6_M7/` | [`DS317_Runner_Song_Song_2_M4_M5_M6_M7.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/02_Runner_Song_Song_Chinh_Thuc_v2/DS317_Runner_Song_Song_2_M4_M5_M6_M7.ipynb) | **329 files (1.49 MB)** phân định rõ: <br>- `results/`: **42 file CSV** số liệu thực nghiệm mới nhất (`m4_*`, `m5_*`, `m6_*`, `m7_*`, `runner2_master_*`). <br>- `parameters/`: **274 file** tham số cấu hình (273 file `*_meta.json` chi tiết + `parameters_summary.csv` tổng hợp 13 biến thể x 7 model x 3 fold). <br>- `execution_flags/`: **13 file `.flag`** theo dõi tiến trình thực thi. <br>- `saved_models/`: lưu trữ trọng số (gói `runner2_saved_models.zip` 74.40 MB chứa 273 file trọng số `.pt`, `.cbm`, `.txt`, `.json`). <br>- `detailed_predictions/`: khung lưu file dự đoán `.parquet`. |
| 9 | `09_Notebook_Tach_Le_Tung_Module/` | Các notebook trong [`03_Notebook_Tach_Le_Tung_Module/`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/03_Notebook_Tach_Le_Tung_Module/) | Phân tầng theo từng module độc lập (`00_Baseline/` đến `M7_Gom_Cum_Khoang_Sai_So/`). |

---

## 3. Quy Tắc Git & Dung Lượng File Lớn (> 100 MB)

- File cấu hình [`.gitignore`](../.gitignore) ở gốc kho lưu trữ tự động chặn các file nặng của Kaggle (`q1..q4.parquet`, `detailed_predictions/*.parquet`, `detailed_predictions/*.csv.gz`, `ata_catalog*.parquet`, `q1_mmsi_medians.parquet`, `raw_sample.parquet`, `runner*_saved_models.zip`, `runner*_results.zip`, `ds317_02_eda_dama_results.zip`, `*_v2_results.zip`).
- Toàn bộ các bảng số liệu đo lường `.csv`, cấu hình tham số `.json` (`*_meta.json`, `parameters_summary.csv`), biểu đồ `.png`, báo cáo `.md`/`.txt` và mô hình nhẹ `.joblib` đều được phép commit an toàn lên GitHub.
- Trước khi thực hiện `git push`, hãy chạy lệnh `python 05_Output_Cac_Notebook/dong_bo_ho_so_nop.py --dry-run` để kiểm soát dung lượng và tính toàn vẹn của hồ sơ nộp.

---

## 4. Kiểm Kê & Đồng Bộ Sang Hồ Sơ Nộp Đồ Án

Script [`dong_bo_ho_so_nop.py`](dong_bo_ho_so_nop.py) tự động quét toàn bộ cây thư mục output, kiểm kê số lượng file và hỗ trợ đồng bộ chuẩn hóa sang [`DS317_R11_Nhom03_HoSoNopDoAn/`](../DS317_R11_Nhom03_HoSoNopDoAn/):
- **Tham số mô hình (`parameters/`) & Trọng số (`saved_models/`):** Tự động chuyển vào [`DS317_R11_Nhom03_HoSoNopDoAn/05_Model/`](../DS317_R11_Nhom03_HoSoNopDoAn/05_Model/).
- **Số liệu đo lường thực nghiệm (`results/`):** Tự động chuyển vào [`DS317_R11_Nhom03_HoSoNopDoAn/06_Results/`](../DS317_R11_Nhom03_HoSoNopDoAn/06_Results/).

### Hướng Dẫn Sử Dụng:

```bash
# 1. Kiểm kê số lượng file và xem trước danh sách đồng bộ (không ghi đè file)
python 05_Output_Cac_Notebook/dong_bo_ho_so_nop.py --dry-run

# 2. Thực hiện đồng bộ thực tế toàn bộ file số liệu và tham số nhẹ (< 95 MB)
python 05_Output_Cac_Notebook/dong_bo_ho_so_nop.py
```
