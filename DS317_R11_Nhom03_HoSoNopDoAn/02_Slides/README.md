# 02 - Slide Báo Cáo Bảo Vệ Đồ Án Cuối Kỳ (`02_Slides/`)

Thư mục này lưu trữ bộ Slide trình chiếu phục vụ buổi báo cáo và bảo vệ đồ án môn học **DS317 - Khai phá dữ liệu trong doanh nghiệp** của **Nhóm 03 (Lớp DS317.R11)**.

---

## 1. Quy Cách Bộ Slide Bảo Vệ

- **Thời lượng thuyết trình quy chuẩn:** 15 - 20 phút (kèm 5 - 10 phút trả lời câu hỏi phản biện của hội đồng giảng viên).
- **Định dạng bàn giao:**
  - `DS317_R11_Nhom03_Slides.pptx`: Bản trình chiếu gốc PowerPoint phục vụ hiệu ứng và trình bày.
  - `DS317_R11_Nhom03_Slides.pdf`: Bản xuất PDF cố định layout để nộp và lưu trữ.
- **Tiêu chuẩn thiết kế:** Tỷ lệ khung hình 16:9, màu sắc nhận diện thương hiệu hàng hải chuyên nghiệp, tích hợp biểu đồ chất lượng cao ($DPI \ge 300$) và ảnh chụp màn hình ứng dụng Demo thực tế.

---

## 2. Cấu Trúc 10 Phần Trình Bày Chuẩn Môn Học

| Phần | Nội dung trình bày trên Slide | Thời lượng dự kiến | Thành viên trình bày chính |
| :---: | :--- | :---: | :--- |
| **Phần 1** | **Giới thiệu Đề tài & Bối cảnh Nghiệp vụ:** Nỗi đau doanh nghiệp cảng biển (sai lệch ETA tự khai báo, chi phí lưu tàu $Demurrage$ 15,000 - 30,000 USD/ngày), mục tiêu giải pháp AI khách quan. | 1.5 phút | **Võ Đình Kiên** |
| **Phần 2** | **Khảo sát SOTA & Cơ sở Lý thuyết:** Đối chuẩn 6 bài báo quốc tế, lựa chọn mô hình GBDT, chuẩn DAMA/ISO 8000, lý thuyết Conformal Prediction và Asymmetric Loss. | 1.5 phút | **Nguyễn Hữu Bảo Lộc** |
| **Phần 3** | **Tài sản Dữ liệu & Kiểm toán 6 Chiều DAMA:** Minh chứng kiểm toán DAMA trên 256.94M dòng thô vs 92.68M dòng nền tảng, tương quan $r = +0.50971$, kiểm soát Data Drift 4 Quý. | 2.0 phút | **Quách Tuấn Kiệt** |
| **Phần 4** | **Kiến trúc Pipeline Tiền Xử Lý 2-Pass:** Quy trình xử lý dữ liệu lớn streaming PyArrow, khử trùng lặp 7 ngày, cơ chế Time-based Split ngăn chặn rò rỉ tương lai. | 1.5 phút | **Võ Đình Kiên** |
| **Phần 5** | **Thiết Kế Chuỗi Thực Nghiệm Ablation 7 Module (M1-M7):** Thiết kế bài bản chuỗi nghiên cứu thành phần từ lọc ngoại lai, điền khuyết đến tích hợp thời tiết RTMA và hàm mất mát bất đối xứng. | 2.0 phút | **Huỳnh Chí Kiên & Trần Hồng Lĩnh** |
| **Phần 6** | **Kết Quả Thực Nghiệm & Kiểm Định Thống Kê:** Kết quả Engine v2 (7 mô hình x 13 biến thể x 3 Fold); sự vượt trội của CatBoost ($MAE \approx 21.64h$ ở tầng $\le 168h$); kiểm định Wilcoxon/DM $p < 0.001$. | 2.5 phút | **Lê Sỹ Liêm** |
| **Phần 7** | **Giải Thích Mô Hình (SHAP) & Phân Tích Lỗi Case Study:** Biểu đồ SHAP Summary/Beeswarm diễn giải tầm quan trọng của `Dist_To_Berth_NM` và vận tốc; phân tích mẫu tàu thật có sai số lớn nhất. | 1.5 phút | **Huỳnh Chí Kiên & Trần Hồng Lĩnh** |
| **Phần 8** | **Tối Ưu Nghiệp Vụ Cảng Biển & Business ROI:** Hiệu quả giảm tỷ lệ trễ tàu từ Asymmetric Loss M6; độ tin cậy $PICP \ge 90\%$ từ Conformal M7; quy đổi tiết kiệm hàng chục nghìn USD/năm theo đơn giá ILWU. | 1.5 phút | **Trần Hồng Lĩnh & Lê Sỹ Liêm** |
| **Phần 9** | **Trực Quan Hóa Demo Web Streamlit & BI Dashboard:** Trình diễn trực tiếp luồng tác nghiệp trên ứng dụng Web: theo dõi CLDL DAMA, phân tích phân phối, suy luận ETA thời gian thực từ trọng số thật. | 2.0 phút | **Đỗ Văn Lộc** |
| **Phần 10** | **Kết Luận, Pháp Lý, Đạo Đức AI & Hướng Mở Rộng:** Tuân thủ Luật BV dữ liệu cá nhân 91/2025/QH15, khai báo sử dụng AI minh bạch, tóm tắt đóng góp đồ án. | 1.0 phút | **Nguyễn Hữu Bảo Lộc** |

---

## 3. Phân Công Trách Nhiệm

- **Đỗ Văn Lộc (Thư ký):** Chủ trì thiết kế bộ Slide tổng hợp, đồng bộ định dạng đồ họa và chuẩn bị video demo màn hình dự phòng.
- **Cả nhóm:** Cung cấp số liệu, biểu đồ thuộc phần phụ trách và tham gia luyện tập thuyết trình khớp mốc 15-20 phút.
