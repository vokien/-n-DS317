# Kết Quả Đầu Ra: Runner Song Song 1 - Baseline, M1, M2, M3 (`07_Runner_Song_Song_1_Baseline_M1_M2_M3/`)

Thư mục này lưu trữ toàn bộ 316 tệp kết quả (tổng dung lượng ~1.48 MB) cùng gói trọng số nén từ quá trình thực thi Runner 1 ([`DS317_Runner_Song_Song_1_Baseline_M1_M2_M3.ipynb`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/02_Runner_Song_Song_Chinh_Thuc_v2/DS317_Runner_Song_Song_1_Baseline_M1_M2_M3.ipynb)).

---

## 1. Cấu Trúc 4 Phân Nhóm Chức Năng Chuẩn Hóa

```text
07_Runner_Song_Song_1_Baseline_M1_M2_M3/
├── results/              <- 42 bảng CSV số liệu thực nghiệm đo lường lỗi
├── parameters/           <- 274 tệp tham số cấu hình (273 file *_meta.json + parameters_summary.csv)
├── saved_models/         <- Lưu trữ trọng số mô hình (gói runner1_saved_models.zip 72.98 MB)
├── detailed_predictions/ <- Khung lưu trữ bảng dự đoán chi tiết cấp hành trình (.parquet)
└── README.md
```

---

## 2. Danh Mục 13 Biến Thể Thực Nghiệm Đảm Nhiệm

Runner 1 đánh giá toàn diện 7 thuật toán học máy (Ridge, Random Forest, XGBoost, LightGBM, CatBoost, Bi-LSTM, Dummy) qua 13 biến thể thuộc chuỗi tiền xử lý:

| Phân hệ thực nghiệm | Ký hiệu biến thể | Tên biến thể | Số tệp CSV results | Mô tả kỹ thuật |
| :--- | :---: | :--- | :---: | :--- |
| **Baseline** | `B0` | `00_baseline_b0` | 3 | Mô hình cơ sở đối chuẩn trên tập dữ liệu sạch ban đầu. |
| **Module M1 (Ngoại lai)** | `M1-A`<br>`M1-B` | `m1_outlier_m1_a`<br>`m1_outlier_m1_b` | 7 | Lọc ngoại lai IQR tiêu chuẩn ($1.5 \times IQR$) so với IQR chuyên biệt theo phân loại tàu hàng hải (kèm tệp đối chiếu `m1_common_rows_comparison.csv`). |
| **Module M2 (Điền khuyết)** | `M2-V1`<br>`M2-V2`<br>`M2-V3`<br>`M2-V4` | `m2_impute_v1_solo_goc`<br>`m2_impute_v2_solo_noisuy`<br>`m2_impute_v3_solo_hinhhoc`<br>`m2_impute_v4_full_combined` | 12 | So sánh 4 chiến lược điền khuyết: V1 Group Median gốc, V2 Nội suy chuỗi thời gian, V3 Hình học cự ly bến, V4 Kết hợp toàn diện. |
| **Module M3 (Tạo đặc trưng)** | `M3-G1`<br>`M3-G2`<br>`M3-G3`<br>`M3-G4`<br>`M3-G5`<br>`M3-G6` | `m3_features_exp1_g1`<br>`m3_features_exp2_g2`<br>`m3_features_exp3_g3`<br>`m3_features_exp4_g4`<br>`m3_features_exp5_g5`<br>`m3_features_exp6_all` | 18 | Đánh giá 6 nhóm đặc trưng tương tác: G1 Động học, G2 Không gian bến, G3 Thân vỏ tàu, G4 Lịch sử di chuyển, G5 Tương tác phi tuyến, G6 Tổng hợp toàn bộ đặc trưng M3. |
| **Master Summary** | `Master` | `runner1_master_*` | 2 | 2 bảng tổng hợp lớn đối chuẩn toàn bộ 13 biến thể x 7 mô hình: `runner1_master_horizons.csv` và `runner1_master_summary.csv`. |

Mỗi biến thể đều có đủ bộ 3 tệp CSV chuẩn hóa:
- `*_summary.csv`: Tổng hợp trung bình và độ lệch chuẩn của các độ đo qua 3 Fold.
- `*_folds.csv`: Chi tiết độ đo của từng mô hình qua từng Fold (Fold 1, Fold 2, Fold 3).
- `*_horizons.csv`: Đánh giá phân tầng theo 3 mốc thời gian: `All`, `LE_168h` ($\le 7$ ngày), `GT_168h` ($> 7$ ngày).

---

## 3. Quản Trị Trọng Số và Tham Số & Đường Link Tải Kaggle Output

- **Đường link Kaggle Output trực tiếp:** [4 Thí nghiệm đầu (Kaggle Output)](https://www.kaggle.com/code/kienvo134/4-th-nghi-m-u/output) - Tải trực tiếp file trọng số nén `runner1_saved_models.zip` và các bảng dự đoán chi tiết `.parquet`.
- **Tham số (`parameters/` - 274 tệp):** Lưu trữ chi tiết 273 tệp `*_meta.json` cho từng mô hình cụ thể ($13 \times 7 \times 3 = 273$), ghi nhận danh sách đặc trưng đầu vào `feature_cols`, giá trị trung vị điền khuyết `fit_medians`, tham số chuẩn hóa và siêu tham số huấn luyện; cùng 1 bảng tra cứu tập trung `parameters_summary.csv`.
- **Trọng số (`saved_models/`):** Toàn bộ 273 tệp nhị phân trọng số (`.pt`, `.cbm`, `.txt`, `.json`) được đóng gói thành tệp nén duy nhất `runner1_saved_models.zip` (dung lượng 72.98 MB, tuân thủ giới hạn < 100 MB của GitHub).
- **Dự đoán chi tiết (`detailed_predictions/`):** Lưu trữ các file `.parquet` chi tiết từng dòng dữ liệu và từng chuyến đi phục vụ kiểm toán sâu sai số.

---

## 4. Phân Công Trách Nhiệm và Luồng Đồng Bộ

- **Võ Đình Kiên:** Trực tiếp thực thi Runner 1 trên Kaggle Kernel, kiểm soát bộ nhớ và đồng bộ kết quả.
- **Quách Tuấn Kiệt:** Khai thác số liệu M3 phục vụ Chương 4 và Chương 5 Báo cáo.
- **Huỳnh Chí Kiên & Đỗ Văn Lộc:** Khai thác số liệu M1 và M2 phục vụ đối chiếu thực nghiệm.
- **Đồng bộ tự động:** Script [`dong_bo_ho_so_nop.py`](../dong_bo_ho_so_nop.py) đồng bộ:
  - `results/` -> [`DS317_R11_Nhom03_HoSoNopDoAn/06_Results/Runner_v2/`](../../DS317_R11_Nhom03_HoSoNopDoAn/06_Results/Runner_v2/)
  - `parameters/` -> [`DS317_R11_Nhom03_HoSoNopDoAn/05_Model/07_Runner_Song_Song_1_Baseline_M1_M2_M3/parameters/`](../../DS317_R11_Nhom03_HoSoNopDoAn/05_Model/07_Runner_Song_Song_1_Baseline_M1_M2_M3/parameters/)
