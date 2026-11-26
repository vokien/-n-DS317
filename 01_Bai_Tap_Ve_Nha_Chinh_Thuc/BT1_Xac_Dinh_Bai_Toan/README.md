# BÀI TẬP VỀ NHÀ 1: XÁC ĐỊNH BÀI TOÁN KHAI PHÁ DỮ LIỆU
**Môn học:** DS317 - Khai phá dữ liệu trong doanh nghiệp  
**Căn cứ:** Nội dung Chương 3 (Giai đoạn tiền đề) và Hướng dẫn viết Đề xuất đề tài  

---

## 1. Mục tiêu bài tập
Thực hiện trọn vẹn 4 bước tiền đề nhằm chuyển hóa nhu cầu nghiệp vụ thực tế của doanh nghiệp cảng biển thành bài toán khai phá dữ liệu khả thi và xác lập văn bản "Đề xuất đề tài" nộp cho giảng viên hướng dẫn.

## 2. Bốn bước thực hiện chi tiết

### Bước 1. Rà soát tài sản dữ liệu (Data Inventory)
- **Tài sản dữ liệu:** Dữ liệu tự động nhận dạng tàu biển NOAA AIS năm 2025 (Hoa Kỳ).
- **Quy chuẩn kiểm kê 7 tiêu chí theo DAMA:** Tên bảng/tập dữ liệu, nguồn thu thập (USCG/NOAA), quy mô vật lý (`13.15 GB` dữ liệu gốc `NOAA_AIS_2025_RAW/`, `320,776,922` dòng thô trước chia, `256,935,254` dòng sau chia ở `01_ban_tho_18_thuoc_tinh`, tiền xử lý còn `92,681,850` dòng sạch ở `02_ban_nen_tang_22_thuoc_tinh` / `03_ban_tien_xu_ly_27_thuoc_tinh`), định dạng lưu trữ (Parquet Snappy / CSV.zst), tần suất phát sinh (1-60 giây/bản tin), mức hạt dữ liệu (Data Grain: bản tin định vị thời gian thực theo từng tàu), và danh mục các trường thông tin chính (MMSI, kinh/vĩ độ, vận tốc sog, hướng cog, mớn nước draft, loại tàu vessel_type, khoảng cách bến, thời điểm cập bến ata_time).
- **Tài liệu chi tiết:** [`Bước 1 - Rà soát tài sản dữ liệu.xlsx`](B%C6%B0%E1%BB%9Bc%201%20-%20R%C3%A0%20so%C3%A1t%20t%C3%A0i%20s%E1%BA%A3n%20d%E1%BB%AF%20li%E1%BB%87u.xlsx)

### Bước 2. Xác định bối cảnh và nhu cầu của doanh nghiệp
- **Bối cảnh doanh nghiệp:** Trung tâm Điều độ và Khai thác Cầu bến cảng biển đối mặt với bài toán tối ưu hóa công suất khai thác luồng lạch và bến bãi. Hiện tượng thông báo giờ đến (ETA) tự khai báo của thuyền trưởng bị sai lệch lớn (sai số trung bình 12-24 giờ) dẫn đến việc cầu bến bị bỏ trống lãng phí hoặc tàu phải neo đậu chờ đợi gây tốn kém chi phí lưu bến (Demurrage cost từ 15,000 - 30,000 USD/ngày).
- **Nhu cầu cốt lõi:** Cần một hệ thống dự báo khách quan, độc lập, liên tục cập nhật giờ cập bến thực tế (Actual Time of Arrival - ATA) trước 24-72 giờ để chủ động lên lịch hoa tiêu, tàu lai dắt, cầu tàu và công nhân bốc dỡ.
- **Tài liệu chi tiết:** [`Bước 2 - Xác định bối cảnh và nhu cầu doanh nghiệp.docx`](B%C6%B0%E1%BB%9Bc%202%20-%20X%C3%A1c%20%C4%91%E1%BB%8Bnh%20b%E1%BB%91i%20c%E1%BA%A3nh%20v%C3%A0%20nhu%20c%E1%BA%A7u%20doanh%20nghi%E1%BB%87p.docx)

### Bước 3. Chuyển bài toán nghiệp vụ thành bài toán khai phá dữ liệu
- **Phát biểu bài toán:** Hồi quy chuỗi thời gian (Time-series Regression) dự báo biến mục tiêu liên tục `Target_Hours` (thời gian còn lại tính bằng giờ đến khi cập bến) từ chuỗi đặc trưng động học không - thời gian.
- **Đầu vào (Input):** 21-22 thuộc tính động học hành hải, vị trí không gian, cự ly hình học đến bến và đặc tính thân vỏ tàu.
- **Đầu ra (Output):** Biến thực $0 < \text{Target\_Hours} \le 168.0$ giờ, kèm khoảng an toàn 90% ($\pm \Delta t$) đóng vai trò biên độ đệm rủi ro cho kế hoạch điều độ.
- **Tài liệu chi tiết:** [`Bước 3 - Chuyển bài toán nghiệp vụ thành bài toán KPDL.docx`](B%C6%B0%E1%BB%9Bc%203%20-%20Chuy%E1%BB%83n%20b%C3%A0i%20to%C3%A1n%20nghi%E1%BB%87p%20v%E1%BB%A5%20th%C3%A0nh%20b%C3%A0i%20to%C3%A1n%20KPDL.docx)

### Bước 4. Thẩm định tính khả thi
- **Khả thi về dữ liệu:** Bộ dữ liệu bao phủ trọn vẹn 365 ngày của năm 2025 với `92,681,850` bản ghi sạch (`68,489,376` dòng Train + `24,192,474` dòng Eval `Q4`), phân bổ qua 4 quý trong năm.
- **Khả thi về kỹ thuật:** Các thuật toán GBDT (LightGBM, CatBoost, XGBoost) và Deep Learning (Bi-LSTM, TFT) hoàn toàn phù hợp để giải quyết dạng bài toán chuỗi thời gian tabular hàng hải.
- **Khả thi về tài nguyên:** Pipeline xử lý phân tán 2-Pass trên Kaggle hoàn thành huấn luyện trong 18-36 giây/lần chạy, đáp ứng hoàn hảo ràng buộc suy luận < 2.0 giây/chuyến tàu trên Web Demo.
- **Tài liệu chi tiết:** [`Bước 4 - Thẩm định tính khả thi.docx`](B%C6%B0%E1%BB%9Bc%204%20-%20Th%E1%BA%A9m%20%C4%91%E1%BB%8Bnh%20t%C3%ADnh%20kh%E1%BA%A3%20thi.docx)

---

## 3. Văn bản nghiệm thu tổng hợp
- **Bản đề xuất đề tài chính thức (chuẩn mẫu quy định `<MãLớp>_<TênNhóm>_DeXuat`):** [`DS317.R11_Nhom03_DeXuat.docx`](DS317.R11_Nhom03_DeXuat.docx) (Văn bản 4 trang tổng hợp đầy đủ 4 bước nộp cho GVHD).
