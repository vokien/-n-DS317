# CHƯƠNG 3: DỮ LIỆU VÀ ĐO LƯỜNG CHẤT LƯỢNG DỮ LIỆU
## (DATA ASSETS & DAMA-DMBOK DATA QUALITY MEASUREMENT)

- **Học phần:** DS317 - Khai phá dữ liệu trong doanh nghiệp (UIT - ĐHQG-HCM)
- **Đề tài:** Dự báo thời điểm cập cảng của tàu biển thay thế ETA tự khai báo (*Prediction of Vessel Port Arrival Time Replacing Self-Reported ETA*)
- **Thành viên phụ trách:** **Quách Tuấn Kiệt** (MSSV: **24520911**) - Kỹ sư Dữ liệu & Quản trị Chất lượng DAMA
- **Nguồn số liệu thực chứng:** `05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/DAMA/`, `02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/`, và `Lab3_DS317.R11_Nhom03_DataInventory.xlsx`

---

## LỜI MỞ ĐẦU CHƯƠNG 3

Trong kỷ nguyên khai phá dữ liệu lớn và học máy doanh nghiệp, nguyên lý *"Garbage In, Garbage Out"* khẳng định rằng độ tin cậy và giá trị kinh tế của một hệ thống dự báo phụ thuộc mang tính quyết định vào chất lượng của dữ liệu đầu vào. Đối với bài toán dự báo thời gian đến cảng (Estimated Time of Arrival - ETA) của tàu biển thương mại, dữ liệu AIS (Automatic Identification System) thu nhận từ sóng vô tuyến VHF có đặc tính dòng dữ liệu thời gian thực (real-time stream) quy mô cực lớn nhưng đồng thời ẩn chứa rất nhiều dị thường, nhiễu cảm biến, xung đột trạm thu và khuyết thiếu thuộc tính.

Chương 3 này cung cấp một báo cáo toàn diện và kiểm toán thực chứng 100% về tài sản dữ liệu NOAA AIS năm 2025 của đề tài. Nội dung chương được chia thành 4 trọng tâm chính:
1. **Kiểm kê tài sản dữ liệu toàn diện** theo 7 tiêu chí chuẩn mực quốc tế của đề tài DS317.
2. **Từ điển và hồ sơ thống kê chi tiết** cho 3 phiên bản dữ liệu: 18 thuộc tính thô (`RAW18`), 22 thuộc tính nền tảng (`Base22`), và 27 thuộc tính tiền xử lý hoàn chỉnh (`PREP27`).
3. **Khung đo lường và đánh giá chất lượng dữ liệu 6 chiều** theo tiêu chuẩn quốc tế DAMA-DMBOK và ISO 8000 trên tổng thể 256,935,254 bản ghi thô.
4. **Phân tích hiện tượng trôi dạt dữ liệu (Data Drift)** qua 4 Quý của năm 2025, làm cơ sở khoa học để thiết kế các module lọc dữ liệu (M1), điền khuyết (M2) và tạo đặc trưng mới (M3) ở các chương tiếp theo.

---

## 3.1. TỔNG QUAN NGUỒN DỮ LIỆU VÀ KIỂM KÊ TÀI SẢN DỮ LIỆU THEO 7 TIÊU CHÍ CHUẨN

Tập dữ liệu nền tảng của đề tài được trích xuất từ Hệ thống Quản lý Duyên hải Hoa Kỳ (Marine Cadastre) do Cục Quản lý Khí quyển và Đại dương Quốc gia Hoa Kỳ (NOAA) phối hợp cùng Cục Quản lý Năng lượng Đại dương (BOEM) và Lực lượng Tuần duyên Hoa Kỳ (USCG) vận hành. Dữ liệu bao phủ toàn bộ 365 ngày của năm 2025 trong vùng biển và vùng đặc quyền kinh tế (EEZ) của Hoa Kỳ.

Dưới đây là Bảng kiểm kê tài sản dữ liệu theo 7 tiêu chí chuẩn mực, đối soát trực tiếp từ sổ kiểm kê `Lab3_DS317.R11_Nhom03_DataInventory.xlsx` và các báo cáo kiểm toán thực chứng:

### Bảng 3.1: Bảng kiểm kê tài sản dữ liệu NOAA AIS 2025 theo 7 tiêu chí chuẩn đồ án DS317

