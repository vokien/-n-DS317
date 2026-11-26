# BÀI TẬP VỀ NHÀ 3: THUYẾT MINH ĐỀ TÀI (VER 1)
**Môn học:** DS317 - Khai phá dữ liệu trong doanh nghiệp  
**Căn cứ:** Hướng dẫn thực hành Lab 3 & Biểu mẫu Thuyết minh đề tài chính thức  

---

## 1. Mục tiêu bài tập
Xác lập hồ sơ "Thuyết minh đề tài" chính thức (Lab 3) nhằm cam kết phạm vi nghiên cứu, kiến trúc giải pháp, kế hoạch thực hiện và đặc biệt là ứng dụng trực tiếp kết quả bài tập Chương 4 (Chất lượng dữ liệu) và Chương 5 (Phân tích dữ liệu doanh nghiệp / BI) vào phần **“Kết quả nghiên cứu sơ khởi”** (Mục 5 của Thuyết minh).

---

## 2. Ứng dụng nội dung bài tập Chương 4 và Chương 5 vào Mục 5 "Kết quả nghiên cứu sơ khởi"

### Ứng dụng bài tập Chương 4 vào Mục 5.1: Báo cáo chất lượng dữ liệu 6 chiều DAMA
- Trích xuất toàn bộ kết quả đo lường định lượng từ **BT2** trên `92,681,850` bản ghi sạch (`Base22`) và `256,935,254` bản ghi thô (`RAW18`):
  - Bảng 5.3 (bộ số liệu chuẩn hóa trong [`05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/DAMA/`](../../05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/DAMA/dama_6_dimensions_by_quarter.csv)):
    - `RAW18 (256.94M dòng)`: Completeness bản ghi `93.5626%` (thuộc tính `99.5467%`), Consistency `36.6940%`, Accuracy `45.9011%` (`r = +0.2589`), Timeliness `64.9956%`, Validity `96.3052%`, Uniqueness `99.7228%`.
    - `Base22 (92.68M dòng)`: Completeness `100.0%` (0 ô khuyết ngoài cột `cargo`), Consistency `100.0%`, Accuracy `92.7259%` (`Q1-Q3: 100.0%`, `Q4: 70.9036%`, `r = +0.50971`), Timeliness `100.0%`, Validity `100.0%`, Uniqueness `100.0%`.
  - Bảng 5.4: Giám sát phân rã 6 chiều chất lượng dữ liệu qua 4 Quý (Q1 - Q4 năm 2025) trên `RAW18` và `Base22`.

### Ứng dụng bài tập Chương 5 vào Mục 5.2: Phân tích khám phá dữ liệu nâng cao (EDA & BI)
- Phân tích tương quan đa biến: ghi nhận `Pearson r(Dist_To_Berth_NM, Target_Hours) = +0.50971` trên `Base22` (`92,681,850` dòng sau chạy lại), tăng từ `+0.2589` trên `RAW18` (và đạt `r = +0.7772` trên tập mẫu lọc pre-split `90,586,699` dòng).
- Đánh giá phân bố động học: Vận tốc tức thời $sog$ có trung vị 11.7 knots (chuẩn vận tốc kinh tế hàng hải).
- Phân tích phân nhóm tàu: Đối chiếu sự khác biệt về kích thước thân vỏ, mớn nước $draft$ và vùng neo đậu giữa nhóm Tàu hàng rời (Bulk Cargo) và Tàu chở dầu (Tanker).
- Trực quan hóa bản đồ nhiệt mật độ luồng tàu cập bến tại các cụm cảng lớn của Hoa Kỳ.

---

## 3. Danh mục tài liệu trong thư mục

### Hồ sơ 5 tệp bắt buộc nộp bài (chuẩn mẫu quy định `Lab3_<MãLớp>_<TênNhóm>_<LoạiSảnPhẩm>`)
- [`Lab3_DS317.R11_Nhom03_ThuyetMinh.docx`](Lab3_DS317.R11_Nhom03_ThuyetMinh.docx) & [`.pdf`](Lab3_DS317.R11_Nhom03_ThuyetMinh.pdf): Văn bản thuyết minh đầy đủ 13 mục chuẩn mực (Mục 5 tích hợp trọn vẹn kết quả Chương 4 & 5).
- [`Lab3_DS317.R11_Nhom03_DataInventory.xlsx`](Lab3_DS317.R11_Nhom03_DataInventory.xlsx): Bảng kiểm kê tài sản dữ liệu chính thức nộp kèm.
- [`Lab3_DS317.R11_Nhom03_Code.ipynb`](Lab3_DS317.R11_Nhom03_Code.ipynb): Notebook mã nguồn kiểm chứng sơ khởi nộp kèm.
- [`Lab3_DS317.R11_Nhom03_Slides.pdf`](Lab3_DS317.R11_Nhom03_Slides.pdf): Bộ slides báo cáo tại buổi 6.
- [`Lab3_DS317.R11_Nhom03_PhanCong.docx`](Lab3_DS317.R11_Nhom03_PhanCong.docx) & [`.pdf`](Lab3_DS317.R11_Nhom03_PhanCong.pdf): Bảng phân công và tự đánh giá của nhóm.

### Tài liệu bổ trợ và hồ sơ lưu trữ gốc
- [`Lab3 DS317.R11 Nhóm 03 - Kịch bản thuyết trình 15 phút.docx`](Lab3%20DS317.R11%20Nh%C3%B3m%2003%20-%20K%E1%BB%8Bch%20b%E1%BA%A3n%20thuy%E1%BA%BFt%20tr%C3%ACnh%2015%20ph%C3%BAt.docx) & [`.pdf`](Lab3%20DS317.R11%20Nh%C3%B3m%2003%20-%20K%E1%BB%8Bch%20b%E1%BA%A3n%20thuy%E1%BA%BFt%20tr%C3%ACnh%2015%20ph%C3%BAt.pdf): Kịch bản thuyết trình bảo vệ 15 phút chi tiết theo từng slide và câu hỏi phản biện.
- `Lab3 DS317.R11 Nhóm 03 - Thuyết minh gốc.docx`: Bản thảo thuyết minh ban đầu (bản lưu trữ gốc ngoài repo).
- `Nội dung gốc thuyết minh đề tài.docx`: Nội dung đề cương gốc (bản lưu trữ gốc ngoài repo).
- `Lab3 DS317 Nhóm 03 - Cũ.zip`: Gói nén lưu trữ phiên bản ban đầu (lưu trữ ngoài repo).
