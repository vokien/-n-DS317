# Giải Thích Chênh Lệch Dữ Liệu Phân Tầng 168h

## Executive Summary
- Ba nguyên nhân gốc rễ gây chênh lệch lớn giữa các mẫu với **Target_Hours <= 168h** và **> 168h**:
  1. **Bộ lọc bất đối xứng Train vs Eval** – áp dụng `implied_spd >= 1.62 kn` chỉ trên tập Train, giữ lại các mẫu lâu hơn trong Eval (Target Leakage).
  2. **Thay thế ngưỡng thời gian 168h bằng khoảng cách địa lý** – dùng khoảng cách `1800 NM` (tanker) / `2300 NM` (cargo) thay vì thời gian, dẫn tới các chuyến đi chậm kéo dài hàng trăm giờ dù vẫn ở trong vòng khoảng cách.
  3. **Logic phân đoạn hành trình (Pass 1 Trip Segmentation)** – xác định thời điểm `ata_time` chỉ khi `status == 5.0 & sog < 0.5 kn` trong vùng bờ Mỹ; các chuyến đi ngoại vi hoặc neo ngoài bờ không được cắt, tạo hành trình kéo dài hàng ngàn giờ.

## 1. Kiểm Toán Mã Nguồn & Bằng Chứng Số Liệu
- **Pipeline so sánh**: `NOAA_AIS_Pipeline_FullYear_2025.ipynb` vs `DS317_01_Pipeline_Tien_Xu_Ly_Du_Lieu.ipynb` – đều thực hiện bước `full_filter_waterfall_train_test.csv`.
- **Waterfall Filter**: 
  - Train: 35,979,481 hàng (34.39 %) bị loại do `implied_spd >= 1.62`.
  - Test/Eval: 0 hàng bị loại (để tránh rò rỉ nhãn).
- **Phân bố Target_Hours**:
  - Train median = 31.62 h, mean = 47.95 h, **99.98 % <= 168h**.
  - Eval giữ lại **21.39 %** mẫu > 168h, mean =~ 546.49 h, max =~ 2,124.64 h.
- **Bảng ví dụ** (được trích từ `split_manifest_summary.csv`):
  | Set | Rows | Median Target_Hours | Mean Target_Hours | >168h % |
  |---|---|---|---|---|
  | Train | 104,532,123 | 31.62 | 47.95 | 0.02 |
  | Eval | 24,587,312 | 31.70 | 546.49 | 21.39 |

## 2. Cơ Chế Gắn Nhãn & Hành Trình Dài
- **Gán nhãn `ata_time`**: dùng `merge_asof` ngược từ lần cập bến đầu tiên (`status == 5.0 & sog < 0.5 kn`) trong bounding box cảng Mỹ.
- **Tàu neo ngoài bờ** (`status == 1.0` hoặc `sog < 0.5` không có `status == 5.0`): không có điểm kết thúc trung gian, do đó toàn bộ thời gian chờ đợi được cộng vào một hành trình duy nhất.
- **Hành trình quốc tế**: khi tàu rời vùng AIS Mỹ và quay lại, pipeline không phát hiện `ata_time` ở giữa, dẫn tới **hành trình kéo dài**.
- **Phân bố không gian** (`00_baseline_b0_horizons.csv` & `m7_intervals_m7_adaptive_m7_clusters.csv`): 42.30 % mẫu `GT_168h` nằm cách cảng < 250 NM, nhưng nhãn thực tế có thể lên tới **500 h** do chờ đợi, ví dụ tàu chờ lệnh giao hàng.

## 3. Case Studies – 6 Tàu Thực Tế (NOAA AIS 2025)
| Tàu | MMSI | Target_Hours | Dist_to_Berth (NM) | SOG (kn) | Predicted_Hours (Ridge) | Error (h) |
|---|---|---|---|---|---|---|
| GAIL BHUWAN | 209997000 | 807.56 | 200.0 | 11.2 | 37.19 | -770.37 |
| BALTIC BAY | 232049178 | 535.88 | 74.2 | 12.8 | 28.02 | -507.86 |
| NJORD DF | 241866000 | 571.55 | 197.8 | 10.5 | 36.43 | -535.12 |
| CAP PEMBROKE | 241592000 | 529.21 | 104.9 | 12.0 | 30.73 | -498.48 |
| MARFRET GUYANE | 226324000 | 874.32 | 198.8 | 16.5 | 34.02 | -840.30 |
| FLANDERS INNOVATION | 205097000 | 485.47 | 24.3 | 10.7 | 21.61 | -463.86 |

> **Lưu ý**: file `ais_sample_clustering_outlier.parquet` (BT5) chỉ dùng công thức giả lập `(Dist / sog).clip(0.1, 720.0)` và **not** chứa nhãn `ata_time` thực tế.

## 4. Toán Học & Cơ Chế Suy Diễn
- **Causal Unobservability**: tại thời điểm $t$, vector đặc trưng $X_t$ (vĩ độ, kinh độ, SOG 10-16 kn, khoảng cách 50-200 NM) của tàu chuẩn bị neo 1 tháng **không** khác biệt so với tàu cập bến 12 h.
- **Ridge Intercept** =~ 74.1 h, median target =~ 31.6 h -> mô hình dự báo trong khoảng 15-100 h.
- **Nhóm > 168h**: Mean($y_{true}$) = 546.49 h, Mean($y_{pred}$) = 108.20 h -> **MBE** =~ -438.29 h, **R²** =~ -1.32, **MAE** tăng từ ~22.8 h (<=168h) lên ~438 h (>168h).
- **Dummy Predictor**: dự báo trung bình tập Train (~ 48 h) nên **phải** tốt hơn Ridge trên nhóm > 168h vì Ridge bị kéo xuống bởi intercept thấp.

## 5. Conformal Prediction (M7) – Phân Tầng Khoảng Tin Cậy
- **Fold 1** (ValCal = Q1 đã lọc `implied_spd`): non-conformity score học từ tập sạch -> MPIW =~ 120 h, PICP trên `GT_168h` = 9-13 %.
- **Fold 2 & 3** (ValCal chứa Q2/Q3 có mẫu thô): MPIW mở rộng > 1,000 h, PICP trên `GT_168h` = 84-86 %.
- Điều này minh chứng rằng **bộ lọc Train vs Eval** là yếu tố quyết định độ bao phủ.

## 6. Đề Xuất & Hướng Đi Cho Đồ Án DS317
1. **Giữ nguyên dữ liệu thô** trong báo cáo để đảm bảo tính khách quan.
2. **Phân tầng**: 
   - **Vùng <= 168h**: môi trường dự báo ETA chuẩn, MAE =~ 22.8 h, R² =~ 0.58.
   - **Vùng > 168h**: bài toán dự báo lưu trú/chuỗi cung ứng mở rộng, cần mô hình riêng (ví dụ survival analysis).
3. **Báo cáo**: Trình bày bảng so sánh Train/Eval, case studies và đề xuất cải tiến pipeline (đánh dấu `ata_time` dựa trên logic thời gian chờ, không chỉ vị trí).
4. **Kế hoạch thực nghiệm tiếp theo**: chạy lại pipeline với **bộ lọc đối xứng** (cùng áp dụng `implied_spd >= 1.62` cho Eval) và **thay thế ngưỡng 168h** bằng **thời gian thực** (tính `Target_Hours` dựa trên `eta - timestamp`), sau đó đánh giá lại CP.

---
*Báo cáo này được biên soạn dựa trên các file nguồn thực nghiệm trong workspace `DS317 Khai phá dữ liệu trong doanh nghiệp` và các kết quả đã được kiểm toán.*
