# Phân Hệ Notebook Tách Lẻ Từng Module (`03_Notebook_Tach_Le_Tung_Module/`)

Thư mục này chứa 8 Jupyter Notebook được phân rã độc lập theo từng module nghiên cứu thành phần (Ablation Study) từ **Baseline B0** đến **Module M7**. 

---

## 1. Mục Đích và Vai Trò Kỹ Thuật

Trong quá trình nghiên cứu khoa học và phát triển mô hình lớn, việc chạy toàn bộ 2 Runner song song (huấn luyện hàng trăm mô hình) đòi hỏi tài nguyên tính toán lớn và thời gian chạy kéo dài từ 4 đến 6 giờ. Phân hệ notebook tách lẻ được thiết kế nhằm đáp ứng 3 mục tiêu:
1. **Kiểm thử đơn vị độc lập (Unit Testing & Debugging):** Cho phép từng thành viên chạy thử nghiệm cô lập module mình phụ trách trên một tập dữ liệu con (sample) để tinh chỉnh mã nguồn và kiểm tra lỗi mà không tốn quota Kaggle.
2. **Đối chiếu kết quả thành phần:** Tạo điều kiện phân tích sâu từng biến thể cụ thể (ví dụ: so sánh riêng lẻ 4 phiên bản điền khuyết của M2 hoặc kiểm tra hành vi phạt lỗi của M6) phục vụ việc viết báo cáo chuyên đề.
3. **Tính mô-đun hóa cao:** Mã nguồn trong các notebook này hoàn toàn tương thích và là nền tảng để ghép nối thành các Runner song song lớn.

---

## 2. Danh Mục 8 Notebook Phân Rã Độc Lập

| STT | Tên Notebook | Module nghiên cứu | Nội dung kỹ thuật và thuật toán | Phân công phụ trách |
| :-: | :--- | :---: | :--- | :--- |
| 1 | `DS317_Thuc_Nghiem_00_Baseline.ipynb` | **Baseline B0** | Huấn luyện mô hình cơ sở Ridge Regression, Random Forest và GBDT trên tập thuộc tính gốc để làm mốc đối chứng tối thiểu ($MAE \approx 24.94h$ ở tầng $\le 168h$). | **Võ Đình Kiên & Trần Hồng Lĩnh** |
| 2 | `DS317_Thuc_Nghiem_M1_Loc_Ngoai_Lai.ipynb` | **Module M1** | Khảo sát thuật toán lọc ngoại lai theo quy tắc IQR truyền thống (M1-A) và IQR thích ứng theo phân loại tàu hàng hải (M1-B). | **Huỳnh Chí Kiên** |
| 3 | `DS317_Thuc_Nghiem_M2_Dien_Khuyet.ipynb` | **Module M2** | Đánh giá 4 chiến lược điền khuyết giá trị thiếu: M2-V1 (Group Median gốc), M2-V2 (Nội suy chuỗi thời gian tuyến tính), M2-V3 (Ước lượng hình học cự ly bến), M2-V4 (Kết hợp đa phương pháp). | **Đỗ Văn Lộc** |
| 4 | `DS317_Thuc_Nghiem_M3_Tao_Dac_Trung.ipynb` | **Module M3** | Đánh giá hiệu quả của 6 nhóm đặc trưng tương tác: G1 Động học ($sog \times \cos(heading)$), G2 Không gian bến, G3 Thân vỏ ($length \times width \times draft$), G4 Lịch sử hành trình, G5 Tương tác phi tuyến, G6 Kết hợp toàn bộ. | **Quách Tuấn Kiệt** |
| 5 | `DS317_Thuc_Nghiem_M4_Thoi_Tiet_RTMA.ipynb` | **Module M4** | Đánh giá tác động của 32 đặc trưng khí tượng NOAA RTMA 2025 (vận tốc gió ngược chiều, gió ngang, nhiệt độ mặt biển, áp suất khí quyển) đến độ chính xác ETA. | **Võ Đình Kiên** |
| 6 | `DS317_Thuc_Nghiem_M5_Chon_Loc_Dac_Trung.ipynb` | **Module M5** | Thử nghiệm các chiến lược lựa chọn đặc trưng: xếp hạng độ tương hỗ thông tin (Mutual Information top 16, top 12) kết hợp biến đổi hàm logarithm $log1p(x)$ cho các biến phân phối lệch. | **Nguyễn Hữu Bảo Lộc** |
| 7 | `DS317_Thuc_Nghiem_M6_Mat_Mat_Bat_Doi_Xung.ipynb` | **Module M6** | Thử nghiệm hàm mất mát bất đối xứng (Asymmetric Loss) phạt nặng trường hợp dự báo trễ tàu (Underprediction) so với dự báo sớm (Overprediction) với các hệ số $\alpha \in \{0.5, 1.0, 2.0\}$. | **Trần Hồng Lĩnh** |
| 8 | `DS317_Thuc_Nghiem_M7_Gom_Cum_Khoang_Sai_So.ipynb` | **Module M7** | Thiết lập khoảng tin cậy conformal không tham số (Conformal Prediction) và phân cụm sai số thích ứng (Adaptive Error Clustering) đảm bảo độ phủ $PICP \ge 90\%$. | **Lê Sỹ Liêm** |

---

## 3. Luồng Dữ Liệu và Quan Hệ với Output

```text
[02_Ma_Nguon_.../03_Notebook_Tach_Le_Tung_Module/]
        │
        ├── Từng notebook chạy độc lập trên tập mẫu hoặc dữ liệu trọn vẹn
        │
        ▼ (Xuất kết quả kiểm chứng thành phần)
[05_Output_Cac_Notebook/09_Notebook_Tach_Le_Tung_Module/]
        ├── 00_Baseline/
        ├── M1_Loc_Ngoai_Lai/
        ├── M2_Dien_Khuyet/
        ├── M3_Tao_Dac_Trung/
        ├── M4_Thoi_Tiet_RTMA/
        ├── M5_Chon_Loc_Dac_Trung/
        ├── M6_Mat_Mat_Bat_Doi_Xung/
        └── M7_Gom_Cum_Khoang_Sai_So/
```

- **Lưu ý:** Kết quả thực nghiệm chính thức dùng để viết Báo cáo tổng hợp cuối kỳ được trích xuất từ 2 Runner tập trung tại [`07_Runner_Song_Song_1_Baseline_M1_M2_M3/`](../../05_Output_Cac_Notebook/07_Runner_Song_Song_1_Baseline_M1_M2_M3/README.md) và [`08_Runner_Song_Song_2_M4_M5_M6_M7/`](../../05_Output_Cac_Notebook/08_Runner_Song_Song_2_M4_M5_M6_M7/README.md). Các notebook tách lẻ trong thư mục này phục vụ mục đích kiểm chứng cục bộ và nghiên cứu chuyên sâu từng phần.

---

## 4. Hướng Dẫn Sử Dụng

1. Mở notebook tương ứng với module bạn cần nghiên cứu bằng JupyterLab hoặc VS Code.
2. Để chạy thử nhanh (Fast Prototyping): Thiết lập biến cờ `SAMPLE_MODE = True` (hoặc `N_SAMPLE = 50_000`) ở cell đầu tiên để kiểm tra logic tính toán trong vòng dưới 2 phút.
3. Để chạy đầy đủ: Đẩy lên Kaggle Kernel và chuyển sang chạy với toàn bộ tập dữ liệu đã tiền xử lý.
