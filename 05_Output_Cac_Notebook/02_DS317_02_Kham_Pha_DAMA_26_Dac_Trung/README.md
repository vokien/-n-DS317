# Kết Quả Đầu Ra: Khám Phá Dữ Liệu và Đo Lường DAMA 26 Đặc Trưng (`02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/`)

Thư mục này chứa toàn bộ 29 tệp kết quả (tổng dung lượng ~0.59 MB) được trích xuất từ gói `ds317_02_eda_dama_results.zip` sau khi thực thi notebook [`DS317_02_Kham_Pha_Kiem_Ke_Chat_Luong.ipynb`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_02_Kham_Pha_Kiem_Ke_Chat_Luong.ipynb).

---

## 1. Cấu Trúc 29 Tệp Tin Phân Loại Chuẩn Hóa

Toàn bộ 29 tệp được tổ chức thành 7 phân nhóm chức năng:

```text
02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/
├── DAMA/             <- 5 bảng CSV đo lường 6 chiều chất lượng dữ liệu DAMA
├── DICTIONARY/       <- 7 bảng CSV từ điển dữ liệu 27 thuộc tính & bảng tra mã chuẩn
├── EDA/              <- 2 bảng CSV thống kê mô tả đặc trưng liên tục & biến phân loại
├── CORRELATION/      <- 2 bảng CSV ma trận tương quan Pearson & Spearman
├── VALIDATION/       <- 4 bảng CSV thẩm định ràng buộc logic, miền giá trị & địa không gian
├── COMMON/           <- 1 bảng CSV metadata thực thi pipeline
├── CHARTS/           <- 6 tệp PNG biểu đồ chất lượng cao phục vụ Báo cáo Chương 3
├── README_results.txt
├── run_manifest.json
└── README.md
```

---

## 2. Danh Mục Chi Tiết Từng Phân Nhóm Tệp Tin

### 1. Phân Nhóm Đo Lường DAMA (`DAMA/` - 5 tệp CSV):
- `dama_6_dimensions_overall.csv`: Bảng tổng hợp điểm đạt 6 chiều DAMA-DMBOK trên toàn bộ tập dữ liệu (Completeness, Consistency, Accuracy, Timeliness, Validity, Uniqueness).
- `dama_completeness_by_column.csv`: Đo lường tỷ lệ điền đầy chi tiết trên từng thuộc tính trước và sau khi điền khuyết.
- `dama_consistency_rules_breakdown.csv`: Đo lường mức độ tuân thủ 4 quy tắc logic hàng hải nghiệp vụ chéo.
- `dama_validity_ranges_breakdown.csv`: Tỷ lệ bản ghi thỏa mãn dải vật lý (WGS84, dải vận tốc $sog$, kích thước thân vỏ).
- `dama_uniqueness_keys_breakdown.csv`: Kiểm toán tỷ lệ trùng lặp theo cặp khóa $(MMSI, BaseDateTime)$.

### 2. Phân Nhóm Từ Điển Dữ Liệu (`DICTIONARY/` - 7 tệp CSV):
- `data_dictionary_27_features.csv`: Từ điển dữ liệu chi tiết 27 thuộc tính (Tên trường, Kiểu dữ liệu, Đơn vị, Ý nghĩa nghiệp vụ, Nguồn gốc).
- `feature_domain_definitions.csv`: Định nghĩa miền giá trị hợp lệ theo chuẩn hàng hải quốc tế ITU-R M.585.
- `feature_lineage_mapping.csv`: Sơ đồ phả hệ dữ liệu thể hiện nguồn gốc từ 18 biến thô sang 22 biến nền tảng và 27 biến tiền xử lý.
- `feature_null_imputation_policy.csv`: Chính sách điền khuyết cụ thể cho từng trường thông tin.
- `feature_scale_types.csv`: Phân loại thang đo (Ratio, Interval, Ordinal, Nominal).
- `vessel_type_code_mapping.csv`: Bảng ánh xạ mã số loại tàu AIS theo quy định USCG.
- `status_navigation_code_mapping.csv`: Bảng ánh xạ mã trạng thái hành hải (Under way, At anchor, Moored).

### 3. Phân Nhóm EDA và Tương Quan (`EDA/` & `CORRELATION/` - 4 tệp CSV):
- `eda_continuous_summary_statistics.csv`: Thống kê mô tả (Mean, Std, Median, IQR, Min, Max, Skewness, Kurtosis) của các biến liên tục.
- `eda_categorical_distributions.csv`: Tần số và tỷ trọng của các nhóm tàu và trạng thái hành hải.
- `pearson_correlation_matrix.csv`: Ma trận tương quan tuyến tính Pearson ghi nhận $r(Dist\_To\_Berth\_NM, Target\_Hours) = +0.50971$.
- `spearman_rank_correlation_matrix.csv`: Ma trận tương quan phi tuyến Spearman.

### 4. Phân Nhóm Kiểm Định & Biểu Đồ (`VALIDATION/` & `CHARTS/` - 10 tệp):
- 4 tệp CSV thẩm định ràng buộc logic, kiểm tra nhân quả thời gian và ranh giới không gian cảng biển Hoa Kỳ.
- 6 tệp PNG biểu đồ chất lượng cao minh họa phân phối, mức độ đầy đủ và tương quan phục vụ trực tiếp Báo cáo Chương 3 và ứng dụng BI Dashboard trên Demo.

---

## 3. Phân Công Trách Nhiệm và Đồng Bộ

- **Quách Tuấn Kiệt:** Chủ trì khai thác thư mục này để xây dựng tab BI Monitoring trên ứng dụng Demo và soạn thảo Mục 3.1, 3.2 Báo cáo Đồ án.
- **Đồng bộ tự động:** Script [`dong_bo_ho_so_nop.py`](../dong_bo_ho_so_nop.py) tự động sao chép các tệp số liệu trong thư mục này sang [`DS317_R11_Nhom03_HoSoNopDoAn/06_Results/DAMA_26_Dac_Trung/`](../../DS317_R11_Nhom03_HoSoNopDoAn/06_Results/DAMA_26_Dac_Trung/).
