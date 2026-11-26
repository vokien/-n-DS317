# KẾ HOẠCH VÀ PHÂN CÔNG NHIỆM VỤ HOÀN THÀNH THUYẾT MINH ĐỀ TÀI (LAB 3)

## HỌC PHẦN: DS317 - KHAI PHÁ DỮ LIỆU TRONG DOANH NGHIỆP (UIT)

---

### I. THÔNG TIN ĐĂNG KÝ ĐỀ TÀI CHÍNH THỨC CỦA NHÓM

* **1. Tên nhóm:** Nhóm 03 - Lớp DS317.P11 (DS317.R11)
* **2. Tên đề tài:** Dự báo thời điểm cập cảng của tàu biển thay thế ETA tự khai báo *(Prediction of Vessel Port Arrival Time Replacing Self-Reported ETA)*
* **3. Lĩnh vực ứng dụng:** Hàng hải - Logistics và Vận tải biển quốc tế
* **4. Tài sản dữ liệu:**
  - *Tên dataset:* NOAA AIS Vessel Dynamic & Static Data 2025
  - *Nguồn cung cấp:* Cục Quản lý Khí quyển và Đại dương Quốc gia Hoa Kỳ (NOAA - National Oceanic and Atmospheric Administration) phối hợp cùng Cục Quản lý Năng lượng Đại dương (BOEM) thông qua nền tảng Marine Cadastre.
  - *Link truy cập:* `https://noaaocm.blob.core.windows.net/ais/csv2/csv2025/index.html?utm_source=chatgpt.com`
* **5. Phân loại đồ án:** **NÂNG CAO**
  - *Hướng phát triển cải tiến:* **"Nghiên cứu cải tiến phương pháp ML/DL và triển khai thêm chức năng demo cho output bài toán"**.
  - *Yêu cầu nền tảng kế thừa (Cơ bản):* Giám sát dữ liệu input; đo lường và giám sát độ đo chất lượng dữ liệu; áp dụng phương pháp cải thiện chất lượng dữ liệu cơ bản (điền khuyết, làm giàu đặc trưng hình học thân vỏ); đối sánh các phương pháp SOTA trong tài liệu tham khảo.
  - *Yêu cầu đột phá (Nâng cao):* Cải tiến phương pháp ML/DL (tích hợp hàm mất mát Asymmetric Loss tùy biến vào thuật toán và mô hình chuỗi); xây dựng hoàn chỉnh ứng dụng Web Demo tương tác (Streamlit) cho output bài toán phục vụ Trung tâm Điều độ Cầu bến (Berth Planning Center).
* **Mã nguồn tiền xử lý nền tảng (Đã hoàn thành bởi Nhóm trưởng):**
  - `NOAA_AIS_Pipeline_FullYear_2025.ipynb` *(Master Pipeline Toàn Năm: Xử lý trọn vẹn 100% cả 365 ngày năm 2025 theo kiến trúc 2-Pass Rolling Stream, Self-Checkpoint Engine và cơ chế Hợp nhất dòng thời gian tuần tự. Tận dụng tối đa dataset phiên trước, triệt tiêu hiệu ứng biên và bảo toàn chuỗi thời gian, xuất tệp Parquet sạch duy nhất `noaa_ais_2025_full_year.parquet` làm đầu vào chuẩn cho toàn bộ nhóm).*
* **HẠN CHÓT HOÀN THÀNH DỨT ĐIỂM (FINAL DEADLINE):** **21:00 - Ngày 12/10/2026**

---

### II. BẢNG TỔNG HỢP MA TRẬN PHÂN CÔNG NHIỆM VỤ 7 THÀNH VIÊN

| STT | Thành viên & MSSV                                     | Nhiệm vụ chuyên trách chính                                                | Các Mini-task đảm nhiệm                                              | Sản phẩm bàn giao chính                                                                            | Tỷ lệ đóng góp |
| :-: | ------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | :-----------------: |
|  1  | **Võ Đình Kiên***(24520893 - Nhóm trưởng)* | Quản trị dự án, Phân tích rủi ro Big Data, Slides & Tổng duyệt hồ sơ | **MT 7.1, MT 7.2, MT 7.3***(Mục 12 trên Docs & Master Pipeline)* | Master Pipeline`NOAA_AIS_Pipeline_FullYear_2025.ipynb` + Slides + `ThuyetMinh.docx`/`.pdf` + ZIP |  **14.28%**  |
|  2  | **Đỗ Văn Lộc***(24520977 - Thư ký)*            | Bối cảnh nghiệp vụ, Mục tiêu SMART & Mockup Demo Output                   | **MT 4.1, MT 4.2***(Mục 1, Mục 2, Mục 9 trên Docs)*            | Bản vẽ Mockup giao diện Web Demo Berth Planning (Streamlit)                                         |  **14.28%**  |
|  3  | **Quách Tuấn Kiệt***(24520911 - Thành viên)*   | Giám sát dữ liệu input & Đo lường chất lượng dữ liệu 6 chiều       | **MT 1.1, MT 1.2, MT 1.3***(Mục 5 trên Docs)*                    | Tệp Excel`Lab3_DS317_Nhom03_DataInventory.xlsx` (3 sheet)                                           |  **14.28%**  |
|  4  | **Huỳnh Chí Kiên***(24520880 - Thành viên)*    | Cải thiện chất lượng dữ liệu & Trực quan hóa EDA                       | **MT 2.1, MT 2.2***(Mục 6 trên Docs)*                            | Bộ 4 biểu đồ EDA sắc nét (DPI$\ge 300$) thư mục `Hinh_Anh_Bieu_Do`                         |  **14.28%**  |
|  5  | **Nguyễn Hữu Bảo Lộc***(24520983 - Thành viên)*| Tổng quan công trình liên quan & Chuẩn hóa trích dẫn IEEE               | **MT 3.1, MT 3.2***(Mục 4, Mục 13 trên Docs)*                   | Bảng đối sánh 5 bài báo SOTA + tệp`references.bib`                                            |  **14.28%**  |
|  6  | **Lê Sỹ Liêm***(24520951 - Thành viên)*        | Phát biểu bài toán KPDL, Kịch bản đánh giá & Lập kế hoạch           | **MT 5.1, MT 5.2, MT 5.3***(Mục 3, Mục 8, Mục 10, Mục 11)*     | Tệp PDF`Lab3_DS317_Nhom03_PhanCong.pdf` (Kèm bảng tự đánh giá)                                |  **14.28%**  |
|  7  | **Trần Hồng Lĩnh***(24520970 - Thành viên)*    | Cải tiến phương pháp ML/DL, Huấn luyện Baseline & Đóng gói Code       | **MT 6.1, MT 6.2, MT 6.3***(Mục 7 trên Docs)*                    | Tệp Jupyter Notebook`Lab3_DS317_Nhom03_Code.ipynb` chạy trên Kaggle                               |  **14.28%**  |

---

### III. BẢN ĐẶC TẢ CHI TIẾT TỪNG MINI-TASK THEO TIÊU CHUẨN ĐỒ ÁN NÂNG CAO

#### 1. QUÁCH TUẤN KIỆT (MSSV: 24520911)

*(Chuyên trách: Giám sát dữ liệu input & Từ điển thuộc tính - Kế thừa Task 1A & 1B)*

##### [MT 1.1] Lập Bảng Kiểm kê Dữ liệu NOAA AIS 2025 theo 7 Tiêu chí Chuẩn

* **Hạn chót:** 21:00 - 05/10/2026
* **Mô tả chi tiết:**
  - Tổng hợp số liệu định lượng từ kết quả thực thi pipeline toàn năm `NOAA_AIS_Pipeline_FullYear_2025.ipynb` của Nhóm trưởng để hoàn thiện bảng kiểm kê 7 tiêu chí:
    1. *Nguồn gốc:* NOAA / BOEM thông qua nền tảng Marine Cadastre, thu thập qua mạng lưới trạm bờ VHF của USCG, giấy phép công cộng U.S. Public Domain.
    2. *Quy mô:* Trọn vẹn 365 ngày năm 2025 (toàn năm liên tục, dung lượng nén gốc `13.15 GB` trong `NOAA_AIS_2025_RAW/`: `31` tệp `.csv.zst`, `1` tệp `.zip`, `1` tệp `.tif`). Tự viết mã nạp tệp Parquet đầu ra để đo đạc và báo cáo chính xác tổng số bản ghi sạch sau lọc (`92,681,850` dòng trên `Base22`/`Prep27`), tổng số chuyến hành hải độc nhất (`trip_id`), số lượng tàu thương mại độc nhất (`mmsi`), và tỷ lệ cơ cấu giữa tàu hàng (Cargo) và tàu dầu (Tanker).
    3. *Cấu trúc:* Bảng dữ liệu chuỗi thời gian nén Snappy theo cấu trúc cột PyArrow; đơn vị phân tích: một quan trắc hành hải của tàu thương mại trước thời điểm cập bến.
    4. *Nhãn:* Mốc cập bến thực tế ATA (suy diễn từ danh bạ Pass 1 `ata_catalog.parquet` của pipeline) và biến mục tiêu liên tục `Target_Hours` trong khung cửa sổ 0 - 168 giờ.
    5. *Chất lượng:* Tự đo lường và lập bảng thống kê tỷ lệ khuyết thiếu (% missing) thực tế từ bản tin AIS gốc cho các trường kích thước thân vỏ (`length`, `width`, `draft`, `cargo`); kiểm tra tính toàn vẹn của các cột tọa độ, vận tốc và thời gian.
    6. *Thời gian:* Trải dài trọn vẹn 12 tháng năm 2025 (từ 01/01/2025 đến 31/12/2025).
    7. *Tính riêng tư:* Dữ liệu hoàn toàn ẩn danh thuyền viên, định danh bằng mã MMSI công khai của tàu hàng hải (No PII).
