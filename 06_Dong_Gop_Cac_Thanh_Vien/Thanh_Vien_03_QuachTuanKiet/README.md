# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 03

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Quách Tuấn Kiệt
- **Mã số sinh viên (MSSV):** 24520911
- **Vai trò trong đồ án:** Kỹ sư Dữ liệu (Data Engineer), Kiểm kê & Giám sát Chất lượng Dữ liệu DAMA
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT
1. **Xây dựng Bộ dữ liệu mẫu chạy Demo (Sample Dataset for Demo):**
   - Trích xuất từ 1,000 đến 5,000 dòng quan trắc hành hải đại diện từ tập kiểm thử Quý 4 (`q4.parquet` trong `03_ban_tien_xu_ly_27_thuoc_tinh/`).
   - Đảm bảo đầy đủ 27 đặc trưng chế tác + trường khí tượng hải văn RTMA, kèm biến mục tiêu `Target_Hours` và mốc cập bến `ata_time`.
   - Bao phủ đa dạng các nhóm tàu (Cargo và Tanker), các phân tầng thời gian (`<= 168h` và `> 168h`) để phục vụ kiểm thử Demo thông suốt.
   - Viết script tự động hóa trích xuất dữ liệu mẫu để phục vụ tái lập độc lập.
2. **Soạn thảo Báo cáo Cuối kỳ:**
   - **Chương 2: Dữ liệu và Đo lường Chất lượng Dữ liệu:**
     + Bảng kiểm kê tài sản dữ liệu NOAA AIS 2025 theo 7 tiêu chí chuẩn.
     + Từ điển dữ liệu chi tiết cho hệ 3 phiên bản thuộc tính (18 cột thô, 22 cột nền tảng, 27 cột tiền xử lý).
     + Bảng đo lường và giám sát độ đo chất lượng dữ liệu 6 chiều DAMA-DMBOK (Completeness, Consistency, Accuracy, Timeliness, Validity, Uniqueness) trên 256.94 triệu dòng thô `RAW18`.
     + Đánh giá tương quan Pearson giữa cự ly `Dist_To_Berth_NM` và biến mục tiêu qua các giai đoạn làm sạch.
3. **Cập nhật và Chuẩn hóa File Kiểm kê Dữ liệu:**
   - Hoàn thiện tệp Excel `Lab3_DS317_Nhom03_DataInventory.xlsx` (3 sheets chuyên nghiệp: `KiemKe_7TieuChi`, `TuDien_22ThuocTinh`, `DoDo_ChatLuong_6Chieu`) khớp 100% với các bảng biểu trong Báo cáo.
4. **Phối hợp Thử nghiệm Demo:**
   - Bàn giao dữ liệu mẫu cho Đỗ Văn Lộc và phối hợp kiểm thử nạp dữ liệu vào ứng dụng `app.py`.

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO
- [ ] Tệp dữ liệu mẫu chạy Demo (`sample_demo_1000.parquet` và `sample_demo_1000.csv`).
- [ ] Script Python trích xuất và kiểm tra tính hợp lệ của dữ liệu mẫu (`extract_sample_data.py`).
- [ ] Bản thảo Chương 2 Báo cáo cuối kỳ (`Chuong_02_Du_Lieu_Va_Do_Luong_DAMA.docx` hoặc `.md`).
- [ ] Tệp Excel kiểm kê và giám sát chất lượng dữ liệu 6 chiều cập nhật (`DataInventory_Final_DAMA.xlsx`).

---

## 4. HƯỚNG DẪN GIT WORKFLOW CHO THÀNH VIÊN
Để tránh xung đột mã nguồn (merge conflict) với các thành viên khác, bạn vui lòng tuân thủ quy trình Git sau:

### Bước 1: Kéo mã nguồn mới nhất từ nhánh chính
```bash
git checkout main
git pull origin main
```

### Bước 2: Tạo nhánh cá nhân của bạn
```bash
git checkout -b feature/quachtuankiet
```

### Bước 3: Thao tác làm việc và lưu sản phẩm
- **QUY TẮC CỐT LÕI:** Bạn chỉ thêm, sửa, xóa file **BÊN TRONG THƯ MỤC CỦA MÌNH**:
  `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_03_QuachTuanKiet/`
- Không chỉnh sửa trực tiếp vào thư mục của thành viên khác hoặc thư mục nộp bài chung `DS317_R11_Nhom03_HoSoNopDoAn/` khi chưa tổng duyệt.

### Bước 4: Commit và Push lên GitHub
```bash
# Kiểm tra trạng thái file thay đổi
git status

# Thêm các file bạn đã làm vào staging
git add 06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_03_QuachTuanKiet/

# Commit với thông điệp rõ ràng
git commit -m "feat(kiet-qt): dong gop du lieu mau demo va ban thao chuong 2 DAMA"

# Push nhánh cá nhân lên remote GitHub
git push origin feature/quachtuankiet
```

### Bước 5: Tạo Pull Request (PR)
- Mở giao diện GitHub của repository, tạo Pull Request từ nhánh `feature/quachtuankiet` vào nhánh `main`.
- Đính kèm tóm tắt các sản phẩm đã hoàn thành để nhóm cùng đối soát trước khi merge.