| STT | Tiêu chí chuẩn | Câu hỏi kiểm kê cốt lõi | Ngưỡng chuẩn đồ án | Kết quả thẩm định thực chứng (Audited Data) | Đánh giá |
| :---: | :--- | :--- | :--- | :--- | :---: |
| **1** | **Nguồn gốc**<br>*(Provenance)* | Dữ liệu được thu thập từ đâu? Cơ quan nào công bố? Có giấy phép sử dụng hợp pháp không? | Nguồn mở uy tín, công khai, có điều khoản cấp phép rõ ràng cho nghiên cứu học thuật. | • Cơ quan công bố: NOAA & BOEM.<br>• Nền tảng: Marine Cadastre AIS Portal.<br>• Thu thập: Mạng lưới trạm bờ VHF của Tuần duyên Hoa Kỳ (USCG).<br>• Giấy phép: U.S. Public Domain / Open Data Policy (được phép khai thác học thuật kèm trích dẫn). | **ĐẠT** |
| **2** | **Quy mô**<br>*(Volume / Scale)* | Số lượng bản ghi? Số lượng thuộc tính? Chu kỳ quan trắc và dung lượng lưu trữ? | Tối thiểu hàng chục triệu bản ghi cho bài toán chuỗi thời gian lớn. | • Chu kỳ quan trắc: Đủ 365/365 ngày năm 2025 (01/01/2025 - 31/12/2025).<br>• Tổng bản ghi thô ban đầu: **256,935,254 bản ghi** (từ 365 tệp nén `.csv.zst`, dung lượng thô ~450 GB).<br>• Bản ghi nền tảng sạch (`Base22`): **92,681,850 bản ghi**.<br>• Số chuyến hành hải độc nhất (`trip_id`): **88,146 chuyến**.<br>• Số tàu thương mại độc nhất (`mmsi`): **11,632 tàu** (Cargo: 68.07%, Tanker: 31.93%). | **ĐẠT XUẤT SẮC** |
| **3** | **Cấu trúc**<br>*(Structure)* | Dữ liệu có cấu trúc không? Định dạng lưu trữ là gì? Đơn vị phân tích (granularity) là gì? | Cấu trúc bảng rõ ràng, định dạng tối ưu cho tính toán phân tán (Parquet/Arrow). | • Dạng dữ liệu: Chuỗi thời gian địa không gian có cấu trúc cao (Spatio-Temporal Time Series).<br>• Đơn vị phân tích (Granularity): Một quan trắc hành hải (AIS record) của tàu thương mại tại mốc thời gian $t$ đang hành trình về bến đích ($0 < Target\_Hours \le 168$h).<br>• Định dạng lưu trữ: Apache Parquet nén Snappy (tối ưu hóa bộ nhớ với kiểu PyArrow). | **ĐẠT** |
| **4** | **Nhãn dữ liệu**<br>*(Ground Truth)* | Biến mục tiêu là gì? Thu thập từ đâu? Cơ chế gán nhãn có khách quan và chuẩn xác không? | Nhãn rõ ràng, cơ chế gán nhãn khách quan, không rò rỉ dữ liệu tương lai. | • Biến mục tiêu: $Target\_Hours = (ata\_time - base\_date\_time) / 3600$.<br>• Nhãn khách quan: Thời điểm cập bến thực tế ($ata\_time$) xác định qua thuật toán nhận diện tọa độ cầu bến (Spatial Berth Radius 500m & $sog < 1.0$ kn trong $\ge 2$ giờ).<br>• Tuyệt đối không dùng ETA tự khai báo của thuyền viên. | **ĐẠT XUẤT SẮC** |
| **5** | **Mức hạt dữ liệu**<br>*(Granularity)* | Mức độ chi tiết của dữ liệu? Tần suất lấy mẫu thời gian và không gian? | Phù hợp bài toán hồi quy chuỗi thời gian liên tục. | • Tần suất phát sóng AIS động học: 2 - 10 giây/bản ghi khi tàu hành trình; giảm xuống khi neo đậu.<br>• Tần suất lấy mẫu phân tích: Dòng dữ liệu được phân chia theo từng chuyến đi độc nhất (`trip_id`), đảm bảo chuỗi thời gian liên tục từ lúc rời bến xuất phát đến khi cập bến đích. | **ĐẠT** |
| **6** | **Chất lượng vệ sinh**<br>*(Cleanliness)* | Dữ liệu có được kiểm tra, làm sạch các dị thường và loại bỏ nhiễu không? | Quy trình tiền xử lý rõ ràng, bảo vệ tính toàn vẹn vật lý của chuyển động tàu. | • Loại bỏ các bản ghi ngoài hải phận Hoa Kỳ hoặc tọa độ không hợp lệ.<br>• Lọc bỏ nhiễu tàu neo đậu kéo dài ($sog < 1.0$ kn hoặc $status \in \{1, 5\}$).<br>• Kiểm soát chặt chẽ ranh giới chuyến đi để triệt tiêu hiện tượng rò rỉ dữ liệu (Zero Data Leakage). | **ĐẠT** |
| **7** | **Pháp lý & Đạo đức**<br>*(Privacy / Ethics)* | Dữ liệu có vi phạm quyền riêng tư, an ninh hàng hải hoặc quy định bảo vệ dữ liệu không? | Tuân thủ pháp luật, bảo vệ bí mật kinh doanh và an toàn hàng hải. | • Dữ liệu AIS là thông tin quảng bá vô tuyến công khai theo công ước SOLAS của Tổ chức Hàng hải Quốc tế (IMO).<br>• Đề tài áp dụng cơ chế băm ẩn danh mã nhận dạng tàu (`MMSI` $\to$ `Vessel_Hash_ID`), tuân thủ Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 và Luật Dữ liệu số 60/2024/QH15. | **ĐẠT** |

---

## 3.2. TỪ ĐIỂN DỮ LIỆU CHUẨN HÓA (DATA DICTIONARY)

Để đảm bảo tính nhất quán xuyên suốt các giai đoạn tiền xử lý, chế tác đặc trưng và huấn luyện mô hình, nhóm nghiên cứu thiết lập từ điển dữ liệu chuẩn hóa qua 3 cấp độ:
- **Cấp độ 1 (`RAW18`):** 18 thuộc tính thô nguyên bản từ các tệp giải nén NOAA AIS.
- **Cấp độ 2 (`Base22`):** 22 thuộc tính nền tảng sau khi trích xuất chuyến đi, tọa độ cầu bến và biến mục tiêu $Target\_Hours$.
- **Cấp độ 3 (`PREP27`):** 27 thuộc tính tiền xử lý hoàn chỉnh (bổ sung biến lượng giác sin/cos, cờ điền khuyết và proxy diện tích/thể tích thân vỏ).