* **Đầu vào (Input):** Thống kê tổng kết Pass 1 và Pass 2 từ notebook master `NOAA_AIS_Pipeline_FullYear_2025.ipynb`.
* **Đầu ra (Output):** Bảng kiểm kê 7 tiêu chí chuẩn mực, số liệu thực tế 100%.
* **Ràng buộc & Lưu ý:**
  - Không tự phỏng đoán số dòng; mọi con số quy mô phải lấy chính xác từ log chạy thực tế của pipeline.

##### [MT 1.2] Xây dựng Từ điển 22 Cột & Bảng Đo lường Độ đo Chất lượng Dữ liệu Input

* **Hạn chót:** 21:00 - 06/10/2026
* **Mô tả chi tiết:**
  - Lập Từ điển dữ liệu (Data Dictionary) chi tiết cho toàn bộ 22 thuộc tính chuẩn đầu ra của pipeline (13 cột AIS cảm biến gốc, 5 cột hành trình/nhãn chuẩn: `trip_id`, `berth_lon`, `berth_lat`, `ata_time`, `Target_Hours` và 4 cột chế tác: `Dist_To_Berth_NM`, `Area_Proxy`, `Volume_Proxy`, `Is_Tanker`).
  - Mỗi thuộc tính nêu rõ: Tên cột, Kiểu dữ liệu, Ý nghĩa nghiệp vụ, Miền giá trị hợp lệ. Tự tính toán tỷ lệ khuyết thiếu (% missing) thực tế của từng cột từ tệp Parquet để điền vào bảng từ điển.
  - Tự lập bảng thống kê mô tả và các chỉ số phân vị (Min, Q1, Median, Mean, Q3, Max, Std) của biến mục tiêu `Target_Hours` (dải 0 - 168h) và tính hệ số tương quan Pearson giữa cự ly di chuyển và thời gian còn lại.
  - **Đáp ứng tiêu chuẩn đồ án:** Thiết lập bảng đo lường và giám sát độ đo chất lượng dữ liệu input theo 6 chiều: Đầy đủ (Completeness), Nhất quán (Consistency), Chính xác (Accuracy), Kịp thời (Timeliness), Hợp lệ (Validity), Duy nhất (Uniqueness).
  - Hoàn thiện tệp Excel `Lab3_DS317_Nhom03_DataInventory.xlsx` gồm 3 sheet chuyên nghiệp:
    * Sheet 1: `KiemKe_7TieuChi`
    * Sheet 2: `TuDien_22ThuocTinh`
    * Sheet 3: `DoDo_ChatLuong_6Chieu`
* **Đầu vào (Input):** Danh sách trường trong `final_cols` từ Cell 5 (PASS 2) của pipeline.
* **Đầu ra (Output):** Tệp Excel hoàn chỉnh `Lab3_DS317_Nhom03_DataInventory.xlsx`.
* **Ràng buộc & Lưu ý:**
  - Định dạng bảng Excel chỉn chu, có màu header, căn lề số liệu chuẩn xác.

##### [MT 1.3] Soạn thảo Mục 5 (Mô tả dữ liệu) trên Google Docs chung

* **Hạn chót:** 21:00 - 08/10/2026
* **Mô tả chi tiết:**
  - Trình bày toàn bộ nội dung **Mục 5 (Mô tả dữ liệu)** trực tiếp vào Docs chung.
  - Tóm lược bảng kiểm kê 7 tiêu chí, đưa bảng từ điển dữ liệu rút gọn (các biến cốt lõi), trình bày kết quả đo lường chất lượng dữ liệu 6 chiều.
  - Tiếp nhận 4 tệp hình ảnh biểu đồ EDA từ Huỳnh Chí Kiên (MT 2.1), chèn vào đúng vị trí và viết nhận xét phân tích chuyên môn cho từng hình.
* **Đầu vào (Input):** Kết quả từ MT 1.1, MT 1.2 và 4 hình ảnh biểu đồ EDA từ Huỳnh Chí Kiên.
* **Đầu ra (Output):** Nội dung hoàn chỉnh của Mục 5 trên Docs chung.
* **Ràng buộc & Lưu ý:**
  - Mọi con số trong Mục 5 trên Docs bắt buộc phải khớp 100% với file Excel `DataInventory.xlsx`.

---

#### 2. HUỲNH CHÍ KIÊN (MSSV: 24520880)

*(Chuyên trách: Cải thiện chất lượng dữ liệu & Trực quan hóa EDA - Kế thừa Task 1A & 1B)*

##### [MT 2.1] Trích xuất và Xuất Bản Bộ 4 Biểu đồ EDA Sắc nét từ Dữ liệu Pipeline

* **Hạn chót:** 21:00 - 05/10/2026
* **Mô tả chi tiết:**
  - Viết script Python (Seaborn/Matplotlib) chạy trên tập dữ liệu đã xuất từ notebook để tạo ra bộ 4 biểu đồ khảo sát khám phá dữ liệu (EDA) chuẩn mực:
    1. *Biểu đồ 1:* Phân phối xác suất (Histogram & KDE) của biến mục tiêu `Target_Hours` trên toàn dải liên tục, thể hiện rõ các mốc 24h, 48h, 72h.
    2. *Biểu đồ 2:* Biểu đồ tương quan phân tán (Scatter plot & Regression line) giữa khoảng cách tới bến `Dist_To_Berth_NM` và `Target_Hours` (kèm đường hồi quy và hệ số tương quan Pearson thực tế tính toán từ dữ liệu).
    3. *Biểu đồ 3:* Biểu đồ hộp (Boxplot) thể hiện phân bố vận tốc `sog` và mớn nước `draft` theo 2 nhóm tàu Cargo vs Tanker (`Is_Tanker`).
    4. *Biểu đồ 4:* Biểu đồ mật độ địa không gian (Geospatial Density Plot) thể hiện luồng vết hành trình tàu hội tụ về khu vực bến cảng.
  - Xuất ra 4 tệp ảnh PNG độ nét cao (DPI $\ge 300$) lưu vào thư mục `Hinh_Anh_Bieu_Do`.
* **Đầu vào (Input):** Tệp dữ liệu CSV/Parquet xuất ra từ pipeline của Nhóm trưởng.
* **Đầu ra (Output):** 4 tệp hình ảnh biểu đồ sắc nét và đoạn văn nhận xét quy luật rút ra từ biểu đồ chuyển cho Quách Tuấn Kiệt (MT 1.3).
* **Ràng buộc & Lưu ý:**
  - Tiêu đề trục, đơn vị đo (giờ, km, knots), nhãn ghi chú phải rõ ràng, kích thước chữ hài hòa, không bị tràn viền.

##### [MT 2.2] Lập luận Phương pháp Cải thiện Chất lượng Dữ liệu và Soạn Mục 6 trên Docs

* **Hạn chót:** 21:00 - 07/10/2026
* **Mô tả chi tiết:**
  - **Đáp ứng tiêu chuẩn đồ án:** Trình bày chi tiết các phương pháp cải thiện chất lượng dữ liệu đã thực hiện:
    * Phương pháp điền khuyết vật lý chuẩn hàng hải (Domain-based Imputation): Đề xuất và lập luận giải pháp điền kích thước danh định phân tầng theo nhóm tàu Cargo và Tanker cho các bản ghi bị khuyết kích thước thân vỏ, triệt tiêu kích thước và diện tích bằng 0 phi vật lý.
    * Phương pháp lọc nhiễu & phân tách hành hải: Lọc vận tốc phi thực tế (loại bỏ tàu đứng yên và mã lỗi cảm biến); loại bỏ trạng thái buộc bến status == 5.0 và vùng thả neo status == 1.0 để phân tách rõ ràng thời gian chờ bến (Waiting Time) và thời gian hành hải thực thụ (Steaming Time).
    * Bộ lọc triệt tiêu ô nhiễm bỏ sót bến (Anti-Skipped Port Call Poisoning Filter): Biện luận cơ chế lọc động học hàng hải dựa trên vận tốc suy diễn trung bình để tự động loại bỏ các hành trình bị gián đoạn do bỏ sót bến cập trung gian, bảo đảm tính thuần khiết của mẫu hành hải.
    * Phương pháp tăng cường và làm giàu dữ liệu (Feature Enrichment): Lập luận việc áp dụng công thức khoảng cách phỏng cầu elip WGS84 có chuẩn hóa xử lý kinh tuyến 180 độ vùng biển Alaska (`Dist_To_Berth_NM`), chế tác biến diện tích cản gió mặt nước $Area\_Proxy$ và thể tích tải trọng $Volume\_Proxy$.
    * Biến đổi dữ liệu tuần hoàn: Mã hóa góc hướng đi `COG` và hướng mũi la bàn `Heading` sang hệ trục trực giao $(\sin, \cos)$.
    * Cơ chế kỹ thuật xử lý dữ liệu lớn: Biện luận kiến trúc xử lý cuốn chiếu 2-Pass Rolling Stream, dọn dẹp đĩa lũy tiến và cơ chế hợp nhất dòng thời gian tuần tự bảo toàn tính liên tục của chuỗi thời gian cho các mô hình học sâu.
  - Soạn thảo toàn bộ nội dung **Mục 6 (Phương pháp tiền xử lý dữ liệu)** trên Docs chung.
* **Đầu vào (Input):** Mã nguồn xử lý trong notebook master `NOAA_AIS_Pipeline_FullYear_2025.ipynb`.
* **Đầu ra (Output):** Nội dung hoàn chỉnh của Mục 6 trên Docs chung.
* **Ràng buộc & Lưu ý:**
  - Phải nêu bật được tính khoa học của việc **không cắt cúp cửa sổ thời gian** ($0 < Target \le 168h$) để loại bỏ hoàn toàn Truncation Bias.

---

#### 3. NGUYỄN HỮU BẢO LỘC (MSSV: 24520983)

*(Chuyên trách: Tổng quan SOTA & Chuẩn hóa Trích dẫn IEEE - Kế thừa Task 2)*

##### [MT 3.1] Nghiên cứu và Tóm tắt Chuyên sâu 5 Công trình Học thuật SOTA Quốc tế

