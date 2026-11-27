# Kết Quả Đầu Ra: Tổng Hợp Xuất Số Liệu BTVN và Kiểm Kê Dữ Liệu (`06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/`)

Thư mục này lưu trữ toàn bộ 102 tệp kết quả (tổng dung lượng ~2.34 MB) được xuất từ notebook tổng hợp [`DS317_Tong_Hop_Xuat_So_Lieu_BTVN.ipynb`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_Tong_Hop_Xuat_So_Lieu_BTVN.ipynb).

---

## 1. Cấu Trúc 102 Tệp Tin Phân Loại Chuẩn Hóa

Kho lưu trữ được cấu trúc thành 11 thư mục con chuyên biệt, phân định rành mạch giữa số liệu đo lường, cấu hình tham số, trọng số mô hình và biểu đồ phân tích:

```text
06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/
├── BENCHMARK_3_VERSIONS/      <- 18 bảng CSV so sánh hiệu năng 3 phiên bản (RAW18, Base22, Prep27)
├── BENCHMARK_DS317_04_RAW_CC/ <- 5 bảng CSV đối chuẩn với mô hình Baseline Ridge thô
├── COMMON/                    <- 1 bảng CSV metadata thực thi pipeline tổng hợp
├── DAMA/                      <- 8 bảng CSV đo lường 6 chiều DAMA phân rã theo 4 Quý (Q1-Q4)
├── Hinh_Anh_Bieu_Do/          <- 12 tệp PNG biểu đồ chất lượng cao phục vụ BTVN & Báo cáo
├── IMPUTE_BENCHMARK/          <- 4 bảng CSV đánh giá trước và sau khi điền khuyết Group Median
├── RAW18_SPLIT/               <- 12 bảng CSV thống kê phân bố tập thô sau phân chia Time-based Split
├── RAW_PRE_SPLIT/             <- 16 bảng CSV thống kê toàn diện dữ liệu thô 256.94M dòng
├── REPORTS/                   <- 2 tệp báo cáo: Muc_6_5_6_6.md và run_manifest.json
├── TASK03_NO_DEST/            <- 12 bảng CSV đánh giá kịch bản không có thông tin cảng đến
├── TASK03_WITH_DEST/          <- 12 bảng CSV đánh giá kịch bản có thông tin cảng đến
├── WEATHER_39/                <- Khung thư mục kiểm kê hệ 39 thuộc tính (27 AIS + 12 RTMA)
└── README.md
```

---

## 2. Bảng Thống Kê 4 Nhóm Thành Phần Chuẩn Hóa

| Nhóm thành phần | Số lượng tệp | Định dạng | Nội dung chính |
| :--- | :---: | :---: | :--- |
| **Số liệu kết quả (`results/`)** | **60 tệp** | CSV | Bảng số liệu đo lường chất lượng 6 chiều DAMA theo quý, bảng đối chuẩn 3 phiên bản dữ liệu, bảng phân phối trước/sau split, bảng đánh giá điền khuyết. |
| **Tham số & Metadata (`parameters/`)** | **9 tệp** | JSON / CSV | Tệp cấu hình siêu tham số mô hình Ridge 3 phiên bản, metadata phạm vi tàu (`ship_scope_metadata.json`), bảng tổng hợp tham số. |
| **Trọng số mô hình (`saved_models/`)** | **8 tệp** | Joblib | 8 tệp trọng số mô hình Ridge Regression và Scaler tương ứng được huấn luyện trên các phiên bản dữ liệu khác nhau. |
| **Biểu đồ phân tích (`charts/`)** | **24 tệp** | PNG | 12 biểu đồ tại `Hinh_Anh_Bieu_Do/` và các biểu đồ phân phối hỗ trợ trực tiếp việc soạn thảo BTVN BT1-BT5 và Báo cáo Chương 3. |
| **Báo cáo tổng hợp (`reports/`)** | **2 tệp** | MD / JSON | Báo cáo phân tích chuyên sâu Mục 6.5 - 6.6 (`Muc_6_5_6_6.md`) và nhật ký chạy `run_manifest.json`. |

---

## 3. Luồng Đồng Bộ Tự Động

Script tự động [`dong_bo_ho_so_nop.py`](../dong_bo_ho_so_nop.py) đồng bộ toàn bộ các tệp số liệu và biểu đồ trong thư mục này sang thư mục nộp bài chính thức tại:
[`DS317_R11_Nhom03_HoSoNopDoAn/06_Results/BTVN_TongHop/`](../../DS317_R11_Nhom03_HoSoNopDoAn/06_Results/BTVN_TongHop/).

---

## 4. Phân Công Trách Nhiệm Thành Viên

- **Quách Tuấn Kiệt & Huỳnh Chí Kiên:** Trực tiếp trích xuất số liệu DAMA, bảng kiểm kê tài sản dữ liệu và các biểu đồ EDA từ thư mục này để nộp các bài tập về nhà BT1, BT2, BT3.
- **Võ Đình Kiên:** Lập trình notebook tổng hợp `DS317_Tong_Hop_Xuat_So_Lieu_BTVN.ipynb` và thẩm định tính toàn vẹn 102 tệp kết quả.
