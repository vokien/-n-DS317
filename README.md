# DS317 - Khai Phá Dữ Liệu Trong Doanh Nghiệp (Nhóm 03 - DS317.R11)

Kho lưu trữ tổng hợp toàn bộ bài tập, tài liệu quản lý, mã nguồn tiền xử lý, kịch bản thực nghiệm Ablation 7 Module, báo cáo phân tích và kết quả thực nghiệm chính thức của **Nhóm 03** cho đề tài **Dự báo Thời gian Đến Cảng (Vessel ETA Prediction)** trên dữ liệu **NOAA AIS 2025** kết hợp thời tiết **NOAA RTMA 2025**.

---

## 1. Giới Thiệu Đề Tài & Kiến Trúc Thực Nghiệm

- **Bài toán:** Dự báo thời gian hành trình còn lại đến khi cập cảng (`Target_Hours`, đơn vị giờ) đối với tàu hàng (`Cargo`, VesselType `70-79`) và tàu chở dầu (`Tanker`, VesselType `80-89`) tại vùng biển Hoa Kỳ năm 2025.
- **Dữ liệu sử dụng:**
  - **NOAA AIS 2025 (Full Year, Q1-Q4):** `320,776,922` bản ghi thô trước chia (`pre-split`); `256,935,254` bản ghi thô sau chia (`01_ban_tho_18_thuoc_tinh`: `209,615,498` train + `47,319,756` test); và `92,681,850` bản ghi đã chuẩn hóa (`02_ban_nen_tang_22_thuoc_tinh` / `03_ban_tien_xu_ly_27_thuoc_tinh`: `68,489,376` train + `24,192,474` test).
  - **NOAA RTMA 2025 Sidecar:** Dữ liệu thời tiết hàng hải phục vụ Module 4 (`M4_RTMA`).
- **7 Mô hình đối sánh:** `LightGBM`, `XGBoost`, `CatBoost`, `Bi-LSTM`, `TFT`, `PatchTST`, `ST-GNN`.
- **Giao thức đánh giá (Engine v2 - 3-Fold Expanding Window):**
  - Fold 1: Train `Q1` -> Eval `Q2`
  - Fold 2: Train `Q1+Q2` -> Eval `Q3`
  - Fold 3: Train `Q1+Q2+Q3` -> Eval `Q4`
  - Tổng cộng **26 thí nghiệm** x **7 mô hình** = **182 cặp biến thể - mô hình** (**546 lượt chạy/fold**) hoàn tất trên Kaggle GPU `Tesla T4 x2`, chấm điểm tách biệt tầng `All`, `LE_168h` (`<= 168h`) và `GT_168h` (`> 168h`).

---

## 2. Cấu Trúc Thư Mục `DS317_DoAn_Nhom03_TongHop/`

```text
DS317_DoAn_Nhom03_TongHop/
├── README.md                                  # Tài liệu hướng dẫn & tổng quan repo
├── .gitignore                                 # Quy tắc loại trừ dữ liệu nặng & file tạm
├── 00_Quan_Ly_Va_Tai_Lieu_Chung/              # Kế hoạch tổng thể, phân công, định nghĩa hàm & related work
├── 01_Bai_Tap_Ve_Nha_Chinh_Thuc/              # Hồ sơ BT1 -> BT5 chính thức (kèm dữ liệu mẫu BT5 1.55 MB)
│   ├── BT1_Xac_Dinh_Bai_Toan/
│   ├── BT2_Do_Luong_Chat_Luong_Du_Lieu/
│   ├── BT3_Thuyet_Minh_De_Tai/
│   ├── BT4_Cong_Nghe_Khai_Pha_Du_Lieu/
│   └── BT5_Gom_Nhom_Va_Ngoai_Lai/
├── 02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/
│   ├── 01_Pipeline_Tien_Xu_Ly_Va_BTVN/        # Notebooks DS317_01..05 & tổng hợp số liệu BTVN
│   ├── 02_Runner_Song_Song_Chinh_Thuc_v2/     # 2 Runner song song chính thức chạy Engine v2
│   └── 03_Notebook_Tach_Le_Tung_Module/       # 8 Notebook tách lẻ độc lập (00_Baseline + M1..M7)
├── 03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/
│   ├── Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md
│   ├── Bao_cao_Modules/                       # Báo cáo chi tiết các module (M3, M5, M6)
│   └── Ket_Qua_Chay_Runner_1_va_2/            # 78 CSV kết quả (26 x 3 file) + master/M1/M7 CSVs
├── 04_So_Lieu_Kiem_Ke_Va_Bieu_Do/
│   ├── Hinh_Anh_Bieu_Do_Chung/                # Biểu đồ EDA, trực quan hóa & thống kê nhận xét
│   └── So_Lieu_Sau_Chay_Lai/                  # Bộ số liệu kiểm kê DAMA, benchmark & waterfall
└── DS317_R11_Nhom03_HoSoNopDoAn/              # Khung 8 thư mục nộp đồ án chuẩn môn học DS317
```

