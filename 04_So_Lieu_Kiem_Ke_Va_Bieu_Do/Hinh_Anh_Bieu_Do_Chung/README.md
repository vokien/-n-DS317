# Hình Ảnh Biểu Đồ Dùng Chung (`04_So_Lieu_Kiem_Ke_Va_Bieu_Do/Hinh_Anh_Bieu_Do_Chung/`)

Thư mục này chứa toàn bộ các biểu đồ phân tích dữ liệu, bản đồ địa không gian, sơ đồ kỹ thuật và hình chụp giao diện (Mockup Demo) với chất lượng cao ($DPI \ge 300$) phục vụ đồ án **DS317 - Khai phá dữ liệu trong doanh nghiệp**.

---

## 1. Danh Mục Tệp Tin và Ý Nghĩa Trực Quan Hóa

| STT | Tên tệp tin | Định dạng | Dung lượng | Ý nghĩa và Vị trí sử dụng trong Báo cáo |
| :-: | :--- | :---: | :-: | :--- |
| 1 | `Hinh1_Phan_Phoi_Target_Hours.png` | PNG | ~258 KB | Biểu đồ phân phối biến mục tiêu `Target_Hours` (thể hiện phân phối lệch phải rõ rệt và lý do phân tầng 168 giờ). Sử dụng tại **Mục 3.2 Báo cáo**. |
| 2 | `Hinh2_Scatter_Dist_vs_Target.png` | PNG | ~1.37 MB | Đồ thị phân tán giữa Cự ly đến bến (`Dist_To_Berth_NM`) và `Target_Hours` (minh họa tương quan tuyến tính mạnh $r = +0.50971$). Sử dụng tại **Mục 3.3 Báo cáo**. |
| 3 | `Hinh3_Boxplot_SOG_Draft_Cargo_vs_Tanker.png` | PNG | ~177 KB | Biểu đồ hộp so sánh vận tốc $sog$ và mớn nước $draft$ giữa 2 nhóm tàu trọng điểm: Tàu chở hàng rời (Cargo) và Tàu chở dầu (Tanker). Sử dụng tại **Mục 3.4 Báo cáo**. |
| 4 | `Hinh4_Mat_Do_Dia_Khong_Gian.png` | PNG | ~1.24 MB | Bản đồ nhiệt mật độ vị trí tàu biển NOAA AIS 2025 dọc bờ biển và các cụm cảng lớn của Hoa Kỳ. Sử dụng tại **Mục 3.1 Báo cáo**. |
| 5 | `Hinh8_1_So_Do_Time_Based_Split.png` | PNG | ~704 KB | Sơ đồ kỹ thuật phân chia tập dữ liệu theo thời gian ($Time-based Split$): Q1-Q3 dùng cho Train/Val (K-Fold), Q4 dùng cho Holdout Test độc lập. Sử dụng tại **Mục 4.2 Báo cáo**. |
| 6 | `Hinh_PL1_Mockup_Demo_Streamlit.png` | PNG | ~599 KB | Bản thiết kế giao diện ứng dụng Web Demo Streamlit tích hợp BI Dashboard và dự báo ETA. Sử dụng tại **Phụ lục và Mục 6.1 Báo cáo**. |
| 7 | `Thong_Ke_Nhan_Xet.txt` | Text | ~1.3 KB | Văn bản ghi nhận các số liệu thống kê mô tả cụ thể trích xuất trực tiếp từ dữ liệu để hỗ trợ thành viên viết lời bình cho từng hình. |
| 8 | `EDA_Kaggle_Output/` | Thư mục | ~568 KB | Thư mục con lưu trữ 4 biểu đồ EDA được kết xuất tự động từ phiên chạy trực tiếp trên môi trường đám mây Kaggle. |

---

## 2. Thư Mục Con `EDA_Kaggle_Output/`

Chứa 4 biểu đồ EDA nguyên bản trích xuất trực tiếp từ notebook chạy trên Kaggle:
- `EDA_Kaggle_BieuDo1_PhanPhoi_Target.png`: Đồ thị phân phối thời gian còn lại đến bến.
- `EDA_Kaggle_BieuDo2_Scatter_Dist_vs_Target.png`: Phân tán cự ly hình học và thời gian đến bến.
- `EDA_Kaggle_BieuDo3_Boxplot_SOG_Draft.png`: Phân phối mớn nước và vận tốc theo loại tàu.
- `EDA_Kaggle_BieuDo4_MatDo_DiaKhongGian.png`: Mật độ không gian tọa độ kinh/vĩ độ AIS.

---

## 3. Quy Cách Sử Dụng trong Tài Liệu

Khi chèn các hình ảnh này vào báo cáo Word hoặc Slide PowerPoint:
- Đảm bảo giữ nguyên tỷ lệ khung hình (Aspect Ratio), không kéo dãn làm méo số liệu trực quan.
- Ghi rõ chú thích nguồn: *(Nguồn: Nhóm 03 - Trích xuất từ tập dữ liệu NOAA AIS 2025)*.
