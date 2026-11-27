# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 05

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Nguyễn Hữu Bảo Lộc
- **Mã số sinh viên (MSSV):** 24520983
- **Vai trò trong đồ án:** Chuyên viên Tổng quan Học thuật & Đạo đức AI (Academic Literature & AI Ethics Specialist)
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT
1. **Nghiên cứu Tổng quan Công trình Liên quan (Related Work) & Bảng Đối sánh SOTA:**
   - Phân tích chuyên sâu 6 bài báo khoa học quốc tế uy tín (Springer, Elsevier) về bài toán ETA hàng hải.
   - Xây dựng bảng ma trận đối sánh toàn diện theo 5 tiêu chí: Phương pháp mô hình, Nguồn và quy mô dữ liệu, Kết quả định lượng (MAE, RMSE), Hạn chế thực tiễn và Điểm kế thừa của đề tài.
   - Khẳng định rõ **Khoảng trống nghiên cứu (Research Gap)**: các nghiên cứu trước đây đa phần chạy trên dữ liệu nhỏ, gọt giũa nhân tạo hoặc không tính đến hàm phạt trễ/sớm bất đối xứng và biến động thời tiết biển mở.
2. **Chuẩn hóa Danh mục Trích dẫn Học thuật chuẩn IEEE:**
   - Quản lý và chuẩn hóa toàn bộ trích dẫn trong Báo cáo cuối kỳ theo chuẩn **IEEE** (đánh số theo thứ tự xuất hiện [1], [2], [3]...).
   - Xuất bản và kiểm tra tính toàn vẹn của tệp `references.bib`, đảm bảo 100% trích dẫn trong văn bản đều có liên kết nguồn rõ ràng.
3. **Soạn thảo Khung Tuân thủ Pháp lý & Đạo đức AI:**
   - Rà soát việc tuân thủ **Luật An toàn thông tin mạng** và **Luật Bảo vệ dữ liệu cá nhân (Decree 13/2023/ND-CP)**: chứng minh dữ liệu NOAA AIS hoàn toàn ẩn danh thuyền viên, định danh bằng mã MMSI công cộng quốc tế, không lưu trữ dữ liệu định danh cá nhân (No PII).
   - Soạn thảo bản **Khai báo Minh bạch Sử dụng AI (AI Transparency & Ethics Declaration)**: công khai mục đích sử dụng các mô hình hỗ trợ viết code/rà soát văn bản, khẳng định tính liêm chính học thuật 100% của nhóm.
4. **Soạn thảo Báo cáo Cuối kỳ:**
   - **Chương 1 (Tiểu mục 1.4):** Toàn bộ nội dung Tổng quan tình hình nghiên cứu trong và ngoài nước.
   - **Chương 5 (phần Module M5):** Phân tích kết quả thực nghiệm Module M5 (Biến đổi mục tiêu phi tuyến $\log(1+y)$ và chọn lọc đặc trưng tối ưu qua Mutual Information).

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO
- [ ] Bản thảo phần Tổng quan công trình liên quan (Related Work) cho Chương 1 (`Tong_Quan_SOTA_Related_Work.docx` hoặc `.md`).
- [ ] Tệp trích dẫn tài liệu tham khảo chuẩn IEEE (`references.bib`).
- [ ] Báo cáo chuyên đề Tuân thủ Pháp lý & Đạo đức AI (`Bao_Cao_Tuan_Thu_Phap_Ly_Va_Dao_Duc_AI.md`).
- [ ] Bản thảo phần phân tích Module M5 trong Chương 5 Báo cáo cuối kỳ.

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
git checkout -b feature/nguyenhuubaoloc
```

### Bước 3: Thao tác làm việc và lưu sản phẩm
- **QUY TẮC CỐT LÕI:** Bạn chỉ thêm, sửa, xóa file **BÊN TRONG THƯ MỤC CỦA MÌNH**:
  `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_05_NguyenHuuBaoLoc/`
- Không chỉnh sửa trực tiếp vào thư mục của thành viên khác hoặc thư mục nộp bài chung `DS317_R11_Nhom03_HoSoNopDoAn/` khi chưa tổng duyệt.

### Bước 4: Commit và Push lên GitHub
```bash
# Kiểm tra trạng thái file thay đổi
git status

# Thêm các file bạn đã làm vào staging
git add 06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_05_NguyenHuuBaoLoc/

# Commit với thông điệp rõ ràng
git commit -m "feat(loc-nhb): hoan thien related work SOTA va bao cao phap ly dao duc AI"

# Push nhánh cá nhân lên remote GitHub
git push origin feature/nguyenhuubaoloc
```

### Bước 5: Tạo Pull Request (PR)
- Mở giao diện GitHub của repository, tạo Pull Request từ nhánh `feature/nguyenhuubaoloc` vào nhánh `main`.
- Đính kèm tóm tắt các sản phẩm đã hoàn thành để nhóm cùng đối soát trước khi merge.
