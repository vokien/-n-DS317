# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 01

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Võ Đình Kiên
- **Mã số sinh viên (MSSV):** 24520893
- **Vai trò trong đồ án:** Nhóm trưởng (Project Leader), Quản trị dự án & Kiến trúc hệ thống
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT
1. **Quản trị dự án & Tích hợp hồ sơ cuối kỳ:**
   - Điều phối tiến độ tổng thể của 7 thành viên theo kế hoạch cuối kỳ.
   - Tiếp nhận, kiểm tra đối chuẩn và tích hợp các phần đóng góp từ 7 thư mục thành viên vào hồ sơ nộp bài chính thức `DS317_R11_Nhom03_HoSoNopDoAn/`.
   - Quản lý quy chuẩn chất lượng: kiểm soát không có broken link, tuân thủ định dạng dấu gạch ngang tiêu chuẩn `-` (ASCII 0x2D), không rò rỉ dữ liệu tạm.
2. **Soạn thảo và Tổng biên tập Báo cáo Cuối kỳ:**
   - Chủ trì tổng biên tập toàn bộ Báo cáo Đồ án Cuối kỳ 7 Chương (`.docx` và `.pdf`).
   - Trực tiếp soạn thảo **Chương 7: Kết luận và Hướng phát triển** (Tóm tắt các đóng góp cốt lõi, giá trị thực tiễn, hạn chế và lộ trình nâng cấp hệ thống).
3. **Môi trường thực thi & Script tự động hóa:**
   - Xây dựng và kiểm tra tệp phụ thuộc môi trường `requirements.txt` chuẩn hóa cho toàn dự án.
   - Cập nhật và vận hành script đồng bộ hồ sơ nộp bài tự động `dong_bo_ho_so_nop.py` đạt chuẩn PEP 8.
4. **Phân tích Rủi ro Kỹ thuật Big Data:**
   - Hoàn thiện tài liệu phân tích rủi ro Big Data khi xử lý 320.78 triệu dòng thô NOAA AIS 2025 (rủi ro OOM RAM, tràn đĩa đệm, tín hiệu gián đoạn và trôi dạt phân phối thời tiết mùa đông).
5. **Tổng duyệt Slide Thuyết trình:**
   - Cùng Đỗ Văn Lộc hoàn thiện và tổng duyệt bộ Slide thuyết trình cuối kỳ (10-12 slides chuẩn môn học).
   - Đóng gói tệp ZIP nộp bài chính thức `DS317_R11_Nhom03.zip`.

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO
- [ ] Bản thảo Chương 7 Báo cáo cuối kỳ (`Chuong_07_Ket_Luan_Huong_Phat_Trien.docx` hoặc `.md`).
- [ ] Tệp môi trường thực thi `requirements.txt` đã được kiểm thử thông suốt.
- [ ] Bản tổng duyệt Báo cáo 7 chương hoàn chỉnh (`BaoCao_CuoiKy_DS317_Nhom03.docx` và `.pdf`).
- [ ] Bản tổng duyệt Slide thuyết trình cuối kỳ (`Slide_Bao_Ve_Cuoi_Ky_Nhom03.pptx` và `.pdf`).
- [ ] Báo cáo phân tích rủi ro Big Data và phương án dự phòng (`Bao_Cao_Rui_Ro_BigData.md`).

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
git checkout -b feature/vodinhkien
```

### Bước 3: Thao tác làm việc và lưu sản phẩm
- **QUY TẮC CỐT LÕI:** Bạn chỉ thêm, sửa, xóa file **BÊN TRONG THƯ MỤC CỦA MÌNH**:
  `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_01_VoDinhKien/`
- Không chỉnh sửa trực tiếp vào thư mục của thành viên khác hoặc thư mục nộp bài chung `DS317_R11_Nhom03_HoSoNopDoAn/` khi chưa tổng duyệt.

### Bước 4: Commit và Push lên GitHub
```bash
# Kiểm tra trạng thái file thay đổi
git status

# Thêm các file bạn đã làm vào staging
git add 06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_01_VoDinhKien/

# Commit với thông điệp rõ ràng
git commit -m "feat(kien-vd): cap nhat ban thao chuong 7 va requirements.txt"

# Push nhánh cá nhân lên remote GitHub
git push origin feature/vodinhkien
```

### Bước 5: Tạo Pull Request (PR)
- Mở giao diện GitHub của repository, tạo Pull Request từ nhánh `feature/vodinhkien` vào nhánh `main`.
- Đính kèm tóm tắt các sản phẩm đã hoàn thành để nhóm cùng đối soát trước khi merge.
