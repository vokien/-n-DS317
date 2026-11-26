# Giải Thích Chênh Lệch Dữ Liệu Phân Tầng 168h

## Executive Summary
- Ba nguyên nhân gốc rễ gây chênh lệch lớn giữa phân tầng **Target_Hours <= 168h** (`LE_168h`, MAE 3-fold `23.78-24.94h`) và **> 168h** (`GT_168h`, MAE 3-fold `438.64-449.19h`):
  1. **Bộ lọc bất đối xứng Train vs Eval (`is_train=True` vs `is_train=False`):** Áp dụng ngưỡng vận tốc biểu kiến `implied_spd >= 1.62 kn` chỉ trên tập Train (`Q1` trong `DS317_01` và `df_fit`/`df_val_clean` trong Engine v2), giữ lại toàn bộ các chuyến đi chậm hoặc neo chờ dài hạn trong tập Eval thô để đảm bảo nguyên tắc không rò rỉ nhãn (Zero Target Leakage).
  2. **Thay thế ngưỡng thời gian 168h bằng khoảng cách địa lý:** Bộ lọc dùng khoảng cách `1,800 NM` (Tanker) / `2,300 NM` (Cargo) thay cho ngưỡng thời gian `Target_Hours <= 168.0`, dẫn tới các chuyến đi tốc độ thấp hoặc neo chờ ngoài bờ kéo dài hàng trăm giờ vẫn lọt vào phạm vi Eval.
  3. **Logic phân đoạn hành trình (Pass 1 Trip Segmentation):** Xác định thời điểm cập bến `ata_time` chỉ khi thỏa đồng thời `status == 5.0` và `sog < 0.5 kn` trong bounding box cảng Hoa Kỳ; các chuyến tàu neo đậu dài ngày (`status == 1.0`) hoặc rời vùng phủ AIS Hoa Kỳ rồi quay lại không được cắt chuyến trung gian, tạo thành hành trình kéo dài hàng trăm đến hàng ngàn giờ.

## 1. Kiểm Toán Mã Nguồn & Bằng Chứng Số Liệu
- **Pipeline đối chiếu:** `NOAA_AIS_Pipeline_FullYear_2025.ipynb` (bản cũ giới hạn `Target_Hours <= 168.0` trên toàn tập) so với `DS317_01_Pipeline_Tien_Xu_Ly_Du_Lieu.ipynb` (Engine v2 dùng `MIN_IMPLIED_SPEED_KNOTS = 1.62` thay cho ngưỡng `168h` và chỉ áp dụng khi `is_train=True`).
- **Thác lọc dữ liệu (`RAW18_SPLIT/full_filter_waterfall_train_test.csv`):**
  - **Train (`Q1-Q3`, `209,615,498` dòng ban đầu):** Sau bước `07_Target_gt_0` còn `104,604,472` dòng; tại bước `08_Implied_Spd_ge_1_62`, còn `68,626,591` dòng. Tổng số bản ghi bị loại bởi `implied_spd >= 1.62 kn` là **`35,977,881` dòng** (chiếm **`34.3942%`** lượng dòng ở bước `07_Target_gt_0`, tương đương `17.1638%` tập Train ban đầu).
  - **Test/Eval (`Q4`, `47,319,756` dòng ban đầu):** Sau bước `06_Dist_1800_2300_NM` và `07_Target_gt_0` còn `24,243,061` dòng; tại bước `08_Implied_Spd_ge_1_62` giữ nguyên **`24,243,061` dòng** (`0` dòng bị loại trên Eval).
- **Quy mô tập dữ liệu chuẩn theo phiên bản (`RAW18_SPLIT/dataset_versions_inventory.csv` & `raw18_moments_and_quantiles.csv`):**
  | Phiên bản / Tập dữ liệu | Số dòng Train (`Q1-Q3`) | Số dòng Eval (`Q4`) | Ghi chú đặc trưng phân bố `Target_Hours` |
  | :--- | ---: | ---: | :--- |
  | `01_ban_tho_18_thuoc_tinh` (trước lọc) | `209,615,498` | `47,319,756` | Train mean `371.01h` (median `92.10h`, max `6,447.65h`); Test mean `180.55h` (median `68.20h`, max `2,164.95h`) |
  | `02_ban_nen_tang_22_thuoc_tinh` / `03_ban_tien_xu_ly_27_thuoc_tinh` | `68,489,376` | `24,192,474` | Train đã lọc (`dummy_median = 31.595h`); Eval `Q4` giữ nguyên `H5_gt_168h` gồm `4,897,584` dòng (`20.24%`), mean nhóm `> 168h` là `546.49h` |
