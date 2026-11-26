# HƯỚNG DẪN VÀ KẾ HOẠCH ĐIỀU CHỈNH THUYẾT MINH ĐỀ TÀI (LAB 3)
## CHUYỂN ĐỔI DATASET ĐẦU VÀO TỪ BẢN NỀN TẢNG SANG BẢN THÔ (NOAA AIS 2025 RAW)

**Học phần:** DS317 - Khai phá dữ liệu trong doanh nghiệp (UIT)  
**Nhóm thực hiện:** Nhóm 03 - Lớp DS317.P11 / DS317.R11  
**Đề tài:** Dự báo thời điểm cập cảng của tàu biển thay thế ETA tự khai báo *(Prediction of Vessel Port Arrival Time Replacing Self-Reported ETA)*  

---

### I. MỤC ĐÍCH VÀ BỐI CẢNH ĐIỀU CHỈNH CHIẾN LƯỢC

1. **Lý do điều chỉnh:**
   - Nhằm **thỏa mãn tuyệt đối yêu cầu của giảng viên hướng dẫn**: Đề tài khai phá dữ liệu phải bắt đầu từ **bộ dữ liệu thô ban đầu (Raw Data)** của doanh nghiệp/ngành thực tế, thay vì lấy một tập dữ liệu đã qua tiền xử lý, gọt giũa và lọc sạch sẵn.
   - Thể hiện rõ nét toàn bộ giá trị gia tăng và kỹ năng của nhóm qua từng bước: Đo lường chất lượng dữ liệu thô $\rightarrow$ Nhận diện lỗi cảm biến, dị biệt, khuyết thiếu $\rightarrow$ Thiết kế Pipeline tinh chế dữ liệu lớn $\rightarrow$ Chế tác đặc trưng và huấn luyện mô hình.

2. **Chiến lược "Trước vs. Sau" (Before vs. After) chuẩn mực:**
   - **Mục 5 (Mô tả dữ liệu):** Tập trung kiểm kê, xây dựng từ điển và đo lường độ đo chất lượng 6 chiều trên **Bản thô (Bản 1 / Raw Labeled - 320,776,922 bản ghi gốc, 18 cột cảm biến AIS)**.
   - **Mục 6 (Tiền xử lý dữ liệu):** Đóng vai trò là "cầu nối tinh chế dữ liệu", mô tả chi tiết quy trình biến đổi 320.78 triệu dòng thô thành **80,660,588 dòng chất lượng cao (Bản nền tảng 22 cột / Bản ML-Ready 27 cột)**.
   - **Mục 7 & Mục 8 (Mô hình & Kịch bản thực nghiệm):** Tiếp tục kế thừa tập dữ liệu sạch 80.66 triệu dòng để huấn luyện mô hình cơ sở (Ridge Regression Baseline) và các mô hình nâng cao. Bảo toàn 100% công sức huấn luyện và kết quả thực nghiệm đã chạy!

---

### II. BẢNG SỐ LIỆU ĐỐI CHUẨN DÙNG CHUNG (SINGLE SOURCE OF TRUTH)
*(Tất cả 7 thành viên bắt buộc phải sử dụng thống nhất các con số chính thức dưới đây, tuyệt đối không tự ý làm tròn hoặc phỏng đoán)*

