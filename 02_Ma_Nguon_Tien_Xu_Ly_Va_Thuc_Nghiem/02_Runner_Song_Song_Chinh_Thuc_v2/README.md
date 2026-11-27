# Phân Hệ Runner Song Song Chính Thức v2 (`02_Runner_Song_Song_Chinh_Thuc_v2/`)

Thư mục này chứa 2 Jupyter Notebook thực thi **Engine v2 chính thức** của đồ án môn học **DS317 - Khai phá dữ liệu trong doanh nghiệp**. Đây là nơi toàn bộ các thực nghiệm so sánh mô hình, nghiên cứu thành phần (Ablation Study) từ Module M1 đến Module M7 được lập trình và huấn luyện đồng bộ, khép kín và có khả năng tái lập 100%.

---

## 1. Cấu Trúc Hai Runner Song Song

Để tối ưu hóa thời gian tính toán và hạn chế giới hạn tài nguyên GPU/CPU trên nền tảng đám mây Kaggle (giới hạn 12 giờ/phiên), toàn bộ 13 biến thể thực nghiệm được phân tách cân bằng thành 2 Runner chạy song song độc lập:

| STT | Tên Notebook | Phân hệ thực nghiệm đảm nhiệm | Số biến thể | Thuật toán đánh giá | Tệp kết quả trong `05_Output_Cac_Notebook/` |
| :-: | :--- | :--- | :---: | :--- | :--- |
| 1 | `DS317_Runner_Song_Song_1_Baseline_M1_M2_M3.ipynb` | **Baseline & Tiền Xử Lý Dữ Liệu:**<br>• `Baseline B0`: Mô hình cơ sở.<br>• `Module M1`: Lọc ngoại lai IQR (M1-A tiêu chuẩn, M1-B hàng hải).<br>• `Module M2`: Điền khuyết (V1 gốc, V2 nội suy, V3 hình học, V4 kết hợp).<br>• `Module M3`: Tạo đặc trưng (G1 động học, G2 bến, G3 thân vỏ, G4 hành trình, G5 phi tuyến, G6 tất cả). | 13 biến thể | 7 mô hình:<br>1. Ridge Regression<br>2. Random Forest<br>3. XGBoost<br>4. LightGBM<br>5. CatBoost<br>6. Bi-LSTM / MLP<br>7. Dummy / Baseline | `07_Runner_Song_Song_1_Baseline_M1_M2_M3/`<br>• 42 CSV kết quả (`results/`)<br>• 274 tệp tham số (`parameters/`)<br>• Gói nén 273 trọng số `runner1_saved_models.zip` (72.98 MB) |
| 2 | `DS317_Runner_Song_Song_2_M4_M5_M6_M7.ipynb` | **Nâng Cao, Tối Ưu Hóa & Conformal:**<br>• `Module M4`: Thời tiết RTMA (32 biến).<br>• `Module M5`: Lựa chọn đặc trưng MI & log1p (S1, S2, ST1, ST2, T1).<br>• `Module M6`: Hàm mất mát bất đối xứng Asymmetric Loss ($\alpha=0.5, 2.0$, v0c, v1, v2, v3).<br>• `Module M7`: Phân cụm khoảng sai số và Conformal Prediction thích ứng (Adaptive Interval). | 13 biến thể | 7 mô hình tương tự Runner 1 (kèm kiểm định phân tầng `All`, `<= 168h`, `> 168h`) | `08_Runner_Song_Song_2_M4_M5_M6_M7/`<br>• 42 CSV kết quả (`results/`)<br>• 274 tệp tham số (`parameters/`)<br>• 13 tệp `execution_flags/`<br>• Gói nén 273 trọng số `runner2_saved_models.zip` (74.40 MB) |

---

## 2. Quy Chuẩn Kỹ Thuật Huấn Luyện (Training Protocol)

1. **Phân chia dữ liệu theo thời gian (Time-based Split):**
   - Tập huấn luyện & kiểm định nội bộ (Train & Validation): Dữ liệu Quý 1, Quý 2, Quý 3 năm 2025.
   - Tập kiểm định độc lập cuối cùng (Holdout Test / Eval): Dữ liệu trọn vẹn Quý 4 năm 2025 (`24,192,474` dòng) nhằm mô phỏng điều kiện triển khai thực tế của cảng biển, ngăn chặn 100% rò rỉ thông tin tương lai (Data Leakage).
