# PHÂN CÔNG KỊCH BẢN THỰC NGHIỆM 7 MODULE PIPELINE (CHIA 4 QUÝ & 7 MÔ HÌNH CHỐT)

**Học phần:** DS317 - Khai phá dữ liệu trong doanh nghiệp (UIT)
**Nhóm thực hiện:** Nhóm 03 (Lớp DS317.P11 / DS317.R11)
**Đề tài:** Dự báo thời điểm cập cảng của tàu biển thay thế ETA tự khai báo (*Prediction of Vessel Port Arrival Time Replacing Self-Reported ETA*)

---

## 1. Quy ước chung của Kịch bản Thực nghiệm (Zero-Leakage & Ablation Study)

1. **Phân chia 4 Quý độc lập (`q1.parquet`..`q4.parquet`):**
   - Toàn bộ các hành trình vắt qua biên giới quý (`CROSSING_Q1_Q2`, `Q2_Q3`, `Q3_Q4`) được loại bỏ trước khi tiền xử lý ($\text{Trips}(Q_i) \cap \text{Trips}(Q_j) = \emptyset$).
   - Chỉ riêng **Quý 1 ($Q_1$)** được Fit và tiền xử lý sẵn (`q1_imputation_artifacts.json`, `train_imputation_artifacts.json`). Các **Quý 2, 3, 4 ($Q_2, Q_3, Q_4$)** giữ nguyên giá trị khuyết `NaN` và chưa lọc biến mục tiêu `Target_Hours` để từng thành viên tự chạy bước tiền xử lý động theo đúng dữ liệu huấn luyện trước mốc đánh giá, bảo đảm tuyệt đối không rò rỉ dữ liệu tương lai (Zero Data Leakage).
2. **Tập đặc trưng đầu vào hợp lệ $X_{\text{baseline}}$ (20 đặc trưng từ bảng 27 cột):**
   - Loại bỏ tuyệt đối **5 cột gây Leakage/Metadata/ID** khỏi ma trận đầu vào $X$: `mmsi`, `trip_id`, `base_date_time`, `ata_time`, `Target_Hours`.
   - Loại bỏ **2 cột góc thô** đã có biến trực giao thay thế: `cog`, `heading` (chỉ giữ `cog_sin`, `cog_cos`, `heading_sin`, `heading_cos`).
   - Giữ **20 đặc trưng hợp lệ** làm chuẩn Baseline đầu vào: `longitude`, `latitude`, `sog`, `cog_sin`, `cog_cos`, `heading_sin`, `heading_cos`, `length`, `width`, `draft`, `cargo`, `Area_Proxy`, `Volume_Proxy`, `status`, `vessel_type`, `Is_Tanker`, `berth_lon`, `berth_lat`, `Dist_To_Berth_NM`, `imputation_flag`.
3. **7 Mô hình cố định (Chốt theo BT4):**
   - `XGBoost`, `CatBoost`, `LightGBM`, `Bi-LSTM`, `ST-GNN`, `PatchTST`, `TFT`.
4. **Nguyên tắc Ablation Study ("Cố định 6, Thử nghiệm 1"):**
   - Mỗi thành viên phụ trách 01 Module dưới đây, giữ cố định 6 Module còn lại theo **Cấu hình Baseline** và tự do sáng tạo, đề xuất, thử nghiệm nhiều kỹ thuật khác nhau trên Module của mình để tìm ra phương án cải thiện tốt nhất và đo lường chính xác mức đóng góp định lượng.

---

## 2. Bảng Phân công 7 Module - 7 Thành viên

| Module                                                  | Thành viên phụ trách             | Cấu hình Baseline (Đối chứng)                                                                                                                                        |
| :------------------------------------------------------ | :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **M1: Lọc Ngoại lai & Làm sạch Nhiễu AIS**              | **Huỳnh Chí Kiên**               | Bộ lọc biên tĩnh cơ bản ($1 \le \text{SOG} \le 40\text{ kn}$, $\text{status} \notin \{1, 5\}$, $v_{\text{implied}} \ge 1.62\text{ kn}$).                             |
| **M2: Điền khuyết Dữ liệu (Imputation)**                | **Đỗ Văn Lộc**                   | Điền khuyết thống kê bằng **Group Median 3 cấp** (`mmsi` $\rightarrow$ `vessel_type` $\rightarrow$ `Cargo/Tanker`) học từ $Q_1$, gán `cog`/`heading` thiếu bằng `0`. |
| **M3: Tạo Đặc trưng Mới (Feature Creation)**            | **Quách Tuấn Kiệt**              | Chỉ dùng 4 đặc trưng chế tác tĩnh cơ bản (`Dist_To_Berth_NM`, `Area_Proxy`, `Volume_Proxy`, `Is_Tanker`) và góc $\sin/\cos$.                                         |
| **M4: Làm giàu Dữ liệu Ngoại sinh (Thời tiết RTMA)**    | **Võ Đình Kiên** *(Nhóm trưởng)* | Chỉ sử dụng dữ liệu nội sinh từ bản tin AIS (không có thông tin khí tượng hải văn).                                                                                  |
| **M5: Chọn lọc Đặc trưng & Biến đổi Mục tiêu**          | **Nguyễn Hữu Bảo Lộc**           | Dùng toàn bộ 20 đặc trưng hợp lệ của tập $X_{\text{baseline}}$ và giữ nguyên phân phối gốc của `Target_Hours` (bị lệch phải mạnh).                                   |
| **M6: Cải tiến Hàm Mất mát Bất đối xứng (Custom Loss)** | **Trần Hồng Lĩnh**               | Huấn luyện với hàm mất mát đối xứng truyền thống (`MSE` / `L1 MAE`), coi sai số dự báo sớm và muộn ngang nhau.                                                       |
| **M7: Gom cụm Hành trình & Khoảng Sai số Thích ứng**    | **Lê Sỹ Liêm**                   | Sử dụng một khoảng sai số dự báo cố định toàn cục (Global Constant Error Margin) cho mọi tàu ở mọi cự ly.                                                            |

