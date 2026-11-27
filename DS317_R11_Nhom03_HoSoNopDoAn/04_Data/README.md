# Dữ Liệu Mẫu Demo, Từ Điển Dữ Liệu & Liên Kết Tập Dữ Liệu Lớn (`04_Data/`)

Thư mục này lưu trữ bộ dữ liệu mẫu chạy Demo/kiểm thử offline tốc độ cao, từ điển dữ liệu đầy đủ 39 thuộc tính (chuẩn `Prep27 + RTMA12`), hồ sơ chất lượng 6 chiều **DAMA-DMBOK**, và liên kết truy cập các tập dữ liệu đầy đủ (> 100 MB) ngoài GitHub.

---

## 1. Bộ Dữ Liệu Mẫu Demo (`demo_sample_3000.csv` & `demo_sample_3000.parquet`)

| Thuộc tính tệp | `demo_sample_3000.csv` | `demo_sample_3000.parquet` |
| :--- | :--- | :--- |
| **Nguồn trích xuất** | [`ais_sample_clustering_outlier.parquet`](../../01_Bai_Tap_Ve_Nha_Chinh_Thuc/BT5_Gom_Nhom_Va_Ngoai_Lai/Ket_Qua_Thuc_Nghiem/ais_sample_clustering_outlier.parquet) (25,000 bản tin AIS 2025 thực tế) | Cùng nguồn trích xuất (nén `zstd`) |
| **Quy mô mẫu** | `3,000` dòng x `39` cột (`485` tàu `mmsi` độc nhất) | `3,000` dòng x `39` cột (`485` tàu `mmsi` độc nhất) |
| **Phân tầng thực tế** | `34.27%` Tanker (`Is_Tanker=1`), `84.73%` hành trình `Target_Hours <= 168h` | Khớp 100% CSV |
| **Dung lượng & Thời gian nạp** | `732,391` bytes (~`0.70 MB`), nạp ~`0.03s` | `190,057` bytes (~`0.18 MB`), nạp ~`0.02s` |
| **Điều kiện lọc sạch** | `1.0 <= sog <= 40.0`, `status not in {1.0, 5.0}`, `heading` & `cargo` không khuyết | Khớp 100% CSV |

> **Lưu ý tính trung thực dữ liệu (Schema Placeholders):**
> Tập nguồn BT5 chứa đầy đủ tọa độ, động học, kích thước thân vỏ, `Dist_To_Berth_NM` và `Target_Hours` thực tế, nhưng chưa kèm 2 cột tọa độ bến (`berth_lon`, `berth_lat`) và 12 cột thời tiết RTMA (`rtma_*`). Để bảo đảm **không giả lập số liệu**, bộ mẫu hiện tại đặt `berth_lon = NaN`, `berth_lat = NaN`, `rtma_domain = 0`, `weather_missing_flag = 1`, và 10 biến liên tục `rtma_TMP_C..rtma_crosswind_knots = NaN` (khớp cơ chế xử lý missing của Engine v2). Sau khi Nhóm trưởng chạy lại Kaggle và trích lát cắt 3,000 dòng từ `03_ban_tien_xu_ly_27_thuoc_tinh/q4.parquet` + `weather_rtma_2025_sidecar/test.parquet`, hai tệp này sẽ được thay thế bằng bản có đầy đủ tọa độ bến và giá trị RTMA thực tế.

---

## 2. Từ Điển Dữ Liệu 39 Thuộc Tính (`SCHEMA_PREPROCESSED` 27 Cột + `WEATHER_12` Cột)

### 2.1. Phần A - 27 Cột Chuẩn Tiền Xử Lý (`03_ban_tien_xu_ly_27_thuoc_tinh`)