* **Hạn chót:** 21:00 - 04/10/2026
* **Mô tả chi tiết:**
  - Đọc và trích xuất thông tin chuyên môn từ 5 bài báo khoa học quốc tế SOTA uy tín trong thư mục `Bài báo/` (lưu trữ ngoài repo; xem bảng tổng hợp tại [TongQuan_RelatedWork_ETA_6BaiBao_v2.xlsx](TongQuan_RelatedWork_ETA_6BaiBao_v2.xlsx)):
    1. *El Mekkaoui et al. (2023, Springer FSMJ):* Deep learning cho cảng hàng rời Jorf Lasfar.
    2. *Abdi & Amrit (2024, Elsevier ESWA):* Fusion-based deep learning cho dự báo ETA.
    3. *Wang et al. (2025, Elsevier TR-C):* Stacked ensemble trên dữ liệu AIS hành trình.
    4. *Saber et al. (2025, Elsevier MTR):* Hybrid machine learning cho seaport ETA vùng Baltic.
    5. *Kim et al. (2017, JORS) hoặc Pani et al. (2015, EJTIR):* Phát hiện sớm độ trễ / Case-based reasoning.
  - Phân tích rành mạch từng bài theo 5 tiêu chí: (1) Phương pháp; (2) Dữ liệu sử dụng; (3) Kết quả định lượng; (4) Hạn chế thực tế; (5) Điểm đề tài có thể kế thừa.
* **Đầu vào (Input):** Các tệp PDF bài báo trong thư mục `Bài báo`.
* **Đầu ra (Output):** Bản phân tích tóm tắt 5 bài báo khoa học SOTA.
* **Ràng buộc & Lưu ý:**
  - Viết bằng văn phong học thuật tiếng Việt, không sao chép nguyên văn tóm tắt tiếng Anh (Abstract).

##### [MT 3.2] Xây dựng Bảng Đối sánh SOTA, Soạn Mục 4 và Mục 13 (chuẩn IEEE) trên Docs

* **Hạn chót:** 21:00 - 07/10/2026
* **Mô tả chi tiết:**
  - **Mục 4 (Tổng quan các công trình liên quan):** Lập bảng đối sánh 5 bài báo SOTA. Viết đoạn kết luận khẳng định rõ **Khoảng trống nghiên cứu (Research Gap)** và luận cứ cho **hướng đề tài Nâng cao**:
    * Các công trình trước chủ yếu thử nghiệm trên dữ liệu nhỏ, cục bộ hoặc dữ liệu đã được làm sạch nhân tạo.
    * Đề tài của nhóm khai thác bộ dữ liệu lớn NOAA AIS 2025 thực tế của toàn bộ bờ biển Hoa Kỳ, dự báo toàn dải thời gian liên tục và nghiên cứu cải tiến mô hình học máy với hàm tổn thất phạt chi phí bất đối xứng.
  - **Mục 13 (Tài liệu tham khảo):** Định dạng toàn bộ danh mục tài liệu tham khảo theo đúng chuẩn học thuật **IEEE** (đánh số theo thứ tự xuất hiện [1], [2], [3]...). Ghi đầy đủ tác giả, tên bài báo, tạp chí, tập, số, trang, năm và mã định danh DOI. Xuất kèm tệp `references.bib`.
* **Đầu vào (Input):** Kết quả phân tích từ MT 3.1.
* **Đầu ra (Output):** Nội dung hoàn chỉnh của Mục 4 và Mục 13 trên Docs chung + file `references.bib`.
* **Ràng buộc & Lưu ý:**
  - Mọi bài báo trong danh mục Mục 13 đều phải có liên kết trích dẫn (cite) cụ thể trong phần nội dung văn bản.

---

#### 4. ĐỖ VĂN LỘC (MSSV: 24520977)

*(Chuyên trách: Bối cảnh nghiệp vụ, Mục tiêu Nâng cao & Mockup Demo Output - Kế thừa Task 3)*

##### [MT 4.1] Soạn Mục 1 (Bối cảnh) & Mục 2 (Mục tiêu Đề tài Nâng cao) trên Docs chung

* **Hạn chót:** 21:00 - 08/10/2026
* **Mô tả chi tiết:**
  - **Mục 1 (Bối cảnh và lý do chọn đề tài):** Trình bày lĩnh vực logistics cảng biển quốc tế. Phân tích chi phí của việc làm sai: Tàu đến muộn gây lãng phí giờ cẩu bãi/công nhân 500-2.000 USD/giờ; tàu đến sớm không có bến phải neo chờ gây phí phạt lưu tàu (demurrage) 10.000-30.000 USD/ngày. Giải thích vì sao khai phá dữ liệu luồng NOAA AIS 2025 là giải pháp tối ưu.
  - Viết chuẩn Câu phát biểu nhu cầu nghiệp vụ đúng 1 câu theo khuôn: *"[Chủ thể] cần [biết/dự đoán điều gì] [trước bao lâu] để [hành động gì], nhằm [cải thiện KPI nào]"*.
  - **Mục 2 (Mục tiêu đề tài):** Viết chuẩn 01 câu mục tiêu tổng quát và 3-5 mục tiêu cụ thể đo lường được (SMART), thể hiện rõ tiêu chí **Đề tài Nâng cao**:
    1. Khai thác thành công bộ dữ liệu lớn NOAA AIS 2025 (toàn năm 365 ngày) giải quyết bài toán dự báo thời gian cập cảng ATA.
    2. Cải tiến phương pháp ML/DL bằng cách tích hợp hàm chi phí Asymmetric Loss, giảm sai số $MAE \ge 15\%$ so với baseline.
    3. Triển khai hoàn chỉnh ứng dụng Web Demo tương tác (Streamlit) phục vụ Trung tâm Điều độ Cầu bến.
* **Đầu vào (Input):** Bối cảnh dữ liệu NOAA AIS 2025 và thông tin đăng ký đề tài Nâng cao.
* **Đầu ra (Output):** Nội dung hoàn chỉnh của Mục 1 và Mục 2 trên Docs chung.
* **Ràng buộc & Lưu ý:**
  - Mục tiêu phải thể hiện tính đo lường được, gắn liền với sản phẩm bàn giao thực tế.

##### [MT 4.2] Thiết kế Mockup Giao diện Demo Output Bài toán và Soạn Mục 9 trên Docs

* **Hạn chót:** 21:00 - 08/10/2026
* **Mô tả chi tiết:**
  - **Đáp ứng yêu cầu trọng tâm của đề tài Nâng cao:** Triển khai thêm chức năng demo cho output bài toán (Web App tương tác bằng Streamlit):
    * *Chức năng Đầu vào:* Cho phép người điều độ cảng biển chọn mã tàu `mmsi` đang hành hải hoặc tải tệp bản tin AIS hành trình mới.
    * *Chức năng Xử lý:* Tự động gọi mô hình suy luận đã huấn luyện để dự báo số giờ di chuyển còn lại.
    * *Chức năng Output Bài toán:*
      - Hiển thị mốc giờ cập bến thực tế dự kiến (Predicted ATA).
      - Hiển thị Khoảng an toàn 90% (Safety Buffer $\pm \Delta t$) làm đệm điều độ cầu bến.
      - Bảng phân cấp rủi ro trễ và danh sách gợi ý phân bổ thứ tự bến cập theo chuẩn JIT.
  - Thiết kế sơ đồ kiến trúc triển khai ứng dụng trong môi trường doanh nghiệp cảng (Data Stream $\rightarrow$ Pipeline tiền xử lý $\rightarrow$ Serving Model $\rightarrow$ Dashboard).
  - Soạn thảo toàn bộ nội dung **Mục 9 (Sản phẩm dự kiến và phương án ứng dụng)** trên Docs chung.
* **Đầu vào (Input):** Yêu cầu nghiệp vụ bối cảnh Cảng biển và tiêu chí demo đồ án Nâng cao.
* **Đầu ra (Output):** Bản vẽ Mockup giao diện hệ thống và nội dung Mục 9 trên Docs chung.
* **Ràng buộc & Lưu ý:**
  - Mockup phải thể hiện được tính ứng dụng thực tiễn cho nhân viên điều độ cảng biển, không vẽ màn hình chung chung.

---

#### 5. LÊ SỸ LIÊM (MSSV: 24520951)

*(Chuyên trách: Bài toán KPDL, Kịch bản đánh giá & Kế hoạch tiến độ - Kế thừa Task 4)*

##### [MT 5.1] Soạn Mục 3 (Phát biểu bài toán khai phá dữ liệu) trên Docs chung

* **Hạn chót:** 21:00 - 08/10/2026
* **Mô tả chi tiết:**
  - Xây dựng Bảng phát biểu bài toán Hồi quy có giám sát (Regression) theo cấu trúc chuẩn môn học:
    * *Cho trước:* Hành trình quan trắc NOAA AIS 2025 của các chuyến tàu hàng/tàu dầu trong cự ly 168h trước khi cập bến.
    * *Cần tìm:* Số giờ di chuyển thực tế còn lại cho đến khi tàu cập bến chính thức (`Target_Hours`).
    * *Đầu vào:* Hệ 3 phiên bản dữ liệu **18 / 22 / 27 thuộc tính** (`SCHEMA_RAW_LABELED` 18 cột, `SCHEMA_BASE` 22 cột, `SCHEMA_PREPROCESSED` 27 cột) gồm đặc trưng động học (vị trí, cự ly `Dist_To_Berth_NM`, vận tốc `sog`, hướng `cog_sin`/`cos`), thông số tàu (`length`, `width`, `draft`, `Area_Proxy`, `Volume_Proxy`, `Is_Tanker`).
    * *Đầu ra:* Giá trị số thực liên tục (giờ) kèm khoảng an toàn 90% ($\pm \Delta t$).
    * *Ràng buộc:* Thời gian phản hồi dự báo $< 2$ giây/chuyến tàu; giải thích được mức độ quan trọng thuộc tính.
    * *Ngoài phạm vi:* Không điều động tránh va chạm luồng (COLREGs), không xếp dỡ container trong bãi cảng.
