# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 03

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Quách Tuấn Kiệt
- **Mã số sinh viên (MSSV):** 24520911
- **Vai trò trong đồ án:** Kỹ sư Dữ liệu (Data Engineer), Chương 2 Dữ liệu & DAMA, Module M3 và Rà soát tái lập code
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT (CHỈ PHẦN CÒN THIẾU)

> [!NOTE]
> Phân công đã được chốt chính thức theo chỉ đạo của ĐẠI CA: chỉ giao phần việc CÒN THIẾU; nội dung đã có sẵn trong workspace không giao lại. Chi tiết xem [Kế hoạch hoàn thiện](../../00_Quan_Ly_Va_Tai_Lieu_Chung/K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md) (Phần A, B, C, D).

1. **Soạn thảo Chương 2: Dữ liệu và Đo lường Chất lượng Dữ liệu** (chỉ viết văn bản, tổng hợp từ số liệu DAMA, từ điển dữ liệu và Data Inventory ĐÃ CÓ SẴN, không tính lại).
2. **Chương 5 phần Module M3:** viết từ Engine v2 (`m3_features_*` và mục M3 trong tệp Ablation `.md`); báo cáo `Bao_cao_Thuc_nghiem_Module_M3_Ablation_Study.docx` đã có là số liệu Engine v1, khi trích dẫn phải đối chiếu số liệu Engine v2.
3. **Rà soát tính tái lập mã nguồn** (chuyển từ Trần Hồng Lĩnh): kiểm tra khả năng chạy lại notebook/script trong `05_Output_Cac_Notebook/` và `02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/`, không có đường dẫn tuyệt đối cứng.
4. **Cung cấp đầu vào cho Slide (Phần 3: Tài sản dữ liệu & DAMA)** gửi cho Trần Hồng Lĩnh. **Không làm slide.**

### 2.1. Đã có sẵn - KHÔNG phân công (chỉ sử dụng/trích dẫn)
- Dữ liệu mẫu Demo (3,000 dòng, 39 cột): [`demo_sample_3000.csv`](../../DS317_R11_Nhom03_HoSoNopDoAn/04_Data/demo_sample_3000.csv), [`.parquet`](../../DS317_R11_Nhom03_HoSoNopDoAn/04_Data/demo_sample_3000.parquet).
- Kiểm kê dữ liệu: [`Lab3_DS317.R11_Nhom03_DataInventory.xlsx`](../../01_Bai_Tap_Ve_Nha_Chinh_Thuc/BT3_Thuyet_Minh_De_Tai/Lab3_DS317.R11_Nhom03_DataInventory.xlsx).
- Đo lường DAMA: [`06_.../DAMA/`](../../05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/DAMA/) (8 tệp), [`02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/`](../../05_Output_Cac_Notebook/02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/README.md) (30 tệp), từ điển RAW18/PREP27 trong `DICTIONARY/`.
- Báo cáo module M3: [`Bao_cao_Modules/`](../../03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Bao_cao_Modules/README.md).

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO (ĐÃ HOÀN THÀNH 100%)
- [x] Bản thảo Chương 3: [`Chuong_03_Du_Lieu_Va_Do_Luong_DAMA.md`](./Chuong_03_Du_Lieu_Va_Do_Luong_DAMA.md) và [`Chuong_03_Du_Lieu_Va_Do_Luong_DAMA.docx`](./Chuong_03_Du_Lieu_Va_Do_Luong_DAMA.docx).
- [x] Bản thảo phần Module M3 trong Chương 5: [`Chuong_05_Phan_Module_M3_Feature_Engineering.md`](./Chuong_05_Phan_Module_M3_Feature_Engineering.md) và [`Chuong_05_Phan_Module_M3_Feature_Engineering.docx`](./Chuong_05_Phan_Module_M3_Feature_Engineering.docx).
- [x] Báo cáo rà soát tái lập mã nguồn: [`Kiem_Tra_Tai_Lap_Code.md`](./Kiem_Tra_Tai_Lap_Code.md).
- [x] Nội dung/ảnh Phần 3 Slide gửi Trần Hồng Lĩnh: [`Noi_Dung_Slide_Phan_03_Tai_San_Du_Lieu_Va_DAMA.md`](./Noi_Dung_Slide_Phan_03_Tai_San_Du_Lieu_Va_DAMA.md).

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