**Tài liệu điều phối & hoàn thiện cuối kỳ:**
- [Kế hoạch hoàn thiện và phân công công việc cuối kỳ (7 thành viên)](00_Quan_Ly_Va_Tai_Lieu_Chung/K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md)

- **Kế hoạch hoàn thiện cuối kỳ & Phân công hiện tại (7 thành viên):** [Kế hoạch hoàn thiện và phân công công việc cuối kỳ](00_Quan_Ly_Va_Tai_Lieu_Chung/K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md)

**Tài liệu điều phối & phân công giai đoạn cuối kỳ:**
- [Kế hoạch hoàn thiện và phân công công việc cuối kỳ](00_Quan_Ly_Va_Tai_Lieu_Chung/K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md)

**Kế hoạch triển khai giai đoạn cuối kỳ:**
- [Kế hoạch hoàn thiện và phân công công việc cuối kỳ (Nhóm 03)](00_Quan_Ly_Va_Tai_Lieu_Chung/K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md)

---

## 3. Thiết Lập Dữ Liệu Ngoài GitHub (Kaggle & Local)

Do giới hạn dung lượng tệp của GitHub (cảnh báo từ 50 MB và chặn push từ 100 MB), các tệp dữ liệu thô và tệp Parquet trung gian kích thước lớn **không được lưu trong Git** (đã cấu hình trong `.gitignore`):
- `NOAA_AIS_2025_RAW/` (31 tệp `.csv.zst`, 1 tệp `.zip`, 1 tệp `.tif`; tổng `13.15 GB`).
- Các tệp Parquet theo quý `q1.parquet`..`q4.parquet` trong các thư mục phiên bản (`01_ban_tho_18_thuoc_tinh`, `03_ban_tien_xu_ly_27_thuoc_tinh`, ...).
- `weather_rtma_2025_sidecar/` (`*.parquet` thời tiết RTMA 2025).

**Lưu ý ngoại lệ:** Tệp mẫu thực nghiệm BT5 `01_Bai_Tap_Ve_Nha_Chinh_Thuc/BT5_Gom_Nhom_Va_Ngoai_Lai/Ket_Qua_Thuc_Nghiem/ais_sample_clustering_outlier.parquet` (`1.55 MB`) vẫn được giữ nguyên trong repo.

Khi chạy trên **Kaggle Notebook**, các Runner v2 tự động tìm dữ liệu tại các đường dẫn đầu vào sau:
- **Bộ dữ liệu AIS Parquet:**
  - `/kaggle/input/noaa-ais-2025-full-year-tin-x-l-nn-tng`
  - `/kaggle/input/datasets/kienvo134/` (tìm đệ quy `/kaggle/input/**/{version_name}/q1.parquet` và `/kaggle/input/**/01_ban_tho_18_thuoc_tinh/q1.parquet`)
- **Bộ dữ liệu thời tiết RTMA 2025:**
  - `/kaggle/input/datasets/kienvo134/dataset-noaa-rtma-2025/`
  - `/kaggle/input/dataset-noaa-rtma-2025/weather_rtma_2025_sidecar`

Nếu chạy cục bộ trên máy cá nhân, thành viên cần đồng bộ các thư mục dữ liệu từ nguồn lưu trữ nhóm (xem liên kết tại `00_Quan_Ly_Va_Tai_Lieu_Chung/Nhom_03.txt`) và đặt cạnh thư mục notebook hoặc trỏ lại biến đường dẫn cấu hình đầu notebook.

---

## 4. Hướng Dẫn Chạy Mã Nguồn

1. **Tiền xử lý & Kiểm kê dữ liệu (tham khảo):**
   - Chạy lần lượt các notebook trong `02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/` (`DS317_01` đến `DS317_05`).
