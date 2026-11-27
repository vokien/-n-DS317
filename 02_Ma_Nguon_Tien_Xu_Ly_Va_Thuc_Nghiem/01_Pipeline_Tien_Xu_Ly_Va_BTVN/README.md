# Phân Hệ Pipeline Tiền Xử Lý Dữ Liệu và BTVN (`01_Pipeline_Tien_Xu_Ly_Va_BTVN/`)

Thư mục này chứa 6 Jupyter Notebook chịu trách nhiệm xử lý luồng dữ liệu lớn (Big Data Pipeline) từ tập dữ liệu thô NOAA AIS 2025 (`256.94M` bản ghi) cho đến khi hình thành các tập dữ liệu sạch chuẩn hóa, kiểm kê chất lượng DAMA 6 chiều, tích hợp thời tiết NOAA RTMA 2025 và xuất số liệu tổng hợp phục vụ các bài tập về nhà.

---

## 1. Danh Mục Các Notebook trong Phân Hệ

| STT | Tên Notebook | Dung lượng | Mục đích & Chức năng xử lý | Output tương ứng trong `05_Output_Cac_Notebook/` |
| :-: | :--- | :---: | :--- | :--- |
| 1 | `DS317_01_Pipeline_Tien_Xu_Ly_Du_Lieu.ipynb` | ~111 KB | **Pipeline 2-Pass cốt lõi:**<br>- *Pass 1:* Khử trùng lặp trượt 7 ngày (`SlidingBatchDeduplicator`), lọc bỏ neo đậu ($status \notin \{1,5\}$, $sog \ge 1.0$), kiểm tra dải vật lý -> Tạo Bản Nền Tảng 22 cột (`92,681,850` dòng).<br>- *Pass 2:* Tính cự ly hình học đến bến (`Dist_To_Berth_NM`), các biến tuần hoàn thời gian -> Tạo Bản Tiền Xử Lý 27 cột. | `01_DS317_01_Pipeline_Tien_Xu_Ly/` |
| 2 | `DS317_02_Kham_Pha_Kiem_Ke_Chat_Luong.ipynb` | ~76 KB | **Đo lường & Kiểm kê DAMA 6 chiều:** Đo định lượng Tính đầy đủ, Tính nhất quán, Tính chính xác ($r = +0.50971$), Tính kịp thời, Tính hợp lệ và Tính duy nhất trên 26 đặc trưng; trích xuất 6 biểu đồ phân phối và từ điển dữ liệu. | `02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/` (29 tệp) |
| 3 | `DS317_03_Kiem_Chung_Lua_Chon_Dac_Trung.ipynb` | ~350 KB | **Kiểm chứng & Lựa chọn đặc trưng:** Thẩm định đa cộng tuyến qua chỉ số VIF, tính toán Mutual Information và phân tích tương quan Spearman/Pearson giữa các biến đầu vào và nhãn `Target_Hours`. | `03_DS317_03_Kiem_Chung_Dac_Trung/` |
| 4 | `DS317_04_Huan_Luyen_Mo_Hinh_Co_So_Baseline.ipynb` | ~60 KB | **Mô hình cơ sở Baseline Ridge:** Huấn luyện mô hình Ridge Regression trên tập dữ liệu thô complete-case làm mốc đối chuẩn tối thiểu (Benchmark Baseline) cho toàn bộ đồ án. | `04_DS317_04_Baseline_Ridge/` (5 tệp) |
| 5 | `DS317_05_Tich_Hop_Thoi_Tiet_RTMA_2025.ipynb` | ~56 KB | **Tích hợp thời tiết NOAA RTMA:** Ghép nối không gian - thời gian (Spatial KD-Tree trên lưới kinh vĩ độ và Nearest Timestamp trong phạm vi 1 giờ) giữa dữ liệu tàu AIS và dữ liệu tái phân tích thời tiết NOAA RTMA 2025 (gió $u/v$, nhiệt độ, áp suất). | `05_DS317_05_Thoi_Tiet_RTMA_2025/` |
| 6 | `DS317_Tong_Hop_Xuat_So_Lieu_BTVN.ipynb` | ~191 KB | **Tổng hợp & Xuất số liệu BTVN:** Thực hiện kiểm kê chéo 3 phiên bản dữ liệu (`RAW18`, `Base22`, `Prep27`), đo lường theo 4 Quý (Q1 - Q4), xuất 60 bảng CSV và 24 biểu đồ PNG cho báo cáo BTVN BT1-BT5. | `06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/` (102 tệp) |

---

## 2. Luồng Dữ Liệu Chi Tiết

```text
[NOAA AIS 2025 RAW: 13.15 GB]
             │
             ▼
[DS317_01_Pipeline_Tien_Xu_Ly_Du_Lieu.ipynb]
   │
   ├──> Pass 1: Deduplication + Kinematic Filter -> 02_ban_nen_tang_22_thuoc_tinh (92.68M dòng)
   └──> Pass 2: Spatial Math + Feature Gen       -> 03_ban_tien_xu_ly_27_thuoc_tinh (92.68M dòng)
             │
             ├─────────────────────────────────────────────────┐
             ▼                                                 ▼
[DS317_02_Kham_Pha_Kiem_Ke...]               [DS317_05_Tich_Hop_Thoi_Tiet_RTMA...]
Xuất 29 file DAMA, Dict & Biểu đồ            Ghép nối gió, sóng, áp suất RTMA
             │                                                 │
             └────────────────────────┬────────────────────────┘
                                      │
                                      ▼
                    [DS317_Tong_Hop_Xuat_So_Lieu_BTVN.ipynb]
                    Xuất 102 file tổng hợp số liệu kiểm kê & benchmark
```

---

## 3. Phân Công Trách Nhiệm Thành Viên

- **Võ Đình Kiên:** Chủ trì lập trình và tối ưu hóa bộ nhớ cho Notebook `DS317_01` (xử lý streaming chunk PyArrow) và Notebook `DS317_05` (ghép nối không gian thời gian RTMA).
- **Quách Tuấn Kiệt:** Chủ trì Notebook `DS317_02` (đo lường 6 chiều DAMA, xây dựng từ điển dữ liệu 27 thuộc tính) và phối hợp chạy `DS317_Tong_Hop_Xuat_So_Lieu_BTVN`.
- **Huỳnh Chí Kiên:** Phụ trách thiết kế và trích xuất các biểu đồ EDA từ Notebook `DS317_02` và `DS317_Tong_Hop_Xuat_So_Lieu_BTVN`.
- **Trần Hồng Lĩnh:** Phụ trách Notebook `DS317_04` (huấn luyện Baseline Ridge Regression).
- **Nguyễn Hữu Bảo Lộc:** Phụ trách Notebook `DS317_03` (kiểm chứng phân phối và độ tương quan các biến).

---

## 4. Hướng Dẫn Tái Lập và Chạy Mẫu

Do dữ liệu đầu vào là tập Big Data hàng chục GB, các notebook này được thiết kế tối ưu để chạy trên môi trường **Kaggle Notebook**:
1. Đẩy notebook lên Kaggle kèm theo dataset `NOAA_AIS_2025` và `RTMA_2025`.
2. Khởi chạy tuần tự: `DS317_01` -> `DS317_02` -> `DS317_05` -> `DS317_Tong_Hop_Xuat_So_Lieu_BTVN`.
3. Tải các file zip kết quả ở mục Output của Kaggle và giải nén vào thư mục [`05_Output_Cac_Notebook/`](../../05_Output_Cac_Notebook/README.md).