| Hạng mục chỉ số | Dữ liệu Thô ban đầu (Raw Input - Mục 5) | Dữ liệu sau Tiền xử lý (ML-Ready - Mục 6, 7, 8) |
| :--- | :--- | :--- |
| **Quy mô số dòng** | **320,776,922 bản ghi gốc** (100% trọn vẹn 365 ngày) | **80,660,588 bản ghi chất lượng cao** (Tỷ lệ lọc: 25.15%) |
| **Số lượng thuộc tính** | **18 cột** (chuẩn cảm biến vô tuyến ITU-R M.1371) | **22 cột** (Bản nền tảng) / **27 cột** (Bản ML-Ready) |
| **Dung lượng lưu trữ** | 62.4 GB uncompressed CSV (365 tệp ngày) | 3.65 GB (Bản nền tảng) / 4.02 GB (ML-Ready) Parquet Snappy |
| **Số chuyến cập bến (trip_id)**| Tự động quét từ 102,050 sự kiện buộc bến | **102,050 chuyến hành hải độc nhất** |
| **Số lượng tàu độc nhất (mmsi)**| Toàn bộ các phương tiện phát sóng AIS | **11,006 tàu thương mại lớn** (Cargo 70-79 & Tanker 80-89) |
| **Tỷ lệ khuyết thiếu thân vỏ**| **Draft: 2.46% \| Length: 0.47% \| Width: 1.23%** | **0.00% tuyệt đối** (nhờ Domain Imputation 4 cấp) |
| **Dải vận tốc di chuyển (SOG)**| 0.0 - 99.9 knots (nhiều lỗi vọt tốc sensor) | **1.0 - 39.9 knots** (vận tốc kinh tế chuẩn hàng hải) |
| **Trạng thái hành hải (Status)**| Đầy đủ mọi trạng thái (Neo đậu status 1 & 5 chiếm >50%) | **Chỉ giữ tàu đang hành trình** (status != 1.0 và != 5.0) |
| **Khoảng cách tới bến đích** | Chưa tính toán trắc địa | **Đã tính Dist_To_Berth_NM** (hải lý) (Haversine WGS84) |
| **Tín hiệu tương quan hành hải**| Chưa xác lập đặc trưng | **Pearson r = +0.7628** (Cự ly vs Target_Hours) |
| **Kết quả Baseline Test Q4** | Chưa áp dụng mô hình | **Dummy MAE = 27.07h $\rightarrow$ Ridge MAE = 15.71h (giảm 41.95%)** |

---

### III. SƠ ĐỒ PHỤ THUỘC GIỮA CÁC NHIỆM VỤ (TASK DEPENDENCY GRAPH)

```mermaid
flowchart TD
    classDef kiet fill:#e8f5e9,stroke:#388e3c,stroke-width:2px;
    classDef kien fill:#fff3e0,stroke:#f57c00,stroke-width:2px;
    classDef liem fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef linh fill:#fce4ec,stroke:#c2185b,stroke-width:2px;
    classDef loc fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;
    classDef leader fill:#ede7f6,stroke:#512da8,stroke-width:3px;

    Start(["Khởi động chuyển đổi Dataset Thô (17/10/2026)"]):::leader

    subgraph Pha1 ["Pha 1: Thiết lập Dữ liệu Thô & Đo lường Chất lượng"]
        T1["Task 1: Kiểm kê 18 cột thô & Đo lường 6 chiều DAMA<br/><b>Quách Tuấn Kiệt (24520911)</b>"]:::kiet
        T2["Task 2A: Biểu đồ EDA phân tích hiện trạng dữ liệu thô<br/><b>Huỳnh Chí Kiên (24520880)</b>"]:::kien
    end

    subgraph Pha2 ["Pha 2: Phát biểu Bài toán & Quy trình Tinh chế Dữ liệu"]
        T3["Task 3: Phát biểu KPDL luồng thô & Time-based Split<br/><b>Lê Sỹ Liêm (24520951)</b>"]:::liem
        T4["Task 2B: Lập luận Pipeline tinh chế Thô -> Sạch Mục 6<br/><b>Huỳnh Chí Kiên (24520880)</b>"]:::kien
    end

    subgraph Pha3 ["Pha 3: Code Baseline & Đồng bộ Bối cảnh, SOTA, Rủi ro"]
        T5["Task 4: Minh họa luồng nạp dữ liệu thô trong Notebook<br/><b>Trần Hồng Lĩnh (24520970)</b>"]:::linh
        T6["Task 5: Đồng bộ Bối cảnh & Mục tiêu quy mô dữ liệu thô<br/><b>Đỗ Văn Lộc (24520977)</b>"]:::loc
        T7["Task 6: Bổ sung luận điểm đối sánh SOTA trên dữ liệu thô<br/><b>Nguyễn Hữu Bảo Lộc (24520983)</b>"]:::loc
    end

    subgraph Pha4 ["Pha 4: Tổng duyệt & Xuất bản Hồ sơ"]
        T8["Task 7: Rủi ro Big Data dữ liệu thô, Slides & Tổng duyệt<br/><b>Võ Đình Kiên (24520893 - NT)</b>"]:::leader
        End(["Hoàn tất xuất file ThuyetMinh chính thức"]):::leader
    end

    Start --> T1
    Start --> T2
    T1 -->|Cung cấp chỉ số lỗi bẩn của bản thô| T4
    T1 -->|Schema 18 cột thô| T3
    T2 --> T4
    T3 --> T5
    T4 --> T5
    T5 --> T8
    T6 --> T8
    T7 --> T8
    T8 --> End
```

