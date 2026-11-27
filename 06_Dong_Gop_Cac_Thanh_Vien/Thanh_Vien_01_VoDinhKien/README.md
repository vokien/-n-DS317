# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 01

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Võ Đình Kiên
- **Mã số sinh viên (MSSV):** 24520893
- **Vai trò trong đồ án:** Nhóm trưởng (Project Leader), Quản trị dự án, Chủ trì Chương 5 & tổng biên tập Báo cáo
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT (CHỈ PHẦN CÒN THIẾU)

> [!NOTE]
> Phân công đã được chốt chính thức theo chỉ đạo của ĐẠI CA: chỉ giao phần việc CÒN THIẾU; nội dung đã có sẵn trong workspace không giao lại. Chi tiết xem [Kế hoạch hoàn thiện](../../00_Quan_Ly_Va_Tai_Lieu_Chung/K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md) (Phần A, B, C, D).

1. **Quản trị dự án & Tích hợp hồ sơ cuối kỳ:**
   - Điều phối tiến độ 7 thành viên; tiếp nhận, kiểm tra và tích hợp sản phẩm vào `DS317_R11_Nhom03_HoSoNopDoAn/`.
   - Kiểm soát chất lượng: 0 broken link, chỉ dùng dấu `-` (ASCII 0x2D), không rò rỉ dữ liệu tạm.
2. **Chương 7: Kết luận và Hướng phát triển** (phối hợp tổng kết cùng Bảo Lộc).
3. **Chủ trì và tổng hợp Chương 5** (tiếp nhận từ Trần Hồng Lĩnh để giảm tải cho Lĩnh); tự viết phần **Module M4 (RTMA)**.
4. **Báo cáo rủi ro Big Data** khi xử lý 320.78 triệu dòng thô NOAA AIS 2025 (OOM RAM, tràn đĩa đệm, tín hiệu gián đoạn, trôi dạt thời tiết mùa đông).
5. **Tổng biên tập Báo cáo 7 chương và đóng gói ZIP** `DS317_R11_Nhom03.zip`; duyệt học thuật nội dung Slide (Slide do Trần Hồng Lĩnh làm toàn bộ, Kiên không làm slide).
6. **Hỗ trợ Kaggle:** là người đã chạy 2 Runner; sẵn sàng hỗ trợ dữ liệu và môi trường cho các thành viên khi thực hiện tác vụ trên Kaggle.
- **Lưu ý chạy trên Kaggle:** `detailed_predictions/*.parquet` bị `.gitignore` và chưa có trong workspace; mọi tác vụ cần dữ liệu này phải chạy trên Kaggle, không chạy nặng trên máy cá nhân.

### 2.1. Đã có sẵn - KHÔNG phân công (chỉ sử dụng/trích dẫn)
- Môi trường `requirements.txt`, `environment.yml`: [`03_SourceCode/requirements.txt`](../../DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/requirements.txt).
- Script đồng bộ: [`dong_bo_ho_so_nop.py`](../../05_Output_Cac_Notebook/dong_bo_ho_so_nop.py) (chỉ vận hành, không phải xây mới).
- Số liệu Runner: [`07_.../results/`](../../05_Output_Cac_Notebook/07_Runner_Song_Song_1_Baseline_M1_M2_M3/results/), [`08_.../results/`](../../05_Output_Cac_Notebook/08_Runner_Song_Song_2_M4_M5_M6_M7/results/); số liệu M4 đã có trong [`Tong_Hop_..._Ablation_7_Module.md`](../../03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md).

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO
- [ ] Bản thảo Chương 7 (`Chuong_07_Ket_Luan_Huong_Phat_Trien.docx` hoặc `.md`).
- [ ] Bản tổng hợp Chương 5 và phần Module M4.
- [ ] Báo cáo rủi ro Big Data (`Bao_Cao_Rui_Ro_BigData.md`).
- [ ] Bản tổng duyệt Báo cáo 7 chương (`BaoCao_CuoiKy_DS317_Nhom03.docx` và `.pdf`).
- [ ] Biên bản duyệt học thuật Slide và gói ZIP nộp bài `DS317_R11_Nhom03.zip`.

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