### 3.2.1. Từ điển 18 thuộc tính thô nguyên bản (`RAW18`)
Tập dữ liệu thô gồm **256,935,254 bản ghi** với 18 thuộc tính đo lường trực tiếp từ cảm biến AIS và điện tín hàng hải:

### Bảng 3.2: Từ điển và thống kê mô tả 18 thuộc tính thô nguyên bản (RAW18)

| STT | Tên thuộc tính | Phân loại | Kiểu dữ liệu | Số bản ghi hợp lệ | Số bản ghi khuyết | Tỷ lệ khuyết (%) | Dải giá trị (Min - Max) | Ý nghĩa nghiệp vụ hàng hải |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| 1 | `mmsi` | Định danh | `int64` | 256,935,254 | 0 | 0.00% | 205097000 - 775345000 | Mã nhận dạng dịch vụ lưu động hàng hải (9 chữ số) theo chuẩn ITU-R M.585. |
| 2 | `base_date_time` | Thời gian | `timestamp` | 256,935,254 | 0 | 0.00% | 2025-01-01 - 2025-12-31 | Mốc thời gian phát tín hiệu AIS (chuẩn UTC). |
| 3 | `latitude` | Tọa độ | `float32` | 256,935,254 | 0 | 0.00% | -25.28° đến 84.31° | Vĩ độ địa lý trắc địa WGS84. |
| 4 | `longitude` | Tọa độ | `float32` | 256,935,254 | 0 | 0.00% | -179.74° đến 179.77° | Kinh độ địa lý trắc địa WGS84. |
| 5 | `sog` | Động học | `float32` | 256,800,910 | 134,344 | 0.0523% | 0.0 - 99.9 knot | Vận tốc di chuyển trên mặt đất (Speed Over Ground). |
| 6 | `cog` | Động học | `float32` | 255,452,073 | 1,483,181 | 0.5773% | 0.0° - 359.9° | Hướng di chuyển thực tế trên mặt đất (Course Over Ground). |
| 7 | `heading` | Động học | `float32` | 248,801,537 | 8,133,717 | 3.1657% | 0.0° - 359.0° | Hướng la bàn con quay của mũi tàu (True Heading). Giá trị 511 biểu thị lỗi. |
| 8 | `status` | Vận hành | `float32` | 256,534,623 | 400,631 | 0.1559% | 0 - 15 | Trạng thái hành hải theo chuẩn AIS (0: Đang chạy máy, 1: Neo, 5: Buộc bến). |
| 9 | `vessel_type` | Thân vỏ | `float32` | 256,934,884 | 370 | 0.0001% | 70 - 89 | Phân loại tàu thương mại theo IMO (70-79: Tàu chở hàng Cargo, 80-89: Tàu chở dầu Tanker). |
| 10 | `length` | Kích thước | `float32` | 255,900,447 | 1,034,807 | 0.4028% | 1.0 - 419.0 m | Chiều dài tổng thể của con tàu (Length Overall - LOA). |
| 11 | `width` | Kích thước | `float32` | 254,196,321 | 2,738,933 | 1.0660% | 2.0 - 61.0 m | Chiều rộng lớn nhất của thân tàu (Beam). |
| 12 | `draft` | Kích thước | `float32` | 251,531,128 | 5,404,126 | 2.1033% | 0.1 - 25.5 m | Mớn nước tác nghiệp thực tế của con tàu. |
| 13 | `cargo` | Hàng hóa | `float32` | 255,301,230 | 1,634,024 | 0.6360% | 1 - 207 | Mã phân loại chi tiết chủng loại hàng hóa vận chuyển. |
| 14 | `trip_id` | Chuyến đi | `string` | 256,935,254 | 0 | 0.00% | 88,146 mã độc nhất | Mã định danh chuyến hành hải độc nhất ghép nối theo thời gian. |
| 15 | `berth_lon` | Cầu cảng | `float32` | 256,935,254 | 0 | 0.00% | -166.54° đến -65.84° | Kinh độ của cầu bến đích cập cảng. |
| 16 | `berth_lat` | Cầu cảng | `float32` | 256,935,254 | 0 | 0.00% | 15.84° đến 53.58° | Vĩ độ của cầu bến đích cập cảng. |
| 17 | `ata_time` | Mốc đích | `timestamp` | 256,935,254 | 0 | 0.00% | 2025-01-01 - 2025-12-31 | Thời điểm tàu thực sự cập bến đích (Actual Time of Arrival). |
| 18 | `Target_Hours` | Mục tiêu | `float32` | 256,935,254 | 0 | 0.00% | 0.0003 - 2124.64 h | Số giờ còn lại cho đến khi tàu cập bến đích (Ground Truth Label). |

---

### 3.2.2. Từ điển 22 thuộc tính nền tảng (`Base22`)
Sau khi lọc dữ liệu hành hải sạch và bổ sung các thuộc tính dẫn xuất hình học trắc địa và thân vỏ, tập dữ liệu đạt quy mô **92,681,850 bản ghi** (`Base22`):

### Bảng 3.3: Hồ sơ thống kê 22 thuộc tính nền tảng (Base22 - 92,681,850 bản ghi)