---

### IV. BẢNG TỔNG HỢP MA TRẬN PHÂN CÔNG NHIỆM VỤ ĐIỀU CHỈNH

| Mã Task | Tên nhiệm vụ điều chỉnh | Thành viên phụ trách | MSSV | Vị trí chèn trong file Word gốc | Mức độ ưu tiên | Hạn chót |
| :---: | :--- | :--- | :---: | :--- | :---: | :---: |
| **TASK-RAW-01** | Kiểm kê 18 cột thô & Đo lường 6 chiều DAMA-DMBOK | **Quách Tuấn Kiệt** | 24520911 | Mục 5.1, 5.2, 5.3 & File Excel | **Khẩn cấp** | **18/10/2026** |
| **TASK-RAW-02** | EDA hiện trạng dữ liệu thô & Quy trình tinh chế Mục 6 | **Huỳnh Chí Kiên** | 24520880 | Mục 5.4 & Mục 6 (tiểu mục 6.1-6.6) | **Khẩn cấp** | **18/10/2026** |
| **TASK-RAW-03** | Cập nhật Bài toán KPDL trên dữ liệu thô & Time-based Split | **Lê Sỹ Liêm** | 24520951 | Mục 3 & Mục 8 (tiểu mục 8.1) | **Quan trọng** | **19/10/2026** |
| **TASK-RAW-04** | Minh họa luồng nạp dữ liệu thô & Hàm làm sạch trong Code | **Trần Hồng Lĩnh** | 24520970 | Notebook Code Kaggle & Mục 7 | **Quan trọng** | **19/10/2026** |
| **TASK-RAW-05** | Cập nhật Bối cảnh & Mục tiêu SMART theo quy mô thô 320M | **Đỗ Văn Lộc** | 24520977 | Mục 1 & Mục 2 (Bảng 2.1) | **Bình thường** | **19/10/2026** |
| **TASK-RAW-06** | Bổ sung luận điểm đối sánh SOTA trên dữ liệu thô lớn | **Nguyễn Hữu Bảo Lộc** | 24520983 | Mục 4 (tiểu mục 4.3) & Mục 13 | **Bình thường** | **19/10/2026** |
| **TASK-RAW-07** | Rủi ro Big Data dữ liệu thô 320M dòng, Slides & Tổng duyệt | **Võ Đình Kiên (NT)** | 24520893 | Mục 12, Slides & Đóng gói ZIP | **Tổng hợp** | **20/10/2026** |

---

### V. BẢN HƯỚNG DẪN CHI TIẾT TỪNG NHIỆM VỤ

#### 1. QUÁCH TUẤN KIỆT (MSSV: 24520911)
**Nhiệm vụ:** Hoàn thiện bảng kiểm kê tài sản dữ liệu thô, lập từ điển 18 thuộc tính gốc và đo lường độ đo chất lượng 6 chiều trên dữ liệu thô.

