# Kết Quả Đầu Ra: Runner Song Song 2 - M4, M5, M6, M7 (`08_Runner_Song_Song_2_M4_M5_M6_M7/`)

Thư mục này lưu trữ toàn bộ 329 tệp kết quả (tổng dung lượng ~1.49 MB) cùng gói trọng số nén từ quá trình thực thi Runner 2 ([`DS317_Runner_Song_Song_2_M4_M5_M6_M7.ipynb`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/02_Runner_Song_Song_Chinh_Thuc_v2/DS317_Runner_Song_Song_2_M4_M5_M6_M7.ipynb)).

---

## 1. Cấu Trúc 5 Phân Nhóm Chức Năng Chuẩn Hóa

```text
08_Runner_Song_Song_2_M4_M5_M6_M7/
├── results/              <- 42 bảng CSV số liệu thực nghiệm đo lường lỗi
├── parameters/           <- 274 tệp tham số cấu hình (273 file *_meta.json + parameters_summary.csv)
├── execution_flags/      <- 13 tệp .flag ghi nhận tiến trình hoàn thành từng biến thể
├── saved_models/         <- Lưu trữ trọng số mô hình (gói runner2_saved_models.zip 74.40 MB)
├── detailed_predictions/ <- Khung lưu trữ bảng dự đoán chi tiết cấp hành trình (.parquet)
└── README.md
```

---

## 2. Danh Mục 13 Biến Thể Thực Nghiệm Đảm Nhiệm

Runner 2 phụ trách các phân hệ thực nghiệm chuyên sâu và tối ưu hóa giải pháp:

| Phân hệ thực nghiệm | Ký hiệu biến thể | Tên biến thể | Số tệp CSV results | Mô tả kỹ thuật và Thuật toán |
| :--- | :---: | :--- | :---: | :--- |
| **Module M4 (Thời tiết)** | `M4` | `m4_rtma_rtma_32` | 3 | Tích hợp 32 đặc trưng khí tượng NOAA RTMA 2025 (vận tốc gió ngược chiều, gió ngang, nhiệt độ, áp suất). |
| **Module M5 (Chọn đặc trưng)** | `M5-S1`<br>`M5-S2`<br>`M5-ST1`<br>`M5-ST2`<br>`M5-T1` | `m5_selection_s1_mi16_raw`<br>`m5_selection_s2_mi12_raw`<br>`m5_selection_st1_mi16_log1p`<br>`m5_selection_st2_mi12_log1p`<br>`m5_selection_t1_all20_log1p` | 15 | So sánh các chiến lược chọn lọc Mutual Information (top 16, top 12) kết hợp biến đổi hàm logarithm $log1p(x)$ cho các đặc trưng phân phối lệch. |
| **Module M6 (Mất mát bất đối xứng)** | `M6-A0.5`<br>`M6-A2.0`<br>`M6-V0C`<br>`M6-V1`<br>`M6-V2`<br>`M6-V3` | `m6_asymloss_a0.5`<br>`m6_asymloss_a2.0`<br>`m6_asymloss_v0c`<br>`m6_asymloss_v1`<br>`m6_asymloss_v2`<br>`m6_asymloss_v3` | 18 | Huấn luyện với hàm mất mát bất đối xứng (Asymmetric Loss) phạt nặng sai số trễ tàu (Underprediction) so với dự báo sớm (Overprediction) với các hệ số $\alpha \in \{0.5, 1.0, 2.0\}$. |
| **Module M7 (Conformal & Phân cụm)** | `M7` | `m7_intervals_m7_adaptive` | 4 | Dự báo khoảng tin cậy không tham số (Conformal Prediction) và phân cụm sai số thích ứng (kèm bảng phân cụm `*_m7_clusters.csv`). |
| **Master Summary** | `Master` | `runner2_master_*` | 2 | 2 bảng tổng hợp lớn đối chuẩn toàn bộ 13 biến thể x 7 mô hình: `runner2_master_horizons.csv` và `runner2_master_summary.csv`. |

---

## 3. Quản Trị Trọng Số và Tham Số

- **Tham số (`parameters/` - 274 tệp):** Chứa 273 tệp `*_meta.json` chi tiết từng mô hình ($13 \times 7 \times 3 = 273$) lưu trữ hệ số mất mát bất đối xứng `asym_alpha`, khoảng tin cậy conformal `conformal_q90`, siêu tham số mô hình và danh sách biến; cùng 1 bảng tổng hợp `parameters_summary.csv`.
- **Cờ thực thi (`execution_flags/` - 13 tệp):** 13 tệp `.flag` đảm bảo tính khép kín và an toàn của pipeline, cho phép tiếp tục chạy nối tiếp nếu phiên Kaggle bị gián đoạn.
- **Trọng số (`saved_models/`):** Toàn bộ 273 tệp nhị phân trọng số (`.pt`, `.cbm`, `.txt`, `.json`) được đóng gói thành tệp nén duy nhất `runner2_saved_models.zip` (dung lượng 74.40 MB, tuân thủ giới hạn < 100 MB của GitHub).

---

## 4. Phân Công Trách Nhiệm và Luồng Đồng Bộ

- **Võ Đình Kiên:** Trực tiếp thực thi Runner 2 trên Kaggle Kernel và đóng gói kết quả.
- **Nguyễn Hữu Bảo Lộc:** Khai thác số liệu M5 phục vụ Chương 4 và Chương 5 Báo cáo.
- **Trần Hồng Lĩnh:** Khai thác số liệu M6 và phân tích hiệu quả giảm thiểu chi phí trễ tàu ($Demurrage$).
- **Lê Sỹ Liêm:** Khai thác số liệu M7, trích xuất biểu đồ Conformal Prediction ($PICP_{90}$ vs $MPIW$) và bài toán quy đổi tài chính USD.
- **Đồng bộ tự động:** Script [`dong_bo_ho_so_nop.py`](../dong_bo_ho_so_nop.py) đồng bộ:
  - `results/` -> [`DS317_R11_Nhom03_HoSoNopDoAn/06_Results/Runner_v2/`](../../DS317_R11_Nhom03_HoSoNopDoAn/06_Results/Runner_v2/)
  - `parameters/` -> [`DS317_R11_Nhom03_HoSoNopDoAn/05_Model/08_Runner_Song_Song_2_M4_M5_M6_M7/parameters/`](../../DS317_R11_Nhom03_HoSoNopDoAn/05_Model/08_Runner_Song_Song_2_M4_M5_M6_M7/parameters/)
