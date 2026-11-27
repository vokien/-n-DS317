# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 06

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Lê Sỹ Liêm
- **Mã số sinh viên (MSSV):** 24520951
- **Vai trò trong đồ án:** Chuyên viên Kiểm định Thống kê & Đánh giá Mô hình (Statistical Evaluation Specialist)
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT
1. **Kiểm định Ý nghĩa Thống kê Chính thức (Statistical Significance Testing):**
   - Kế thừa số liệu thực nghiệm qua 3 Fold của 7 mô hình và 13 biến thể trong `05_Output_Cac_Notebook/`.
   - Viết script Python thực hiện các kiểm định thống kê chuẩn mực:
     + `Wilcoxon signed-rank test` (kiểm định phi tham số cho từng cặp mô hình).
     + `Diebold-Mariano test` (kiểm định chuyên dụng cho chuỗi thời gian dự báo).
     + `Paired Bootstrap Test` (với 2,000 lần lấy mẫu lại có hoàn lại) tính toán khoảng tin cậy $95\%$ và giá trị $p$-value.
   - So sánh định lượng xem mức cải thiện của các mô hình nâng cao (CatBoost, XGBoost, LightGBM, M6 Asymmetric, M7 Conformal) so với Baseline B0 có ý nghĩa thống kê thực sự hay không ($p < 0.05$).
2. **Xây dựng Bảng Quy đổi Tài chính Doanh nghiệp (Business ROI Model):**
   - Tham chiếu các chỉ số kinh tế thực tế của ngành hàng hải:
     + Đơn giá nhân công bốc xếp cảng biển ILWU (56.85 USD/giờ).
     + Chi phí phạt lưu tàu / thuê tàu chở hàng (Demurrage / Charter Rate: 15,800 - 90,500 USD/ngày).
   - Lập mô hình tính toán số tiền tiết kiệm cụ thể hàng triệu USD khi giảm tỷ lệ dự báo sớm (`Underprediction_pct`) từ mô hình M6 và đảm bảo độ phủ an toàn 90% từ mô hình M7 Conformal.
3. **Soạn thảo Báo cáo Cuối kỳ:**
   - **Chương 4: Phương pháp Nghiên cứu và Thiết kế Thực nghiệm:**
     + Phát biểu bài toán KPDL hồi quy chuỗi thời gian có kiểm soát trôi dạt.
     + Kịch bản phân chia dữ liệu Expanding Window 3 Folds (Walk-Forward Validation) chống rò rỉ dữ liệu ngoài thời gian (Out-of-Time).
     + Định nghĩa hệ thống độ đo kỹ thuật ($MAE, RMSE, R^2, \text{Within 3h}$) và độ đo nghiệp vụ bất đối xứng ($AsymCost$).
   - **Chương 5 (phần Module M7 & Kiểm định Thống kê):**
     + Phân tích kết quả thực nghiệm Module M7 (Khoảng dự báo Conformal Prediction: `PICP_90`, `MPIW`).
     + Bảng tổng hợp kết quả kiểm định thống kê $p$-value và bảng tính ROI tài chính.

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO
- [ ] Script Python kiểm định thống kê (`statistical_significance_tests.py`).
- [ ] Bảng kết quả kiểm định thống kê và $p$-value (`statistical_test_results.csv` hoặc `.xlsx`).
- [ ] Bảng tính mô hình quy đổi tài chính doanh nghiệp ROI (`Maritime_Logistics_ROI_Model.xlsx`).
- [ ] Bản thảo Chương 4 Báo cáo cuối kỳ (`Chuong_04_Thiet_Ke_Thuc_Nghiem.docx` hoặc `.md`).
- [ ] Bản thảo phần Module M7 và Kiểm định Thống kê trong Chương 5.

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
git checkout -b feature/lesyliem
```

### Bước 3: Thao tác làm việc và lưu sản phẩm
- **QUY TẮC CỐT LÕI:** Bạn chỉ thêm, sửa, xóa file **BÊN TRONG THƯ MỤC CỦA MÌNH**:
  `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_06_LeSyLiem/`
- Không chỉnh sửa trực tiếp vào thư mục của thành viên khác hoặc thư mục nộp bài chung `DS317_R11_Nhom03_HoSoNopDoAn/` khi chưa tổng duyệt.

### Bước 4: Commit và Push lên GitHub
```bash
# Kiểm tra trạng thái file thay đổi
git status

# Thêm các file bạn đã làm vào staging
git add 06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_06_LeSyLiem/

# Commit với thông điệp rõ ràng
git commit -m "feat(liem-ls): hoan thanh kiem dinh thong ke va mo hinh ROI tai chinh"

# Push nhánh cá nhân lên remote GitHub
git push origin feature/lesyliem
```

### Bước 5: Tạo Pull Request (PR)
- Mở giao diện GitHub của repository, tạo Pull Request từ nhánh `feature/lesyliem` vào nhánh `main`.
- Đính kèm tóm tắt các sản phẩm đã hoàn thành để nhóm cùng đối soát trước khi merge.
