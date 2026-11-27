# Kết Quả Đầu Ra: Notebook Tách Lẻ Từng Module (`09_Notebook_Tach_Le_Tung_Module/`)

Thư mục này lưu trữ cấu trúc kết quả từ các notebook thực nghiệm tách lẻ trong phân hệ [`02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/03_Notebook_Tach_Le_Tung_Module/`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/03_Notebook_Tach_Le_Tung_Module/).

---

## 1. Mục Đích và Vai Trò Kỹ Thuật

Thư mục được phân tách thành 8 thư mục con độc lập, tương ứng với từng module nghiên cứu thành phần (Ablation Study):
1. **Kiểm thử cục bộ độc lập:** Nơi lưu trữ tạm thời các kết quả chạy thử nghiệm đơn vị (Unit Testing) trên tập dữ liệu con (Sample) của từng thành viên phụ trách module.
2. **Đối chiếu vi mô:** Cho phép phân tích chi tiết hành vi của từng mô hình mà không cần nạp toàn bộ ma trận kết quả lớn từ các Runner song song.

---

## 2. Cấu Trúc 8 Thư Mục Con

```text
09_Notebook_Tach_Le_Tung_Module/
├── 00_Baseline/               <- Kết quả kiểm thử nhanh mô hình cơ sở
├── M1_Loc_Ngoai_Lai/          <- Kết quả kiểm thử thuật toán lọc ngoại lai IQR
├── M2_Dien_Khuyet/            <- Kết quả kiểm thử các phương pháp điền khuyết
├── M3_Tao_Dac_Trung/          <- Kết quả kiểm thử các nhóm đặc trưng tương tác
├── M4_Thoi_Tiet_RTMA/         <- Kết quả kiểm thử đặc trưng khí tượng RTMA
├── M5_Chon_Loc_Dac_Trung/     <- Kết quả kiểm thử chọn lọc Mutual Information & log1p
├── M6_Mat_Mat_Bat_Doi_Xung/   <- Kết quả kiểm thử hàm phạt mất mát bất đối xứng
├── M7_Gom_Cum_Khoang_Sai_So/  <- Kết quả kiểm thử khoảng tin cậy Conformal Prediction
└── README.md
```

---

## 3. Lưu Ý về Số Liệu Chính Thức của Đồ Án

- Các thư mục con ở đây chủ yếu phục vụ các đợt chạy thử nghiệm nhanh (prototyping) trong quá trình nghiên cứu.
- **Nguồn số liệu chính thức duy nhất** được công nhận để báo cáo trong Báo cáo Đồ án Cuối kỳ và Slide thuyết trình được trích xuất từ 2 Runner tập trung tại:
  - [`07_Runner_Song_Song_1_Baseline_M1_M2_M3/`](../07_Runner_Song_Song_1_Baseline_M1_M2_M3/README.md)
  - [`08_Runner_Song_Song_2_M4_M5_M6_M7/`](../08_Runner_Song_Song_2_M4_M5_M6_M7/README.md)