| STT | Tên cột | Kiểu PyArrow | Vai trò (X / ID / Target) | Ý nghĩa nghiệp vụ & Miền giá trị chuẩn (`Base22`/`Prep27` 92.68M dòng) |
| :-: | :--- | :--- | :--- | :--- |
| 1 | `mmsi` | `int64` | ID (Cấm đưa vào $X$) | Mã nhận dạng di động hàng hải 9 chữ số (`205097000` - `720233000`) |
| 2 | `trip_id` | `string` | ID (Cấm đưa vào $X$) | Định danh chuyến hành trình tách theo cập bến & biên quý |
| 3 | `base_date_time` | `timestamp[us]` | Thời gian (Cấm vào $X$) | Mốc thời gian quan trắc bản tin AIS (UTC, năm 2025) |
| 4 | `longitude` | `float32` | Đầu vào $X$ | Kinh độ WGS84 (`-166.64` đến `-65.00` độ) |
| 5 | `latitude` | `float32` | Đầu vào $X$ | Vĩ độ WGS84 (`15.00` đến `53.58` độ) |
| 6 | `sog` | `float32` | Đầu vào $X$ | Vận tốc tức thời trên mặt đất (`1.0` - `39.9` knots, mean `11.36`) |
| 7 | `cog` | `float32` | Góc thô (Bỏ khỏi $X$) | Hướng di chuyển mặt đất (`0.0` - `359.9` độ; thay bằng `cog_sin/cos`) |
| 8 | `heading` | `float32` | Góc thô (Bỏ khỏi $X$) | Hướng mũi tàu la bàn (`0.0` - `359.0` độ; thay bằng `heading_sin/cos`) |
| 9 | `cog_sin` | `float32` | Đầu vào $X$ | $\sin(\text{radians}(\text{cog})) \in [-1, 1]$ |
| 10 | `cog_cos` | `float32` | Đầu vào $X$ | $\cos(\text{radians}(\text{cog})) \in [-1, 1]$ |
| 11 | `heading_sin` | `float32` | Đầu vào $X$ | $\sin(\text{radians}(\text{heading})) \in [-1, 1]$ |
| 12 | `heading_cos` | `float32` | Đầu vào $X$ | $\cos(\text{radians}(\text{heading})) \in [-1, 1]$ |
| 13 | `status` | `float32` | Đầu vào $X$ (Rời rạc) | Trạng thái hành hải (`0.0` - `13.0`, đã loại `1.0` neo & `5.0` buộc bến) |
| 14 | `vessel_type` | `int32` | Đầu vào $X$ (Rời rạc) | Mã loại tàu ITU (`70-79`: Cargo, `80-89`: Tanker) |
| 15 | `length` | `float32` | Đầu vào $X$ | Chiều dài thân tàu (`5.0` - `400.0` m, mean `213.49`, missing `0.0%`) |
| 16 | `width` | `float32` | Đầu vào $X$ | Chiều rộng thân tàu (`3.0` - `61.0` m, mean `32.34`, missing `0.0%`) |
| 17 | `draft` | `float32` | Đầu vào $X$ | Mớn nước tĩnh (`0.1` - `22.2` m, mean `9.02`, missing `0.0%`) |
| 18 | `cargo` | `float32` | Đầu vào $X$ | Mã hàng hóa (`1.0` - `207.0`, tỷ lệ khuyết `0.5009%`) |
| 19 | `berth_lon` | `float32` | Đầu vào $X$ | Kinh độ bến cập đích (`-159.36` đến `-65.84` độ) |
| 20 | `berth_lat` | `float32` | Đầu vào $X$ | Vĩ độ bến cập đích (`15.84` đến `49.69` độ) |
| 21 | `ata_time` | `timestamp[us]` | Nhãn (Cấm đưa vào $X$) | Mốc thời gian cập bến thực tế (Actual Time of Arrival) |
| 22 | `Dist_To_Berth_NM` | `float32` | Đầu vào $X$ | Cự ly trắc địa Haversine tới bến đích (`0.0` - `2,300.0` NM) |
| 23 | `Area_Proxy` | `float32` | Đầu vào $X$ | Diện tích mặt boong đại diện $\text{length} \times \text{width}$ (`36` - `24,400` $\text{m}^2$) |
| 24 | `Volume_Proxy` | `float32` | Đầu vào $X$ | Thể tích thân vỏ đại diện $\text{length} \times \text{width} \times \text{draft}$ (`57.6` - `437,562` $\text{m}^3$) |
| 25 | `Is_Tanker` | `int32` | Đầu vào $X$ (Rời rạc) | Cờ nhị phân loại tàu (`1`: Tanker `32.51%`, `0`: Cargo `67.49%`) |
| 26 | `imputation_flag` | `int32` | Đầu vào $X$ (Rời rạc) | Cờ đánh dấu bản ghi đã qua điền khuyết Domain Imputation (`0` / `1`) |
| 27 | `Target_Hours` | `float32` | Biến mục tiêu $y$ | Thời gian hành trình còn lại tới ATA (Train lọc `<= 168h`; Eval giữ gốc `max 2,124.64h`) |

### 2.2. Phần B - 12 Cột Thời Tiết NOAA RTMA 2025 (`weather_rtma_2025_sidecar`, Module M4)

