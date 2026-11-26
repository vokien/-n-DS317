# BÁO CÁO KẾT QUẢ THỰC NGHIỆM ĐỐI CHỨNG ABLATION STUDY - MODULE M7
## Chuyên đề: Gom Cụm Hành Trình & Khoảng Sai Số Dự Báo Thích Ứng (Adaptive Prediction Intervals)

---

### THÔNG TIN ĐỊNH DANH THỰC NGHIỆM
- **Học viên thực hiện:** Lê Sỹ Liêm (MSSV: `24520951`)
- **Lớp học:** DS317.P11 - Khai phá Dữ liệu trong Doanh nghiệp
- **Đơn vị:** Nhóm 03 (Đồ án DS317 - UIT)
- **Đề tài:** Dự báo Thời điểm Cập bến (`Target_Hours`) thay thế ETA tự khai báo từ Dữ liệu Quỹ đạo Hàng hải NOAA AIS 2025
- **Module phụ trách:** **MODULE M7: Gom Cụm Hành Trình & Khoảng Sai Số Thích Ứng**
- **Notebook thực nghiệm có kết quả:** `DS317_M7_LeSyLiem_Clustering_Adaptive_Intervals.ipynb` (lưu trữ ngoài repo; xem bản chính thức Engine v2 trong repo tại [`DS317_Thuc_Nghiem_M7_Gom_Cum_Khoang_Sai_So.ipynb`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/03_Notebook_Tach_Le_Tung_Module/DS317_Thuc_Nghiem_M7_Gom_Cum_Khoang_Sai_So.ipynb))
- **Phương pháp thực nghiệm:** **Ablation Study ("Cố định 6, Thử nghiệm 1")** kết hợp **Expanding Window 3 Folds** qua 4 Quý (Q1 $\rightarrow$ Q4).

---

## 1. THIẾT LẬP THỰC NGHIỆM & DỮ LIỆU ĐẦU VÀO

Các tham số và điều kiện thực nghiệm được ghi nhận trực tiếp từ log thực thi của notebook:

- **Môi trường tính toán:** Kaggle Notebook, Accelerator GPU Tesla T4 (`HAS_CUDA = True`).
- **Thư mục dữ liệu nguồn:** `03_ban_tien_xu_ly_27_thuoc_tinh/` (gồm 4 tệp `q1.parquet`, `q2.parquet`, `q3.parquet`, `q4.parquet`).
- **Quy mô dữ liệu nạp vào thực tế:** Lấy mẫu trọn vẹn theo chuyến (`MAX_TRIPS_PER_QUARTER = 2500` trips/quý):
  - **Quý 1 (Q1):** 2,226,420 dòng dữ liệu ($2,500$ trips)
  - **Quý 2 (Q2):** 3,543,951 dòng dữ liệu ($2,500$ trips)
  - **Quý 3 (Q3):** 3,632,498 dòng dữ liệu ($2,500$ trips)
  - **Quý 4 (Q4):** 3,482,238 dòng dữ liệu ($2,500$ trips)
  - **Tổng cộng dữ liệu kiểm thử:** **12,885,107 dòng bản ghi AIS** (từ $10,000$ hành trình trọn vẹn).
- **Bộ 3 mô hình GBDT chủ lực:** `LightGBM`, `XGBoost`, `CatBoost`.
- **Thiết kế 3 Folds Expanding Window (Không rò rỉ dữ liệu tương lai):**
  - **Fold 1:** Huấn luyện trên $Q_1$ ($2.23\text{M}$ dòng) $\rightarrow$ Đánh giá trên $Q_2$ ($3.54\text{M}$ dòng).
  - **Fold 2:** Huấn luyện tích lũy $Q_1 + Q_2$ ($5.77\text{M}$ dòng) $\rightarrow$ Đánh giá trên $Q_3$ ($3.63\text{M}$ dòng).
  - **Fold 3:** Huấn luyện tích lũy $Q_1 + Q_2 + Q_3$ ($9.40\text{M}$ dòng) $\rightarrow$ Đánh giá trên $Q_4$ ($3.48\text{M}$ dòng - *Blind Test*).
