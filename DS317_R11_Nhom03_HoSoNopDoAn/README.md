# Hồ Sơ Nộp Đồ Án Môn Học DS317 - Nhóm 03 (DS317.R11)

Thư mục này tập hợp toàn diện các sản phẩm nghiệm thu cuối kỳ của **Nhóm 03** theo đúng cấu trúc 8 thư mục con quy định của học phần **DS317 - Khai phá dữ liệu trong doanh nghiệp**, Trường Đại học Công nghệ Thông tin (ĐHQG-HCM).

- **Đề tài:** Dự báo thời điểm cập cảng của tàu biển thay thế ETA tự khai báo (*Prediction of Vessel Port Arrival Time Replacing Self-Reported ETA*)
- **Dữ liệu nghiên cứu:** NOAA AIS 2025 (`256.94M` bản tin thô, `92.68M` bản ghi nền tảng) kết hợp thời tiết NOAA RTMA 2025.
- **Engine thực nghiệm:** Engine v2 chính thức (7 mô hình x 13 biến thể x 3-Fold Time-based Cross Validation).

---

## 1. Cấu Trúc 8 Thư Mục Con Chuẩn Môn Học

| STT | Thư mục nộp bài | Phân loại sản phẩm | Trách nhiệm chính | Chi tiết tài liệu hướng dẫn |
| :-: | :--- | :--- | :--- | :--- |
| 1 | [`01_BaoCao/`](01_BaoCao/README.md) | Báo cáo Đồ án Cuối kỳ 7 Chương (`.docx`, `.pdf`, 30-50 trang) | **Cả nhóm** (Võ Đình Kiên chủ trì) | [`01_BaoCao/README.md`](01_BaoCao/README.md) |
| 2 | [`02_Slides/`](02_Slides/README.md) | Bộ Slide Thuyết trình Bảo vệ 10 phần (`.pptx`, `.pdf`, 15-20 phút) | **Trần Hồng Lĩnh** chủ trì toàn bộ (các thành viên khác cung cấp nội dung đầu vào) | [`02_Slides/README.md`](02_Slides/README.md) |
| 3 | [`03_SourceCode/`](03_SourceCode/README.md) | Toàn bộ mã nguồn, script kiểm định thống kê, `requirements.txt`, `environment.yml` | **Võ Đình Kiên** | [`03_SourceCode/README.md`](03_SourceCode/README.md) |
| 4 | [`04_Data/`](04_Data/README.md) | Dữ liệu mẫu demo (`demo_sample_3000.*`), từ điển 39 thuộc tính, liên kết dữ liệu lớn | **Quách Tuấn Kiệt** | [`04_Data/README.md`](04_Data/README.md) |
| 5 | [`05_Model/`](05_Model/README.md) | Hệ thống tham số cấu hình (`parameters/`), siêu tham số và trọng số mô hình (`saved_models/`) | **Võ Đình Kiên & Trần Hồng Lĩnh** | [`05_Model/README.md`](05_Model/README.md) |
| 6 | [`06_Results/`](06_Results/README.md) | 216 bảng CSV số liệu thực nghiệm đo lỗi, ma trận tương quan, kiểm toán DAMA và biểu đồ | **Lê Sỹ Liêm & Huỳnh Chí Kiên** | [`06_Results/README.md`](06_Results/README.md) |
| 7 | [`07_Demo/`](07_Demo/README.md) | Kịch bản demo, video quay màn hình dự phòng ($\le 3$ phút) và ảnh chụp các tab chức năng | **Đỗ Văn Lộc** | [`07_Demo/README.md`](07_Demo/README.md) |
| 8 | [`08_QuanLyNhom/`](08_QuanLyNhom/README.md) | Bảng phân công & đánh giá đóng góp %, nhật ký thực nghiệm, biên bản họp, đạo đức AI | **Võ Đình Kiên & Đỗ Văn Lộc** | [`08_QuanLyNhom/README.md`](08_QuanLyNhom/README.md) |

---

## 2. Quy Chuẩn Đồng Bộ Tự Động từ Kho Output

Toàn bộ kết quả đầu ra của các notebook được quản lý tập trung tại [`05_Output_Cac_Notebook/`](../05_Output_Cac_Notebook/README.md). Nhóm sử dụng công cụ Python chuẩn hóa để kiểm kê và đồng bộ:

```bash
# 1. Kiểm tra số lượng tệp và xem trước danh sách đồng bộ (không ghi đè file)
python 05_Output_Cac_Notebook/dong_bo_ho_so_nop.py --dry-run

# 2. Thực hiện đồng bộ thực tế toàn bộ file số liệu và tham số nhẹ (< 95 MB) sang 05_Model/ và 06_Results/
python 05_Output_Cac_Notebook/dong_bo_ho_so_nop.py
```

---

## 3. Quy Tắc Quản Trị Tệp Lớn và Git

- **Giới hạn kích thước tệp:** Các tệp nhị phân có dung lượng $> 100 \text{ MB}$ (bộ dữ liệu gốc `.parquet`, tệp dự đoán chi tiết hàng chục triệu dòng) được quản lý tự động bởi [`.gitignore`](../.gitignore) và được lưu trữ trên nền tảng đám mây **Kaggle Datasets** và **Google Drive Nhóm 03**.
- **Tính khả thi và tái lập:** Mọi thành viên và giảng viên có thể tái lập toàn bộ kết quả thực nghiệm thông qua các tệp tham số JSON (`*_meta.json`) và bộ dữ liệu mẫu offline (`04_Data/demo_sample_3000.*`) chạy trong dưới 2.0 giây.