- **Tỷ lệ phân tầng trên Engine v2 (mẫu `2,500` chuyến/quý, `00_baseline_b0_folds.csv` & `runner1_master_summary.csv`):**
  - Fold 1 (`Q1 -> Q2`): `Eval_Rows = 3,543,951`, tỷ lệ `GT_168h = 21.01%` (`LE_168h = 78.99%`).
  - Fold 2 (`Q1+Q2 -> Q3`): `Eval_Rows = 3,632,498`, tỷ lệ `GT_168h = 23.43%` (`LE_168h = 76.57%`).
  - Fold 3 (`Q1+Q2+Q3 -> Q4`): `Eval_Rows = 3,482,238`, tỷ lệ `GT_168h = 19.74%` (`LE_168h = 80.26%`).
  - Trung bình 3 Fold: `GT_168h` chiếm **`21.39%`**, `LE_168h` chiếm **`78.61%`**.

## 2. Cơ Chế Gắn Nhãn & Hành Trình Dài
- **Gán nhãn `ata_time`:** Dùng `merge_asof` hướng tới tương lai từ lần cập bến đầu tiên thỏa `status == 5.0` và `sog < 0.5 kn` trong bounding box cảng Hoa Kỳ.
- **Tàu neo ngoài bờ (`status == 1.0` hoặc `sog < 0.5` nhưng không mang `status == 5.0`):** Không tạo mốc kết thúc hành trình trung gian, khiến toàn bộ thời gian neo chờ ngoài vùng neo đậu được cộng dồn vào `Target_Hours` của hành trình.
- **Hành trình rời vùng phủ AIS:** Khi tàu ra khỏi vùng thu phát AIS Hoa Kỳ rồi quay lại cập cảng sau nhiều tuần, pipeline ghép toàn bộ khoảng vắng mặt vào cùng một chuyến đi, kéo dài `Target_Hours` lên nhiều trăm giờ.
- **Phân bố không gian (`m7_intervals_m7_adaptive_m7_clusters.csv`):** Tính trung bình qua các fold/mô hình của `GT_168h`, các vùng cận cảng `< 250 NM` (`Stage_0_LE_25NM`: `31,448.67`, `Stage_1_25_75NM`: `61,908.44`, `Stage_2_75_250NM`: `121,234.67` so với `Stage_3_GT_250NM`: `292,676.44`) chiếm tới **`42.30%`** (`42.3034%`) tổng số bản ghi `GT_168h`. Điều này xác nhận phần lớn mẫu `> 168h` không phải do khoảng cách xa mà do thời gian neo chờ hoặc trễ tác nghiệp gần cảng.

## 3. Ghi Chú Về Trích Xuất Case Study Từng Chuyến
- Các bản ghi dự đoán chi tiết cấp dòng (`detailed_predictions/*.parquet`) của Runner 1 và Runner 2 chưa được lưu trong kho GitHub sau đợt chạy Kaggle đầu tiên. Do đó, báo cáo này không liệt kê bảng case study từng tàu khi chưa có tệp `detailed_predictions` đối soát trực tiếp.
- Runner 1 và Runner 2 đã được nâng cấp để tự động xuất `saved_models/` và `detailed_predictions/pred_{exp_id}_{model_name}_fold{fold}.parquet` (gồm `MMSI`, `trip_id`, `BaseDateTime`, `y_true`, `y_pred`, `residual`, `abs_error`, `is_le_168h`) ở lượt chạy kế tiếp, phục vụ trích xuất case study chính xác từng chuyến tàu.
- **Lưu ý về dữ liệu BT5:** Tệp `ais_sample_clustering_outlier.parquet` trong BT5 sử dụng nhãn mô phỏng `(Dist / v_implied).clip(0.1, 720.0)` để phục vụ phân cụm/ngoại lai, không chứa nhãn `ata_time` thực tế của bài toán dự báo ETA.