* **Đầu vào (Input):** Nhu cầu nghiệp vụ từ Đỗ Văn Lộc (MT 4.1) và cấu trúc 22 cột pipeline.
* **Đầu ra (Output):** Nội dung hoàn chỉnh của Mục 3 trên Docs chung.
* **Ràng buộc & Lưu ý:**
  - Mọi thuộc tính đầu vào bắt buộc phải tính được tại thời điểm quan sát để bảo đảm không rò rỉ dữ liệu.

##### [MT 5.2] Thiết kế Kịch bản Thực nghiệm, Hàm Chi phí Asymmetric Loss và Soạn Mục 8

* **Hạn chót:** 21:00 - 08/10/2026
* **Mô tả chi tiết:**
  - Thiết kế kịch bản thực nghiệm: Vẽ sơ đồ luồng chia dữ liệu Time-based split (Train 9 tháng đầu năm: 01/01 - 30/09/2025, Test 3 tháng cuối năm: 01/10 - 31/12/2025) từ bộ dữ liệu cả năm để đánh giá tính bền vững theo mùa vụ của mô hình.
  - Xây dựng Bảng độ đo kỹ thuật: Nêu công thức và lý do chọn $MAE$, $RMSE$, $R^2$.
  - Thiết kế Bảng độ đo giá trị nghiệp vụ (Trọng tâm Đề tài Nâng cao):
    * Định nghĩa hàm phạt chi phí dự báo sớm bất đối xứng (Asymmetric Loss): Phạt dự báo sớm gấp 2.5 lần dự báo trễ (do cảng bị lãng phí nhân công cẩu bãi chờ đợi).
    * Thiết lập Khoảng an toàn 90% (Safety Buffer): Xác định biên độ giờ đệm $\pm \Delta t$ để Trung tâm điều độ bến đưa vào lịch trình an toàn.
  - Xác lập **Ngưỡng chấp nhận (Acceptance Threshold)** của đề tài: $MAE \le 6.0$ giờ và vượt baseline ít nhất 15% tương đối.
  - Soạn thảo toàn bộ nội dung **Mục 8 (Kịch bản thực nghiệm và tiêu chí đánh giá)** trên Docs chung.
* **Đầu vào (Input):** Bảng số liệu baseline thực tế từ Trần Hồng Lĩnh (MT 6.2).
* **Đầu ra (Output):** Nội dung hoàn chỉnh của Mục 8 trên Docs chung.
* **Ràng buộc & Lưu ý:**
  - Công thức Asymmetric Loss phải được giải thích rõ ràng bằng ý nghĩa kinh tế thực tế của cảng biển.

##### [MT 5.3] Soạn Mục 10, Mục 11 trên Docs chung và Xuất File PhanCong.pdf Nộp bài

* **Hạn chót:** 12:00 (Trưa) - 12/10/2026
* **Mô tả chi tiết:**
  - **Mục 10 (Kế hoạch thực hiện theo tuần):** Lập bảng tiến độ 8 tuần triển khai Đồ án môn học bám sát lộ trình Đề tài Nâng cao (Tuần 1: Dữ liệu sạch $\rightarrow$ Tuần 2: EDA & Baseline $\rightarrow$ Tuần 3-4: Cải tiến ML/DL & Custom Loss $\rightarrow$ Tuần 5: Đánh giá Asymmetric Loss $\rightarrow$ Tuần 6: Xây dựng Streamlit Demo Output $\rightarrow$ Tuần 7: Báo cáo & Tổng duyệt $\rightarrow$ Tuần 8: Báo cáo trước lớp).
  - **Mục 11 (Phân công nhiệm vụ):** Đưa bảng ma trận phân công 7 thành viên (tương ứng Phần II tài liệu này) vào Docs.
  - Soạn thảo và xuất bản tệp `Lab3_DS317_Nhom03_PhanCong.pdf`: Bảng phân công và tự đánh giá đóng góp công việc nhóm (~14.28% cho mỗi người), đầy đủ chữ ký/xác nhận thành viên.
* **Đầu vào (Input):** Kế hoạch môn học và kết quả đóng góp của 7 thành viên.
* **Đầu ra (Output):** Nội dung Mục 10, Mục 11 trên Docs và file `Lab3_DS317_Nhom03_PhanCong.pdf`.
* **Ràng buộc & Lưu ý:**
  - Tỷ lệ đóng góp phải ghi nhận sự cân bằng công việc như cam kết.

---

#### 6. TRẦN HỒNG LĨNH (MSSV: 24520970)

*(Chuyên trách: Cải tiến phương pháp ML/DL, Baseline & Đóng gói Code - Kế thừa Task 5)*

##### [MT 6.1] Nghiên cứu Đề xuất Cải tiến Phương pháp ML/DL và Soạn Mục 7 trên Docs

* **Hạn chót:** 21:00 - 08/10/2026
* **Mô tả chi tiết:**
  - **Đáp ứng yêu cầu trọng tâm của Đồ án Nâng cao:** Nghiên cứu và đề xuất hướng **Cải tiến phương pháp ML/DL**:
    1. *Mô hình cơ sở (Baseline):* Ridge Regression (mô hình tuyến tính có hiệu chỉnh $L_2$).
    2. *Mô hình học máy tăng cường gradient:* LightGBM / CatBoost Regressor.
    3. *Mô hình học sâu chuỗi thời gian:* WaveNet / Bi-LSTM hoặc 1D-CNN.
    4. *ĐIỂM CẢI TIẾN NÂNG CAO ĐỀ XUẤT:* Thiết kế và cài đặt **Hàm mất mát tùy biến (Custom Asymmetric Objective Function)** trực tiếp vào thuật toán học máy (LightGBM/Mạng nơ-ron), giúp mô hình tự động tối ưu hóa theo độ đo chi phí nghiệp vụ bất đối xứng của cảng thay vì chỉ tối ưu sai số MSE đối xứng thông thường.
  - Với mỗi phương pháp, trình bày đủ: Ý tưởng cốt lõi, Ưu điểm, Nhược điểm, Độ phức tạp tính toán thuật toán ($O$), và Chiến lược tinh chỉnh siêu tham số (Optuna / RandomizedSearchCV).
  - Soạn thảo toàn bộ nội dung **Mục 7 (Phương pháp khai phá dữ liệu dự kiến)** trên Docs chung.
* **Đầu vào (Input):** Khung lý thuyết môn học và phương án bài toán từ Lê Sỹ Liêm (MT 5.1).
* **Đầu ra (Output):** Nội dung hoàn chỉnh của Mục 7 trên Docs chung.
* **Ràng buộc & Lưu ý:**
  - Phải lập luận rõ tính ưu việt của việc cải tiến hàm mục tiêu đối với bài toán thực tế của cảng biển.

##### [MT 6.2] Huấn luyện Mô hình Cơ sở (Ridge Regression Baseline) và Đo đạc Chỉ số

* **Hạn chót:** 21:00 - 05/10/2026
* **Mô tả chi tiết:**
  - Kế thừa tập dữ liệu sạch toàn năm 2025 từ notebook master `NOAA_AIS_Pipeline_FullYear_2025.ipynb` của Nhóm trưởng, thiết lập pipeline huấn luyện mô hình học máy trên Kaggle:
    * Chia tập dữ liệu có kiểm soát thời gian (Time-based split): Huấn luyện trên dữ liệu 9 tháng đầu năm (01/01 - 30/09/2025) và kiểm thử trên 3 tháng cuối năm (01/10 - 31/12/2025) (hoặc GroupKFold theo `mmsi` để chống rò rỉ vết tàu).
    * Huấn luyện mô hình ngây thơ Dummy Regressor (dự đoán bằng trung bình/trung vị) làm mốc cơ sở.
    * Huấn luyện mô hình Ridge Regression (chuẩn hóa `StandardScaler`, tối ưu hệ số phạt $\alpha$).
    * Đo đạc và xuất bảng chỉ số: Sai số tuyệt đối trung bình ($MAE$), Sai số căn bậc hai trung bình ($RMSE$), Hệ số xác định ($R^2$), và tính giá trị tổn thất hàm Asymmetric Loss.
    * Định lượng mức độ cải thiện: Chứng minh mô hình Ridge giảm bao nhiêu % sai số so với mô hình ngây thơ Dummy.
* **Đầu vào (Input):** Tệp dữ liệu Parquet đã xử lý từ notebook master `NOAA_AIS_Pipeline_FullYear_2025.ipynb` của Nhóm trưởng.
* **Đầu ra (Output):** Bảng số liệu kiểm chứng baseline định lượng chính xác chuyển cho Lê Sỹ Liêm (MT 5.2).
* **Ràng buộc & Lưu ý:**
  - Cố định hạt giống ngẫu nhiên (`random_state=42`) để đảm bảo kết quả tái lập được 100%.

##### [MT 6.3] Dọn dẹp, Chuẩn hóa và Đóng gói File Notebook Code.ipynb Nộp bài

* **Hạn chót:** 21:00 - 11/10/2026
* **Mô tả chi tiết:**
  - Dọn dẹp toàn bộ notebook thực nghiệm trên Kaggle: Gom luồng nạp dữ liệu từ pipeline, định nghĩa mô hình baseline, hàm tính Asymmetric Loss, và xuất bảng chỉ số độ đo.
  - Bổ sung markdown giải thích chi tiết cho từng cell, ghi chú rõ môi trường thực thi (Python version, các thư viện cần thiết).
  - Chạy lại từ đầu (Restart & Run All) để xác nhận notebook chạy thông suốt từ cell đầu đến cell cuối không có lỗi.
  - Tải về và lưu thành tệp `Lab3_DS317_Nhom03_Code.ipynb` đặt tại thư mục nộp bài.
* **Đầu vào (Input):** Mã nguồn thực nghiệm baseline từ MT 6.2.
* **Đầu ra (Output):** Tệp notebook `Lab3_DS317_Nhom03_Code.ipynb` sạch sẽ, chạy tái lập 100%.
* **Ràng buộc & Lưu ý:**
  - Mã nguồn không chứa đường dẫn tuyệt đối cục bộ; không để lộ thông tin nhạy cảm.

