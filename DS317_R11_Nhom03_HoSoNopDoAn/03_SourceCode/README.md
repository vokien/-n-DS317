# Mã Nguồn Chính Thức & Hướng Dẫn Tái Lập Môi Trường (`03_SourceCode/`)

Thư mục này chứa cấu hình môi trường thực thi, script kiểm định ý nghĩa thống kê, công cụ đồng bộ mã nguồn sạch từ [`02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/) và hướng dẫn chạy lại toàn bộ pipeline thực nghiệm của **Nhóm 03 (DS317.R11)**.

---

## 1. Thiết Lập Môi Trường

### Cách 1: Dùng `pip` + `requirements.txt` (Khuyến nghị trên Python 3.10 - 3.12)
```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# Linux / macOS:
# source .venv/bin/activate

pip install --upgrade pip
pip install -r DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/requirements.txt
```

### Cách 2: Dùng `conda` + `environment.yml`
```bash
conda env create -f DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/environment.yml
conda activate ds317_maritime_env
```

*(Lưu ý: Nếu huấn luyện lại 4 mô hình Deep Learning `Bi-LSTM`, `PatchTST`, `TFT`, `ST-GNN`, cài đặt thêm `torch>=2.2.0` tương ứng phiên bản CUDA/CPU của máy hoặc chạy trực tiếp trên Kaggle GPU `Tesla T4 x2`.)*

---

## 2. Cấu Trúc & Trình Tự Chạy Pipeline Thực Nghiệm

Mã nguồn gốc được duy trì tập trung tại [`02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/) để tránh nhân bản trùng lặp trong quá trình phát triển:

1. **Giai đoạn 1 - Tiền xử lý, Kiểm kê DAMA & Baseline Ridge ([`01_Pipeline_Tien_Xu_Ly_Va_BTVN/`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/)):**
   - `DS317_01_Pipeline_Tien_Xu_Ly_Du_Lieu.ipynb`: Chuẩn hóa luồng thô 320.78M pre-split / 256.94M `RAW18` sang `Base22` và `Prep27` (`92.68M` dòng).
   - `DS317_02_Kham_Pha_Kiem_Ke_Chat_Luong.ipynb`: Kiểm kê DAMA 6 chiều và thống kê phân tầng `RAW18` vs `Prep27`.
   - `DS317_03_Kiem_Chung_Lua_Chon_Dac_Trung.ipynb`: Kiểm chứng đa cộng tuyến Pearson & chọn lọc đặc trưng.
   - `DS317_04_Huan_Luyen_Mo_Hinh_Co_So_Baseline.ipynb`: Đối chứng tuyến tính `Dummy` & `Ridge` trên `RAW_CC`.
   - `DS317_05_Tich_Hop_Thoi_Tiet_RTMA_2025.ipynb`: Trích xuất sidecar thời tiết 16 cột (`weather_rtma_2025_sidecar`).
   - `DS317_Tong_Hop_Xuat_So_Lieu_BTVN.ipynb`: Tổng hợp số liệu kiểm kê phục vụ BTVN & báo cáo.
2. **Giai đoạn 2 - Thực nghiệm Ablation 7 Module Engine v2 ([`02_Runner_Song_Song_Chinh_Thuc_v2/`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/02_Runner_Song_Song_Chinh_Thuc_v2/)):**
   - `DS317_Runner_Song_Song_1_Baseline_M1_M2_M3.ipynb`: Chạy `00_Baseline` + `M1` + `M2` + `M3` qua 3-Fold Expanding Window trên Kaggle `T4 x2`.
   - `DS317_Runner_Song_Song_2_M4_M5_M6_M7.ipynb`: Chạy `M4` + `M5` + `M6` + `M7` qua 3-Fold Expanding Window.
3. **Giai đoạn 3 - Notebook tách lẻ từng module ([`03_Notebook_Tach_Le_Tung_Module/`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/03_Notebook_Tach_Le_Tung_Module/)):**
   - `DS317_Thuc_Nghiem_00_Baseline.ipynb` và `DS317_Thuc_Nghiem_M1..M7_*.ipynb` cho phép tái lập độc lập từng module.
4. **Giai đoạn 4 - Kiểm định ý nghĩa thống kê (`kiem_dinh_thong_ke_wilcoxon_dm.py`):**
   - Thực hiện kiểm định **Wilcoxon signed-rank test** và **Diebold-Mariano test (Harvey-Leybourne-Newbold)** trên `detailed_predictions/` qua từng Fold (`Fold_1..Fold_3`) và phân tầng `All / LE_168h / GT_168h`.

---

## 3. Chạy Kiểm Định Thống Kê (`kiem_dinh_thong_ke_wilcoxon_dm.py`)

```bash
# Chay thu nghiem tren du lieu demo (khi chua co file parquet trong detailed_predictions/)
python DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/kiem_dinh_thong_ke_wilcoxon_dm.py --demo

# Tu dong nap file that tu 05_Output_Cac_Notebook/ khi da co detailed_predictions/
python DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/kiem_dinh_thong_ke_wilcoxon_dm.py \
  --pred-dir 05_Output_Cac_Notebook/07_Runner_Song_Song_1_Baseline_M1_M2_M3/detailed_predictions \
  --base-slug 00_baseline_b0 \
  --cand-slug m3_features_exp1_g1 \
  --output-csv DS317_R11_Nhom03_HoSoNopDoAn/06_Results/wilcoxon_dm_m3_vs_b0.csv
```

---

## 4. Đồng Bộ Mã Nguồn Sạch Khi Đóng Gói Nộp Đồ Án

Để giữ kho Git gọn nhẹ trong lúc phát triển và chỉ sao chép toàn bộ 16 notebook vào `03_SourceCode/notebooks/` khi chốt nộp bài cuối kỳ, sử dụng [`dong_bo_ma_nguon.py`](dong_bo_ma_nguon.py):

```bash
# Xem truoc danh sach 16 notebook se sao chep (khong ghi file)
python DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/dong_bo_ma_nguon.py --dry-run

# Thuc hien sao chep ma nguon sach vao 03_SourceCode/notebooks/
python DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/dong_bo_ma_nguon.py
```