| STT | Tên thuộc tính | Kiểu dữ liệu | Số bản ghi hợp lệ | Tỷ lệ khuyết (%) | Mean | Std | Min | Median (Q2) | Max |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | `mmsi` | `int64` | 92,681,850 | 0.00% | 4.19 × 10⁸ | 1.37 × 10⁸ | 205,097,000 | 367,775,000 | 720,233,000 |
| 2 | `longitude` | `float32` | 92,681,850 | 0.00% | -92.88° | 19.66° | -166.64° | -85.00° | -65.00° |
| 3 | `latitude` | `float32` | 92,681,850 | 0.00% | 33.65° | 7.57° | 15.00° | 33.55° | 53.58° |
| 4 | `sog` | `float32` | 92,681,850 | 0.00% | 11.36 kn | 3.97 kn | 1.00 kn | 11.70 kn | 39.90 kn |
| 5 | `cog` | `float32` | 92,681,850 | 0.00% | 195.01° | 106.32° | 0.00° | 211.90° | 359.90° |
| 6 | `heading` | `float32` | 92,681,850 | 0.00% | 192.27° | 107.20° | 0.00° | 208.00° | 359.00° |
| 7 | `status` | `float32` | 92,681,850 | 0.00% | 0.065 | 0.739 | 0.00 | 0.00 | 13.00 |
| 8 | `vessel_type` | `float32` | 92,681,850 | 0.00% | 74.47 | 5.37 | 70.00 | 70.00 | 89.00 |
| 9 | `length` | `float32` | 92,681,850 | 0.00% | 213.49 m | 67.05 m | 5.00 m | 200.00 m | 400.00 m |
| 10 | `width` | `float32` | 92,681,850 | 0.00% | 32.34 m | 8.92 m | 3.00 m | 32.00 m | 61.00 m |
| 11 | `draft` | `float32` | 92,681,850 | 0.00% | 9.02 m | 2.50 m | 0.10 m | 8.90 m | 22.20 m |
| 12 | `cargo` | `float32` | 92,217,643 | 0.5009% | 74.44 | 6.13 | 1.00 | 70.00 | 207.00 |
| 13 | `berth_lon` | `float32` | 92,681,850 | 0.00% | -93.80° | 17.97° | -159.36° | -88.00° | -65.84° |
| 14 | `berth_lat` | `float32` | 92,681,850 | 0.00% | 34.93° | 7.28° | 15.84° | 34.13° | 49.69° |
| 15 | `Dist_To_Berth_NM` | `float32` | 92,681,850 | 0.00% | 336.94 NM | 412.14 NM | 0.00 NM | 185.42 NM | 2,299.99 NM |
| 16 | `Area_Proxy` | `float32` | 92,681,850 | 0.00% | 7,417.85 m² | 4,100.15 m² | 36.00 m² | 6,400.00 m² | 24,400.00 m² |
| 17 | `Volume_Proxy` | `float32` | 92,681,850 | 0.00% | 74,258.13 m³ | 56,868.29 m³ | 57.60 m³ | 57,600.00 m³ | 437,562.00 m³ |
| 18 | `Is_Tanker` | `int8` | 92,681,850 | 0.00% | 0.3251 | 0.4684 | 0 | 0 | 1 |
| 19 | `Target_Hours` | `float32` | 92,681,850 | 0.00% | 92.67 h | 177.58 h | 0.0003 h | 41.25 h | 2,124.64 h |
| 20 | `trip_id` | `string` | 92,681,850 | 0.00% | - | - | - | - | 88,146 trips |
| 21 | `base_date_time` | `timestamp` | 92,681,850 | 0.00% | - | - | 2025-01-01 | 2025-07-05 | 2025-12-31 |
| 22 | `ata_time` | `timestamp` | 92,681,850 | 0.00% | - | - | 2025-01-01 | 2025-07-07 | 2025-12-31 |

> [!NOTE]
> **Điểm nổi bật của phiên bản Base22:** 21/22 thuộc tính đạt tỷ lệ đầy đủ tuyệt đối 100.0000% (0 bản ghi khuyết). Thuộc tính duy nhất còn khuyết là `cargo` (chỉ chiếm 0.5009%), sẽ được điền khuyết bằng phương pháp phân tầng theo loại tàu ở Module M2.

---

### 3.2.3. Từ điển 27 thuộc tính tiền xử lý (`PREP27`)
Để khắc phục tính tuần hoàn gián đoạn của các góc la bàn (0° và 360° là cùng một hướng) và hỗ trợ các mô hình học máy tính toán vectơ chuyển động, phiên bản `PREP27` bổ sung 5 thuộc tính dẫn xuất:
1. `cog_cos = cos(cog * π / 180)`: Thành phần hình chiếu dọc của vectơ hướng đi.
2. `cog_sin = sin(cog * π / 180)`: Thành phần hình chiếu ngang của vectơ hướng đi.
3. `heading_cos = cos(heading * π / 180)`: Thành phần hình chiếu dọc của hướng mũi tàu.
4. `heading_sin = sin(heading * π / 180)`: Thành phần hình chiếu ngang của hướng mũi tàu.
5. `imputation_flag`: Cờ đánh dấu các giá trị được nội suy/điền khuyết (0: dữ liệu gốc sạch, 1: nội suy thời gian, 2: điền trung vị phân tầng, -1: khuyết kích thước).

---

