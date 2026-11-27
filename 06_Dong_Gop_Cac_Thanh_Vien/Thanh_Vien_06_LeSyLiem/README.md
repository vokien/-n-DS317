# THƯ MỤC LÀM VIỆC CÁ NHÂN - THÀNH VIÊN 06

## 1. THÔNG TIN THÀNH VIÊN
- **Họ và tên:** Lê Sỹ Liêm
- **Mã số sinh viên (MSSV):** 24520951
- **Vai trò trong đồ án:** Chuyên viên Kiểm định Thống kê, Phân tích theo nhóm thời gian & ROI
- **Tỷ lệ đóng góp cam kết:** 14.28%

---

## 2. NHIỆM VỤ ĐƯỢC GIAO CHI TIẾT (CHỈ PHẦN CÒN THIẾU)

> [!NOTE]
> Phân công đã được điều chỉnh theo yêu cầu của ĐẠI CA: chỉ giao phần việc CÒN THIẾU; nội dung đã có sẵn trong workspace không giao lại. Chi tiết xem [Kế hoạch hoàn thiện](../../00_Quan_Ly_Va_Tai_Lieu_Chung/K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md) (Phần A, B, C). Các điểm ghi **[Chờ ĐẠI CA xác nhận]** là đề xuất, chưa là quyết định cuối.

1. **Hạng mục bổ sung - Phân tích theo nhóm thời gian đến cảng `Target_Hours`: `<24h`, `24-72h`, `72-168h`** **[Chờ ĐẠI CA xác nhận người phụ trách và biên nhóm]**:
   - **Hiện trạng:** KHÔNG có sẵn. Bảng Runner chỉ có `All`, `LE_168h`, `GT_168h`; phải tính mới từ `detailed_predictions/*.parquet` của Runner 1 và 2 (chưa có trong workspace, bị `.gitignore`) và chạy trên Kaggle.
   - Bảng `MAE/RMSE/R2/Underprediction_pct` (nên thêm `N`, `Share_pct`, `MBE`, `Within_3h`, `AsymCost`) theo 3 nhóm x 7 mô hình x 3 Fold; biểu đồ (`DPI >= 300`); nhận xét chỉ dựa trên số liệu tính được.
   - Script `time_group_analysis.py`, kiểm tra khớp `N` với `LE_168h`; lưu kết quả trong `Thanh_Vien_06_LeSyLiem/time_group_analysis/`.
   - Đặc tả đầy đủ: Phần A.3 của [Kế hoạch hoàn thiện](../../00_Quan_Ly_Va_Tai_Lieu_Chung/K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md).
2. **Kiểm định thống kê:** chạy script Wilcoxon + Diebold-Mariano ĐÃ CÓ (không viết lại) trên dữ liệu thật; bổ sung Paired Bootstrap 2,000 lần nếu cần; xuất bảng `p-value` so Baseline B0 với các mô hình/biến thể tốt nhất (chạy trên Kaggle cùng lượt với nhóm thời gian).
3. **Bảng quy đổi tài chính ROI** (làm một mình): ILWU 56.85 USD/giờ, chi phí thuê tàu 15,800 - 90,500 USD/ngày, giá trị từ `Underprediction_pct` (M6) và `PICP_90_pct`, `MPIW_hours` (M7) trong Runner 2; ghi rõ giả định.
4. **Soạn thảo Báo cáo:** Chương 4 (gồm định nghĩa 3 nhóm thời gian) và Chương 5 phần Module M7, kiểm định thống kê, phân tích nhóm thời gian.
5. **Cung cấp nội dung cho Slide (Phần 6, Phần 8)** gửi Trần Hồng Lĩnh. **Không làm slide.**
- **Lưu ý chạy trên Kaggle:** `detailed_predictions/*.parquet` bị `.gitignore` và chưa có trong workspace; mọi tác vụ cần dữ liệu này phải chạy trên Kaggle, không chạy nặng trên máy cá nhân.

### 2.1. Đã có sẵn - KHÔNG phân công (chỉ sử dụng/trích dẫn)
- Script kiểm định: [`kiem_dinh_thong_ke_wilcoxon_dm.py`](../../DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/kiem_dinh_thong_ke_wilcoxon_dm.py) (chỉ script, chưa có kết quả chạy).
- Số liệu M6/M7 và 3 mốc phân tầng: [`runner2_master_horizons.csv`](../../05_Output_Cac_Notebook/08_Runner_Song_Song_2_M4_M5_M6_M7/results/runner2_master_horizons.csv), [`m7_intervals_m7_adaptive_summary.csv`](../../05_Output_Cac_Notebook/08_Runner_Song_Song_2_M4_M5_M6_M7/results/m7_intervals_m7_adaptive_summary.csv).
- Chỉ số PSI: [`bang_chi_so_troi_du_lieu_psi.csv`](../../01_Bai_Tap_Ve_Nha_Chinh_Thuc/BT5_Gom_Nhom_Va_Ngoai_Lai/Ket_Qua_Thuc_Nghiem/bang_chi_so_troi_du_lieu_psi.csv).
- Tham khảo đối chiếu (không phải Engine v2): [`benchmark_by_horizon.csv`](../../05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/BENCHMARK_3_VERSIONS/benchmark_by_horizon.csv) (5 mốc, chỉ Dummy_Median và Ridge_Streaming).

---

## 3. DANH MỤC SẢN PHẨM CẦN BÀN GIAO
- [ ] Script `time_group_analysis.py`, bảng `time_group_metrics_by_fold.csv`, `time_group_metrics_summary.csv`, biểu đồ và bản nhận xét 3 nhóm thời gian.
- [ ] Bảng kết quả kiểm định thống kê và `p-value` (`statistical_test_results.csv` hoặc `.xlsx`) chạy từ script có sẵn.
- [ ] Bảng tính mô hình ROI (`Maritime_Logistics_ROI_Model.xlsx`).
- [ ] Bản thảo Chương 4 và phần Module M7, kiểm định, nhóm thời gian trong Chương 5.
- [ ] Nội dung Phần 6 và Phần 8 Slide gửi Trần Hồng Lĩnh.

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
