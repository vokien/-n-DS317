# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 02

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Đỗ Văn Lộc
- **Mã số sinh viên (MSSV):** 24520977
- **Vai trò trong đồ án:** Thư ký nhóm (Secretary), Kỹ sư Ứng dụng & Demo Web (Frontend/Backend Streamlit)
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT (CHỈ PHẦN CÒN THIẾU)

> [!NOTE]
> Phân công đã được chốt chính thức theo chỉ đạo của ĐẠI CA: chỉ giao phần việc CÒN THIẾU; nội dung đã có sẵn trong workspace không giao lại. Chi tiết xem [Kế hoạch hoàn thiện](../../00_Quan_Ly_Va_Tai_Lieu_Chung/K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md) (Phần A, B, C, D).

1. **Phát triển Web Demo tương tác (`app.py`)** (50% điểm sản phẩm A4; hiện chưa có `app.py`, chỉ có `07_Demo/README.md`):
   - Ứng dụng Streamlit cho Trung tâm Điều độ Cầu bến; nạp trọng số CatBoost/LightGBM/XGBoost từ gói `runner*_saved_models.zip` đã có.
   - Dùng trực tiếp dữ liệu mẫu có sẵn `demo_sample_3000.csv/.parquet` (không chờ thêm).
   - Hiển thị: Predicted ATA, khoảng an toàn 90% Conformal, bảng phân cấp rủi ro trễ, đề xuất phân bổ cầu bến JIT; tích hợp BI Dashboard DAMA 6 chiều (số liệu DAMA đã có).
2. **Soạn thảo Báo cáo:** Chương 1 (Tổng quan và Bối cảnh nghiệp vụ; tiểu mục 1.4 do Bảo Lộc viết) và Chương 6 (Kiến trúc Ứng dụng và Triển khai).
3. **Hồ sơ Quản lý Nhóm (`08_QuanLyNhom/`):** Biên bản họp giai đoạn sau Lab 3, Nhật ký thực nghiệm, Scope Changelog Engine v1 -> v2, Bảng tự đánh giá đóng góp 7 thành viên (hiện thư mục chỉ có `README.md`).
4. **Cung cấp đầu vào cho Slide (Phần 9):** ảnh chụp màn hình/video Demo gửi cho Trần Hồng Lĩnh. **Không làm slide.**

### 2.1. Đã có sẵn - KHÔNG phân công (chỉ sử dụng/trích dẫn)
- Dữ liệu mẫu Demo: [`demo_sample_3000.csv`](../../DS317_R11_Nhom03_HoSoNopDoAn/04_Data/demo_sample_3000.csv), [`.parquet`](../../DS317_R11_Nhom03_HoSoNopDoAn/04_Data/demo_sample_3000.parquet).
- Trọng số: [`runner1_saved_models.zip`](../../05_Output_Cac_Notebook/runner1_saved_models.zip), [`runner2_saved_models.zip`](../../05_Output_Cac_Notebook/runner2_saved_models.zip).
- Số liệu DAMA: [`DAMA_26_Dac_Trung/`](../../DS317_R11_Nhom03_HoSoNopDoAn/06_Results/DAMA_26_Dac_Trung/) (29 tệp); mockup giao diện: [`Hinh_PL1_Mockup_Demo_Streamlit.png`](../../04_So_Lieu_Kiem_Ke_Va_Bieu_Do/Hinh_Anh_Bieu_Do_Chung/Hinh_PL1_Mockup_Demo_Streamlit.png).

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO
- [ ] Mã nguồn Web Demo (`app.py`, components, `config.yaml`, assets).
- [ ] Hướng dẫn cài đặt và sử dụng (`HDSD_Demo_Streamlit.md`).
- [ ] Bản thảo Chương 1 và Chương 6.
- [ ] Hồ sơ quản lý nhóm (`Bien_Ban_Hop_Nhom.docx`, `Nhat_Ky_Thuc_Nghiem.md`, `Scope_Changelog_Engine_v1_sang_v2.md`, `Bang_Tu_Danh_Gia_7_Thanh_Vien.xlsx`).
- [ ] Ảnh/video màn hình Demo gửi Trần Hồng Lĩnh cho Phần 9 Slide.

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