| STT | Tên cột | Kiểu PyArrow | Đơn vị / Giá trị | Ý nghĩa vật lý |
| :-: | :--- | :--- | :--- | :--- |
| 28 | `rtma_domain` | `int8` | `0..4` | `0`: OOG/Missing, `1`: CONUS (`rtma2p5`), `2`: AK, `3`: HI, `4`: PR |
| 29 | `weather_missing_flag` | `int8` | `0` hoặc `1` | Cờ `1` nếu ngoài lưới RTMA hoặc thiếu biến lõi |
| 30 | `rtma_TMP_C` | `float32` | `°C` | Nhiệt độ không khí 2 m (`TMP - 273.15`) |
| 31 | `rtma_DPT_C` | `float32` | `°C` | Nhiệt độ điểm sương 2 m (`DPT - 273.15`) |
| 32 | `rtma_PRES_hpa` | `float32` | `hPa` | Áp suất khí quyển bề mặt (`PRES / 100.0`) |
| 33 | `rtma_VIS_nm` | `float32` | `NM` | Tầm nhìn bề mặt (`VIS / 1852.0`) |
| 34 | `rtma_WIND_knots` | `float32` | `knots` | Tốc độ gió duy trì 10 m |
| 35 | `rtma_GUST_knots` | `float32` | `knots` | Tốc độ gió giật 10 m |
| 36 | `rtma_wdir_sin` | `float32` | `[-1, 1]` | $\sin(\text{radians}(\text{WDIR}))$ |
| 37 | `rtma_wdir_cos` | `float32` | `[-1, 1]` | $\cos(\text{radians}(\text{WDIR}))$ |
| 38 | `rtma_headwind_knots` | `float32` | `knots` | Thành phần gió cản dọc hướng tàu (`+` ngược mũi, `-` xuôi gió) |
| 39 | `rtma_crosswind_knots` | `float32` | `knots` | Thành phần gió ngang mạn tàu (`+` mạn phải, `-` mạn trái) |

---

## 3. Tiêu Chuẩn Chất Lượng Dữ Liệu 6 Chiều DAMA-DMBOK

Bảng đối chiếu chất lượng trích từ [`05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/DAMA/`](../../05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/DAMA/) (`RAW18`: `256,935,254` dòng vs `Base22/Prep27`: `92,681,850` dòng):

| Chiều chất lượng DAMA | Bản thô `RAW18` (256.94M dòng) | Bản sạch `Base22/Prep27` (92.68M dòng) | Chênh lệch |
| :--- | :---: | :---: | :---: |
| **1. Tính đầy đủ (Completeness)** | `93.5626%` (bản ghi) / `99.5467%` (thuộc tính) | `100.00%` (0 ô khuyết ngoài `cargo` `0.5009%`) | `+6.44%` |
| **2. Tính nhất quán (Consistency)** | `36.6940%` (`94,279,701` dòng đạt 4 ràng buộc) | `100.00%` (`92,681,850` dòng thỏa mãn) | `+63.31%` |
| **3. Tính chính xác (Accuracy)** | `45.9011%` (`Pearson r = +0.2589`) | `92.7259%` (`Q1-Q3: 100%`, `Q4: 70.90%`, `r = +0.50971`) | `+46.82%` |
| **4. Tính kịp thời (Timeliness)** | `64.9956%` (35.00% ngoài cửa sổ 168h) | `100.00%` (365/365 ngày, cửa sổ tác nghiệp) | `+35.00%` |
| **5. Tính hợp lệ (Validity)** | `96.3052%` | `100.00%` (Khớp PyArrow schema & dải vật lý) | `+3.69%` |
| **6. Tính duy nhất (Uniqueness)** | `99.7228%` (trùng `0.2772%` trạm bờ VHF) | `100.00%` (Khử trùng hoàn toàn theo `(mmsi, base_date_time)`) | `+0.28%` |

---

## 4. Liên Kết Bộ Dữ Liệu Đầy Đủ Ngoài GitHub (Kaggle & Google Drive)

Do giới hạn dung lượng tệp của GitHub (`100 MB`), toàn bộ dữ liệu thô (`320,776,922` dòng pre-split / `13.15 GB` nén gốc), `RAW18` (`256,935,254` dòng / `6.83 GB`), `Base22/Prep27` (`92,681,850` dòng / `3.47 - 3.95 GB`), và sidecar thời tiết RTMA 2025 được lưu trữ tại các nguồn chính thức sau:

- **Dataset NOAA AIS 2025 Full Year (Kaggle Dataset):**
  - `https://www.kaggle.com/datasets/kienvo134/noaa-ais-2025-full-year-tin-x-l-nn-tng`
  - Đường dẫn mount trên Kaggle Kernel: `/kaggle/input/noaa-ais-2025-full-year-tin-x-l-nn-tng` (hoặc `/kaggle/input/datasets/kienvo134/`)
- **Notebook Tiền xử lý & Baseline tham khảo trên Kaggle:**
  - Tiền xử lý nền tảng: `https://www.kaggle.com/code/kienvo134/t-i-v-x-l-noaa-ais-2025-full-year?scriptVersionId=371126211`
  - Baseline thực nghiệm: `https://www.kaggle.com/code/kienvo134/baseline-th-c-nghi-m`
- **Dataset Thời tiết NOAA RTMA 2025 Sidecar (Kaggle Dataset):**
  - `/kaggle/input/datasets/kienvo134/dataset-noaa-rtma-2025/` (`weather_rtma_2025_sidecar/{train,test}.parquet`)
- **Kho lưu trữ Google Drive dùng chung của Nhóm 03 (theo [`Nhom_03.txt`](../../00_Quan_Ly_Va_Tai_Lieu_Chung/Nhom_03.txt)):**
  - `https://drive.google.com/drive/folders/1o-AYkqTawWejyt4N9J-BupZTDJr6AsP-?usp=sharing`