2. **Kiểm định chéo theo thời gian (Time-based 3-Fold Cross Validation):**
   - Mỗi biến thể được huấn luyện và đánh giá độc lập qua 3 Fold tuần tự theo trục thời gian.
   - Tổng số mô hình được huấn luyện trong mỗi Runner: $13 \text{ biến thể} \times 7 \text{ mô hình} \times 3 \text{ Fold} = 273 \text{ mô hình}$.
   - Cả 2 Runner hoàn tất tổng cộng: $273 + 273 = 546 \text{ mô hình}$ được ghi nhận đầy đủ siêu tham số (`*_meta.json`) và trọng số (`.pt`, `.cbm`, `.txt`, `.json`).
3. **Phân tầng đánh giá sai số theo cự ly thời gian:**
   - `All`: Đánh giá trên toàn bộ dải thời gian dự báo ($0 < \text{Target\_Hours} \le 2,124.64h$).
   - `LE_168h`: Đánh giá trong phạm vi cửa sổ tác nghiệp hữu dụng của cảng biển ($\le 168.0$ giờ, tức 7 ngày).
   - `GT_168h`: Đánh giá ngoài phạm vi 7 ngày ($> 168.0$ giờ).

---

## 3. Luồng Ghi Nhận Dữ Liệu và Trọng Số

```text
[Kaggle Kernel: GPU Tesla T4]
       │
       ├── Huấn luyện 273 mô hình / Runner
       │      │
       │      ├──> results/ (42 CSV: *_summary.csv, *_folds.csv, *_horizons.csv)
       │      ├──> parameters/ (273 file *_meta.json + parameters_summary.csv)
       │      └──> saved_models/ (273 file binary trọng số -> nén zip)
       │
       ▼ (Đóng gói Output Kaggle)
[runner1_results.zip] & [runner1_saved_models.zip]
[runner2_results.zip] & [runner2_saved_models.zip]
       │
       ▼ (Giải nén & Tổ chức chuẩn hóa)
05_Output_Cac_Notebook/
├── 07_Runner_Song_Song_1_Baseline_M1_M2_M3/
└── 08_Runner_Song_Song_2_M4_M5_M6_M7/
       │
       ▼ (Đồng bộ hồ sơ nộp bằng dong_bo_ho_so_nop.py)
DS317_R11_Nhom03_HoSoNopDoAn/05_Model/ & 06_Results/
```

---

## 4. Phân Công Trách Nhiệm Thành Viên

- **Võ Đình Kiên:** Chủ trì lập trình cấu trúc chung 2 Runner, quản lý vòng lặp huấn luyện, cơ chế lưu trữ tham số/trọng số tự động và trực tiếp chạy 2 Runner trên Kaggle.
- **Huỳnh Chí Kiên & Đỗ Văn Lộc:** Tham gia thẩm định mã nguồn Runner 1 (Module M1, M2).
- **Quách Tuấn Kiệt:** Tham gia thẩm định cấu hình đặc trưng M3 trong Runner 1.
- **Nguyễn Hữu Bảo Lộc & Trần Hồng Lĩnh:** Tham gia thẩm định cấu hình M5 và M6 trong Runner 2.
- **Lê Sỹ Liêm:** Tham gia thẩm định cấu hình Conformal Prediction M7 trong Runner 2.

---

## 5. Hướng Dẫn Tái Lập (Replication Guide)

1. Tải notebook lên Kaggle Kernel (môi trường Python 3.10, GPU T4 x2 hoặc CPU).
2. Đính kèm tập dữ liệu tiền xử lý `03_ban_tien_xu_ly_27_thuoc_tinh` và sidecar thời tiết `RTMA_2025`.
3. Nhấn **Run All**. Thời gian chạy ước tính:
   - Runner 1: ~4.5 - 6.0 giờ CPU/GPU.
   - Runner 2: ~5.0 - 6.5 giờ CPU/GPU.
4. Sau khi chạy xong, toàn bộ 42 bảng số liệu, 274 file tham số và trọng số sẽ được tự động xuất ra thư mục Output của Kaggle.