---

#### 7. VÕ ĐÌNH KIÊN (MSSV: 24520893 - NHÓM TRƯỞNG)

*(Chuyên trách: Quản trị Dự án, Phân tích Rủi ro, Thiết kế Slides & Tổng duyệt Hồ sơ)*

##### [MT 7.1] Phân tích Rủi ro Kỹ thuật Big Data và Soạn Mục 12 trên Docs chung

* **Hạn chót:** 21:00 - 08/10/2026
* **Mô tả chi tiết:**
  - Phân tích sâu sắc 3 rủi ro cốt lõi khi khai phá bộ dữ liệu lớn NOAA 2025:
    1. *Rủi ro 1: Kích thước dữ liệu lớn & Giới hạn tài nguyên hạ tầng đám mây (Thời gian session, Dung lượng đĩa làm việc, Giới hạn RAM).* Biện pháp: Đã giải quyết bằng kiến trúc Self-Checkpoint Engine, cơ chế dọn dẹp đĩa lũy tiến (Progressive Disk Cleanup) và chèn dữ liệu tuần tự theo row-group trong notebook master `NOAA_AIS_Pipeline_FullYear_2025.ipynb`, bảo đảm mức chiếm dụng đĩa và RAM luôn thấp hơn nhiều so với hạn mức cho phép.
    2. *Rủi ro 2: Tín hiệu AIS bị mất sóng hoặc trễ bản tin do thời tiết bão.* Biện pháp: Thuật toán nội suy tuyến tính quỹ đạo và tạo cờ cảnh báo bất thường.
    3. *Rủi ro 3: Trôi dạt khái niệm (Concept Drift) giữa các mùa vụ.* Biện pháp: Kiểm định chéo theo thời gian (Time-based split 9 tháng đầu năm vs 3 tháng cuối năm) và thiết lập cơ chế tái huấn luyện định kỳ.
  - Soạn thảo toàn bộ nội dung **Mục 12 (Rủi ro và phương án dự phòng)** trên Docs chung.
* **Đầu vào (Input):** Kinh nghiệm thực tế từ quá trình xây dựng notebook master `NOAA_AIS_Pipeline_FullYear_2025.ipynb`.
* **Đầu ra (Output):** Nội dung hoàn chỉnh của Mục 12 trên Docs chung.
* **Ràng buộc & Lưu ý:**
  - Mỗi rủi ro phải có đủ 3 thành phần: Mức độ ảnh hưởng, Xác suất xảy ra, và Giải pháp xử lý khả thi.

##### [MT 7.2] Thiết kế Toàn bộ Bộ Slides Thuyết trình Buổi 6 (`Slides.pptx` & `.pdf`)

* **Hạn chót:** 18:00 - 11/10/2026
* **Mô tả chi tiết:**
  - Thiết kế bộ Slides thuyết trình Buổi 6 gồm 10 đến 12 slides theo đúng khung mẫu hướng dẫn của môn học:
    * Slide 1: Trang bìa (Tên đề tài, Nhóm 03, Lớp, 7 thành viên, GVHD).
    * Slide 2-3: Bối cảnh nghiệp vụ Cảng biển và Nhu cầu dự báo ATA thay thế ETA tự khai báo.
    * Slide 4: Phát biểu bài toán Hồi quy và Mục tiêu Đồ án Nâng cao.
    * Slide 5-6: Dữ liệu lớn NOAA AIS 2025 và Master Pipeline xử lý cuốn chiếu toàn năm 365 ngày (2-Pass Rolling Stream) của nhóm.
    * Slide 7: Quy trình tiền xử lý và Chế tác đặc trưng thân vỏ.
    * Slide 8: Kiến trúc giải pháp và Đề xuất Cải tiến phương pháp ML/DL (Custom Asymmetric Loss).
    * Slide 9: Kết quả kiểm chứng Baseline thực tế (Ridge vs Dummy, MAE, Asymmetric Loss).
    * Slide 10: Chức năng Demo Output bài toán (Mockup Web Demo Berth Planning Streamlit).
    * Slide 11: Kế hoạch 8 tuần triển khai đồ án và Phân công nhiệm vụ 7 thành viên.
    * Slide 12: Lời cảm ơn và Sẵn sàng thảo luận/trả lời câu hỏi.
* **Đầu vào (Input):** Nội dung từ 13 mục trên Docs chung, biểu đồ EDA từ Huỳnh Chí Kiên và Mockup từ Đỗ Văn Lộc.
* **Đầu ra (Output):** Bộ tệp `Lab3_DS317_Nhom03_Slides.pptx` và `Lab3_DS317_Nhom03_Slides.pdf`.
* **Ràng buộc & Lưu ý:**
  - Slides tuyệt đối không chứa đoạn văn bản dài dòng. Tập trung vào sơ đồ kiến trúc, biểu đồ trực quan, bảng số liệu đối chuẩn và mockup giao diện.

##### [MT 7.3] Tổng duyệt Văn bản, Đối chuẩn Số liệu và Đóng gói Tệp ZIP Nộp bài Chính thức

* **Hạn chót:** 21:00 - 10/10/2026 (Xuất văn bản) & 21:00 - 12/10/2026 (Chốt nộp ZIP)
* **Mô tả chi tiết:**
  - Căn chỉnh định dạng chuẩn văn bản học thuật: Font Times New Roman, cỡ 13, giãn dòng 1.5, lề chuẩn. Kiểm soát độ dài nghiêm ngặt trong khoảng **5 đến 8 trang A4** (không tính phụ lục).
  - Xuất ra 2 tệp văn bản chính thức: `Lab3_DS317_Nhom03_ThuyetMinh.docx` và `Lab3_DS317_Nhom03_ThuyetMinh.pdf` vào ngày 10/10/2026.
  - Trưa ngày 12/10/2026: Chủ trì buổi kiểm tra chéo đối chuẩn số liệu 100%: Số liệu trên Docs = Excel = Code = Slides.
  - Chiều ngày 12/10/2026: Chủ trì tổng duyệt thuyết trình nội bộ (mỗi thành viên tập nói 1-2 phút).
  - Tối ngày 12/10/2026: Thu thập đủ 5 sản phẩm thành phần, đóng gói thành 1 tệp ZIP duy nhất theo cú pháp quy định: `Lab3_DS317_Nhom03.zip` và nộp lên hệ thống.
* **Đầu vào (Input):** Đủ 5 sản phẩm thành phần từ các thành viên.
* **Đầu ra (Output):** Tệp nén tổng `Lab3_DS317_Nhom03.zip` nộp bài chính thức.
* **Ràng buộc & Lưu ý:**
  - Kiểm tra kỹ dung lượng tệp và tính toàn vẹn của file ZIP trước khi bấm nộp bài.

---

### IV. LỊCH TRÌNH TIẾN ĐỘ THỜI GIAN THEO MỐC NGÀY (CHỐT 12/10/2026)

```
+------------+------------------------------------------------------------------------------------+--------------------------+
| Ngày       | Các Mini-task phải hoàn thành nghiệm thu trong ngày                                | Người phụ trách chính    |
+------------+------------------------------------------------------------------------------------+--------------------------+
| 02/10/2026 - 04/10/2026 | [ĐÃ XONG] Nhóm trưởng hoàn tất Master Pipeline Toàn Năm NOAA_AIS_Pipeline_FullYear_2025.ipynb trên Kaggle (Trọn vẹn 365 ngày, xuất tệp Parquet sạch duy nhất noaa_ais_2025_full_year.parquet) | Võ Đình Kiên |
| 04/10/2026 | [MT 3.1] Tóm tắt chuyên sâu 5 bài báo khoa học SOTA quốc tế                        | Nguyễn Hữu Bảo Lộc       |
| 05/10/2026 | [MT 6.2] Chạy xong Baseline Ridge Regression trên Kaggle, xuất chỉ số MAE          | Trần Hồng Lĩnh           |
|            | [MT 2.1] Xuất bộ 4 biểu đồ EDA chất lượng cao từ dữ liệu pipeline                  | Huỳnh Chí Kiên           |
|            | [MT 1.1] Hoàn thành bảng kiểm kê tài sản dữ liệu NOAA 7 tiêu chí                   | Quách Tuấn Kiệt          |
| 06/10/2026 | [MT 1.2] Xây dựng Từ điển 22 cột & Hoàn thiện DataInventory.xlsx (3 sheet)         | Quách Tuấn Kiệt          |
| 07/10/2026 | [MT 2.2] Soạn Mục 6 (Tiền xử lý, Rolling Stream, Haversine, Thân vỏ) trên Docs     | Huỳnh Chí Kiên           |
|            | [MT 3.2] Hoàn thành Bảng đối sánh SOTA, soạn Mục 4 & Mục 13 (IEEE) trên Docs       | Nguyễn Hữu Bảo Lộc       |
| 08/10/2026 | [MT 4.1] Soạn Mục 1 (Bối cảnh) & Mục 2 (Mục tiêu SMART Đề tài Nâng cao) trên Docs | Đỗ Văn Lộc               |
|            | [MT 4.2] Thiết kế Mockup Demo Output Berth Planning & Soạn Mục 9 trên Docs         | Đỗ Văn Lộc               |
|            | [MT 1.3] Đánh giá chất lượng 6 chiều & Soạn Mục 5 trên Docs                        | Quách Tuấn Kiệt          |
|            | [MT 5.1] Soạn Mục 3 (Phát biểu bài toán theo cấu trúc chuẩn) trên Docs             | Lê Sỹ Liêm               |
|            | [MT 5.2] Soạn Mục 8 (Kịch bản thực nghiệm & Asymmetric Loss) trên Docs             | Lê Sỹ Liêm               |
|            | [MT 6.1] Soạn Mục 7 (Cải tiến phương pháp ML/DL đề xuất) trên Docs                 | Trần Hồng Lĩnh           |
|            | [MT 7.1] Soạn Mục 12 (3 Rủi ro Big Data & Phương án dự phòng) trên Docs            | Võ Đình Kiên             |
| 09/10/2026 | [MT 5.3A] Soạn Mục 10 (Kế hoạch 8 tuần) & Mục 11 (Bảng phân công) trên Docs        | Lê Sỹ Liêm               |
|            | >>> ĐÓNG BĂNG DOCS CHUNG (FREEZE DOCS LÚC 18:00 ĐỂ TỔNG BIÊN TẬP) <<<             | Toàn nhóm                |
| 10/10/2026 | [MT 7.3A] Căn chỉnh 5-8 trang A4, xuất ThuyetMinh.docx & ThuyetMinh.pdf            | Võ Đình Kiên             |
| 11/10/2026 | [MT 7.2] Thiết kế hoàn chỉnh bộ Slides thuyết trình Buổi 6 (Slides.pptx & .pdf)    | Võ Đình Kiên             |
|            | [MT 6.3] Dọn dẹp markdown và đóng gói tệp Code.ipynb sạch sẽ                        | Trần Hồng Lĩnh           |
| 12/10/2026 | [MT 5.3B] Xuất file PhanCong.pdf (Bảng tự đánh giá đóng góp của nhóm)              | Lê Sỹ Liêm               |
| (Trưa 12h) | Kiểm tra chéo 100% số liệu giữa Docs - Excel - Code - Slides                       | Toàn nhóm                |
| (Chiều 18h)| Tổng duyệt thuyết trình nội bộ Buổi 6 (mỗi thành viên tập nói 1-2 phút)            | Toàn nhóm                |
| (Tối 21h)  | [MT 7.3B] NÉN TỆP ZIP TỔNG Lab3_DS317_Nhom03.zip NỘP BÀI CHÍNH THỨC (HOÀN TẤT)   | Võ Đình Kiên (Chốt nộp)   |
+------------+------------------------------------------------------------------------------------+--------------------------+
```