## 3.3. KHUNG ĐO LƯỜNG VÀ ĐÁNH GIÁ CHẤT LƯỢNG DỮ LIỆU 6 CHIỀU THEO DAMA-DMBOK / ISO 8000

Để thiết lập cơ sở khoa học vững chắc cho toàn bộ đồ án, nhóm nghiên cứu đã triển khai đánh giá toàn diện chất lượng dữ liệu theo **6 chiều chuẩn DAMA-DMBOK** (Data Management Body of Knowledge) và tiêu chuẩn quốc tế **ISO 8000-61**:
1. **Tính đầy đủ (Completeness)**
2. **Tính nhất quán (Consistency)**
3. **Tính chính xác (Accuracy)**
4. **Tính kịp thời (Timeliness)**
5. **Tính hợp lệ (Validity)**
6. **Tính duy nhất (Uniqueness)**

### 3.3.1. Kết quả kiểm toán tổng thể 6 chiều DAMA trên 256.94 triệu bản ghi thô (RAW18)
Dưới đây là Bảng kiểm kê thực chứng nguyên gốc (trích xuất từ `table_4_1_dama_raw_six_dimensions_overall.csv`):

### Bảng 3.4: Bảng tổng hợp kiểm toán 6 chiều chất lượng dữ liệu DAMA trên 256.94M bản ghi thô RAW18

| STT | Chiều chất lượng DAMA | Số bản ghi thỏa mãn | Tổng số bản ghi kiểm tra | Tỷ lệ đạt (%) | Ngưỡng chuẩn ISO/DAMA | Đánh giá kiểm toán |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **1a** | **Completeness (Mức bản ghi)** | 240,395,409 | 256,935,254 | **93.5626%** | $\ge 95.0\%$ | **KHÔNG ĐẠT** (Khuyết cargo và thông số vỏ tàu) |
| **1b** | **Completeness (Mức thuộc tính)** | 4,603,870,439 | 4,624,834,572 | **99.5467%** | $\ge 95.0\%$ | **ĐẠT XUẤT SẮC** |
| **2** | **Consistency (Tính nhất quán)** | 94,279,701 | 256,935,254 | **36.6940%** | $100.0\%$ | **KHÔNG ĐẠT** (Nhiễu neo đậu status 1, 5 & trôi dạt) |
| **3** | **Accuracy (Tính chính xác động học)** | 117,936,010 | 256,935,254 | **45.9011%** | $\ge 90.0\%$ | **KHÔNG ĐẠT** ($v_{implied} < 1.62$ kn, $r = 0.2589$) |
| **4** | **Timeliness (Tính kịp thời tác nghiệp)** | 166,996,581 | 256,935,254 | **64.9956%** | $\ge 90.0\%$ | **KHÔNG ĐẠT** (Nhiều quan trắc ngoài cửa sổ 7 ngày) |
| **5** | **Validity (Tính hợp lệ dải vật lý)** | 247,442,006 | 256,935,254 | **96.3052%** | $\ge 95.0\%$ | **ĐẠT** |
| **6** | **Uniqueness (Tính duy nhất)** | 256,223,135 | 256,935,254 | **99.7228%** | $\ge 99.0\%$ | **ĐẠT** (Trùng lặp trạm bờ VHF nhỏ 0.28%) |

---

### 3.3.2. Phân tích chi tiết từng chiều chất lượng DAMA

#### 1. Chiều 1: Tính đầy đủ (Completeness)
- **Phương pháp đo lường:** 
  $$	ext{Comp}_{	ext{record}} = rac{1}{N} \sum_{i=1}^N \prod_{j=1}^M (1 - 	ext{is\_null}(x_{ij}))$$
  $$	ext{Comp}_{	ext{field}} = 1 - rac{\sum_{i,j} 	ext{is\_null}(x_{ij})}{N 	imes M}$$
- **Phân tích thực tế:** Ở mức thuộc tính, dữ liệu đạt tỷ lệ đầy đủ rất cao (**99.5467%**). Tuy nhiên, ở mức bản ghi (không khuyết bất kỳ ô nào), tỷ lệ đạt chỉ là **93.5626%** (thấp hơn ngưỡng chuẩn 95.0%). Phân tích chi tiết 9 cột có khuyết thiếu trong tập thô:
  1. `heading`: Khuyết **8,133,717 ô (3.1657%)** do lỗi la bàn con quay không truyền tín hiệu NMEA.
  2. `draft`: Khuyết **5,404,126 ô (2.1033%)** do thủy thủ đoàn chưa cập nhật mớn nước sau khi bốc dỡ hàng.
  3. `width`: Khuyết **2,738,933 ô (1.0660%)** và `length`: Khuyết **1,034,807 ô (0.4028%)** trong bảng tin tĩnh AIS.
  4. `cargo`: Khuyết **1,634,024 ô (0.6360%)** do không khai báo mã hàng hóa.
  5. `cog`: Khuyết **1,483,181 ô (0.5773%)** và `sog`: Khuyết **134,344 ô (0.0523%)**.
  6. `status`: Khuyết **400,631 ô (0.1559%)**; `vessel_type`: Khuyết **370 ô (0.0001%)**.
  7. Toàn bộ 9 thuộc tính cốt lõi còn lại (`mmsi`, `base_date_time`, `latitude`, `longitude`, `trip_id`, `berth_lon`, `berth_lat`, `ata_time`, `Target_Hours`) đạt **100.0000% hoàn hảo**.

