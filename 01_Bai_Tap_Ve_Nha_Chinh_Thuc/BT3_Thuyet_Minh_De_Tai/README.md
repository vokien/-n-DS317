# BÀI TẬP VỀ NHÀ 3: THUYẾT MINH ĐỀ TÀI (VER 1)
**Môn học:** DS317 - Khai phá dữ liệu trong doanh nghiệp  
**Căn cứ:** Hướng dẫn thực hành Lab 3 & Biểu mẫu Thuyết minh đề tài chính thức  

---

## 1. Mục tiêu bài tập
Xác lập hồ sơ "Thuyết minh đề tài" chính thức (Lab 3) nhằm cam kết phạm vi nghiên cứu, kiến trúc giải pháp, kế hoạch thực hiện và đặc biệt là ứng dụng trực tiếp kết quả bài tập Chương 4 (Chất lượng dữ liệu) và Chương 5 (Phân tích dữ liệu doanh nghiệp / BI) vào phần **“Kết quả nghiên cứu sơ khởi”** (Mục 5 của Thuyết minh).

---

## 2. Ứng dụng nội dung bài tập Chương 4 và Chương 5 vào Mục 5 "Kết quả nghiên cứu sơ khởi"

### Ứng dụng bài tập Chương 4 vào Mục 5.1: Báo cáo chất lượng dữ liệu 6 chiều DAMA
- Trích xuất toàn bộ kết quả đo lường định lượng từ **BT2** trên 92,681,850 bản ghi sạch năm 2025 (và 256,935,254 bản ghi thô):
  - Bảng 5.3: Đo lường 6 khía cạnh ở mức hạt dữ liệu (Tính đầy đủ 97.52%, Tính nhất quán 100%, Tính chính xác 100%, Tính kịp thời 100%, Tính hợp lệ 99.99995%, Tính duy nhất 99.7901%).
  - Bảng 5.4: Giám sát phân rã 6 chiều chất lượng dữ liệu qua 4 Quý (Q1 - Q4 năm 2025) chứng minh dữ liệu đồng nhất, không bị trôi dạt (Data Drift) theo mùa vụ.

### Ứng dụng bài tập Chương 5 vào Mục 5.2: Phân tích khám phá dữ liệu nâng cao (EDA & BI)
- Phân tích tương quan đa biến và đường xu hướng hồi quy OLS: chứng minh tương quan thuận rất mạnh ($r = +0.7629$) giữa cự ly đến bến (`Dist_To_Berth_NM`; r = +0.7629 từ lần chạy trước khi chuyển ngưỡng 1,800/2,300 NM) và thời gian cập cảng (`Target_Hours`).
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