* **Công việc cụ thể:**
  1. **Bảng 5.1 (Kiểm kê 7 tiêu chí):**
     - Tiêu chí Quy mô: Báo cáo rõ dữ liệu thô ban đầu gồm **320,776,922 bản ghi gốc** (62.4 GB uncompressed CSV, trải dài 365 ngày của năm 2025). Nhận diện 102,050 lượt cập bến thực tế của 11,006 tàu thương mại lớn.
     - Tiêu chí Chất lượng: Nêu rõ hiện trạng khuyết thiếu ban đầu (Draft thiếu 2.46%, Length thiếu 0.47%, Width thiếu 1.23%, Cargo thiếu 2.87%).
  2. **Bảng 5.2 (Từ điển dữ liệu thô 18 cột):**
     - Đổi sang từ điển 18 thuộc tính gốc cảm biến: `mmsi`, `base_date_time`, `latitude`, `longitude`, `sog`, `cog`, `heading`, `vessel_name`, `imo`, `call_sign`, `vessel_type`, `status`, `length`, `width`, `draft`, `cargo`, `transceiver_class`, `Target_Hours` (nhãn nội sinh).
     - Báo cáo số lượng bản ghi hợp lệ và tỷ lệ khuyết thiếu (% missing) thực tế trên dữ liệu thô.
  3. **Mục 5.3 (Đo lường chất lượng 6 chiều DAMA-DMBOK):**
     - **BẮT BUỘC ĐO TRÊN DỮ LIỆU THÔ** để chỉ ra lỗi chất lượng dữ liệu:
       * *Tính đầy đủ:* Có 1,999,693 bản ghi khuyết thiếu kích thước thân vỏ (chiếm 2.48%).
       * *Tính nhất quán:* Bản thô vi phạm nghiêm trọng do tàu neo đậu status 1 & 5 chiếm hơn 50% số dòng; lỗi cảm biến vận tốc $SOG > 40$ kn và $SOG = 0$.
       * *Tính duy nhất:* Xuất hiện 169,543 bản ghi trùng lặp thời gian do vùng phủ sóng chồng lấn giữa các trạm bờ VHF USCG.
  4. **Sản phẩm bàn giao:** Cập nhật tệp Excel `Lab3_DS317_Nhom03_DataInventory.xlsx` và nhập trực tiếp vào Mục 5.1, 5.2, 5.3 trên file Word gốc.

---

#### 2. HUỲNH CHÍ KIÊN (MSSV: 24520880)
**Nhiệm vụ:** Trực quan hóa hiện trạng dữ liệu thô và xây dựng toàn diện Chương 6 (Phương pháp tiền xử lý tinh chế dữ liệu từ Thô sang Sạch).

* **Công việc cụ thể:**
  1. **Mục 5.4 (Kết quả EDA):**
     - Bổ sung phân tích hiện trạng dữ liệu thô: Biểu đồ phân phối vận tốc SOG thô (thấy đỉnh nhọn tại $0$ kn do tàu neo buộc bến và các điểm ngoại lai $>40$ kn do lỗi sensor); biểu đồ cơ cấu các loại tàu cho thấy cần phải lọc phân nhóm Cargo/Tanker.
  2. **Mục 6 (Phương pháp tiền xử lý dữ liệu - TRỌNG TÂM):**
     - Viết chi tiết quy trình tinh chế biến đổi từ 320.78M dòng thô thành 80.66M dòng sạch:
       * *Tiểu mục 6.1 (Kiến trúc 2-Pass Rolling Stream):* Thuật toán quét Pass 1 lập Catalog 102,050 lượt cập bến và Pass 2 gán nhãn `Target_Hours` trong cửa sổ 0 - 168 giờ.
       * *Tiểu mục 6.2 (Bộ lọc 3 tầng):* Lọc vận tốc chuẩn hàng hải $1.0 \le SOG \le 40.0$ kn; lọc trạng thái hành hải (loại status 1 & 5); lọc loại tàu thương mại (mã ITU-R 70-89).
       * *Tiểu mục 6.3 (Xử lý khuyết thiếu - Domain-based Imputation):* Giải thích thuật toán 4 cấp (theo chuyến $\rightarrow$ theo tàu $\rightarrow$ theo loại tàu $\rightarrow$ theo nhóm tàu) đưa tỷ lệ thiếu kích thước thân vỏ từ 2.46% về **0.00% tuyệt đối** (kèm Bảng 6.1 kết quả kiểm chứng mask-and-recover).
       * *Tiểu mục 6.4 (Chế tác đặc trưng - Feature Engineering):* Công thức tính cự ly trắc địa Haversine/WGS84 `Dist_To_Berth_NM`, chế tác diện tích cản gió `Area_Proxy` và thể tích choán nước `Volume_Proxy`.
       * *Tiểu mục 6.5 & 6.6:* Xử lý target lệch phải và giải thích lý do không áp dụng giảm chiều PCA (giữ nguyên ngữ nghĩa vật lý).

---

