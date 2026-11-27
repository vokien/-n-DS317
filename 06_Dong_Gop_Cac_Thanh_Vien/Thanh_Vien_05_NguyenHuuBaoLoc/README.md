# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 05

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Nguyễn Hữu Bảo Lộc
- **Mã số sinh viên (MSSV):** 24520983
- **Vai trò trong đồ án:** Chuyên viên Tổng quan Học thuật, Trích dẫn IEEE & Đạo đức AI
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT (CHỈ PHẦN CÒN THIẾU)

> [!NOTE]
> Phân công đã được chốt chính thức theo chỉ đạo của ĐẠI CA: chỉ giao phần việc CÒN THIẾU; nội dung đã có sẵn trong workspace không giao lại. Chi tiết xem [Kế hoạch hoàn thiện](../../00_Quan_Ly_Va_Tai_Lieu_Chung/K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md) (Phần A, B, C, D).

1. **Chuẩn hóa trích dẫn IEEE:** xây dựng và kiểm tra `references.bib` (chưa có trong workspace), bảo đảm 100% trích dẫn trong văn bản có nguồn.
2. **Chương 1 (tiểu mục 1.4):** viết nội dung Tổng quan tình hình nghiên cứu và Research Gap, dựa trên bảng Related Work ĐÃ CÓ (`TongQuan_RelatedWork_ETA_6BaiBao_v2.xlsx`), không làm lại phần nghiên cứu 6 bài báo.
3. **Tuân thủ Pháp lý & Đạo đức AI:** tài liệu tuân thủ pháp luật bảo vệ dữ liệu cá nhân và Bản khai báo sử dụng AI minh bạch (`08_QuanLyNhom/` hiện chỉ có `README.md`).
4. **Chương 5 phần Module M5** (log1p và chọn lọc Mutual Information; viết từ số liệu Engine v2 `m5_selection_*`).
5. **Cung cấp nội dung cho Slide (Phần 2, Phần 10)** gửi Trần Hồng Lĩnh. **Không làm slide.**

### 2.1. Đã có sẵn - KHÔNG phân công (chỉ sử dụng/trích dẫn)
- Bảng Related Work 6 bài báo: [`TongQuan_RelatedWork_ETA_6BaiBao_v2.xlsx`](../../00_Quan_Ly_Va_Tai_Lieu_Chung/TongQuan_RelatedWork_ETA_6BaiBao_v2.xlsx).
- Báo cáo M5 (Engine v1): [`BaoCao_M5.docx`](../../03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Bao_cao_Modules/BaoCao_M5.docx); số liệu Engine v2 M5: [`Tong_Hop_..._Ablation_7_Module.md`](../../03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md) và `m5_*` trong `08_.../results/`.

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO
- [ ] Tệp `references.bib` chuẩn IEEE.
- [ ] Bản thảo tiểu mục 1.4 Chương 1 (`Tong_Quan_SOTA_Related_Work.docx` hoặc `.md`).
- [ ] Tài liệu Tuân thủ Pháp lý & Đạo đức AI và Bản khai báo sử dụng AI.
- [ ] Bản thảo phần Module M5 trong Chương 5.
- [ ] Nội dung Phần 2 và Phần 10 Slide gửi Trần Hồng Lĩnh.

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
