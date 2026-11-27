# 08 - Quản Lý Nhóm, Biên Bản Họp & Đạo Đức AI (`08_QuanLyNhom/`)

Thư mục này quản lý toàn bộ hồ sơ hành chính, nhật ký thực nghiệm kỹ thuật, biên bản họp nhóm, bảng đánh giá mức độ đóng góp của từng thành viên và tài liệu tuân thủ pháp lý, liêm chính học thuật của **Nhóm 03 (Lớp DS317.R11)** trong học phần **DS317 - Khai phá dữ liệu trong doanh nghiệp**.

---

## 1. Cấu Trúc Các Văn Bản Quản Lý

```text
08_QuanLyNhom/
├── Bang_Phan_Cong_Va_Danh_Gia_Thanh_Vien.docx  <- Bảng phân công chi tiết & tỷ lệ đóng góp % của 7 thành viên
├── Nhat_Ky_Thuc_Nghiem_Experiment_Log.md       <- Nhật ký theo dõi toàn bộ các phiên chạy trên Kaggle
├── Scope_Changelog_Engine_v1_sang_v2.md        <- Lý giải kỹ thuật chuyển dịch từ Engine v1 sang Engine v2
├── Bien_Ban_Hop_Nhom_Giai_Doan_Cuoi_Ky.docx    <- Tập hợp các biên bản họp nhóm tuần và nước rút
├── Tai_Lieu_Tuan_Thu_Phap_Ly_Va_Dao_Duc_AI.docx <- Tuân thủ Luật 91/2025/QH15 & Luật 60/2024/QH15
├── Ban_Khai_Bao_Su_Dung_AI.docx                <- Bản khai báo sử dụng công cụ AI minh bạch
└── README.md
```

---

## 2. Danh Sách 7 Thành Viên và Tỷ Lệ Đóng Góp Dự Kiến

Nhóm 03 hoạt động theo cơ chế phối hợp đa tác tử, phân quyền rõ ràng theo thế mạnh chuyên môn, bảo đảm 100% thành viên đều hoàn thành tốt nhiệm vụ được giao:

| STT | Họ và Tên | MSSV | Vai trò trong nhóm | Trách nhiệm chính trong đồ án | Đóng góp dự kiến |
| :-: | :--- | :---: | :--- | :--- | :---: |
| 1 | **Võ Đình Kiên** | `24520893` | **Nhóm trưởng** | Kiến trúc Pipeline dữ liệu lớn 2-Pass, quản trị repo, chạy 2 Runner trên Kaggle, M4 RTMA, tích hợp Báo cáo cuối kỳ. | **100%** |
| 2 | **Đỗ Văn Lộc** | `24520977` | **Thư ký** | Phát triển ứng dụng Web Demo Streamlit (`app.py`), thiết kế bộ Slide 10 phần, tập hợp biên bản họp nhóm. | **100%** |
| 3 | **Quách Tuấn Kiệt** | `24520911` | Thành viên | Data Inventory 7 tiêu chí, kiểm toán 6 chiều DAMA, từ điển 27 thuộc tính, trích xuất bộ dữ liệu mẫu demo. | **100%** |
| 4 | **Huỳnh Chí Kiên** | `24520880` | Thành viên | Biểu đồ EDA chất lượng cao ($DPI \ge 300$), giải thích mô hình bằng SHAP (Summary & Beeswarm Plot), Module M1 IQR. | **100%** |
| 5 | **Nguyễn Hữu Bảo Lộc** | `24520983` | Thành viên | Khảo sát SOTA 6 bài báo quốc tế, danh mục IEEE `references.bib`, Module M5 (MI & log1p), soạn thảo tài liệu Pháp lý & Đạo đức AI. | **100%** |
| 6 | **Lê Sỹ Liêm** | `24520951` | Thành viên | Kiểm định ý nghĩa thống kê chính thức (Wilcoxon/DM $p < 0.001$), giám sát độ trôi dữ liệu $PSI$, Module M7 Conformal Prediction, bài toán tài chính USD. | **100%** |
| 7 | **Trần Hồng Lĩnh** | `24520970` | Thành viên | Huấn luyện Baseline Ridge, Module M6 (Asymmetric Loss), phân tích lỗi Case Study có kiểm chứng, biểu đồ Business ROI/AsymCost. | **100%** |

---

## 3. Nhật Ký Kỹ Thuật và Scope Changelog

- **Nhật ký thực nghiệm (`Nhat_Ky_Thuc_Nghiem_Experiment_Log.md`):** Ghi nhận chi tiết từng phiên chạy trên môi trường đám mây Kaggle, cấu hình GPU Tesla T4, thời gian bắt đầu/kết thúc, tài nguyên tiêu thụ, và mã băm SHA-256 của các tệp output kết xuất.
- **Lý giải chuyển dịch Engine v1 sang v2 (`Scope_Changelog_Engine_v1_sang_v2.md`):** Minh bạch hóa quyết định nâng cấp thuật toán từ đợt chạy ban đầu (Engine v1) sang Engine v2 (chuẩn hóa Time-based 3-Fold, sửa lỗi phân tầng 168h, tối ưu hóa các hàm mất mát) giúp nâng cao độ chính xác và đảm bảo tính khoa học tuyệt đối.

---

## 4. Tuân Thủ Pháp Lý và Đạo Đức AI

- **Tuân thủ pháp luật Việt Nam:**
  - **Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15:** Toàn bộ định danh định vị tàu biển thật (`MMSI`) đều được ẩn danh hóa một chiều thành mã định danh giả lập ngẫu nhiên (`Vessel_Hash_ID`) trước khi công bố và tích hợp lên Web Demo.
  - **Luật Dữ liệu 60/2024/QH15:** Dữ liệu NOAA AIS và NOAA RTMA được khai thác hợp pháp theo chính sách truy cập mở (Public Domain) của Chính phủ Hoa Kỳ phục vụ mục đích nghiên cứu học thuật phi thương mại.
- **Liêm chính học thuật & Khai báo sử dụng AI:**
  - Nhóm công khai việc sử dụng các trợ lý AI mã nguồn mở trong việc tối ưu hóa cú pháp mã nguồn và kiểm tra lỗi chính tả.
  - Toàn bộ kết quả thực nghiệm, số liệu đo lường và nhận định khoa học đều được chạy thực chứng 100% trên dữ liệu thật, không có hiện tượng bịa đặt số liệu hay gian lận học thuật.

---

## 5. Phân Công Quản Trị Thư Mục

- **Võ Đình Kiên & Đỗ Văn Lộc:** Chủ trì quản lý và cập nhật tiến độ biên bản họp nhóm, bảng đánh giá thành viên.
- **Nguyễn Hữu Bảo Lộc:** Hoàn thiện tài liệu Pháp lý và Đạo đức AI.
