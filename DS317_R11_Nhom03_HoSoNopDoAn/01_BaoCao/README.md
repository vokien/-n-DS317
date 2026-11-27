# 01 - Báo Cáo Đồ Án Cuối Kỳ (`01_BaoCao/`)

Thư mục này lưu trữ văn bản Báo cáo Đồ án Cuối kỳ hoàn chỉnh dưới hai định dạng Microsoft Word (`.docx`) và Adobe PDF (`.pdf`) của **Nhóm 03 (Lớp DS317.R11)** cho đề tài **Dự báo Thời điểm Cập Cảng của Tàu Biển Thay Thế ETA Tự Khai Báo** (*Prediction of Vessel Port Arrival Time Replacing Self-Reported ETA*).

---

## 1. Quy Cách Báo Cáo theo Chuẩn Môn Học DS317

- **Dung lượng quy chuẩn:** 30 - 50 trang (không tính trang bìa, mục lục và phụ lục).
- **Định dạng nộp bài:**
  - `DS317_R11_Nhom03_BaoCao.docx`: Bản Word phục vụ chấm điểm và kiểm tra đạo văn.
  - `DS317_R11_Nhom03_BaoCao.pdf`: Bản xuất PDF chính thức lưu trữ thư viện.
- **Quy chuẩn ký hiệu & văn bản:** Sử dụng dấu chấm `.` làm dấu thập phân (ví dụ: `21.64`), 100% dấu gạch ngang tiêu chuẩn `-` (ASCII 0x2D), công thức toán học chuẩn LaTeX/OMML, trích dẫn tài liệu tham khảo chuẩn IEEE.

---

## 2. Bố Cục 7 Chương Cốt Lõi và Phân Công Biên Soạn

| Chương | Tên chương và Trọng tâm nghiên cứu | Thành viên chủ trì | Thành viên phối hợp | Tệp nguồn số liệu chính |
| :---: | :--- | :--- | :--- | :--- |
| **Chương 1** | **Tổng quan Đề tài & Bối cảnh Doanh nghiệp:** Bài toán sai lệch ETA tự khai báo, bối cảnh chuỗi cung ứng cảng biển, chi phí lưu bến $Demurrage$ (15,000 - 30,000 USD/ngày), đơn giá bốc xếp ILWU (56.85 USD/h), mục tiêu và phạm vi đề tài. | **Võ Đình Kiên** | **Đỗ Văn Lộc** | `01_Bai_Tap_Ve_Nha_Chinh_Thuc/BT1_Xac_Dinh_Bai_Toan/` |
| **Chương 2** | **Khảo sát Hiện trạng & Cơ sở Lý thuyết:** Khảo sát 6 công trình SOTA hàng hải quốc tế; cơ sở lý thuyết thuật toán học máy (Ridge, Random Forest, LightGBM, XGBoost, CatBoost, Bi-LSTM); chuẩn chất lượng dữ liệu DAMA/ISO 8000; lý thuyết Conformal Prediction và Asymmetric Loss. | **Nguyễn Hữu Bảo Lộc** | **Lê Sỹ Liêm** | `00_Quan_Ly_Va_Tai_Lieu_Chung/TongQuan_RelatedWork_ETA_6BaiBao_v2.xlsx`, `Dinh_nghia_ham_toan_hoc.docx` |
| **Chương 3** | **Khám phá Dữ liệu & Kiểm toán Chất lượng 6 Chiều DAMA:** Kiểm toán 6 chiều chất lượng DAMA trên 256.94M dòng thô vs 92.68M dòng nền tảng; giám sát Data Drift qua 4 Quý (Q1-Q4); phân tích tương quan Pearson ($r = +0.50971$) và từ điển 27 thuộc tính. | **Quách Tuấn Kiệt** | **Huỳnh Chí Kiên** | `05_Output_Cac_Notebook/02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/`, `06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/` |
| **Chương 4** | **Đề xuất Kỹ thuật Khai phá Dữ liệu & Kiến trúc Engine v2:** Thiết kế pipeline 2-Pass; cơ chế Time-based Split ngăn chặn rò rỉ dữ liệu; chi tiết 7 Module thực nghiệm (M1 Lọc ngoại lai IQR, M2 Điền khuyết, M3 Tạo đặc trưng, M4 Thời tiết RTMA, M5 Chọn lọc MI & log1p, M6 Asymmetric Loss, M7 Adaptive Conformal). | **Võ Đình Kiên** | **Trần Hồng Lĩnh** | `02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/02_Runner_Song_Song_Chinh_Thuc_v2/` |
| **Chương 5** | **Kết quả Thực nghiệm, Kiểm định Thống kê & Thảo luận:** Kết quả thực nghiệm Engine v2 của 7 mô hình x 13 biến thể x 3 Fold; đánh giá phân tầng (`All`, `LE_168h`, `GT_168h`); kiểm định ý nghĩa thống kê Wilcoxon / Diebold-Mariano ($p < 0.001$); giải thích mô hình qua SHAP; phân tích lỗi Case Study; bài toán quy đổi tài chính USD ($ROI$). | **Cả nhóm** (Võ Đình Kiên tổng hợp) | **Lê Sỹ Liêm & Huỳnh Chí Kiên** | `03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md`, `06_Results/` |
| **Chương 6** | **Triển khai Ứng dụng Demo Web BI Dashboard & Dự báo ETA:** Kiến trúc ứng dụng Streamlit (`app.py`), tab giám sát CLDL DAMA tương tác, tab phân tích phân phối, tab suy luận ETA thời gian thực từ trọng số thật, diễn giải điều độ cảng. | **Đỗ Văn Lộc** | **Quách Tuấn Kiệt** | `07_Demo/`, `03_SourceCode/app.py`, `04_Data/demo_sample_3000.*` |
| **Chương 7** | **Kết luận, Đạo đức AI, Tuân thủ Pháp lý & Hướng Phát triển:** Tổng kết đóng góp đề tài; tuân thủ Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 & Luật Dữ liệu 60/2024/QH15 (cơ chế ẩn danh `MMSI` -> `Vessel_Hash_ID`); khai báo sử dụng AI minh bạch; hạn chế và hướng mở rộng. | **Nguyễn Hữu Bảo Lộc** | **Võ Đình Kiên** | `08_QuanLyNhom/` |

---

## 3. Danh Mục Tệp Bàn Giao

- `DS317_R11_Nhom03_BaoCao.docx`: Báo cáo chính thức (Word).
- `DS317_R11_Nhom03_BaoCao.pdf`: Báo cáo chính thức (PDF).
- `Phu_Luc_Chuyen_De/` (nếu có): Tập hợp các tài liệu kỹ thuật phụ trợ.