---

### V. QUY CHUẨN FORMAT VÀ HƯỚNG DẪN TRÌNH BÀY TRÊN GOOGLE DOCS CỦA NHÓM

Nhằm đảm bảo văn bản Thuyết minh đề tài đạt tính thẩm mỹ cao nhất, đồng nhất phong cách khoa học giữa 7 thành viên và phục vụ trực tiếp cho việc xuất bản tệp `Lab3_DS317_Nhom03_ThuyetMinh.docx` (khống chế độ dài chuẩn **5 đến 8 trang A4**), tất cả thành viên bắt buộc phải tuân thủ nghiêm ngặt các quy chuẩn định dạng dưới đây khi soạn thảo trên tệp Google Docs/Word Online dùng chung:

#### 1. Thiết lập Trang và Phân vùng Văn bản (Page Setup)

* **Khổ giấy:** Kích thước chuẩn **A4** ($210 \times 297$ mm).
* **Quy chuẩn Căn lề học thuật UIT:**
  - Lề trái (Left margin): **3.0 cm** (khoảng trống phục vụ đóng gáy hồ sơ).
  - Lề phải (Right margin): **2.0 cm**.
  - Lề trên (Top margin): **2.0 cm**.
  - Lề dưới (Bottom margin): **2.0 cm**.
* **Định hướng trang:** Toàn văn bản định hướng dọc (Portrait). Không tự ý đổi sang trang ngang (Landscape) trong nội dung chính 13 mục; các bảng quá rộng phải điều chỉnh co cột hoặc đưa xuống phần Phụ lục.
* **Đánh số trang:** Đánh số tự nhiên liên tục (1, 2, 3...) đặt ở góc dưới bên phải hoặc căn giữa phía chân trang (Footer). Không đánh số trang bìa.

#### 2. Quy chuẩn Kiểu chữ và Giãn dòng (Typography & Spacing)

* **Phông chữ (Font Family):** Sử dụng duy nhất phông chữ **Times New Roman** thống nhất cho 100% văn bản.
* **Cỡ chữ nội dung thường (Body Text):** Sử dụng cỡ chữ **12 pt** hoặc **13 pt** (khuyến nghị dùng cỡ 12 pt để nội dung cô đọng, dễ kiểm soát độ dài dưới 8 trang).
* **Màu chữ:** Màu đen tự động (`#000000`). Tuyệt đối không dùng chữ màu xám, xanh hay highlight màu trong văn bản báo cáo chính thức.
* **Căn lề đoạn văn (Alignment):** Bắt buộc căn đều hai bên (**Justified** - phím tắt `Ctrl + Shift + J` trên Docs / `Ctrl + J` trên Word).
* **Thụt đầu dòng (First Line Indent):** Thụt đầu dòng **1.0 cm** hoặc **1.27 cm** cho dòng đầu tiên của mỗi đoạn văn xuôi; hoặc thống nhất không thụt đầu dòng nếu khoảng cách giữa các đoạn được giãn cách rõ ràng.
* **Giãn dòng (Line Spacing):** Đặt ở mức **1.3 lines** đến **1.5 lines**. Tuyệt đối không để giãn dòng đôi (2.0) làm loãng trang hoặc giãn dòng đơn (1.0) gây dính chữ khó đọc.
* **Khoảng cách đoạn (Paragraph Spacing):**
  - Cách đoạn trước (Spacing Before): **0 pt**.
  - Cách đoạn sau (Spacing After): **3 pt** đến **6 pt**.
  - *Lưu ý:* Tuyệt đối không nhấn phím Enter 2 lần liên tục để tạo khoảng trắng giữa các đoạn văn.

#### 3. Cấu trúc Phân cấp Tiêu đề (Heading Hierarchy)

Giữ nguyên vẹn thứ tự và tên gọi của **13 mục chuẩn** theo quy định biểu mẫu Khoa, phân cấp tối đa 3 cấp:

* **Tiêu đề cấp 1 (Heading 1 - Các Mục lớn):**
  - Định dạng: Chữ in hoa, đậm, cỡ **13 pt - 14 pt** (ví dụ: **MỤC 1. BỐI CẢNH VÀ LÝ DO CHỌN ĐỀ TÀI**).
  - Khoảng cách: Before 12 pt, After 6 pt. Bắt buộc kích hoạt chế độ "Keep with next" để tiêu đề không bị rớt lẻ loi ở cuối trang.
* **Tiêu đề cấp 2 (Heading 2 - Các phân mục):**
  - Định dạng: Chữ in thường, đậm, cỡ **12 pt - 13 pt** (ví dụ: **1.1. Bối cảnh lĩnh vực logistics cảng biển và vận tải container**).
  - Khoảng cách: Before 6 pt, After 3 pt.
* **Tiêu đề cấp 3 (Heading 3 - Các tiểu mục chi tiết):**
  - Định dạng: Chữ in thường, đậm nghiêng, cỡ **12 pt - 13 pt** (ví dụ: *1.1.1. Thực trạng phụ thuộc vào giờ ETA tự khai báo của tàu*).
  - Khoảng cách: Before 3 pt, After 3 pt.

#### 4. Quy chuẩn Trình bày Bảng biểu (Tables)

* **Vị trí và định dạng Tiêu đề Bảng:**
  - Tiêu đề đặt ở **phía trên** bảng, căn trái hoặc căn giữa, in đậm:
    * Cú pháp: **Bảng X. Tên mô tả nội dung bảng** (ví dụ: **Bảng 1. Bảng kiểm kê 7 tiêu chí bộ dữ liệu NOAA AIS 2025 RAW**).
  - Số thứ tự bảng ($X$) đánh số liên tục từ Bảng 1 đến hết văn bản, hoặc đánh theo số mục (ví dụ: Bảng 5.1).
* **Định dạng Ô và Dữ liệu trong Bảng:**
  - Hàng tiêu đề cột (Header row): Nền màu xám nhạt (`#F2F2F2`) hoặc xanh nhạt (`#E8EEF5`), chữ in đậm, căn giữa theo cả chiều ngang và dọc. Kích hoạt tính năng "Lặp lại hàng tiêu đề ở đầu mỗi trang" (Repeat header row on every page).
  - Cỡ chữ trong bảng: Sử dụng cỡ **10 pt** đến **11 pt** (nhỏ hơn văn bản chính 1-2 pt để bảng gọn gàng, tiết kiệm diện tích), giãn dòng đơn (Single, 1.0 - 1.15).
  - Căn lề dữ liệu ô: Dữ liệu chuỗi ký tự căn lề trái; dữ liệu số, ngày tháng, phần trăm, kết luận căn lề giữa hoặc căn lề phải.
* **Nguồn và Ghi chú Bảng:**
  - Đặt ngay sát phía dưới bảng, in nghiêng, cỡ chữ **10 pt**:
    * Cú pháp: *Nguồn: Nhóm 03 tổng hợp từ kết quả thực thi Pipeline NOAA AIS 2025*.
