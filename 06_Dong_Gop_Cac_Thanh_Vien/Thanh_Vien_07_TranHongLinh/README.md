# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 07

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Trần Hồng Lĩnh
- **Mã số sinh viên (MSSV):** 24520970
- **Vai trò trong đồ án:** Kỹ sư Học máy & Tối ưu hóa Mô hình (ML/DL Engineer & Error Analysis Specialist)
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT
1. **Phân tích Lỗi Chuyên sâu có Kiểm chứng (Case Study Error Analysis):**
   - Viết script Python trích xuất từ dữ liệu kiểm thử các chuyến tàu biển thật (kèm định danh `MMSI`, tên/loại tàu, vận tốc `sog`, cự ly `Dist_To_Berth_NM`) có sai số thặng dư (Residual) cực trị:
     + Nhóm chuyến tàu dự báo cực kỳ chính xác (sai số $< 3$ giờ).
     + Nhóm chuyến tàu sai số lớn ở phân tầng `<= 168h` (giải thích nguyên nhân vật lý/hàng hải: thời tiết bão, giảm tốc đột ngột, chờ lệnh hoa tiêu).
     + Nhóm chuyến tàu ở phân tầng `> 168h` (giải thích đặc thù tàu neo đậu kéo dài, hải trình đa chặng).
   - Soạn thảo tài liệu **Báo cáo Phân tích Lỗi Case Study và Bản chất Phân tầng 168h** chuẩn mực thay thế tài liệu cũ đã xóa.
2. **Soạn thảo Báo cáo Cuối kỳ:**
   - **Chương 5: Kết quả Thực nghiệm và Thảo luận (Trọng tâm kỹ thuật):**
     + Soạn thảo phân tích kết quả Baseline toàn cục B0 trên 7 kiến trúc mô hình (Ridge, CatBoost, LightGBM, XGBoost, Bi-LSTM, ST-GNN, PatchTST, TFT).
     + Phân tích Module M3: Đóng góp của các đặc trưng tương tác vật lý hàng hải (Cự ly $\times$ Vận tốc, Tỷ lệ cản gió, Gia tốc).
     + Phân tích Module M4: Đóng góp của trường khí tượng hải văn RTMA (Tốc độ gió, Chiều cao sóng, Hướng gió ngược).
     + Phân tích Module M6: Đóng góp của hàm mất mát tùy biến Custom Asymmetric Loss (cơ chế phạt lệch dự báo sớm với trọng số $w=2.5$, đánh đổi giữa MAE đối xứng và chi phí vận hành cảng).
3. **Đóng gói và Rà soát Mã nguồn Thực nghiệm:**
   - Kiểm tra khả năng chạy tái lập của các file mã nguồn và notebook trong `05_Output_Cac_Notebook/`.
   - Bảo đảm cấu trúc dữ liệu đầu ra ngăn nắp, sạch sẽ, không có đường dẫn tuyệt đối cứng.

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO
- [ ] Báo cáo phân tích lỗi Case Study và Bản chất phân tầng 168h (`Bao_Cao_Phan_Tich_Loi_Case_Study.md` hoặc `.docx`).
- [ ] Script Python trích xuất case study và vẽ biểu đồ quỹ đạo sai số (`case_study_error_analysis.py`).
- [ ] Bản thảo nội dung Baseline B0, Module M3, Module M4, Module M6 trong Chương 5 Báo cáo cuối kỳ.
- [ ] Báo cáo rà soát tính tái lập của mã nguồn thực nghiệm (`Kiem_Tra_Tai_Lap_Code.md`).

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