## 4. Toán Học & Cơ Chế Suy Diễn
- **Causal Unobservability:** Tại thời điểm quan trắc $t$, tàu chuẩn bị neo chờ ngoài khơi nhiều ngày có thể sở hữu đặc trưng tức thời $X_t$ (tọa độ gần cảng, `sog` 10-16 kn, `Dist_To_Berth_NM` 50-200 NM) giống hệt tàu cập bến bình thường sau 12-48h. Vì thông tin hàng đợi cầu bến và kế hoạch chủ tàu trong tương lai không nằm trong luồng AIS thô, mọi mô hình nhân quả chỉ quan sát quá khứ và hiện tại đều không thể phân biệt hai trạng thái này.
- **Độ lệch phân bố giữa tập huấn luyện và tầng `GT_168h`:**
  - Trên `03_ban_tien_xu_ly_27_thuoc_tinh` (`benchmark_metadata` & `BENCHMARK_3_VERSIONS/benchmark_horizons_prep27.csv`): `Dummy_Median` (`31.595h`) đạt `Bias = -514.8941h` và `MAE = 514.8941h` trên tầng `H5_gt_168h` (`N = 4,897,584`, `Underprediction = 100.0%`), suy ra `Mean(y_true | GT_168h) = 546.4891h` (`~546.49h`).
  - `Ridge_Streaming` trên `H5_gt_168h` đạt `MAE = 447.7835h`, `RMSE = 595.2917h`, `R2 = -1.3137`, `Bias = -438.2851h` (tương ứng `Mean(y_pred) = 108.2040h`, dự báo sớm `93.91%`).
- **Kết quả thực tế của Baseline `B0` (7 mô hình, trung bình 3 Fold trên Engine v2, `runner1_master_summary.csv`):**
  - Tầng `LE_168h` (`78.61%` tập Eval): `MAE = 23.78-24.94h` (`23.7802h` ở `PatchTST` đến `24.9443h` ở `ST-GNN`), `PICP_90 = 92.71%-93.87%`.
  - Tầng `GT_168h` (`21.39%` tập Eval): `MAE = 438.64-449.19h` (`438.6427h` ở `ST-GNN` đến `449.1927h` ở `PatchTST`), `MBE = -441.70h` đến `-426.30h`, `R2 = -1.38` đến `-1.31` (`-1.3766` đến `-1.3063`).

## 5. Conformal Prediction (M7) - Phân Tầng Khoảng Tin Cậy
- **Fold 1 (`ValCal` trích từ `Q1` đã lọc `implied_spd >= 1.62`):** Điểm bất phù hợp (non-conformity score) chỉ phản ánh nhiễu của các chuyến di chuyển bình thường (`MPIW = 120.55-129.96h`), nên khi đánh giá trên `GT_168h` ở `Q2`, `PICP_90` giảm xuống **`9.18%-13.36%`**.
- **Fold 2 & Fold 3 (`ValCal` trích từ đuôi `Q2`/`Q3` không lọc `implied_spd`):** `ValCal` chứa đầy đủ mẫu `GT_168h` thô, làm `MPIW` trên `GT_168h` tự động mở rộng lên **`1,013.80-1,095.55h`** và khôi phục `PICP_90` lên **`84.21%-86.24%`**.
- Điều này chứng minh trực tiếp rằng sự hiện diện của phân bố `GT_168h` trong tập hiệu chuẩn `ValCal` quyết định độ bao phủ của Conformal Prediction.

## 6. Đề Xuất & Hướng Xử Lý Trong Báo Cáo DS317
1. **Giữ nguyên giao thức Eval thô không lọc nhãn** khi báo cáo đối sánh 7 mô hình Engine v2 để bảo toàn tính trung thực và tránh rò rỉ nhãn (`Zero Target Leakage`).
2. **Báo cáo tách biệt 3 tầng (`All`, `LE_168h`, `GT_168h`):**
   - **Vùng `LE_168h` (`<= 168h`):** Phản ánh năng lực dự báo ETA tác nghiệp thực tế (`MAE = 23.78-24.94h` ở `B0`, giảm xuống `21.64h` ở `M5 T1_all20_log1p` `XGBoost`).
   - **Vùng `GT_168h` (`> 168h`):** Thể hiện rõ giới hạn vật lý do neo chờ dài hạn và rời vùng phủ AIS, cần bổ sung dữ liệu trạng thái cảng/lịch cập bến hoặc mô hình phân tách riêng giữa thời gian chạy biển và thời gian neo chờ.
3. **Trích xuất case study tự động ở lần chạy tới:** Sử dụng `detailed_predictions/*.parquet` từ Runner 1 & 2 mới để minh họa các chuyến neo chờ điển hình bằng số liệu truy vết trực tiếp.

---
*Báo cáo được đối soát trực tiếp từ các tệp nguồn trong `DS317_DoAn_Nhom03_TongHop/` (`RAW18_SPLIT/`, `BENCHMARK_3_VERSIONS/`, `Ket_Qua_Chay_Runner_1_va_2/`).*
