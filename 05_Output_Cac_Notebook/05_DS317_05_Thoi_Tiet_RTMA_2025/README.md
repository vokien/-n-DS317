# Kết Quả Đầu Ra: Tích Hợp Thời Tiết NOAA RTMA 2025 (`05_DS317_05_Thoi_Tiet_RTMA_2025/`)

Thư mục này lưu trữ cấu trúc kết quả từ quá trình ghép nối không gian - thời gian dữ liệu tái phân tích thời tiết NOAA RTMA 2025 trong notebook [`DS317_05_Tich_Hop_Thoi_Tiet_RTMA_2025.ipynb`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_05_Tich_Hop_Thoi_Tiet_RTMA_2025.ipynb).

---

## 1. Mục Đích và Vai Trò Kỹ Thuật

Notebook `DS317_05` giải quyết bài toán làm giàu dữ liệu hàng hải bằng các yếu tố ngoại cảnh tự nhiên:
1. **Ghép nối không gian - thời gian (Spatio-Temporal Nearest Matching):** Sử dụng thuật toán cây KD-Tree trên tọa độ kinh vĩ độ và tìm mốc thời gian gần nhất (Nearest Timestamp trong phạm vi $\pm 1.0$ giờ) để ghép nối dữ liệu tàu AIS với dữ liệu lưới thời tiết NOAA RTMA (độ phân giải lưới $2.5 \times 2.5 \text{ km}$).
2. **Hệ 12 đặc trưng khí tượng chuẩn hóa:**
   - Vận tốc và hướng gió: Thành phần gió đông tây $u_{10}$, thành phần gió nam bắc $v_{10}$, tốc độ gió tổng hợp, góc lệch giữa hướng gió và hướng mũi tàu ($wind\_ship\_angle$).
   - Thành phần gió tác động: Vận tốc gió ngược chiều ($headwind$), vận tốc gió ngang thân tàu ($crosswind$).
   - Điều kiện môi trường biển: Nhiệt độ không khí bề mặt ($TMP_{2m}$), độ ẩm riêng ($SPFH_{2m}$), áp suất khí quyển bề mặt biển ($PRES_{sfc}$), tầm nhìn xa ($VIS_{sfc}$), độ cao mây trần ($HGT_{cld}$).
3. **Phục vụ Module M4 trong Runner 2:** Cung cấp tập đặc trưng thời tiết phục vụ thực nghiệm 32 biến thể trong `08_Runner_Song_Song_2_M4_M5_M6_M7/`.

---

## 2. Quản Trị Tệp Lớn và Lưu Trữ Đám Mây

> [!NOTE]
> - Tệp dữ liệu thời tiết sau ghép nối (`weather_rtma_2025_sidecar/` và `ais_rtma_matched_*.parquet`) có dung lượng từ 1.2 GB đến 3.8 GB, được bảo vệ bởi [`.gitignore`](../../.gitignore).
> - Tập dữ liệu hoàn chỉnh được lưu trữ trên **Kaggle Datasets** và thư mục Google Drive của Nhóm 03.
> - Bảng thống kê đặc trưng và schema 12 trường RTMA được tích hợp tại [`DS317_R11_Nhom03_HoSoNopDoAn/04_Data/README.md`](../../DS317_R11_Nhom03_HoSoNopDoAn/04_Data/README.md).

---

## 3. Phân Công Trách Nhiệm

- **Võ Đình Kiên:** Trực tiếp lập trình thuật toán ghép nối không gian KD-Tree và tối ưu hóa xử lý song song PyArrow trên Kaggle.
- **Lê Sỹ Liêm:** Kiểm tra độ hợp lệ của các giá trị vật lý khí tượng sau khi ghép nối.