- **Nguyên tắc Ablation Study:** Giữ cố định 100% cấu hình và tham số của 6 Module trước đó (M1 Outlier Filter, M2 Imputer, M3 Feature Creator, M4 Weather Enricher, M5 Feature Selector, M6 Loss & Post-hoc Shift). Chỉ thay đổi Module M7:
  - **Kịch bản 1 (Baseline M7 - Võ Đình Kiên):** Sử dụng khoảng sai số cố định toàn cục trên tập `InnerVal` (`Module7ClusteringIntervals`).
  - **Kịch bản 2 (Cải tiến M7 - Lê Sỹ Liêm):** Gom cụm thích ứng phân tầng 4 chặng cự ly hàng hải (`Dist_To_Berth_NM`) kết hợp nhóm tàu (`Is_Tanker`) (`Module7AdaptiveClusteringIntervals`).

---

## 2. BẢNG KẾT QUẢ ĐỐI CHỨNG ĐỊNH LƯỢNG (DỮ LIỆU ĐO THỰC TẾ)

### 2.1. Bảng Tổng Hợp Trung Bình Qua 3 Folds (Trích xuất từ Cell 9)

Số liệu đo lường trung bình qua 3 Folds được ghi nhận từ tệp xuất `m7_ablation_comparison_summary.csv`:

| Mô hình (Model) | MAE Trung bình (giờ) | RMSE Trung bình (giờ) | Baseline PICP 90% (%) | Baseline MPIW (giờ) | **M7 Adapt PICP 90% (%)** | **M7 Adapt MPIW (giờ)** | Mức thay đổi MPIW (%) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **XGBoost** | **113.2425** | **273.1417** | **73.9297%** | **108.7503h** | **66.6550%** | **115.9477h** | **-6.62%** |
| **CatBoost** | 113.7515 | 272.7526 | 74.0048% | 112.1273h | 66.4594% | 119.4243h | -6.51% |
| **LightGBM** | 113.9426 | 273.7924 | 73.7885% | 110.7125h | 66.2404% | 113.7550h | -2.75% |

*Ghi chú:*
- Cột `MPIW_Reduction_%` âm mang ý nghĩa độ rộng dải sai số bình quân toàn cục của M7 Adaptive rộng hơn Baseline từ $2.75\%$ đến $6.62\%$.
- Cột MAE và RMSE giống nhau giữa 2 kịch bản vì M7 là bước hậu xử lý ước lượng khoảng tin cậy, không làm thay đổi giá trị điểm dự báo $\hat{y}$.

---

### 2.2. Bảng Chi Tiết Kết Quả Từng Fold (Trích xuất từ Cell 8)

Dữ liệu chi tiết cho từng Fold từ các tệp `baseline_m7_global_folds.csv` và `m7_le_sy_liem_adaptive_folds.csv`:

#### A. Kịch bản Baseline M7 (Khoảng Cố Định Toàn Cục)
| Fold | Tập Đánh giá | Mô hình | MAE (h) | RMSE (h) | MBE Bias (h) | Baseline PICP (%) | Thời gian Train (s) |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **Fold 1** | $Q_2$ | LightGBM | 112.14 | 272.84 | -89.11 | 75.4% | 9.0s |
| | | XGBoost | 110.87 | 271.83 | -88.45 | 75.7% | 5.9s |
| | | CatBoost | 112.92 | 273.02 | -88.93 | 75.2% | 3.5s |
| **Fold 2** | $Q_3$ | LightGBM | 125.52 | 290.80 | -102.91 | 68.2% | 38.8s |
| | | XGBoost | 125.30 | 290.34 | -102.50 | 68.3% | 11.4s |
| | | CatBoost | 123.59 | 286.83 | -100.88 | 68.6% | 16.1s |
| **Fold 3** | $Q_4$ (*Blind*) | LightGBM | 104.17 | 257.73 | -88.56 | 77.7% | 53.5s |
| | | XGBoost | 103.55 | 257.25 | -88.58 | 77.8% | 20.2s |
| | | CatBoost | 104.74 | 258.41 | -88.19 | 78.2% | 12.6s |