#### 3. LÊ SỸ LIÊM (MSSV: 24520951)
**Nhiệm vụ:** Cập nhật Phát biểu bài toán KPDL trên dữ liệu thô và Sơ đồ phân chia Time-based Split.

* **Công việc cụ thể:**
  1. **Mục 3 (Phát biểu bài toán khai phá dữ liệu):**
     - Bảng phát biểu bài toán:
       * *Cho trước:* Bộ dữ liệu thô NOAA AIS 2025 gồm 320,776,922 bản ghi cảm biến của các tàu hàng rời và tàu dầu tại vùng biển Hoa Kỳ.
       * *Đầu vào:* Bản tin định vị AIS thô từ trạm thu vô tuyến của tàu, được đưa qua pipeline tự động lọc nhiễu, điền khuyết và trích xuất đặc trưng.
       * *Đầu ra:* Số giờ di chuyển thực tế còn lại (`Target_Hours`) và mốc giờ cập bến dự báo (`Predicted ATA`) kèm khoảng an toàn 90%.
  2. **Mục 8.1 (Kịch bản phân chia tập dữ liệu Time-based Split):**
     - Trình bày sơ đồ phân chia theo dòng thời gian thực tế: **Tập Train (01/01 - 30/09/2025, 9 tháng đầu năm, ~60 triệu dòng sau lọc)** và **Tập Test (01/10 - 31/12/2025, 3 tháng mùa đông, ~20 triệu dòng sau lọc)**.
     - Khẳng định nguyên tắc chống rò rỉ thông tin: **Mốc cắt thời gian được xác lập ngay trên dữ liệu thô**; toàn bộ các bước tính toán trung vị điền khuyết và chuẩn hóa đặc trưng chỉ được học (fit) trên tập Train và áp dụng (transform) sang tập Test.

---

#### 4. TRẦN HỒNG LĨNH (MSSV: 24520970)
**Nhiệm vụ:** Minh họa luồng nạp dữ liệu thô và hàm tiền xử lý trong Notebook Kaggle, bảo toàn kết quả Baseline.

* **Công việc cụ thể:**
  1. **Cập nhật Notebook `Lab3_DS317_Nhom03_Code.ipynb`:**
     - Bổ sung 1-2 cell đầu tiên: Minh họa việc đọc mẫu bản tin AIS thô (18 cột gốc), in ra các dòng chứa giá trị khuyết thiếu thân vỏ và vận tốc $SOG = 0$.
     - Minh họa hàm tiền xử lý dữ liệu thô: Lọc dải vận tốc, loại bỏ status neo đậu và gọi hàm điền khuyết Domain Imputation trước khi nạp dữ liệu vào mô hình.
  2. **Mục 7.5 (Phương pháp khai phá dữ liệu dự kiến):**
     - Giữ nguyên công thức và lý giải toán học của hàm mất mát tùy biến Custom Asymmetric Loss (đạo hàm Gradient bậc 1 và Hessian bậc 2).
     - Giữ nguyên kết quả kiểm chứng mô hình cơ sở Ridge Regression Baseline trên tập Test Q4 (MAE = 15.71h, giảm 41.95% so với Dummy 27.07h).

---

#### 5. ĐỖ VĂN LỘC (MSSV: 24520977)
**Nhiệm vụ:** Đồng bộ hóa quy mô dữ liệu thô trong Mục 1 (Bối cảnh) và Mục 2 (Mục tiêu đề tài).

* **Công việc cụ thể:**
  1. **Mục 1 (Bối cảnh và lý do chọn đề tài):**
     - Nhấn mạnh: Dữ liệu AIS thu thập từ trạm bờ USCG trong thực tế luôn ở dạng thô với tần suất phát 2-10 giây/lần, chứa đựng lượng lớn nhiễu sóng và thông tin gián đoạn. Do đó, doanh nghiệp khai thác cảng cần một giải pháp khai phá dữ liệu tự động từ khâu làm sạch đến khâu dự báo.
  2. **Bảng 2.1 (Mục tiêu SMART):**
     - Mục tiêu 1: *Khai thác thành công bộ dữ liệu lớn NOAA AIS 2025 với quy mô 320,776,922 bản ghi thô (62.4 GB uncompressed), xây dựng pipeline tiền xử lý tinh chế thu được 80,660,588 bản ghi chất lượng cao phục vụ dự báo*.

