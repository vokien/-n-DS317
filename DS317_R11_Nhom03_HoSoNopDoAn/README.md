# Hồ Sơ Nộp Đồ Án Môn Học DS317 - Nhóm 03 (DS317.R11)

Thư mục chuẩn bị tập hợp sản phẩm nghiệm thu cuối kỳ của **Nhóm 03** theo cấu trúc 8 thư mục con quy định của học phần **DS317 - Khai phá dữ liệu trong doanh nghiệp**.

## Cấu Trúc 8 Thư Mục Con

| STT | Thư mục | Nội dung cần đưa vào khi nộp đồ án |
| :--- | :--- | :--- |
| 1 | `01_BaoCao/` | Báo cáo tổng kết đồ án (`.docx`, `.pdf`) và báo cáo chi tiết các module |
| 2 | `02_Slides/` | Slide thuyết trình bảo vệ đồ án cuối kỳ (`.pptx`, `.pdf`) |
| 3 | `03_SourceCode/` | Mã nguồn chính thức (pipeline tiền xử lý, Runner v2, notebook module, `requirements.txt`) |
| 4 | `04_Data/` | Mô tả dữ liệu / Data Dictionary / liên kết lưu trữ ngoài cho dữ liệu AIS & RTMA lớn (> 100 MB) |
| 5 | `05_Model/` | Tệp trọng số mô hình đã huấn luyện (`saved_models/*.txt`, `.json`, `.cbm`, `.pt`) |
| 6 | `06_Results/` | Bảng CSV tổng hợp (`_summary.csv`, `_folds.csv`, `_horizons.csv`), dự đoán chi tiết (`detailed_predictions/`) và biểu đồ |
| 7 | `07_Demo/` | Mã nguồn ứng dụng Demo (Streamlit / script suy luận ETA) và ảnh/video minh họa |
| 8 | `08_QuanLyNhom/` | Kế hoạch tổng thể, bảng phân công nhiệm vụ và đánh giá thành viên nhóm |

## Lưu Ý Đẩy Lên GitHub & Đồng Bộ Output
- Toàn bộ kết quả đầu ra của các notebook được tập trung trước tại [`05_Output_Cac_Notebook/`](../05_Output_Cac_Notebook/README.md). Khi đã tổng hợp đủ output sau các lượt chạy Kaggle, sử dụng [`dong_bo_ho_so_nop.py`](../05_Output_Cac_Notebook/dong_bo_ho_so_nop.py) (`--dry-run` để xem trước) để sao chép các tệp trọng số và kết quả nhẹ sang `05_Model/` và `06_Results/`.
- Các tệp dữ liệu hoặc trọng số dung lượng lớn (`>= 50 MB` hoặc `>= 100 MB`) cần kiểm tra với `.gitignore` ở thư mục gốc repo hoặc lưu trữ ngoài qua liên kết trong `04_Data/` / `05_Model/` trước khi `git push`.