#### B. Kịch bản M7 Cải Tiến (Khoảng Thích Ứng Phân Tầng Cụm - Lê Sỹ Liêm)
| Fold | Tập Đánh giá | Mô hình | MAE (h) | RMSE (h) | MBE Bias (h) | **M7 Adapt PICP (%)** | Thời gian Train (s) |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **Fold 1** | $Q_2$ | LightGBM | 112.14 | 272.84 | -89.11 | **69.0%** | 9.1s |
| | | XGBoost | 110.87 | 271.83 | -88.45 | **69.5%** | 5.4s |
| | | CatBoost | 112.92 | 273.02 | -88.93 | **68.8%** | 3.2s |
| **Fold 2** | $Q_3$ | LightGBM | 125.52 | 290.80 | -102.91 | **63.9%** | 39.2s |
| | | XGBoost | 125.30 | 290.34 | -102.50 | **64.3%** | 11.8s |
| | | CatBoost | 123.59 | 286.83 | -100.88 | **64.3%** | 16.1s |
| **Fold 3** | $Q_4$ (*Blind*) | LightGBM | 104.17 | 257.73 | -88.56 | **65.8%** | 54.5s |
| | | XGBoost | 103.55 | 257.25 | -88.58 | **66.1%** | 20.6s |
| | | CatBoost | 104.74 | 258.41 | -88.19 | **66.3%** | 12.9s |

---

## 3. PHÂN TÍCH KHÁCH QUAN SỐ LIỆU ĐO ĐƯỢC

### 3.1. Đánh giá Khách quan về Mô hình Hồi quy Điểm (Point Forecast)
1. **Mô hình có sai số thấp nhất:**
   - **XGBoost** đạt MAE thấp nhất trên cả 3 Fold: Fold 1 đạt $110.87\text{h}$, Fold 2 đạt $125.30\text{h}$, và Fold 3 đạt $103.55\text{h}$ (Trung bình: $113.24\text{h}$).
   - **CatBoost** bám sát với MAE trung bình $113.75\text{h}$, và đạt RMSE thấp nhất ($272.75\text{h}$).
   - **LightGBM** có MAE trung bình $113.94\text{h}$ và RMSE $273.79\text{h}$.
   - Chênh lệch MAE giữa mô hình tốt nhất (XGBoost) và thấp nhất (LightGBM) chỉ là $0.70$ giờ ($< 0.62\%$).
2. **Hiệu ứng tích lũy dữ liệu qua Expanding Window:**
   - Khi lượng dữ liệu huấn luyện tăng từ Fold 1 ($2.23\text{M}$ dòng) lên Fold 3 ($9.40\text{M}$ dòng), MAE của cả 3 mô hình giảm rõ rệt từ $\approx 111 - 112\text{h}$ xuống $\approx 103 - 104\text{h}$ (giảm khoảng $7 - 8$ giờ sai số).
3. **Hiện tượng Dự báo non có hệ thống (Systematic Underprediction):**
   - Chỉ số sai số trung bình (MBE - Mean Bias Error) ở tất cả các mô hình và các fold đều mang giá trị âm sâu: dao động từ $-88.19\text{h}$ đến $-102.91\text{h}$.
   - Điều này xác nhận rằng mô hình hồi quy tiêu chuẩn với hàm mất mát đối xứng có xu hướng dự báo thời gian hành trình ngắn hơn đáng kể so với thực tế cập cảng.

---

### 3.2. Đánh giá Khách quan về Khoảng Sai số Dự báo (Module M7)

1. **Về Tỷ lệ Bao phủ Thực tế (PICP 90%):**
   - **Mức độ đạt chuẩn lý thuyết:** Cả Baseline M7 lẫn M7 Adaptive đều chưa đạt ngưỡng tin cậy lý thuyết $90.0\%$ trên dữ liệu 4 Quý (Baseline đạt trung bình $73.8\% - 74.0\%$; M7 Adaptive đạt trung bình $66.2\% - 66.7\%$).
   - **Độ biến thiên giữa các Quý (Temporal Shift):**
     * Ở cả 2 phương pháp, **Fold 2 (Đánh giá trên $Q_3$)** đều có độ bao phủ thấp nhất (Baseline rớt xuống $68.2\% - 68.6\%$, M7 Adaptive rớt xuống $63.9\% - 64.3\%$), đồng thời là quý có MAE cao nhất ($123.6 - 125.5\text{h}$) và MBE âm sâu nhất ($-100.9\text{h}$ đến $-102.9\text{h}$).
     * **Fold 3 (Đánh giá trên $Q_4$ - Blind Test)** có độ bao phủ phục hồi cao nhất ở Baseline ($77.7\% - 78.2\%$).
2. **Về Độ rộng Dải Sai số Bình quân Toàn cục (MPIW):**
   - Baseline M7 giữ một dải cố định toàn cục với MPIW trung bình dao động từ $108.75\text{h}$ (XGBoost) đến $112.13\text{h}$ (CatBoost).
   - M7 Adaptive ghi nhận MPIW trung bình toàn cục dao động từ $113.76\text{h}$ (LightGBM) đến $119.42\text{h}$ (CatBoost).
