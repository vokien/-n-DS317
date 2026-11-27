# 07 - Chương Trình Demo & Video Minh Họa Dự Phòng (`07_Demo/`)

Thư mục này quản lý các sản phẩm phục vụ phần trình diễn trực tiếp (Live Demonstration) ứng dụng khai phá dữ liệu của **Nhóm 03 (Lớp DS317.R11)** cho đề tài **Dự báo Thời điểm Cập Cảng của Tàu Biển Thay Thế ETA Tự Khai Báo**.

---

## 1. Mục Tiêu và Tỷ Trọng Điểm của Phần Demo

> [!IMPORTANT]
> **Vai trò trong cơ cấu điểm A4:**
> - Chương trình Demo chiếm **50% điểm sản phẩm cuối kỳ (A4)** theo quy định của học phần DS317.
> - Yêu cầu bắt buộc: Phải kết nối trực tiếp với trọng số mô hình thật đã huấn luyện, tích hợp BI Dashboard tương tác giám sát CLDL DAMA 6 chiều, hỗ trợ người dùng nhập liệu/chọn tàu để suy luận thời gian thực và đưa ra khuyến nghị điều độ luồng lạch.

---

## 2. Cấu Trúc Các Sản Phẩm Bàn Giao

```text
07_Demo/
├── Kich_Ban_Demo_Va_Huong_Dan.md          <- Kịch bản thuyết trình demo & tài liệu hướng dẫn
├── DS317_R11_Nhom03_Demo_Video.mp4        <- Video quay màn hình dự phòng (thời lượng <= 3 phút)
├── screenshots/                           <- Bộ ảnh chụp các tab chức năng chính trên Demo
│   ├── tab1_bi_monitoring_dama.png
│   ├── tab2_distribution_eda.png
│   ├── tab3_realtime_eta_inference.png
│   └── tab4_berth_dispatch_recommendation.png
└── README.md
```

---

## 3. Kiến Trúc Ứng Dụng Web Demo Streamlit

Mã nguồn chính của ứng dụng được đặt tại [`DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/app.py`](../03_SourceCode/) (hoặc chạy trực tiếp từ thư mục này):
1. **Tab 1 - BI Monitoring & Giám sát CLDL DAMA 6 chiều:** Hiển thị scorecard 6 chiều chất lượng dữ liệu, biểu đồ radar đánh giá chất lượng trước vs sau tiền xử lý, bảng theo dõi Data Drift qua 4 Quý (Q1-Q4 năm 2025).
2. **Tab 2 - Phân tích Phân phối & Không gian Hàng hải (EDA):** Tích hợp biểu đồ tương quan Pearson $r = +0.50971$, bản đồ nhiệt luồng tàu cập bến tại các cụm cảng lớn của Hoa Kỳ, phân tích tương quan vận tốc và mớn nước.
3. **Tab 3 - Suy luận ETA Thời gian thực (Real-time Inference):**
   - Cho phép người dùng chọn chuyến tàu từ tập dữ liệu mẫu chuẩn (`04_Data/demo_sample_3000.csv`) hoặc tự điều chỉnh các tham số động học ($sog$, $heading$, $draft$, $dist\_to\_berth$).
   - Kết nối trực tiếp mô hình tốt nhất (CatBoost / XGBoost) để dự báo biến liên tục `Target_Hours`.
   - Hiển thị khoảng tin cậy an toàn $90\%$ Conformal Prediction ($\pm \Delta t$).
4. **Tab 4 - Hỗ trợ Quyết định Điều độ Cầu Bến (Decision Support):** So sánh giữa ETA tự khai báo của tàu và ETA dự báo bởi mô hình AI; cảnh báo nguy cơ trễ tàu, tính toán chi phí lưu bến tiềm ẩn ($Demurrage$) và khuyến nghị xếp lịch hoa tiêu, tàu lai dắt.

---

## 4. Hướng Dẫn Khởi Chạy Ứng Dụng Demo

### Bước 1: Chuẩn bị môi trường
Đảm bảo đã cài đặt các thư viện cần thiết từ `03_SourceCode/requirements.txt`:

```bash
pip install streamlit plotly pandas numpy joblib catboost
```

### Bước 2: Chạy ứng dụng Streamlit
Từ thư mục gốc dự án, thực thi lệnh:

```bash
streamlit run DS317_R11_Nhom03_HoSoNopDoAn/03_SourceCode/app.py
```

Ứng dụng sẽ tự động mở trên trình duyệt tại địa chỉ: `http://localhost:8501`. Thời gian nạp dữ liệu mẫu và mô hình được tối ưu hóa tải trong vòng dưới 2.0 giây.

---

## 5. Phân Công Trách Nhiệm

- **Đỗ Văn Lộc (Thư ký):** Lập trình toàn bộ ứng dụng `app.py`, thiết kế giao diện UI/UX tương tác, chuẩn bị kịch bản thuyết trình và quay video demo màn hình dự phòng ($\le 3$ phút).
- **Quách Tuấn Kiệt:** Cung cấp bộ dữ liệu mẫu nhẹ (`demo_sample_3000.*`) và số liệu DAMA tích hợp vào Tab 1.
- **Võ Đình Kiên:** Cung cấp mã nạp trọng số mô hình CatBoost và kiểm thử hiệu năng suy luận.
