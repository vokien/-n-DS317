# Kết Quả Đầu Ra: Kiểm Chứng và Lựa Chọn Đặc Trưng (`03_DS317_03_Kiem_Chung_Dac_Trung/`)

Thư mục này lưu trữ cấu trúc kết quả từ notebook kiểm chứng đặc trưng [`DS317_03_Kiem_Chung_Lua_Chon_Dac_Trung.ipynb`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_03_Kiem_Chung_Lua_Chon_Dac_Trung.ipynb).

---

## 1. Mục Đích và Vai Trò Kỹ Thuật

Notebook `DS317_03` thực hiện thẩm định thống kê chuyên sâu trên hệ 27 đặc trưng sau tiền xử lý nhằm phục vụ thiết kế các kịch bản thực nghiệm:
1. **Kiểm tra hiện tượng đa cộng tuyến (Multicollinearity):** Đo hệ số phóng đại phương sai (VIF - Variance Inflation Factor) giữa các cặp biến động học như vận tốc $sog$ và vận tốc biểu kiến $v_{implied}$.
2. **Đo lường độ tương hỗ thông tin (Mutual Information - MI):** Xác định mức độ liên quan phi tuyến giữa từng đặc trưng đầu vào và biến mục tiêu liên tục `Target_Hours`.
3. **Thẩm định tính ổn định phân phối:** Đánh giá độ lệch phân phối (Skewness) để xác lập yêu cầu áp dụng phép biến đổi logarit $log1p$ cho Module M5.

---

## 2. Cấu Trúc Phân Tầng Thư Mục

```text
03_DS317_03_Kiem_Chung_Dac_Trung/
├── AUDIT/     <- Lưu trữ các bảng kiểm toán phương sai và chỉ số VIF
├── COMMON/    <- Metadata tham số chạy kiểm chứng
├── RAW2/      <- Kết quả kiểm định phân phối trên tập nền tảng 22 cột
├── TASK03/    <- Bảng xếp hạng đặc trưng theo Mutual Information
└── README.md
```

---

## 3. Phân Công Trách Nhiệm

- **Nguyễn Hữu Bảo Lộc:** Trực tiếp phân tích kết quả kiểm chứng đặc trưng, làm cơ sở xây dựng Module M5 (Lựa chọn đặc trưng qua MI & log1p).
- **Võ Đình Kiên:** Thẩm định kết quả VIF để cấu hình danh sách đặc trưng đầu vào trong Runner 1 và Runner 2.
