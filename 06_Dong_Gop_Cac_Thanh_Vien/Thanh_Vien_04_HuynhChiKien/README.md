# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 04

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Huỳnh Chí Kiên
- **Mã số sinh viên (MSSV):** 24520880
- **Vai trò trong đồ án:** Chuyên viên Khám phá & Trực quan hóa Dữ liệu (Data Visualization & EDA Specialist), Giải thích Mô hình XAI
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT
1. **Thiết kế Biểu đồ Chương 4 & Chương 5 chuẩn Engine v2 (`DPI >= 300`):**
   - Thiết kế các sơ đồ và biểu đồ độ phân giải cao phục vụ Báo cáo cuối kỳ:
     + Sơ đồ kiến trúc Engine v2 tích hợp tiền xử lý và phục vụ điều độ cảng.
     + Biểu đồ đối sánh hiệu năng 7 mô hình theo 3 phân tầng (`All`, `LE_168h`, `GT_168h`).
     + Biểu đồ Delta Ablation Study từ Module M1 đến Module M7 (thể hiện rõ mức tăng/giảm MAE, RMSE, AsymCost).
     + Biểu đồ phân tích sai số thặng dư (Residual Analysis: Residual vs Target, Residual vs Distance).
2. **Giải thích Mô hình chuyên sâu bằng SHAP (Explainable AI - XAI):**
   - Viết script nạp mô hình tốt nhất (CatBoost / LightGBM / XGBoost) từ các runner và dữ liệu kiểm thử.
   - Trích xuất SHAP values, vẽ `SHAP Summary Plot` (Bar plot xếp hạng tầm quan trọng đặc trưng) và `SHAP Beeswarm Plot` (phân tích chiều hướng tác động của từng đặc trưng lên ETA).
   - Phân tích vai trò của cự ly trắc địa `Dist_To_Berth_NM`, vận tốc `sog`, các tương tác M3 và tác động cản gió/sóng RTMA M4.
3. **Soạn thảo Báo cáo Cuối kỳ:**
   - **Chương 3: Phương pháp Tiền xử lý Dữ liệu:**
     + Kiến trúc xử lý luồng 2-Pass Rolling Stream trên 320.78M dòng thô.
     + Bộ lọc 3 tầng (lọc vận tốc phi vật lý, lọc trạng thái neo đậu, lọc loại tàu thương mại).
     + Thuật toán Domain-based Imputation (điền khuyết kích thước thân vỏ đưa tỷ lệ khuyết về 0.00% tuyệt đối).
     + Chế tác đặc trưng hình học thân vỏ ($Area\_Proxy$, $Volume\_Proxy$) và biến đổi lượng giác góc hành hải $(\sin, \cos)$.
   - **Chương 5 (phần Module M1 & Module M2):**
     + Phân tích kết quả thực nghiệm Module M1 (Lọc ngoại lai động học) và Module M2 (Khôi phục dữ liệu khuyết thiếu thân vỏ).

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO
- [ ] Bộ thư mục ảnh biểu đồ chất lượng cao (`DPI >= 300`) xuất ra định dạng `.png` hoặc `.pdf` (`figures_report/`).
- [ ] Script Python tạo biểu đồ EDA, biểu đồ Ablation và SHAP plots (`generate_shap_plots.py`, `generate_ablation_charts.py`).
- [ ] Bản thảo Chương 3 Báo cáo cuối kỳ (`Chuong_03_Tien_Xu_Ly_Du_Lieu.docx` hoặc `.md`).
- [ ] Bản thảo phần Module M1 và Module M2 trong Chương 5.

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