* **Nguyên tắc ngắt trang:** Bảng ngắn không được ngắt đôi sang trang khác vô lý; bảng dài qua trang phải lặp lại header và không được ngắt ngang giữa chừng một dòng dữ liệu (Don't split row across pages).

#### 5. Quy chuẩn Trình bày Hình ảnh, Sơ đồ và Biểu đồ (Figures & Charts)

* **Yêu cầu Kỹ thuật Hình ảnh:**
  - Sử dụng hình ảnh gốc xuất từ code Python, lưu định dạng PNG độ phân giải cao ($\ge 300$ DPI), hình ảnh phải sắc nét, chữ trên hình không bị răng cưa hay vỡ hạt.
  - Kích thước ảnh: Căn chỉnh chiều rộng vừa vặn với trang giấy (thường từ $12$ cm đến $15$ cm), căn giữa trang (Center).
* **Vị trí và định dạng Tiêu đề Hình:**
  - Tiêu đề đặt ở **phía dưới** hình ảnh, căn giữa, in đậm hoặc in nghiêng:
    * Cú pháp: *Hình Y. Tên mô tả nội dung biểu đồ/sơ đồ* (ví dụ: *Hình 1. Phân phối xác suất biến mục tiêu Target_Hours trong dải liên tục 168 giờ*).
  - Số thứ tự hình ($Y$) đánh số liên tục từ Hình 1 đến hết tài liệu.
* **Nguồn và Ghi chú Hình:**
  - Đặt ngay dưới tên hình hoặc ghi chú trong ngoặc đơn: *Nguồn: Nhóm 03 trích xuất từ dữ liệu thực tế*.
* **Quy tắc viện dẫn bắt buộc:**
  - 100% hình ảnh và bảng biểu xuất hiện trong tài liệu bắt buộc phải được dẫn nhập, viện dẫn trong nội dung văn bản trước đó (ví dụ: *"Đặc tính phân phối của biến mục tiêu được thể hiện tại Hình 1..."* hoặc *"Số liệu kiểm chứng baseline được tổng hợp tại Bảng 3..."*). Tuyệt đối không thả hình/bảng nằm trơ trọi mà không có lời dẫn.

#### 6. Quy chuẩn Viết Công thức Toán học (Equations)

* Soạn thảo bằng công cụ Equation có sẵn của Google Docs (`Chèn -> Phương trình`) hoặc Word (`Insert -> Equation`). Tuyệt đối không chụp ảnh màn hình công thức từ tài liệu khác rồi dán vào.
* Biến số toán học in nghiêng (ví dụ: $x, y, ATA, Target\_Hours$), các hàm toán học, toán tử và từ viết tắt in đứng (ví dụ: $\sin, \cos, \ln, \min, \max, MAE, RMSE$).
* Đánh số công thức: Các công thức quan trọng được đánh số thứ tự trong ngoặc đơn, căn sát lề phải trang giấy: `(1)`, `(2)`...
* Giải thích ký hiệu: Ngay bên dưới công thức phải có phần giải thích tường minh:
  * Ví dụ:

    $$
    \text{Target\_Hours} = \frac{ATA - t_{obs}}{3600} \quad (1)
    $$

    *Trong đó: $ATA$ là mốc thời gian cập bến thực tế; $t_{obs}$ là thời điểm quan trắc bản tin AIS.*

#### 7. Quy chuẩn Trích dẫn Tài liệu Tham khảo (IEEE Citation Standards)

* Toàn văn bản áp dụng thống nhất chuẩn trích dẫn quốc tế **IEEE**:
  - Dẫn trích trong văn bản: Đặt số thứ tự trong ngoặc vuông ngay sau nhận định hoặc tác giả được trích dẫn. Ví dụ: *"Theo nghiên cứu của El Mekkaoui và cộng sự [1], các mô hình học sâu..."* hoặc *"Độ chính xác dự báo ETA đóng vai trò sống còn trong việc lập lịch cầu bến JIT [2], [4]..."*.
  - Thứ tự trích dẫn: Đánh số từ `[1]`, `[2]`, `[3]` theo đúng thứ tự lần đầu tiên xuất hiện trong văn bản Thuyết minh (từ trên xuống dưới).
  - Danh mục ở Mục 13: Trình bày chi tiết, chuẩn xác từng trường thông tin (Tên tác giả, Tên bài báo trong ngoặc kép, Tên tạp chí in nghiêng, Tập, Số, Trang, Năm, và đường dẫn DOI).

#### 8. Quy chuẩn Dấu câu, Đơn vị đo và Số liệu Khoa học

* **Dấu gạch ngang:** Luôn sử dụng dấu gạch ngang tiêu chuẩn "-" (hyphen-minus, mã ASCII 45) trong toàn bộ văn bản. Tuyệt đối không dùng dấu gạch ngang dài (en-dash hoặc em-dash).
* **Định dạng số thập phân:** Sử dụng dấu chấm `.` cho phần thập phân (ví dụ: $5.88$ giờ, $47.54$\%, $0.8625$) để đồng nhất với quy chuẩn hiển thị trong Python/Kaggle. Dùng dấu phẩy `,` hoặc khoảng trắng để phân cách hàng nghìn (ví dụ: $155,734$ bản ghi hoặc $155.734$ dòng).
* **Khoảng trắng đơn vị đo:** Luôn có khoảng trắng giữa con số và đơn vị đo lường (ví dụ: `24 giờ`, `100 km`, `14.5 knots`, `10.000 USD`, `30 phút`).
* **Thuật ngữ viết tắt:** Thuật ngữ viết tắt chuyên ngành khi xuất hiện lần đầu tiên phải viết đầy đủ tiếng Anh kèm từ viết tắt trong ngoặc đơn (ví dụ: *Estimated Time of Arrival (ETA)*, *Automatic Identification System (AIS)*, *Exploratory Data Analysis (EDA)*); từ lần xuất hiện thứ hai trở đi chỉ cần ghi từ viết tắt.

#### 9. Quy tắc Ứng xử Phối hợp Nhóm trên Google Docs (Collaborative Rules)

* **Độc lập và Đúng vị trí:** Mỗi thành viên chỉ thao tác nhập liệu trong đúng các Mục được phân công theo bảng phân công tại Phần II và III. Không gõ nội dung lan man sang phần của thành viên khác.
* **Tuyệt đối không sửa đè (No Direct Overwrite):**
  - Nếu phát hiện nội dung của bạn khác có sai sót hoặc muốn góp ý bổ sung: Chuyển sang chế độ **"Đề xuất" (Suggesting mode)** hoặc bôi đen văn bản và bấm **"Thêm nhận xét" (Add Comment)** để trao đổi.
  - Nghiêm cấm hành vi tự ý bôi đen và bấm phím xóa (Delete/Backspace) làm mất bài của thành viên khác.
* **Nguyên tắc "Một nguồn sự thật" (Single Source of Truth):**
  - Mọi số liệu thực nghiệm báo cáo trên Docs (tổng số dòng dữ liệu, số lượng tàu độc lập, độ lệch chuẩn, $MAE$, $RMSE$, phần trăm cải thiện...) BẮT BUỘC phải lấy từ kết quả thực tế xuất ra từ Notebook Kaggle của Trần Hồng Lĩnh và bảng của Quách Tuấn Kiệt.
  - Tuyệt đối không tự ý bịa đặt hoặc làm tròn sai lệch số liệu gây mâu thuẫn giữa Báo cáo, Slide và Code.
* **Mốc đóng băng văn bản (Docs Freeze):**
  - Đúng **18:00 - Ngày 09/10/2026**, toàn bộ quyền chỉnh sửa trực tiếp trên file Docs chung sẽ được khóa để chuyển sang chế độ chỉ xem.
  - Nhóm trưởng (Võ Đình Kiên) chịu trách nhiệm độc lập trong ngày 10/10/2026 để tổng duyệt, gọt giũa câu từ, căn chỉnh chuẩn lề trang và xuất bản tệp Thuyết minh chính thức dài từ 5 đến 8 trang A4.


---

## 📂 PHỤ LỤC: LỊCH SỬ PHÂN CÔNG VÀ THEO DÕI NỘI BỘ NHÓM QUA CÁC GIAI ĐOẠN

### 1. Kho lưu trữ Google Drive nhóm
* **Đường dẫn thư mục dùng chung:** [Google Drive Nhóm 03](https://drive.google.com/drive/folders/1BKo6dFzhz2POhghYX9noPKl1Q8UfB7WR?usp=sharing)
*(Lưu ý: Tệp nguồn định danh độc lập được duy trì tại `Quản lý nhóm/Nhom_3.txt`)*

### 2. Nhật ký theo dõi điểm danh và kỷ luật nội bộ
```text
Hồng Lĩnh: vô họp trễ 1 buổi
Bảo Lộc: vắng họp 1 buổi, trễ deadline viết đề xuất đề tài
Báo cáo thuyết minh ver1 đi trễ: bảo lộc, liêm, chí kiên, lĩnh
```

### 3. Phân công nhiệm vụ Bài tập Xác định bài toán
* Tất cả output upload lên (sau khi thực hiện xong thì thông báo vào nhóm)https://drive.google.com/drive/u/2/folders/1BKo6dFzhz2POhghYX9noPKl1Q8UfB7WR
* Nên đọc file DS317_Huong_dan_THUC_HANH.pdf trước khi làm 

1. Rà soát tài sản dữ liệu (Data Inventory) (3 người - mỗi người kiếm 1-2 dataset): 

- Nhiệm vụ thực hiện: tìm kiếm dataset phù hợp với bài toán hiện tại (ưu tiên các dataset được công bố kèm bài báo Q1/A* hoặc được công nhận rộng rãi) => lập bảng so sánh các thuộc tính (theo tiêu chí ở bước 1 trong file DS317_Huong_dan_THUC_HANH.pdf) => kiểm tra cấu trúc dữ liệu, đếm tỉ lệ missing, xem các thuộc tính có đầy đủ để phục vụ bài toán không (dùng python)

- Output: file "Rà soát tài sản dữ liệu (Data Inventory).xlsx" (chứa bảng so sánh theo các thuộc tính, kèm theo cấu trúc dữ liệu, tỉ lệ missing, các thuộc tính có đầy đủ để phục vụ bài toán không)

2. Xác định bối cảnh và nhu cầu của doanh nghiệp (1 người):

- Nhiệm vụ thực hiện: mô tả chi tiết Doanh nghiệp / lĩnh vực, chủ thể ra quyết định , quyêt định cần hỗ trợ, hiện trạng, chi phí của việc làm sai

- Output: file "Xác định bối cảnh và nhu cầu của doanh nghiệp.docs" (nội dung này dùng cho thuyết minh đề tài: Bối cảnh)

3. Chuyển bài toán nghiệp vụ thành bài toán khai phá dữ liệu và Thẩm định tính khả thi (2 người)

- Nhiệm vụ thực hiện: chuyển hóa bài toán (phát biểu theo cấu trúc: Cho trước – Cần tìm – Đầu vào – Đầu ra – Ràng buộc; xác định rõ là bài toán hồi quy hay phân loại); Thẩm định tính khả thi (đánh giá theo các tiêu chí trong file DS317_Huong_dan_THUC_HANH.pdf); chạy thử nghiệm dataset với các mô hình đơn giản (Linear Regression / Decision Tree / Random Forest) để kiểm chứng tính khả thi

- Output: "Phát biểu bài toán và thẩm định tính khả thi.docs" (nội dung này dùng cho thuyết minh đề tài: Phát biểu bài toán)

### 4. Phân công nhiệm vụ Rà soát dữ liệu (Data Inventory - EDA 4 Datasets)
```text
--------------------------------------------------------------------------------
TASK 1A & 1B: EDA 4 DATASETS (HOÀN THÀNH PHẦN 1 TRONG MẪU)
--------------------------------------------------------------------------------
- Phân bổ nhân sự: 02 người 
- Căn cứ biểu mẫu: Phần 1 (Rà soát tài sản dữ liệu - Mục 1.1, 1.2, 1.3 trong Mẫu đề xuất)
- Phụ thuộc: Độc lập - Bắt đầu ngay 24/09/2026.
- DEADLINE: 21:00 - Ngày 25/09/2026.
- Nhiệm vụ cụ thể:
  1. Viết script Python đếm `shape`, `dtypes`, tỷ lệ % missing, số bản ghi trùng lặp trên 4 datasets thực tế.
  2. Điền Mục 1.1 (Danh sách 4 nguồn dữ liệu: mô tả, đường dẫn, giấy phép, ngày truy cập, đơn vị quan sát).
  3. Điền Mục 1.2 (Bảng kiểm kê 7 tiêu chí: Nguồn gốc, Quy mô, Cấu trúc, Nhãn, Chất lượng, Thời gian, Tính riêng tư).
  4. Viết Mục 1.3 (Nhận định 3-5 ý nêu rõ dữ liệu cho phép/không cho phép làm gì và chốt 01 Dataset chính).
  5. Lập file Excel `Lab3_<MãLớp>_<TênNhóm>_DataInventory.xlsx` đính kèm.
- Sản phẩm bàn giao: File Excel DataInventory + Code EDA + Nội dung Phần 1 trong Mẫu.
- Lỗi thường gặp: Chép mô tả từ web/Kaggle thay vì tự chạy code đếm tệp thật; nhầm đơn vị quan sát; bỏ trống tiêu chí Nhãn.
- Lưu ý quan trọng: Mọi con số ở Phần 1 BẮT BUỘC phải trùng khớp 100% với output xuất ra từ notebook Python.

--------------------------------------------------------------------------------
TASK 2: HỌC THUẬT BASELINE (TẠO CƠ SỞ CHO PHẦN 2, 3, 4)
--------------------------------------------------------------------------------
- Phân bổ nhân sự: 01 người 
- Căn cứ biểu mẫu: Cung cấp mốc chỉ số so sánh & quy tắc gán nhãn học thuật cho Phần 2, 3, 4.
- Phụ thuộc: Độc lập - Bắt đầu ngay 24/09/2026.
- DEADLINE: 21:00 - Ngày 25/09/2026.
- Nhiệm vụ cụ thể:
  1. Đọc và tóm tắt 07 bài báo research/baseline hiện có của nhóm.
  2. Trích xuất mốc chỉ số so sánh baseline cho Hồi quy (MAE/RMSE) & Phân loại (F1/AUC-ROC).
  3. Trích xuất quy tắc gán nhãn mẫu mà các bài báo trước sử dụng làm tài liệu tham khảo cho Task 4 & Task 5.
- Sản phẩm bàn giao: Bảng tổng hợp tóm tắt 7 bài báo kèm mốc chỉ số baseline & quy tắc gán nhãn.
- Lỗi thường gặp: Đọc lướt không nắm được quy tắc gán nhãn hoặc mô hình baseline đơn giản.
- Lưu ý quan trọng: Tóm tắt tập trung vào mô hình cơ sở (baseline) đơn giản mà các nghiên cứu trước áp dụng.

--------------------------------------------------------------------------------
TASK 3: BỐI CẢNH NGHIỆP VỤ (HOÀN THÀNH PHẦN 2 TRONG MẪU)
--------------------------------------------------------------------------------
- Phân bổ nhân sự: 01 người 
- Căn cứ biểu mẫu: Phần 2 (Bối cảnh và nhu cầu của doanh nghiệp - Mục 2.1, 2.2 trong Mẫu đề xuất)
- Phụ thuộc: Phụ thuộc Task 1 (biết thuộc tính dataset chính) & Task 2 (bối cảnh từ 7 bài báo).
- DEADLINE: 12:00 (Trưa) - Ngày 27/09/2026.
- Nhiệm vụ cụ thể:
  1. Tận dụng kết quả Bước 2 đã có: Điền Mục 2.1 (6 yếu tố bối cảnh: Lĩnh vực, Chủ thể ra quyết định, Quyết định hỗ trợ, Hiện trạng, Chi phí làm sai, KPI).
  2. Viết Mục 2.2 (Câu phát biểu nhu cầu nghiệp vụ): Chuẩn 01 câu duy nhất theo khuôn mẫu môn học.
- Sản phẩm bàn giao: Nội dung hoàn chỉnh Phần 2 trong Mẫu đề xuất.
- Lỗi thường gặp: Dùng thuật ngữ kỹ thuật trong câu nhu cầu nghiệp vụ; chủ thể ra quyết định chung chung; bỏ qua mốc chi phí làm sai.
- Lưu ý quan trọng: Số liệu bối cảnh lấy từ thực tế hoặc nguồn trích dẫn rõ ràng, không tự đặt ra.

--------------------------------------------------------------------------------
TASK 4: PHÁT BIỂU BÀI TOÁN KHAI PHÁ DỮ LIỆU (HOÀN THÀNH PHẦN 3 TRONG MẪU)
--------------------------------------------------------------------------------
- Phân bổ nhân sự: 01 người 
- Căn cứ biểu mẫu: Phần 3 (Phát biểu bài toán khai phá dữ liệu - Bảng 3 phương án PA1, PA2, PA3 trong Mẫu đề xuất)
- Phụ thuộc: Phụ thuộc Task 1 (đặc trưng dữ liệu thực tế) & Task 3 (Câu nhu cầu nghiệp vụ ở Phần 2).
- DEADLINE: 21:00 - Ngày 27/09/2026.
- Nhiệm vụ cụ thể:
  1. Tận dụng kết quả Bước 3 đã có: Xây dựng Bảng so sánh 3 Phương án bài toán (PA1: Hồi quy, PA2: Phân loại nhị phân, PA3: Phân loại đa lớp).
  2. Điền đầy đủ 10 thuộc tính chuẩn cho từng phương án: Nhóm bài toán, Đơn vị phân tích, Cho trước, Cần tìm, Biến mục tiêu (quy tắc tính), Đầu vào, Đầu ra, Ràng buộc, Ngoài phạm vi, Mức đáp ứng câu nhu cầu.
- Sản phẩm bàn giao: Bảng so sánh 10 thuộc tính cho 3 Phương án bài toán ở Phần 3.
- Lỗi thường gặp: Biến mục tiêu mơ hồ không tính được trên dữ liệu; bỏ qua mốc thời gian cắt (cutting point) gây rò rỉ dữ liệu (Data Leakage); lẫn đơn vị phân tích.
- Lưu ý quan trọng: Mọi thuộc tính đầu vào BẮT BUỘC phải tính được tại thời điểm dự đoán (trước mốc cắt) để tránh Data Leakage.

--------------------------------------------------------------------------------
TASK 5: CODE BASELINE & THẨM ĐỊNH TÍNH KHẢ THI (HOÀN THÀNH PHẦN 4 & CODE NOTEBOOK)
--------------------------------------------------------------------------------
- Phân bổ nhân sự: 01 người 
- Căn cứ biểu mẫu: Phần 4 (Thẩm định tính khả thi - Mục 4.1, 4.2, 4.3) & Tệp Notebook đính kèm.
- Phụ thuộc: Phụ thuộc Task 1 (Dataset chính) & Task 4 (Quy tắc gán nhãn Biến mục tiêu của PA1 & PA2).
- DEADLINE: 21:00 - Ngày 28/09/2026.
- Nhiệm vụ cụ thể:
  1. Viết code Python gán nhãn/tạo biến mục tiêu cho PA1 & PA2 trên dữ liệu thật, đếm phân bố nhãn.
  2. Chia tập train/test (BẮT BUỘC Time-based split nếu dữ liệu có yếu tố thời gian).
  3. Fit thử mô hình Baseline đơn giản: Linear Regression (PA1) & Logistic Regression (PA2).
  4. Xuất các chỉ số độ đo sơ bộ (MAE, RMSE, Accuracy, F1, AUC-ROC) để điền vào Mục 4.1 (Kết quả kiểm chứng nhanh).
  5. Lập Mục 4.2 (Bảng tổng hợp thẩm định 4 nhóm kiểm tra: Dữ liệu, Kỹ thuật, Nguồn lực, Đạo đức/Pháp lý) cho cả 3 phương án.
  6. Viết Mục 4.3 (Phương án đề nghị): Đoạn văn 3-5 câu chốt PA chọn, lý do, rủi ro lớn nhất và phương án dự phòng.
  7. Đóng gói tệp notebook Jupyter `Lab3_<MãLớp>_<TênNhóm>_DeXuat_Code.ipynb` (gộp chung code EDA của Task 1).
- Sản phẩm bàn giao: Nội dung Phần 4 trong Mẫu đề xuất + Tệp Jupyter Notebook `.ipynb`.
- Lỗi thường gặp: Khẳng định "Đạt" thẩm định mà không kèm bằng chứng số liệu từ code; chia tập ngẫu nhiên cho dữ liệu thời gian; không chạy baseline.
- Lưu ý quan trọng: Kiểm chứng nhanh nhằm phát hiện sớm phương án không làm được, chưa đòi hỏi kết quả quá cao.
```

