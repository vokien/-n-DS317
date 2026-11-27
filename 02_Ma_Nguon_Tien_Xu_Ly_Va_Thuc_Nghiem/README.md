# Mã Nguồn Tiền Xử Lý và Thực Nghiệm (`02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/`)

Thư mục này là trung tâm kỹ thuật và mã nguồn tính toán toàn diện của **Nhóm 03 (Lớp DS317.R11)** cho đề tài **Dự báo Thời gian Đến Cảng (Vessel ETA Prediction)** trên dữ liệu **NOAA AIS 2025** và thời tiết **NOAA RTMA 2025**.

---

## 1. Cấu Trúc Tổng Thể 3 Phân Hệ Mã Nguồn

Hệ thống mã nguồn được tổ chức theo 3 tầng kiến trúc phục vụ các mục đích nghiên cứu khác nhau:

```text
02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/
├── 01_Pipeline_Tien_Xu_Ly_Va_BTVN/        <- 6 Notebook tiền xử lý dữ liệu lớn, kiểm kê DAMA & BTVN
├── 02_Runner_Song_Song_Chinh_Thuc_v2/     <- 2 Notebook Runner song song v2 (Engine v2 chính thức)
└── 03_Notebook_Tach_Le_Tung_Module/       <- 8 Notebook thực nghiệm tách lẻ phục vụ thẩm định độc lập
```

---

## 2. Bảng Mô Tả Chi Tiết 3 Phân Hệ

| STT | Phân hệ mã nguồn | Số lượng Notebook | Mục đích & Đặc tính kỹ thuật | Output tương ứng trong `05_Output_Cac_Notebook/` |
| :-: | :--- | :---: | :--- | :--- |
| 1 | [`01_Pipeline_Tien_Xu_Ly_Va_BTVN/`](01_Pipeline_Tien_Xu_Ly_Va_BTVN/README.md) | 6 Notebook | Xử lý Big Data phân tán 2-Pass trên dữ liệu thô (256.94M dòng), tạo 3 phiên bản dữ liệu (Bản thô 18, Bản nền tảng 22, Bản tiền xử lý 27), kiểm toán 6 chiều DAMA, tích hợp thời tiết RTMA và xuất số liệu BTVN. | `01_...` đến `06_...` |
| 2 | [`02_Runner_Song_Song_Chinh_Thuc_v2/`](02_Runner_Song_Song_Chinh_Thuc_v2/README.md) | 2 Notebook | **Engine v2 chính thức của đồ án**: Chạy song song 2 Runner huấn luyện 7 thuật toán (Ridge, RF, LightGBM, XGBoost, CatBoost, Bi-LSTM, Conformal) x 13 biến thể Ablation x 3-Fold Time-based Split. | `07_Runner_Song_Song_1_Baseline_M1_M2_M3/` & `08_Runner_Song_Song_2_M4_M5_M6_M7/` |
| 3 | [`03_Notebook_Tach_Le_Tung_Module/`](03_Notebook_Tach_Le_Tung_Module/README.md) | 8 Notebook | Phân rã độc lập từng module (Baseline B0, M1 Lọc ngoại lai IQR, M2 Điền khuyết, M3 Tạo đặc trưng, M4 Thời tiết, M5 Chọn lọc MI, M6 Hàm mất mát bất đối xứng, M7 Phân cụm khoảng sai số) giúp các thành viên chạy thử nghiệm cô lập mà không cần chạy cả Runner lớn. | `09_Notebook_Tach_Le_Tung_Module/` |

---

## 3. Luồng Xử Lý Dữ Liệu Tổng Thể (End-to-End Pipeline)

```text
[Dữ liệu thô NOAA AIS 2025: 256.94M dòng]
               │
               ▼  (Pass 1: Deduplication, Filtering, Kinematics)
[01_Pipeline: DS317_01] -> Tạo Bản Nền Tảng 22 cột (92.68M dòng sạch)
               │
               ▼  (Pass 2: Feature Engineering, Spatial Distances)
[01_Pipeline: DS317_01] -> Tạo Bản Tiền Xử Lý 27 cột (92.68M dòng)
               │
               ├────────────────────────────────────────┐
               ▼                                        ▼
[01_Pipeline: DS317_02 & 06]              [01_Pipeline: DS317_05]
Kiểm toán DAMA 6 chiều & Xuất số liệu     Tích hợp Thời tiết NOAA RTMA 2025
               │                                        │
               └───────────────────┬────────────────────┘
                                   │
                                   ▼
        ┌─────────────────────────────────────────────────────┐
        │  02_Runner_Song_Song_Chinh_Thuc_v2                  │
        │  ├── Runner 1: Baseline B0, M1 Outlier, M2 Impute,  │
        │  │             M3 Feature Creation (13 biến thể)    │
        │  └── Runner 2: M4 RTMA, M5 Feature Selection,       │
        │                M6 AsymLoss, M7 Conformal Prediction │
        └──────────────────────────┬──────────────────────────┘
                                   │
                                   ▼
[05_Output_Cac_Notebook/]: 781 tệp kết quả (Results, Parameters, Models)
                                   │
                                   ▼ (Đồng bộ chuẩn hóa)
[DS317_R11_Nhom03_HoSoNopDoAn/]: 05_Model/ & 06_Results/
```

---

## 4. Phân Công Trách Nhiệm Thành Viên

- **Võ Đình Kiên (Nhóm trưởng):** Chủ trì thiết kế kiến trúc Pipeline 2-Pass, tối ưu hóa PyArrow/Polars xử lý dữ liệu lớn, xây dựng module thời tiết RTMA M4 và điều phối chạy Runner 1 & Runner 2 trên Kaggle.
- **Huỳnh Chí Kiên:** Phụ trách Module M1 (Lọc ngoại lai IQR) và trực quan hóa EDA trên Kaggle.
- **Đỗ Văn Lộc:** Phụ trách Module M2 (Điền khuyết chuỗi thời gian Median 3 cấp).
- **Quách Tuấn Kiệt:** Phụ trách Module M3 (Tạo đặc trưng tương tác động học và hình học).
- **Nguyễn Hữu Bảo Lộc:** Phụ trách Module M5 (Lựa chọn đặc trưng qua Mutual Information và biến đổi log1p).
- **Trần Hồng Lĩnh:** Phụ trách Module M6 (Hàm mất mát bất đối xứng Asymmetric Loss).
- **Lê Sỹ Liêm:** Phụ trách Module M7 (Dự báo khoảng sai số Conformal Prediction và kiểm định thống kê).

---

## 5. Hướng Dẫn Tái Lập Môi Trường Thực Thi

Môi trường thực thi khuyến nghị: **Kaggle Kernel (GPU Tesla T4 hoặc CPU 4-core)** hoặc máy trạm có Python >= 3.10.

```bash
# 1. Cài đặt các thư viện phụ thuộc
pip install -r DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/requirements.txt

# 2. Để chạy lại kiểm định thống kê ý nghĩa p-value:
python DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/kiem_dinh_thong_ke_wilcoxon_dm.py

# 3. Để kiểm tra tính toàn vẹn của kết quả thực nghiệm:
python 05_Output_Cac_Notebook/dong_bo_ho_so_nop.py --dry-run
```