2. **Chạy toàn bộ thực nghiệm chính thức (Khuyến nghị trên Kaggle GPU T4 x2):**
   - Mở 2 session Kaggle song song và chạy hai notebook trong `02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/02_Runner_Song_Song_Chinh_Thuc_v2/`:
     - `DS317_Runner_Song_Song_1_Baseline_M1_M2_M3.ipynb` -> xuất `runner1_results.zip`, `saved_models/` và `detailed_predictions/`.
     - `DS317_Runner_Song_Song_2_M4_M5_M6_M7.ipynb` -> xuất `runner2_results.zip`, `saved_models/` và `detailed_predictions/`.
3. **Chạy hoặc kiểm thử riêng từng Module:**
   - Sử dụng các notebook trong `02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/03_Notebook_Tach_Le_Tung_Module/` (`DS317_Thuc_Nghiem_00_Baseline.ipynb` và `DS317_Thuc_Nghiem_M1..M7_*.ipynb`), thuận tiện khi thành viên phụ trách module cần tái lập hoặc tinh chỉnh độc lập.

---

## 5. Tóm Tắt Kết Quả Nổi Bật (Engine v2)

Chi tiết đầy đủ cho toàn bộ 182 cặp biến thể - mô hình được trình bày tại:
- [Báo cáo tổng hợp Ablation 7 Module](03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md)

| Hạng mục / Module | Biến thể & Mô hình tiêu biểu | Chỉ số nổi bật (Trung bình 3 Fold) | Ý nghĩa kỹ thuật |
| :--- | :--- | :--- | :--- |
| **Baseline B0 (All)** | `Bi-LSTM` .. `PatchTST` (7 mô hình) | MAE `113.12h - 114.85h`, RMSE `272.16h - 276.24h` | Thiết lập chuẩn đối chứng không rò rỉ nhãn trên tập Eval thô |
| **Baseline B0 (`LE_168h`)** | 7 mô hình (`y_true <= 168h`, ~78.61% tập Eval) | MAE `23.78h - 24.94h`, `PICP_90` `92.71% - 93.87%` | Dự báo hành trình ngắn/trung bình ổn định, độ phủ cao |
| **M3 - Tạo đặc trưng** | `EXP1_G1` (`XGBoost`) | MAE `110.12h`, RMSE `267.11h`, `R2 = 0.0610` | Đạt MAE toàn tập thấp nhất toàn hệ thống |
| **M4 - Thời tiết RTMA** | `RTMA_32` (`TFT`) | MAE `110.85h`, RMSE `268.39h`, `PICP_90 = 87.25%` | Thời tiết giúp cải thiện mạnh `TFT` so với B0 (`114.47h`) |
| **M5 - Chọn lọc & `log1p`** | `T1_all20_log1p` (`XGBoost`), `ST2_mi12_log1p` (`CatBoost`) | `LE_168h` MAE `21.64h` (`XGBoost`), `21.67h` (`CatBoost`) | Giảm sai số tầng ngắn hạn xuống mức thấp nhất hệ thống |
| **M6 - Mất mát bất đối xứng** | `V3` (`TFT`) | `AsymCost_w2_5 = 173,123.40`, `Underprediction = 44.52%` | Giảm phạt trễ so với `V0c` (`182,932.49`, `56.56%`) và B0 (`188,214.14`) |
| **M7 - Khoảng tin cậy thích nghi** | `M7_Adaptive` (7 mô hình) | `MPIW = 688.93h - 697.61h`, `PICP_90 = 83.91% - 84.48%` | Thu hẹp bề rộng khoảng tin cậy so với B0 (`730.71h - 738.32h`) |

---

## 6. Hướng Dẫn Đưa Lên GitHub (Dành Cho Thành Viên Quản Lý Repo)

Thực hiện ngay bên trong thư mục `DS317_DoAn_Nhom03_TongHop/`:

```bash
cd "DS317_DoAn_Nhom03_TongHop"
git init
git branch -M main
git status
git add .
git commit -m "Initialize DS317 Nhom 03 project repository (code, reports, results)"
git remote add origin <URL_REPO_GITHUB_CUA_NHOM>
git push -u origin main
```

Trước khi `git push`, khuyến nghị kiểm tra lại bằng `git status` để chắc chắn không có tệp `.parquet` lớn, `.zst`, hay tệp tạm `catboost_info/` lọt vào staging.
