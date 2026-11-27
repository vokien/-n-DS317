# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 07

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Trần Hồng Lĩnh
- **Mã số sinh viên (MSSV):** 24520970
- **Vai trò trong đồ án:** Chủ trì toàn bộ Slide Bảo vệ; Kỹ sư ML/DL & Error Analysis Specialist
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT (CHỈ PHẦN CÒN THIẾU)

> [!NOTE]
> Phân công đã được điều chỉnh theo yêu cầu của ĐẠI CA: chỉ giao phần việc CÒN THIẾU; nội dung đã có sẵn trong workspace không giao lại. Chi tiết xem [Kế hoạch hoàn thiện](../../00_Quan_Ly_Va_Tai_Lieu_Chung/K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md) (Phần A, B, C). Các điểm ghi **[Chờ ĐẠI CA xác nhận]** là đề xuất, chưa là quyết định cuối.

1. **CHỦ TRÌ TOÀN BỘ SLIDE BẢO VỆ CUỐI KỲ** (20% điểm sản phẩm A4; thư mục `02_Slides/`):
   - Tự thiết kế và dựng cả **10 phần** theo [`02_Slides/README.md`](../../DS317_R11_Nhom03_HoSoNopDoAn/02_Slides/README.md), xuất `DS317_R11_Nhom03_Slides.pptx` và `.pdf` (16:9, 15-20 phút).
   - Các thành viên khác chỉ gửi nội dung/biểu đồ/số liệu đầu vào của phần mình; Hồng Lĩnh tích hợp, thống nhất định dạng và chuẩn bị ghi chú trình bày.
   - Chỉ dùng số liệu có nguồn trong workspace hoặc kết quả mới đã nghiệm thu; nhận ảnh/video Demo từ Đỗ Văn Lộc. Nhóm trưởng duyệt học thuật.
2. **Phân tích lỗi Case Study có kiểm chứng:** trích xuất các chuyến tàu thật (`MMSI`, loại tàu, `sog`, `Dist_To_Berth_NM`) có residual cực trị ở cả hai tầng `<= 168h` và `> 168h` từ `detailed_predictions/` (chưa có trong workspace, chạy trên Kaggle); viết **Báo cáo Phân tích Lỗi Case Study và Bản chất Phân tầng 168h**.
3. **Chương 5:** chỉ phần **Baseline B0** và **Module M6** (viết từ số liệu Engine v2 `00_baseline_b0_*`, `m6_asymloss_*`).
- **Lưu ý chạy trên Kaggle:** `detailed_predictions/*.parquet` bị `.gitignore` và chưa có trong workspace; mọi tác vụ cần dữ liệu này phải chạy trên Kaggle, không chạy nặng trên máy cá nhân.

### 2.1. Đã có sẵn - KHÔNG phân công (chỉ sử dụng/trích dẫn)
- Số liệu Baseline B0, M6 và phân tầng: [`runner1_master_horizons.csv`](../../05_Output_Cac_Notebook/07_Runner_Song_Song_1_Baseline_M1_M2_M3/results/runner1_master_horizons.csv), [`runner2_master_horizons.csv`](../../05_Output_Cac_Notebook/08_Runner_Song_Song_2_M4_M5_M6_M7/results/runner2_master_horizons.csv).
- Báo cáo M6 (Engine v1): [`Bao_cao_Thuc_nghiem_Module_M6.docx`](../../03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Bao_cao_Modules/Bao_cao_Thuc_nghiem_Module_M6.docx); số liệu Engine v2: [`Tong_Hop_..._Ablation_7_Module.md`](../../03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md).
- Baseline Ridge: [`04_DS317_04_Baseline_Ridge/`](../../05_Output_Cac_Notebook/04_DS317_04_Baseline_Ridge/README.md).
- Biểu đồ có sẵn dùng cho Slide: [`04_So_Lieu_Kiem_Ke_Va_Bieu_Do/`](../../04_So_Lieu_Kiem_Ke_Va_Bieu_Do/README.md).
- **Đã chuyển đi để giảm tải:** chủ trì Chương 5 (Võ Đình Kiên), phần M3 (Quách Tuấn Kiệt), phần M4 (Võ Đình Kiên), rà soát tái lập code (Quách Tuấn Kiệt), đồng phụ trách ROI (Lê Sỹ Liêm).

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO
- [ ] Slide Bảo vệ 10 phần: `DS317_R11_Nhom03_Slides.pptx` và `DS317_R11_Nhom03_Slides.pdf`.
- [ ] Báo cáo phân tích lỗi Case Study và Bản chất phân tầng 168h (`Bao_Cao_Phan_Tich_Loi_Case_Study.md` hoặc `.docx`).
- [ ] Script trích xuất case study (`case_study_error_analysis.py`, chạy được trên Kaggle).
- [ ] Bản thảo phần Baseline B0 và Module M6 trong Chương 5.

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
git checkout -b feature/tranhonglinh
```

### Bước 3: Thao tác làm việc và lưu sản phẩm
- **QUY TẮC CỐT LÕI:** Bạn chỉ thêm, sửa, xóa file **BÊN TRONG THƯ MỤC CỦA MÌNH**:
  `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_07_TranHongLinh/`
- Không chỉnh sửa trực tiếp vào thư mục của thành viên khác hoặc thư mục nộp bài chung `DS317_R11_Nhom03_HoSoNopDoAn/` khi chưa tổng duyệt.

### Bước 4: Commit và Push lên GitHub
```bash
# Kiểm tra trạng thái file thay đổi
git status

# Thêm các file bạn đã làm vào staging
git add 06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_07_TranHongLinh/

# Commit với thông điệp rõ ràng
git commit -m "feat(linh-th): hoan tat phan tich case study va ban thao M3 M4 M6 chuong 5"

# Push nhánh cá nhân lên remote GitHub
git push origin feature/tranhonglinh
```

### Bước 5: Tạo Pull Request (PR)
- Mở giao diện GitHub của repository, tạo Pull Request từ nhánh `feature/tranhonglinh` vào nhánh `main`.
- Đính kèm tóm tắt các sản phẩm đã hoàn thành để nhóm cùng đối soát trước khi merge.
