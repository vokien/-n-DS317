# Kho Lưu Trữ Output Tập Trung Các Notebook (`05_Output_Cac_Notebook/`)

Thư mục này tập trung toàn bộ kết quả đầu ra từ các notebook trong [`02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/) để nhóm quản lý tập trung, đối chiếu số liệu báo cáo và đồng bộ sang [`DS317_R11_Nhom03_HoSoNopDoAn/`](../DS317_R11_Nhom03_HoSoNopDoAn/README.md) bằng script [`dong_bo_ho_so_nop.py`](dong_bo_ho_so_nop.py).

## 1. Bảng Ánh Xạ Thư Mục Đích Theo Từng Notebook

| STT | Thư mục trong `05_Output_Cac_Notebook/` | Notebook nguồn tương ứng | Output cần chép vào sau khi chạy Kaggle |
| :-: | :--- | :--- | :--- |
| 1 | `01_DS317_01_Pipeline_Tien_Xu_Ly/` | [`DS317_01_Pipeline_Tien_Xu_Ly_Du_Lieu.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_01_Pipeline_Tien_Xu_Ly_Du_Lieu.ipynb) | Giải nén hoặc đặt dữ liệu theo 3 phiên bản `01_ban_tho_18_thuoc_tinh/`, `02_ban_nen_tang_22_thuoc_tinh/`, `03_ban_tien_xu_ly_27_thuoc_tinh/` (`q1..q4.parquet` bị `.gitignore` chặn) và `artifacts/` (`.json`, manifest nhẹ). |
| 2 | `02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/` | [`DS317_02_Kham_Pha_Kiem_Ke_Chat_Luong.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_02_Kham_Pha_Kiem_Ke_Chat_Luong.ipynb) | Giải nén `ds317_02_eda_dama_results.zip` vào các thư mục con `COMMON/`, `DICTIONARY/`, `DAMA/`, `EDA/`, `CORRELATION/`, `VALIDATION/`, `CHARTS/`. |
| 3 | `03_DS317_03_Kiem_Chung_Dac_Trung/` | [`DS317_03_Kiem_Chung_Lua_Chon_Dac_Trung.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_03_Kiem_Chung_Lua_Chon_Dac_Trung.ipynb) | Giải nén kết quả kiểm chứng vào `COMMON/`, `RAW2/`, `AUDIT/`, `TASK03/` (file `raw_sample.parquet` nặng sẽ bị `.gitignore` bỏ qua). |
| 4 | `04_DS317_04_Baseline_Ridge/` | [`DS317_04_Huan_Luyen_Mo_Hinh_Co_So_Baseline.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_04_Huan_Luyen_Mo_Hinh_Co_So_Baseline.ipynb) | Các file CSV, JSON metadata, scaler/model Ridge Baseline (`benchmark_results_raw_complete_case.csv`, `.json`, `.joblib`). |
| 5 | `05_DS317_05_Thoi_Tiet_RTMA_2025/` | [`DS317_05_Tich_Hop_Thoi_Tiet_RTMA_2025.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_05_Tich_Hop_Thoi_Tiet_RTMA_2025.ipynb) | Báo cáo kiểm tra ghép nối thời tiết RTMA, schema, biểu đồ và thống kê nhẹ (`weather_rtma_2025_sidecar/*.parquet` bị `.gitignore` chặn). |
| 6 | `06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/` | [`DS317_Tong_Hop_Xuat_So_Lieu_BTVN.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_Tong_Hop_Xuat_So_Lieu_BTVN.ipynb) | Đã chứa `102` file số liệu kiểm kê hiện có (`COMMON/`, `RAW_PRE_SPLIT/`, `RAW18_SPLIT/`, `IMPUTE_BENCHMARK/`, `DAMA/`, `TASK03_NO_DEST/`, `TASK03_WITH_DEST/`, `BENCHMARK_DS317_04_RAW_CC/`, `BENCHMARK_3_VERSIONS/`, `Hinh_Anh_Bieu_Do/`, `REPORTS/`) và khung chờ `WEATHER_39/`. |
| 7 | `07_Runner_Song_Song_1_Baseline_M1_M2_M3/` | [`DS317_Runner_Song_Song_1_Baseline_M1_M2_M3.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/02_Runner_Song_Song_Chinh_Thuc_v2/DS317_Runner_Song_Song_1_Baseline_M1_M2_M3.ipynb) | Đặt toàn bộ CSV kết quả (`00_baseline_*`, `m1_*`, `m2_*`, `m3_*`, `runner1_master_*`) vào `results/` (đã có `42` file), giải nén trọng số từ `runner1_saved_models.zip` vào `saved_models/`, và đặt `eval_meta_fold*.parquet` + `pred_*.parquet` vào `detailed_predictions/`. |
| 8 | `08_Runner_Song_Song_2_M4_M5_M6_M7/` | [`DS317_Runner_Song_Song_2_M4_M5_M6_M7.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/02_Runner_Song_Song_Chinh_Thuc_v2/DS317_Runner_Song_Song_2_M4_M5_M6_M7.ipynb) | Đặt toàn bộ CSV kết quả (`m4_*`, `m5_*`, `m6_*`, `m7_*`, `runner2_master_*`) vào `results/` (đã có `42` file), giải nén trọng số từ `runner2_saved_models.zip` vào `saved_models/`, và đặt `pred_*.parquet` vào `detailed_predictions/`. |
| 9 | `09_Notebook_Tach_Le_Tung_Module/` | Các notebook trong [`03_Notebook_Tach_Le_Tung_Module/`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/03_Notebook_Tach_Le_Tung_Module/) | Kết quả chạy thử/tinh chỉnh độc lập từng module (`00_Baseline/` đến `M7_Gom_Cum_Khoang_Sai_So/`). |

## 2. Quy Tắc Git & Dung Lượng File Lớn (> 100 MB)

- File cấu hình [`.gitignore`](../.gitignore) ở gốc kho lưu trữ tự động chặn các file nặng của Kaggle (`q1..q4.parquet`, `detailed_predictions/*.parquet`, `detailed_predictions/*.csv.gz`, `ata_catalog*.parquet`, `q1_mmsi_medians.parquet`, `raw_sample.parquet`, `runner*_saved_models.zip`, `runner*_results.zip`, `ds317_02_eda_dama_results.zip`, `*_v2_results.zip`).
- Toàn bộ các bảng tổng hợp `.csv`, metadata `.json`, sidecar `*_meta.json`, biểu đồ `.png`, báo cáo `.md`/`.txt` và preview `.csv` đều được phép commit lên GitHub.
- Khuyến nghị giải nén các gói `.zip` từ Kaggle trước khi đưa file vào đúng thư mục con và kiểm tra lại bằng `git status` trước khi `git push`.

## 3. Kiểm Kê & Đồng Bộ Sang Hồ Sơ Nộp Đồ Án

Sử dụng script [`dong_bo_ho_so_nop.py`](dong_bo_ho_so_nop.py) để kiểm kê số lượng file hiện có trong `05_Output_Cac_Notebook/` và đồng bộ các tệp trọng số/kết quả nhẹ sang [`DS317_R11_Nhom03_HoSoNopDoAn/05_Model/`](../DS317_R11_Nhom03_HoSoNopDoAn/05_Model/) và [`06_Results/`](../DS317_R11_Nhom03_HoSoNopDoAn/06_Results/):

```bash
# Kiểm kê và xem trước danh sách file sẽ đồng bộ (không ghi file)
python 05_Output_Cac_Notebook/dong_bo_ho_so_nop.py --dry-run

# Thực hiện đồng bộ thực tế các file nhẹ (< 95 MB)
python 05_Output_Cac_Notebook/dong_bo_ho_so_nop.py
```
