# 06 - Kết Quả Thực Nghiệm & Bảng Số Liệu Đo Lường (`06_Results/`)

Thư mục này là kho dữ liệu thực nghiệm trung tâm của toàn bộ hồ sơ nộp đồ án **DS317 - Khai phá dữ liệu trong doanh nghiệp** của **Nhóm 03 (Lớp DS317.R11)**. Mọi bảng số liệu đánh giá, độ đo lỗi, kết quả kiểm định thống kê và biểu đồ phân tích chính thức đều được đồng bộ và lưu trữ tại đây.

---

## 1. Cấu Trúc 4 Phân Hệ Kết Quả Thực Nghiệm

```text
06_Results/
├── Baseline_Ridge/      <- 1 bảng CSV đo lỗi của mô hình cơ sở Baseline Ridge
├── Runner_v2/           <- 84 bảng CSV số liệu thực nghiệm chính thức Engine v2 (Runner 1 & Runner 2)
├── DAMA_26_Dac_Trung/   <- 29 tệp số liệu & biểu đồ kiểm toán 6 chiều chất lượng dữ liệu DAMA
├── BTVN_TongHop/        <- 102 tệp bảng biểu, biểu đồ kiểm kê dữ liệu 3 phiên bản & BTVN
└── README.md
```

---

## 2. Bảng Thống Kê Chi Tiết Các Tệp Kết Quả

| Phân hệ kết quả | Số lượng tệp | Định dạng | Nội dung chính và Vai trò trong Báo cáo |
| :--- | :---: | :---: | :--- |
| **`Baseline_Ridge/`** | 1 tệp | CSV | `benchmark_results_raw_complete_case.csv`: Mốc đối chuẩn tối thiểu trên tập dữ liệu thô ($MAE = 43.12h$, $RMSE = 88.54h$). Trích dẫn tại **Mục 5.1 Báo cáo**. |
| **`Runner_v2/`** | **84 tệp** | CSV | **Trọng tâm của đồ án (Engine v2):** Bao gồm đầy đủ kết quả của 7 mô hình x 13 biến thể x 3 Fold từ cả Runner 1 (42 CSV: `00_baseline_*`, `m1_*`, `m2_*`, `m3_*`, `runner1_master_*`) và Runner 2 (42 CSV: `m4_*`, `m5_*`, `m6_*`, `m7_*`, `runner2_master_*`). Trích dẫn tại **Mục 5.2 - 5.5 Báo cáo**. |
| **`DAMA_26_Dac_Trung/`** | **29 tệp** | CSV / PNG | Bảng tổng hợp điểm 6 chiều DAMA (`DAMA/`), từ điển 27 thuộc tính (`DICTIONARY/`), ma trận tương quan Pearson $r = +0.50971$ (`CORRELATION/`), bảng kiểm định ràng buộc (`VALIDATION/`) và 6 biểu đồ chất lượng cao (`CHARTS/`). Trích dẫn tại **Chương 3 Báo cáo** và tích hợp trên Web Demo. |
| **`BTVN_TongHop/`** | **102 tệp** | CSV / PNG / MD | 60 bảng CSV đối chuẩn 3 phiên bản dữ liệu (`RAW18`, `Base22`, `Prep27`), 24 biểu đồ PNG trực quan hóa, và báo cáo kiểm toán tổng hợp. Trích dẫn tại **BTVN BT1-BT5 và Phụ lục Báo cáo**. |
| **TỔNG CỘNG** | **216 tệp** | - | **Số liệu minh bạch, chuẩn xác, sẵn sàng kiểm tra chéo 100%** |

---

## 3. Bản Đồ Tra Cứu Số Liệu Cốt Lõi cho Thành Viên Viết Báo Cáo

Khi soạn thảo các mục phân tích trong Báo cáo Đồ án Cuối kỳ và Slide, các thành viên tra cứu trực tiếp theo bảng dưới đây:

- **Bảng tổng hợp đối chuẩn 7 mô hình:** Mở tệp `Runner_v2/runner2_master_summary.csv` và `Runner_v2/runner2_master_horizons.csv`.
- **Số liệu mô hình tốt nhất (CatBoost Engine v2):**
  - Tầng hữu dụng $\le 168.0$ giờ (`LE_168h`): $MAE \approx 21.64h$, $RMSE \approx 36.85h$, $R^2 \approx 0.621$.
  - Tầng toàn bộ (`All`): $MAE \approx 110.12h$, $RMSE \approx 205.40h$, $R^2 \approx 0.742$.
- **Số liệu kiểm định giả thuyết ý nghĩa thống kê:** Chạy script [`DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/kiem_dinh_thong_ke_wilcoxon_dm.py`](../03_SourceCode/kiem_dinh_thong_ke_wilcoxon_dm.py) để xuất các giá trị $p-value < 0.001$ so sánh CatBoost với Baseline B0.
- **Số liệu độ đo mất mát bất đối xứng (M6):** Tra cứu tại `Runner_v2/m6_asymloss_*_summary.csv` để thấy rõ tỷ lệ dự báo trễ tàu giảm từ 52.4% xuống còn 28.1% khi tăng hệ số phạt $\alpha$.
- **Số liệu độ phủ Conformal Prediction (M7):** Tra cứu tại `Runner_v2/m7_intervals_m7_adaptive_summary.csv` ghi nhận độ phủ thực tế $PICP_{90} \ge 90.2\%$ trên tập kiểm thử độc lập Quý 4.

---

## 4. Quy Chuẩn Đồng Bộ và Bảo Toàn Tính Toàn Vẹn

Thư mục này được đồng bộ tự động từ [`05_Output_Cac_Notebook/`](../../05_Output_Cac_Notebook/README.md) bằng lệnh:

```bash
python 05_Output_Cac_Notebook/dong_bo_ho_so_nop.py
```
