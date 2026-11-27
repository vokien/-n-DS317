# Kết Quả Đầu Ra: Mô Hình Cơ Sở Baseline Ridge (`04_DS317_04_Baseline_Ridge/`)

Thư mục này lưu trữ đầy đủ 5 tệp kết quả chuẩn hóa từ quá trình huấn luyện mô hình cơ sở Ridge Regression trên tập dữ liệu thô complete-case trong notebook [`DS317_04_Huan_Luyen_Mo_Hinh_Co_So_Baseline.ipynb`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_04_Huan_Luyen_Mo_Hinh_Co_So_Baseline.ipynb).

---

## 1. Mục Đích và Vai Trò Đối Chuẩn (Benchmarking)

Mô hình Ridge Regression huấn luyện trên tập thô complete-case đóng vai trò là **mốc đối chuẩn sàn tối thiểu (Minimal Baseline Benchmark)** của toàn bộ đồ án:
1. **Thiết lập mốc đối chứng khoa học:** Đánh giá độ lỗi $MAE$, $RMSE$ và $R^2$ khi chưa qua bất kỳ bước tiền xử lý hay trích xuất đặc trưng phức tạp nào.
2. **Chứng minh giá trị gia tăng của Pipeline:** Làm cơ sở so sánh định lượng để chứng minh sự vượt trội của chuỗi Module tiền xử lý M1-M7 và các mô hình học máy phi tuyến nâng cao (GBDT: CatBoost, XGBoost, LightGBM).

---

## 2. Cấu Trúc 5 Tệp Tin Chuẩn Hóa Phân Loại

```text
04_DS317_04_Baseline_Ridge/
├── results/                                         <- 1 bảng CSV số liệu thực nghiệm
│   └── benchmark_results_raw_complete_case.csv      <- Kết quả đo lỗi MAE, RMSE, R2
├── parameters/                                      <- 2 tệp tham số cấu hình
│   ├── raw_baseline_metadata.json                   <- Siêu tham số mô hình & danh sách cột
│   └── scaler_readable.csv                          <- Giá trị trung bình & độ lệch chuẩn StandardScaler
├── saved_models/                                    <- 2 tệp nhị phân trọng số mô hình
│   ├── ridge_raw_cc_model.joblib                    <- Trọng số mô hình Ridge Regression
│   └── scaler_raw_cc.joblib                         <- Trọng số chuẩn hóa dữ liệu
└── README.md
```

### Chi Tiết Từng Tệp Tin:

| STT | Tên tệp tin | Phân loại | Định dạng | Nội dung và Ý nghĩa |
| :-: | :--- | :---: | :---: | :--- |
| 1 | `results/benchmark_results_raw_complete_case.csv` | **Số liệu** | CSV | Ghi nhận chi tiết kết quả đo lỗi: $MAE = 43.12h$, $RMSE = 88.54h$, $R^2 = 0.124$ trên tập thô complete-case làm mốc so sánh tối thiểu. |
| 2 | `parameters/raw_baseline_metadata.json` | **Tham số** | JSON | Lưu trữ cấu hình siêu tham số: hệ số điều chuẩn $\alpha = 1.0$, danh sách đặc trưng đầu vào, thời gian huấn luyện và phiên bản scikit-learn. |
| 3 | `parameters/scaler_readable.csv` | **Tham số** | CSV | Bảng tra cứu trực quan các hệ số chuẩn hóa $mean$ và $scale$ của từng thuộc tính. |
| 4 | `saved_models/ridge_raw_cc_model.joblib` | **Trọng số** | Joblib | Tệp nhị phân lưu trữ toàn bộ trạng thái trọng số hệ số góc ($\beta$) và hệ số chặn ($intercept$) của mô hình Ridge đã huấn luyện. |
| 5 | `saved_models/scaler_raw_cc.joblib` | **Trọng số** | Joblib | Đối tượng StandardScaler đã được fit trên tập dữ liệu huấn luyện thô. |

---

## 3. Luồng Đồng Bộ Sang Hồ Sơ Nộp Bài

Script tự động [`dong_bo_ho_so_nop.py`](../dong_bo_ho_so_nop.py) đồng bộ các tệp trên sang thư mục nộp bài chính thức:
- Tệp số liệu `results/` -> [`DS317_R11_Nhom03_HoSoNopDoAn/06_Results/Baseline_Ridge/`](../../DS317_R11_Nhom03_HoSoNopDoAn/06_Results/Baseline_Ridge/)
- Tệp tham số `parameters/` -> [`DS317_R11_Nhom03_HoSoNopDoAn/05_Model/04_Baseline_Ridge/parameters/`](../../DS317_R11_Nhom03_HoSoNopDoAn/05_Model/04_Baseline_Ridge/parameters/)
- Tệp trọng số `saved_models/` -> [`DS317_R11_Nhom03_HoSoNopDoAn/05_Model/04_Baseline_Ridge/saved_models/`](../../DS317_R11_Nhom03_HoSoNopDoAn/05_Model/04_Baseline_Ridge/saved_models/)

---

## 4. Phân Công Trách Nhiệm

- **Trần Hồng Lĩnh:** Trực tiếp huấn luyện mô hình cơ sở Ridge Regression và ghi nhận bảng kết quả.
- **Võ Đình Kiên:** Thẩm định tham số cấu hình và tích hợp vào quy trình đồng bộ hồ sơ nộp.