3. **Nguyên nhân khách quan đo được từ cấu trúc dữ liệu:**
   - Trong M7 Adaptive, do đặc thù phân bố khoảng cách `Dist_To_Berth_NM` trong tập dữ liệu thực tế có lượng lớn mẫu nằm ở cự ly viễn dương ($> 250\text{ NM}$), khoảng sai số ở chặng này được mở rộng để hấp thụ bất định ngoài đại dương, khiến giá trị trung bình cộng MPIW toàn cục bị kéo tăng nhẹ ($2.75\% - 6.62\%$).
   - Đồng thời, do mô hình hồi quy gốc có độ chệch âm lớn ($\text{MBE} \approx -88\text{h}$ đến $-103\text{h}$), tâm dự báo $\hat{y}$ bị lệch mạnh sang trái. Khi phân cụm cục bộ không kết hợp bù độ chệch trung tâm, một phần các giá trị thực tế ở đuôi phải bị rơi ra ngoài dải tin cậy, dẫn đến PICP toàn cục của M7 Adaptive thấp hơn Baseline khoảng $7.2\% - 7.5\%$.

---

### 3.3. Đánh giá Khách quan về Thời gian Huấn luyện & Tối ưu Tài nguyên (Train_Sec)

| Mô hình | Thời gian Fold 1 ($2.23\text{M}$ dòng) | Thời gian Fold 2 ($5.77\text{M}$ dòng) | Thời gian Fold 3 ($9.40\text{M}$ dòng) | Tổng thời gian 3 Folds |
| :--- | :---: | :---: | :---: | :---: |
| **CatBoost** | **3.2s - 3.5s** | **16.1s** | **12.6s - 12.9s** | **~32.5s (Nhanh nhất)** |
| **XGBoost** | 5.4s - 5.9s | 11.4s - 11.8s | 20.2s - 20.6s | ~37.5s |
| **LightGBM** | 9.0s - 9.1s | 38.8s - 39.2s | 53.5s - 54.5s | ~102.0s |

- **CatBoost** có tốc độ huấn luyện trên GPU Tesla T4 nhanh nhất trong bài toán này (chỉ mất $\approx 32.5$ giây cho toàn bộ 3 Folds với hơn $17.4$ triệu lượt mẫu fit).
- **XGBoost** cân bằng tối ưu giữa thời gian huấn luyện ($\approx 37.5$ giây) và độ chính xác MAE tốt nhất ($113.24\text{h}$).
- Thời gian chạy của Module M7 (cả Baseline lẫn Adaptive) ở bước `fit` và `predict_intervals` chỉ chiếm từ vài mili-giây đến dưới 1 giây, hoàn toàn không làm gia tăng tổng thời gian huấn luyện của pipeline.

---

## 4. TỔNG KẾT TUÂN THỦ YÊU CẦU NHÓM TRƯỞNG

1. **Tuân thủ Kiến trúc Thực nghiệm:**
   - Thực hiện đầy đủ quy trình **Expanding Window 3 Folds** qua 4 Quý theo đúng phân công.
   - Tuân thủ nguyên tắc **Ablation Study**: Cố định tuyệt đối 6 module nền tảng, chỉ đánh giá sự khác biệt duy nhất từ Module M7.
2. **Khách quan & Minh bạch Dữ liệu:**
   - 100% các số liệu bảng biểu, chỉ số MAE, RMSE, MBE, PICP, MPIW trong báo cáo này được trích xuất trực tiếp từ kết quả thực thi notebook trên Kaggle.
   - Không tự ý thêm bớt các giả định hoặc suy đoán ngoài dữ liệu đo lường.
3. **Tệp Lưu Trữ Kèm Theo:**
   - Bảng tổng hợp đối chứng 3 Folds: `m7_ablation_comparison_summary.csv`
   - Bảng chi tiết 3 Folds kịch bản Baseline: `baseline_m7_global_folds.csv` & `baseline_m7_global_summary.csv`
   - Bảng chi tiết 3 Folds kịch bản M7 Cải tiến: `m7_le_sy_liem_adaptive_folds.csv` & `m7_le_sy_liem_adaptive_summary.csv`
   - Biểu đồ trực quan hóa: `m7_ablation_intervals_comparison.png`