---

## 3. Cảnh báo Bắt buộc cho Module M6 (Trần Hồng Lĩnh): Rủi ro Bias với Hàm Loss & Độ đo Bất đối xứng

> [!WARNING]
> **Nguy cơ Circularity / Evaluation Bias khi huấn luyện và đánh giá bất đối xứng:**
> Khi sử dụng hàm mất mát bất đối xứng (ví dụ $\mathcal{L}_{\alpha}(e) = w(e) \cdot e^2$ với $e = \hat{y} - y$, phạt nặng lỗi dự báo sớm $e < 0$ bằng trọng số $1 + \alpha > 1$), nghiệm tối ưu sẽ tự động dịch chuyển kỳ vọng dự báo về phía dương ($\mathbb{E}[\hat{y} - y] > 0$, tức cộng thêm một khoảng đệm giờ dự phòng). Nếu dùng **chính độ đo phạt lệch cùng chiều** để chấm điểm và kết luận mô hình tốt hơn Baseline đối xứng, kết quả sẽ rơi vào thiên vị tự nghiệm (**Circularity Bias**): mô hình chỉ đang đẩy lệch dự báo sang phải chứ chưa chắc học được quy luật hành trình tốt hơn, thậm chí có thể làm suy giảm độ chính xác thực tế.

---

## 4. Mã nguồn Thực nghiệm Nền tảng (Baseline Code Reference)

Toàn bộ khung chạy thực nghiệm chuẩn đã được cài đặt tại:

- `Luu_tru_goc/3_Code/DS317_06_Thuc_Nghiem_Baseline_7_Module.ipynb`

### Cơ chế Vận hành & Cách Tùy biến cho 7 Thành viên

1. **Cơ chế Expanding Window 3 Fold (Zero Leakage):**
   - `Fold 1`: Train `Q1` $\rightarrow$ Đánh giá `Q2`
   - `Fold 2`: Train `Q1 + Q2` $\rightarrow$ Đánh giá `Q3`
   - `Fold 3`: Train `Q1 + Q2 + Q3` $\rightarrow$ Đánh giá `Q4` (*Blind Test*)
   - Bên trong mỗi Fold, tập Train được tách theo `trip_id` (`85% Fit / 15% InnerVal`) để dừng sớm (`Early Stopping`) và hiệu chỉnh tham số hậu xử lý, giữ nguyên tính độc lập của quý đánh giá.
2. **Tích hợp 7 Mô hình Chốt:**
   - GBDT: `LightGBM`, `XGBoost` (tự động bật GPU CUDA khi khả dụng), `CatBoost` (tự thử `task_type='GPU'`, fallback CPU). `ACTIVE_MODELS` mặc định chạy đủ 7 mô hình chốt; có thể rút gọn về 3 GBDT (`['LightGBM', 'XGBoost', 'CatBoost']`) nếu muốn sàng lọc nhanh đóng góp của từng module.
   - Deep Learning (PyTorch Zero-OOM): `Bi-LSTM`, `PatchTST`, `TFT`, `ST-GNN` (dùng cơ chế `build_causal_window_indices` + `LazyCausalTripDataset` cắt cửa sổ 12 bước tức thời theo mini-batch, không tràn RAM).
3. **Cách thành viên thử nghiệm kỹ thuật mới (Ablation Study):**
   - Kế thừa đúng class Module của mình (`Module1OutlierFilter` .. `Module7ClusteringIntervals`) và truyền vào hàm `run_expanding_window_experiment(..., mX_cls=MyCustomModuleX)` ở Cell 8, giữ nguyên 6 Module còn lại ở mặc định Baseline để xuất bảng đối chứng `*_folds.csv` và `*_summary.csv`. *(Riêng thành viên M2 có thể bật `RECOVER_Q1_RAW_NANS = True` tại Cell 1 nếu muốn thử nghiệm kỹ thuật điền khuyết mới từ trạng thái khuyết gốc trên cả 4 quý).*