#### 2. Chiều 2: Tính nhất quán (Consistency)
- **Phương pháp đo lường:** Thẩm định tính tương thích logic giữa trạng thái hành hải khai báo (`status`) và vận tốc di chuyển thực tế (`sog`), cùng độ lệch hướng trôi dạt:
  $$	ext{Consistency} = \mathbb{I}(sog \ge 1.0 	ext{ kn} \land status 
otin \{1, 5\} \land |heading - cog| \le 45^\circ)$$
- **Phân tích thực tế:** Tỷ lệ nhất quán của tập thô rất thấp, chỉ đạt **36.6940%** (94,279,701 / 256,935,254 bản ghi). Nguyên nhân cốt lõi là do tàu neo đậu tại chỗ nhưng GPS bị trôi dạt nhẹ (GPS jitter), hoặc thuyền viên quên cập nhật trạng thái `status = 0` (Under way using engine) trong khi tàu đang neo đậu buộc bến (`status = 1` hoặc `5`). Đây là lý do bắt buộc phải xây dựng bộ lọc 3 tầng ở Module M1.

#### 3. Chiều 3: Tính chính xác (Accuracy)
- **Phương pháp đo lường:** Đánh giá vận tốc biểu kiến rút ngắn cự ly đến bến đích:
  $$v_{	ext{implied}} = rac{Dist\_To\_Berth\_NM(t_1) - Dist\_To\_Berth\_NM(t_2)}{t_2 - t_1}$$
  Yêu cầu $v_{	ext{implied}} \ge 1.62$ knot (tương đương 3 km/h) và hệ số tương quan Pearson $r(Dist\_To\_Berth\_NM, Target\_Hours) \ge 0.50$.
- **Phân tích thực tế:** Tập thô chỉ đạt **45.9011%** về độ chính xác động học, với hệ số tương quan tuyến tính $r = +0.26336$ (quá thấp). Sau khi loại bỏ các quan trắc hành hải tĩnh và lọc nhiễu ở Module M1, hệ số tương quan trên tập nền tảng `Base22` đã tăng vọt lên **$r = +0.50971$**, và Spearman rank correlation trên mẫu tăng lên **$
ho = 0.62287$**, phản ánh quy luật vật lý chuyển động chuẩn xác.

#### 4. Chiều 4: Tính kịp thời (Timeliness)
- **Phương pháp đo lường:** Kiểm tra độ phủ thời gian trọn vẹn trong năm 2025 và tỷ lệ bản ghi nằm trong cửa sổ tác nghiệp hữu ích:
  $$	ext{Timeliness} = \mathbb{I}(base\_date\_time \in [2025	ext{-}01	ext{-}01, 2025	ext{-}12	ext{-}31] \land 0 < Target\_Hours \le 168	ext{h})$$
- **Phân tích thực tế:** Tập thô đạt **64.9956%** do có rất nhiều quan trắc ghi nhận khi tàu còn ở ngoài khơi xa (cách cảng hàng nghìn hải lý, thời gian đến cảng $> 7$ ngày, thậm chí hàng tháng). Đối với bài toán điều độ cảng biển, cửa sổ hữu hiệu tác nghiệp là $\le 168$ giờ (7 ngày). Tỷ lệ này được nâng lên **81.2076%** trong tập `PREP27`.

#### 5. Chiều 5: Tính hợp lệ (Validity)
- **Phương pháp đo lường:** Kiểm tra 100% thuộc tính tuân thủ dải giá trị vật lý và chuẩn mã hóa quốc tế:
  * `mmsi`: 9 chữ số thuộc dải $[201000000, 775999999]$ theo ITU-R M.585.
  * `latitude` $\in [15.0^\circ, 53.6^\circ]$, `longitude` $\in [-166.6^\circ, -65.0^\circ]$ thuộc hải phận Hoa Kỳ.
  * `sog` $\in [0.0, 40.0]$ knot, `cog` $\in [0.0^\circ, 360.0^\circ]$, `heading` $\in [0.0^\circ, 359.0^\circ]$.
  * `vessel_type` $\in [70, 89]$ (Tàu chở hàng Cargo và Tàu chở dầu Tanker).
- **Phân tích thực tế:** Tập thô đạt **96.3052%** hợp lệ tổng thể. Sau khi xử lý lọc dị thường, tỷ lệ hợp lệ đạt **97.3901%** trên toàn bộ 27 thuộc tính và đạt **100.0000%** trên các thuộc tính điều hướng cốt lõi.

#### 6. Chiều 6: Tính duy nhất (Uniqueness)
- **Phương pháp đo lường:** 
  $$	ext{Uniqueness} = 1 - rac{N_{	ext{duplicate}}}{N_{	ext{total}}}$$
  với khóa nghiệp vụ kiểm tra trùng lặp là cặp khóa kép `(mmsi, base_date_time)`.
- **Phân tích thực tế:** Tập thô đạt **99.7228%** duy nhất (chỉ có 718,171 bản ghi trùng lặp, chiếm 0.2772%). Hiện tượng trùng lặp này xuất phát từ việc hai trạm bờ VHF thu sóng gần nhau cùng nhận được một bức điện AIS phát từ một con tàu tại cùng một giây. Các bản ghi trùng lặp này được khử sạch 100% ở bước tiền xử lý, đưa tính duy nhất lên mức **100.0000% tuyệt đối** (0 duplicate rows).

---

### 3.3.3. So sánh đối chứng chất lượng 6 chiều DAMA: RAW18 vs PREP27

