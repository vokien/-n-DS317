# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 04

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Huỳnh Chí Kiên
- **Mã số sinh viên (MSSV):** 24520880
- **Vai trò trong đồ án:** Chuyên viên Biểu đồ Engine v2 & Giải thích Mô hình XAI
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT (CHỈ PHẦN CÒN THIẾU)

> [!NOTE]
> Phân công đã được điều chỉnh theo yêu cầu của ĐẠI CA: chỉ giao phần việc CÒN THIẾU; nội dung đã có sẵn trong workspace không giao lại. Chi tiết xem [Kế hoạch hoàn thiện](../../00_Quan_Ly_Va_Tai_Lieu_Chung/K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md) (Phần A, B, C). Các điểm ghi **[Chờ ĐẠI CA xác nhận]** là đề xuất, chưa là quyết định cuối.

1. **Biểu đồ Engine v2 mới cho Chương 4 & 5 (`DPI >= 300`)** (Runner chỉ xuất CSV, chưa có biểu đồ Engine v2):
   - Sơ đồ kiến trúc Engine v2 tích hợp tiền xử lý và điều độ cảng.
   - Biểu đồ so sánh 7 mô hình theo phân tầng (`All`, `LE_168h`, `GT_168h`) vẽ từ `runner*_master_horizons.csv`.
   - Biểu đồ Delta Ablation M1-M7 (MAE, RMSE, AsymCost).
   - Biểu đồ residual theo phân tầng 168h (cần dữ liệu cấp dòng, chạy trên Kaggle).
2. **SHAP (XAI):** script nạp mô hình tốt nhất, `SHAP Summary Plot` và `SHAP Beeswarm Plot` (chưa có trong workspace; cần dữ liệu kiểm thử bị `.gitignore`, chạy trên Kaggle).
3. **Báo cáo:** Chương 3 (Phương pháp Tiền xử lý) và Chương 5 phần Module M1, M2 (viết từ số liệu Engine v2 đã có).
4. **Cung cấp biểu đồ/hình cho Slide (Phần 5, Phần 7)** gửi Trần Hồng Lĩnh. **Không làm slide.**
- **Lưu ý chạy trên Kaggle:** `detailed_predictions/*.parquet` bị `.gitignore` và chưa có trong workspace; mọi tác vụ cần dữ liệu này phải chạy trên Kaggle, không chạy nặng trên máy cá nhân.

### 2.1. Đã có sẵn - KHÔNG phân công (chỉ sử dụng/trích dẫn)
- Biểu đồ EDA/DAMA/BTVN: [`04_So_Lieu_Kiem_Ke_Va_Bieu_Do/`](../../04_So_Lieu_Kiem_Ke_Va_Bieu_Do/README.md) (10 PNG), [`02_.../CHARTS/`](../../05_Output_Cac_Notebook/02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/CHARTS/) (6 PNG), [`06_.../Hinh_Anh_Bieu_Do/`](../../05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/Hinh_Anh_Bieu_Do/) (12 PNG).
- Số liệu M1, M2: [`Tong_Hop_..._Ablation_7_Module.md`](../../03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md) và `m1_*`, `m2_*` trong `07_.../results/`.
- Trọng số: [`runner1_saved_models.zip`](../../05_Output_Cac_Notebook/runner1_saved_models.zip), [`runner2_saved_models.zip`](../../05_Output_Cac_Notebook/runner2_saved_models.zip).

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO
- [ ] Thư mục biểu đồ Engine v2 chất lượng cao `figures_report/` (`.png`/`.pdf`, `DPI >= 300`).
- [ ] Script biểu đồ Ablation/phân tầng và SHAP (`generate_ablation_charts.py`, `generate_shap_plots.py`, chạy được trên Kaggle).
- [ ] Bản thảo Chương 3 và phần Module M1, M2 trong Chương 5.
- [ ] Biểu đồ/hình gửi Trần Hồng Lĩnh cho Phần 5 và Phần 7 Slide.

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
git checkout -b feature/huynhchikien
```

### Bước 3: Thao tác làm việc và lưu sản phẩm
- **QUY TẮC CỐT LÕI:** Bạn chỉ thêm, sửa, xóa file **BÊN TRONG THƯ MỤC CỦA MÌNH**:
  `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_04_HuynhChiKien/`
- Không chỉnh sửa trực tiếp vào thư mục của thành viên khác hoặc thư mục nộp bài chung `DS317_R11_Nhom03_HoSoNopDoAn/` khi chưa tổng duyệt.

### Bước 4: Commit và Push lên GitHub
```bash
# Kiểm tra trạng thái file thay đổi
git status

# Thêm các file bạn đã làm vào staging
git add 06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_04_HuynhChiKien/

# Commit với thông điệp rõ ràng
git commit -m "feat(kien-hc): hoan thien shap plots va ban thao chuong 3 tien xu ly"

# Push nhánh cá nhân lên remote GitHub
git push origin feature/huynhchikien
```

### Bước 5: Tạo Pull Request (PR)
- Mở giao diện GitHub của repository, tạo Pull Request từ nhánh `feature/huynhchikien` vào nhánh `main`.
- Đính kèm tóm tắt các sản phẩm đã hoàn thành để nhóm cùng đối soát trước khi merge.
