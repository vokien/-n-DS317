# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 02

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Đỗ Văn Lộc
- **Mã số sinh viên (MSSV):** 24520977
- **Vai trò trong đồ án:** Thư ký nhóm (Secretary), Kỹ sư Ứng dụng & Demo Web (Frontend/Backend Streamlit)
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT
1. **Phát triển Chương trình Web Demo tương tác (`app.py`):**
   - Trọng tâm chiếm **50% điểm sản phẩm A4**: Xây dựng hoàn chỉnh ứng dụng Web Demo bằng Streamlit phục vụ Trung tâm Điều độ Cầu bến (Berth Planning Center).
   - Nạp trọng số mô hình đã huấn luyện (CatBoost/LightGBM/XGBoost từ `05_Model/` hoặc `05_Output_Cac_Notebook/07_Runner_Song_Song_1_Baseline_M1_M2_M3/results/`).
   - Nạp dữ liệu mẫu từ Quách Tuấn Kiệt để mô phỏng suy luận thời gian thực cho tàu biển đang hành trình.
   - Hiển thị: Mốc giờ cập bến dự báo (Predicted ATA), Khoảng an toàn 90% Conformal (Safety Buffer), Bảng phân cấp rủi ro trễ và đề xuất phân bổ cầu bến JIT.
   - Tích hợp BI Dashboard trực quan hóa chất lượng dữ liệu DAMA 6 chiều.
2. **Soạn thảo Báo cáo Cuối kỳ:**
   - **Chương 1: Tổng quan và Bối cảnh nghiệp vụ:** Lý do chọn đề tài, phân tích chi phí sai lệch ETA trong logistics hàng hải quốc tế, mục tiêu SMART của đề tài Nâng cao.
   - **Chương 6: Kiến trúc Ứng dụng và Triển khai Doanh nghiệp:** Thiết kế kiến trúc tổng thể của hệ thống, luồng dữ liệu (Data Pipeline -> Serving Engine -> Web Dashboard), mô tả giao diện và các ca sử dụng (Use Cases) cho nhân viên điều độ.
3. **Thiết kế Bộ Slide Bảo vệ Cuối kỳ:**
   - Chủ trì thiết kế bộ Slide bảo vệ cuối kỳ (10-12 slides chuẩn môn học), bảo đảm thẩm mỹ cao, bố cục trực quan, tập trung vào sơ đồ, biểu đồ và mockup giao diện.
4. **Quản lý Hồ sơ Nhóm Cuối kỳ (`08_QuanLyNhom/`):**
   - Tập hợp và hoàn thiện các Biên bản họp nhóm giai đoạn sau Lab 3.
   - Nhật ký thực nghiệm tổng hợp và Scope Changelog (lý giải sự điều chỉnh từ Engine v1 sang Engine v2).
   - Bảng tự đánh giá đóng góp công việc của 7 thành viên.

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO
- [ ] Toàn bộ mã nguồn Web Demo (`app.py`, components, `config.yaml`, assets).
- [ ] Hướng dẫn cài đặt và sử dụng Web Demo (`HDSD_Demo_Streamlit.md`).
- [ ] Bản thảo Chương 1 và Chương 6 Báo cáo cuối kỳ (`Chuong_01_Tong_Quan.docx`, `Chuong_06_Kien_Truc_Ung_Dung_Demo.docx` hoặc `.md`).
- [ ] Bộ Slide bảo vệ cuối kỳ (`Slide_Bao_Ve_Cuoi_Ky_DS317.pptx` và `.pdf`).
- [ ] Hồ sơ quản lý nhóm (`Bien_Ban_Hop_Nhom.docx`, `Nhat_Ky_Thuc_Nghiem.md`, `Bang_Tu_Danh_Gia_7_Thanh_Vien.xlsx`).

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
git checkout -b feature/dovanloc
```

### Bước 3: Thao tác làm việc và lưu sản phẩm
- **QUY TẮC CỐT LÕI:** Bạn chỉ thêm, sửa, xóa file **BÊN TRONG THƯ MỤC CỦA MÌNH**:
  `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_02_DoVanLoc/`
- Không chỉnh sửa trực tiếp vào thư mục của thành viên khác hoặc thư mục nộp bài chung `DS317_R11_Nhom03_HoSoNopDoAn/` khi chưa tổng duyệt.

### Bước 4: Commit và Push lên GitHub
```bash
# Kiểm tra trạng thái file thay đổi
git status

# Thêm các file bạn đã làm vào staging
git add 06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_02_DoVanLoc/

# Commit với thông điệp rõ ràng
git commit -m "feat(loc-dv): hoan thien app.py demo va ban thao chuong 1, 6"

# Push nhánh cá nhân lên remote GitHub
git push origin feature/dovanloc
```

### Bước 5: Tạo Pull Request (PR)
- Mở giao diện GitHub của repository, tạo Pull Request từ nhánh `feature/dovanloc` vào nhánh `main`.
- Đính kèm tóm tắt các sản phẩm đã hoàn thành để nhóm cùng đối soát trước khi merge.