Dưới đây là Bảng so sánh bước nhảy vọt về chất lượng dữ liệu giữa phiên bản thô ban đầu (`RAW18`) và phiên bản sau tiền xử lý (`PREP27`):

### Bảng 3.5: Bảng đối chứng chất lượng dữ liệu 6 chiều DAMA giữa RAW18 và PREP27

| STT | Chiều chất lượng DAMA / Chỉ số đo lường | Phiên bản thô RAW18 (%) | Phiên bản sạch PREP27 (%) | Mức cải thiện Delta (%) | Đánh giá bước nhảy chất lượng |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1a** | Completeness (Mức bản ghi toàn bộ) | 94.2348% | **96.9054%** | **+2.6706%** | Vượt ngưỡng chuẩn 95.0% của ISO 8000 |
| **1b** | Completeness (Mức bản ghi không tính Cargo) | 94.6955% | **97.3901%** | **+2.6946%** | Khôi phục gần như hoàn chỉnh các ô khuyết |
| **1c** | Completeness (Mức thuộc tính toàn bộ) | 99.6181% | **99.6937%** | **+0.0756%** | Duy trì mức xuất sắc cận tuyệt đối |
| **2a** | **Consistency (Tính nhất quán động học)** | 51.1433% | **99.9870%** | **+48.8437%** | **Đột phá:** Loại bỏ hoàn toàn nhiễu trôi neo |
| **2b** | Consistency (Nhất quán tác nghiệp $\le 168$h) | 40.3009% | **81.1977%** | **+40.8968%** | Tối ưu hóa cho nghiệp vụ điều độ cảng |
| **3** | **Accuracy (Độ chính xác vận tốc $\ge 1.62$ kn)** | 50.3233% | **77.2877%** | **+26.9644%** | Đảm bảo tàu đang thực sự hành trình về bến |
| **4a** | Timeliness (Tính nhân quả năm 2025) | 99.9575% | **100.0000%** | **+0.0425%** | Tuyệt đối không rò rỉ dữ liệu xuyên năm |
| **4b** | Timeliness (Cửa sổ tác nghiệp 7 ngày $\le 168$h) | 71.9671% | **81.2076%** | **+9.2405%** | Tập trung trọng tâm dự báo ngắn hạn |
| **5** | **Validity (Tính hợp lệ quy tắc vật lý)** | 49.6629% | **97.3901%** | **+47.7272%** | **Đột phá:** Chuẩn hóa toàn bộ dải giá trị |
| **6** | **Uniqueness (Tính duy nhất khóa kép)** | 99.6558% | **100.0000%** | **+0.3442%** | Khử sạch 100% bản ghi trùng đa trạm bờ |
| **-** | **Hệ số tương quan Pearson $r(Dist, Target)$** | **+0.26336** | **+0.35068** | **+0.08732** | Tương quan tuyến tính tăng 33.15% |
| **-** | **Hệ số tương quan Spearman $\rho(Dist, Target)$** | **+0.27402** | **+0.62287** | **+0.34885** | Tương quan thứ hạng tăng vọt **+127.31%** |

---

## 3.4. PHÂN TÍCH HIỆN TƯỢNG TRÔI DẠT DỮ LIỆU (DATA DRIFT) QUA 4 QUÝ NĂM 2025

Để kiểm chứng tính ổn định của môi trường dữ liệu và đảm bảo mô hình học máy không bị suy giảm hiệu năng do phân phối dữ liệu thay đổi theo thời gian (Concept Drift / Data Drift), nhóm nghiên cứu đã tiến hành phân rã kiểm toán DAMA độc lập trên từng Quý của năm 2025:
- **Quý 1 (Q1):** 01/01/2025 đến 31/03/2025 (72,355,477 bản ghi thô $	o$ 19,266,035 bản ghi nền tảng sạch).
- **Quý 2 (Q2):** 01/04/2025 đến 30/06/2025 (75,608,632 bản ghi thô $	o$ 25,088,114 bản ghi nền tảng sạch).
- **Quý 3 (Q3):** 01/07/2025 đến 30/09/2025 (61,651,389 bản ghi thô $	o$ 24,135,227 bản ghi nền tảng sạch).
- **Quý 4 (Q4):** 01/10/2025 đến 31/12/2025 (47,319,756 bản ghi thô $	o$ 24,192,474 bản ghi nền tảng sạch).

### Bảng 3.6: Bảng theo dõi các chỉ số chất lượng dữ liệu DAMA qua 4 Quý năm 2025 (RAW18)