---

#### 6. NGUYỄN HỮU BẢO LỘC (MSSV: 24520983)
**Nhiệm vụ:** Bổ sung luận cứ đối sánh SOTA trên bộ dữ liệu lớn thô tại Mục 4.

* **Công việc cụ thể:**
  1. **Mục 4.3 (Khoảng trống nghiên cứu & Luận cứ đề tài):**
     - Bổ sung nhận định so sánh: *Trong 5 nghiên cứu SOTA đã khảo sát (El Mekkaoui 2023, Abdi 2024, Wang 2025, Saber 2025), đa số các tác giả thực nghiệm trên các bộ dữ liệu nhỏ hoặc dữ liệu đã qua tiền xử lý/giả lập nhân tạo. Đề tài của nhóm đối mặt trực tiếp với thách thức xử lý dữ liệu thô quy mô lớn 320 triệu bản ghi của toàn bộ bờ biển Hoa Kỳ, phản ánh trọn vẹn sự phức tạp của vận tải hàng hải thực tế*.
  2. **Mục 13 (Tài liệu tham khảo):** Đảm bảo giữ chuẩn trích dẫn IEEE và tệp `references.bib`.

---

#### 7. VÕ ĐÌNH KIÊN (MSSV: 24520893 - NHÓM TRƯỞNG)
**Nhiệm vụ:** Cập nhật phân tích rủi ro Big Data dữ liệu thô Mục 12, thiết kế Slides và tổng duyệt toàn bộ hồ sơ.

* **Công việc cụ thể:**
  1. **Mục 12 (Rủi ro kỹ thuật và phương án dự phòng):**
     - Rủi ro 1: Nhấn mạnh rủi ro tràn bộ nhớ RAM và quá tải đĩa khi xử lý 320.78 triệu dòng thô (62.4 GB). Biện pháp: Đã giải quyết thành công bằng kiến trúc Self-Checkpoint Engine kết hợp dọn dẹp đĩa lũy tiến (Progressive Disk Cleanup), duy trì RAM < 4 GB và đĩa < 10 GB trong suốt quá trình chạy.
  2. **Bộ Slides thuyết trình Buổi 6 (`Slides.pptx` & `.pdf`):**
     - Cập nhật sơ đồ luồng dữ liệu 4 tầng: *Dữ liệu thô (320M) $\rightarrow$ Pipeline tiền xử lý $\rightarrow$ Dữ liệu sạch (80M) $\rightarrow$ Mô hình dự báo ATA*.
  3. **Tổng duyệt và kiểm tra đối chuẩn chéo 100%:**
     - Kiểm tra sự nhất quán giữa Báo cáo Word, File Excel kiểm kê, Slides và Code Kaggle. Đảm bảo toàn văn bản sử dụng dấu gạch ngang tiêu chuẩn `-` (ASCII 45).

---

### VI. QUY CHUẨN KỸ THUẬT VÀ LƯU Ý BẮT BUỘC KHI LÀM BÀI

1. **Quy chuẩn dấu gạch ngang:**
   - **BẮT BUỘC sử dụng duy nhất dấu gạch ngang tiêu chuẩn `-` (hyphen-minus, mã phím ASCII 45)**.
   - **TUYỆT ĐỐI KHÔNG** dùng dấu gạch ngang dài en-dash (`-`) hoặc em-dash (`-`).
2. **Nguyên tắc "Một nguồn sự thật" (Single Source of Truth):**
   - 100% các con số báo cáo bắt buộc phải sao chép chính xác từ **Bảng II (Bảng số liệu đối chuẩn dùng chung)** của tài liệu này. Không tự làm tròn sai lệch.
3. **Phối hợp làm việc trên file gốc:**
   - Các thành viên soạn thảo trực tiếp vào file: `d:\Workspace\DS317 Khai phá dữ liệu trong doanh nghiệp\Luu_tru_goc\Nội dung gốc thuyết minh đề tài.docx`.
   - Đúng **21:00 ngày 19/10/2026**, toàn bộ các mục phải được hoàn tất để Nhóm trưởng tiến hành tổng duyệt và xuất bản báo cáo chính thức.
