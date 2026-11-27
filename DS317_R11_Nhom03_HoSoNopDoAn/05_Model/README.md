# 05 - Mô Hình Huấn Luyện, Tham Số & Trọng Số (`05_Model/`)

Thư mục này lưu trữ hệ thống tham số cấu hình mô hình (Parameters), siêu tham số (Hyperparameters), tệp chuẩn hóa (Scalers) và các tệp nhị phân trọng số mô hình đã huấn luyện (Saved Models) của **Nhóm 03 (Lớp DS317.R11)**.

---

## 1. Cấu Trúc Tổ Chức Chuẩn Hóa

Dữ liệu mô hình được tổ chức phân tầng rõ ràng giữa "Tham số cấu hình" (`parameters/`) và "Trọng số mô hình" (`saved_models/`):

```text
05_Model/
├── 04_Baseline_Ridge/                         <- Phân hệ mô hình cơ sở
│   ├── parameters/                            <- raw_baseline_metadata.json, scaler_readable.csv
│   └── saved_models/                          <- ridge_raw_cc_model.joblib, scaler_raw_cc.joblib
├── 07_Runner_Song_Song_1_Baseline_M1_M2_M3/   <- Phân hệ Runner 1
│   ├── parameters/                            <- 274 tệp (273 file *_meta.json + parameters_summary.csv)
│   └── saved_models/                          <- Gói nén runner1_saved_models.zip (72.98 MB, 273 weights)
├── 08_Runner_Song_Song_2_M4_M5_M6_M7/         <- Phân hệ Runner 2
│   ├── parameters/                            <- 274 tệp (273 file *_meta.json + parameters_summary.csv)
│   └── saved_models/                          <- Gói nén runner2_saved_models.zip (74.40 MB, 273 weights)
└── README.md
```

---

## 2. Bảng Thống Kê Tham Số và Trọng Số Đã Huấn Luyện

| Phân hệ thực nghiệm | Số lượng tham số (`parameters/`) | Số lượng trọng số (`saved_models/`) | Định dạng lưu trữ | Mô hình đại diện |
| :--- | :---: | :---: | :---: | :--- |
| **Baseline Ridge** | 2 tệp | 2 tệp | `.joblib`, `.json`, `.csv` | Scikit-learn Ridge Regression & StandardScaler |
| **Runner 1 (Baseline, M1, M2, M3)** | 274 tệp | 273 tệp (trong gói zip 72.98 MB) | `.cbm`, `.txt`, `.json`, `.pt`, `.joblib` | CatBoost, LightGBM, XGBoost, Random Forest, Ridge, Bi-LSTM |
| **Runner 2 (M4, M5, M6, M7)** | 274 tệp | 273 tệp (trong gói zip 74.40 MB) | `.cbm`, `.txt`, `.json`, `.pt`, `.joblib` | CatBoost AsymLoss, XGBoost, LightGBM, Conformal Models |
| **TỔNG CỘNG** | **550 tệp** | **548 tệp trọng số** | - | **Đầy đủ 100% ma trận thực nghiệm Engine v2** |

---

## 3. Quản Trị Trọng Số Lớn và Hướng Dẫn Tải Về

- **Tham số cấu hình:** Toàn bộ 550 tệp JSON/CSV tham số (`*_meta.json`, `parameters_summary.csv`) được commit đầy đủ trên GitHub để bất kỳ ai cũng có thể đọc cấu hình và tái lập mô hình.
- **Trọng số nhị phân lớn:**
  - Mô hình nhẹ Baseline Ridge (`ridge_raw_cc_model.joblib`) được lưu trực tiếp tại chỗ.
  - Các tệp trọng số lớn của Runner 1 và Runner 2 được đóng gói trong 2 gói zip chuẩn mực (`runner1_saved_models.zip` 72.98 MB và `runner2_saved_models.zip` 74.40 MB). Cả 2 gói nén này đều nằm dưới ngưỡng 100 MB của GitHub và có thể tải trực tiếp từ thư mục `05_Output_Cac_Notebook/` hoặc tải từ Google Drive của nhóm:
  - **Liên kết Google Drive chính thức:** [`Nhom_03.txt`](../../00_Quan_Ly_Va_Tai_Lieu_Chung/Nhom_03.txt)

---

## 4. Hướng Dẫn Nạp Mô Hình để Dự Báo (Inference Code)

Ví dụ mã Python nạp mô hình CatBoost đã huấn luyện để dự báo ETA:

```python
import catboost as cb
import json

# 1. Đọc tham số cấu hình
with open("05_Model/07_Runner_Song_Song_1_Baseline_M1_M2_M3/parameters/catboost_00_baseline_b0_f1_meta.json", "r") as f:
    metadata = json.load(f)
feature_cols = metadata["feature_cols"]

# 2. Nạp trọng số mô hình CatBoost
model = cb.CatBoostRegressor()
model.load_model("05_Output_Cac_Notebook/07_Runner_Song_Song_1_Baseline_M1_M2_M3/saved_models/catboost_00_baseline_b0_f1.cbm")

# 3. Dự báo ETA
# y_pred = model.predict(df[feature_cols])
```