| Chiều chất lượng DAMA / Chỉ tiêu | Quý 1 (Q1) | Quý 2 (Q2) | Quý 3 (Q3) | Quý 4 (Q4) | Nhận xét tính ổn định |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **Số bản ghi thô (Rows)** | 72,355,477 | 75,608,632 | 61,651,389 | 47,319,756 | Giảm nhẹ vào mùa đông Q4 |
| **Completeness (Mức bản ghi)** | 93.8166% | 92.9675% | 93.6552% | 94.0047% | Cực kỳ ổn định (biến thiên < 1.0%) |
| **Completeness (Mức thuộc tính)** | 99.5882% | 99.4840% | 99.5518% | 99.5769% | Đạt chuẩn xuất sắc cả 4 quý |
| Tỷ lệ khuyết `cargo` | 0.5018% | 0.7796% | 0.5872% | 0.6751% | Dao động nhẹ trong dải 0.5 - 0.8% |
| Tỷ lệ khuyết `draft` | 1.9806% | 2.3990% | 2.2113% | 1.6778% | Đạt mức hoàn thiện tốt nhất ở Q4 |
| **Consistency (Tính nhất quán)** | 30.5125% | 35.3623% | 42.1587% | 41.1537% | Tăng dần do mật độ hành hải cao |
| **Accuracy (Tính chính xác động học)** | 37.6004% | 45.0963% | 52.8213% | 50.8631% | Tàu chạy nhanh hơn vào mùa hè Q3 |
| **Timeliness ($\le 168$h)** | 58.0309% | 61.1896% | 71.7615% | 72.9112% | Tàu cận cảng tăng mạnh nửa cuối năm |
| **Validity (Tính hợp lệ)** | 97.2745% | 95.7846% | 95.7016% | 96.4412% | Đạt chuẩn $\ge 95\%$ xuyên suốt 4 quý |
| **Uniqueness (Tính duy nhất)** | 99.9659% | 99.9527% | 99.2592% | 99.5880% | Tỷ lệ trùng trạm bờ cực thấp |

### Bảng 3.7: Bảng đo lường 6 chiều DAMA qua 4 Quý trên tập dữ liệu nền tảng (Base22)

| Quý | Số bản ghi sạch | Completeness (21 cols) | Tỷ lệ khuyết Cargo | Uniqueness | Validity | Accuracy | Consistency | Timeliness |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Q1** | 19,266,035 | **100.00%** | 0.4635% | **100.00%** | **100.00%** | **100.00%** | **100.00%** | **100.00%** |
| **Q2** | 25,088,114 | **100.00%** | 0.5190% | **100.00%** | **100.00%** | **100.00%** | **100.00%** | **100.00%** |
| **Q3** | 24,135,227 | **100.00%** | 0.3325% | **100.00%** | **100.00%** | **100.00%** | **100.00%** | **100.00%** |
| **Q4** | 24,192,474 | **100.00%** | 0.6798% | **100.00%** | **100.00%** | 70.9036% | **100.00%** | **100.00%** |

> [!TIP]
> **Nhận xét chuyên môn về Data Drift:**
> 1. Dữ liệu thể hiện tính nhất quán rất cao qua 4 Quý. Sự sụt giảm số bản ghi ở Q4 phản ánh tính mùa vụ tự nhiên của ngành vận tải biển Bắc Mỹ khi thời tiết mùa đông gây băng giá ở các cảng phía Bắc.
> 2. Việc Accuracy ở Q4 trên tập kiểm tra đạt 70.90% (so với 100% ở tập huấn luyện Q1-Q3) giải thích tại sao ở các thực nghiệm học máy, Fold 2 và Fold 3 luôn gặp thách thức lớn hơn Fold 1. Đây là căn cứ thực nghiệm then chốt để áp dụng kỹ thuật **Expanding Window Cross-Validation** (huấn luyện mở rộng dần theo thời gian) thay vì K-Fold ngẫu nhiên.

---

## 3.5. KẾT LUẬN CHƯƠNG 3 VÀ HÀM Ý THIẾT KẾ CHO CÁC MODULE TIẾP THEO

Báo cáo kiểm toán dữ liệu và đo lường chất lượng 6 chiều DAMA tại Chương 3 đã thiết lập một hệ quy chiếu định lượng vững chắc với các kết luận quan trọng sau:
1. **Khẳng định quy mô Big Data đạt chuẩn công nghiệp:** Đề tài đã xử lý thành công **256.94 triệu bản ghi thô**, trích xuất chính xác **88,146 chuyến hành hải** và **92.68 triệu bản ghi nền tảng sạch**, vượt xa các nghiên cứu học thuật trước đây (thường chỉ khảo sát vài nghìn chuyến đi).
2. **Nhận diện chính xác 3 điểm nghẽn dữ liệu:**
   - Điểm nghẽn 1: Nhiễu neo đậu và trôi dạt GPS làm tính nhất quán của dữ liệu thô chỉ đạt 36.69%.
   - Điểm nghẽn 2: Dữ liệu thô khuyết thiếu cục bộ ở các thuộc tính thân vỏ (`draft`: 2.10%, `width`: 1.07%, `cargo`: 0.64%).
   - Điểm nghẽn 3: Dữ liệu thô có tương quan tuyến tính yếu ($r = +0.263$), đòi hỏi phải chế tác các đặc trưng động lực học tiếp cận bến phi tuyến.
3. **Cung cấp định hướng kỹ thuật cho Pipeline 7 Module:**
   - **Module M1 (Lọc dữ liệu):** Sử dụng bộ lọc 3 tầng để triệt tiêu nhiễu neo đậu, đưa Consistency từ 36.69% lên 99.99%.
   - **Module M2 (Điền khuyết):** Áp dụng nội suy tuyến tính chuỗi thời gian kết hợp trung vị phân tầng theo loại tàu, đưa Completeness lên 97.39%.
   - **Module M3 (Chế tác đặc trưng):** Xây dựng các đặc trưng động học tiếp cận bến ($v_{\text{closing}}$, $\text{approach\_cos}$, $\text{bearing\_to\_berth}$) để nâng cao hệ số tương quan Spearman lên $\rho = 0.6229$, sẵn sàng cho các mô hình học máy Gradient Boosting đạt độ chính xác tối ưu.
