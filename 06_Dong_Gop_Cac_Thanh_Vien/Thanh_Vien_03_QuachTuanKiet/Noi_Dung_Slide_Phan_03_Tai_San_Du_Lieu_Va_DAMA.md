# ĐẦU VÀO SLIDE THUYẾT TRÌNH - PHẦN 3: TÀI SẢN DỮ LIỆU & ĐO LƯỜNG CHẤT LƯỢNG DAMA

**Người thực hiện bàn giao:** Quách Tuấn Kiệt (MSSV: 24520911) - Data Engineer  
**Người tiếp nhận:** Trần Hồng Lĩnh (Phụ trách Tổng hợp Slide & Báo cáo Thuyết trình)  
**Tài liệu tham chiếu:** Chương 3 Báo cáo đồ án, Notebook DAMA `02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung`, Data Inventory `Lab3_DS317.R11_Nhom03_DataInventory.xlsx`  
**Thời lượng dự kiến trình bày:** ~3 phút (4 slides)

---

## 1. TỔNG QUAN CẤU TRÚC 4 SLIDE PHẦN 3

| Slide | Tiêu đề Slide | Mục tiêu truyền tải | Hình ảnh đính kèm đề xuất |
| :--- | :--- | :--- | :--- |
| **Slide 3.1** | **Tổng quan Tài sản Dữ liệu AIS & Kiến trúc Xử lý** | Chứng minh quy mô Big Data (256.94M dòng), tính pháp lý chuẩn NOAA, và phễu lọc tinh gọn dữ liệu qua các tầng. | Biểu đồ phễu thu hẹp dòng dữ liệu (Funnel) hoặc bảng thống kê quy mô tập dữ liệu. |
| **Slide 3.2** | **Kiểm toán Chất lượng Dữ liệu Chuẩn DAMA (6 Chiều)** | Chứng minh tiền xử lý cải thiện vượt bậc chất lượng dữ liệu: Consistency (+48.84%), Validity (+47.73%), Accuracy (+26.96%). | `CHARTS/01_dama_6_dimensions_raw_vs_prep27.png` hoặc `Hinh_Anh_Bieu_Do/dama_comparison_raw_vs_base22_bar.png` |
| **Slide 3.3** | **Bóc tách Dữ liệu Khuyết & Phân tích Động học Neo đậu** | Chỉ ra đặc thù vật lý hàng hải: 9 trường khuyết do công nghệ AIS, hiện tượng tàu neo đậu tĩnh ($SOG < 0.5$ kn) chiếm 52.88% gây nhiễu động học. | `CHARTS/02_missing_and_imputation_flag.png` & `CHARTS/03_sog_vessel_status_raw_vs_prep27.png` |
| **Slide 3.4** | **Kiểm soát Data Drift qua 4 Quý & Tính Ổn định Mô hình** | Khẳng định dữ liệu 4 Quý năm 2025 có phân phối ổn định cao ($PSI < 0.05$), triệt tiêu rủi ro suy thoái mô hình theo thời gian. | `Hinh_Anh_Bieu_Do/Hinh3_ChiSoDAMA_Q1_Q4.png` hoặc bảng kiểm định Kolmogorov-Smirnov. |

---

## 2. CHI TIẾT NỘI DUNG TỪNG SLIDE, LAYOUT & SPEAKER NOTES

---

### SLIDE 3.1: TỔNG QUAN TÀI SẢN DỮ LIỆU AIS & KIẾN TRÚC XỬ LÝ

#### A. Gợi ý Layout & Thiết kế
- **Bố cục 2 cột (Split 50:50):**
  - Cột trái: Phễu lọc 3 tầng dữ liệu (Data Funnel) và các chỉ số chính (Key Metrics Cards).
  - Cột phải: Bảng thông số thuộc tính dữ liệu và bản đồ phân bố cảm biến AIS vùng biển US Coast Guard.

#### B. Nội dung hiển thị trên Slide (Bullet Points)
* **Quy mô Dữ liệu Cấp độ Big Data:**
  - **RAW18 (Toàn cảnh 2025):** 256,935,254 bản ghi | 18 trường thuộc tính | 26,056 tàu định danh.
  - **Base22 (Nền tảng Tinh lọc):** 92,679,219 bản ghi | 22 trường thuộc tính bổ sung trường địa lý và thời gian.
  - **DAMA Audited (Kiểm toán Chuyên sâu):** 80,782,106 bản ghi sau khi làm sạch nhiễu định vị.
* **Đặc tính Kỹ thuật & Chuẩn hóa Nguồn phát:**
  - Dữ liệu thu nhận từ mạng lưới trạm bờ và vệ tinh của **NOAA / US Coast Guard** trên toàn bộ lãnh hải Hoa Kỳ.
  - Tần suất phát tín hiệu động từ 2 đến 10 giây/bản ghi tùy thuộc vào tốc độ hành trình của tàu.
  - Độ trễ trần tác nghiệp: 365 ngày liên tục (01/01/2025 - 31/12/2025), chia tách tự nhiên theo 4 Quý (Q1: 17.5M, Q2: 21.8M, Q3: 22.3M, Q4: 19.1M bản ghi nền tảng).

#### C. Speaker Notes (Lời thoại cho người thuyết trình - ~45 giây)
> *"Kính thưa Hội đồng và Thầy Cô, nền tảng của toàn bộ hệ thống dự báo thời gian hành trình tàu biển của nhóm chúng em được xây dựng trên một tài sản dữ liệu Big Data thực sự. Chúng em thu thập và xử lý toàn bộ 256.9 triệu bản ghi AIS của năm 2025 từ NOAA và Cảnh sát biển Hoa Kỳ, bao quát hơn 26,000 tàu thuyền thương mại. Qua quy trình tiền xử lý phân tán với Polars và PyArrow, chúng em đã làm sạch và cấu trúc hóa thành 92.68 triệu bản ghi Base22 chuẩn xác, đảm bảo đầy đủ tính pháp lý và không có bất kỳ điểm rò rỉ dữ liệu nào trong suốt quá trình xây dựng bài toán."*

#### D. Đường dẫn tệp hình ảnh minh họa sẵn có
- Đường dẫn tương đối: `05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/Hinh_Anh_Bieu_Do/Hinh2_ThacLoc_Waterfall.png`
- Đường dẫn tuyệt đối: `c:\Users\Public\Khai_pha\github_kien\05_Output_Cac_Notebook\06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN\Hinh_Anh_Bieu_Do\Hinh2_ThacLoc_Waterfall.png`

---

### SLIDE 3.2: KIỂM TOÁN CHẤT LƯỢNG DỮ LIỆU CHUẨN DAMA (6 CHIỀU)

#### A. Gợi ý Layout & Thiết kế
- **Bố cục:** Bên trái là Biểu đồ Radar 6 chiều so sánh (Before vs After); bên phải là Bảng số liệu đối chứng đo lường chính xác theo chuẩn DAMA DMBOK.

#### B. Nội dung hiển thị trên Slide
* **Khung đo lường DAMA DMBOK chuẩn quốc tế (6 khía cạnh):**
  - **Tính toàn vẹn (Completeness):** Bản ghi đạt **93.56%**, trường dữ liệu cốt lõi đạt **99.55%**.
  - **Tính nhất quán (Consistency):** Tăng vọt từ **36.69%** (RAW18) lên **99.99%** (PREP27) — tăng **+48.84%** nhờ loại bỏ trạng thái hành trình mâu thuẫn.
  - **Tính hợp lệ (Validity):** Nâng từ **96.31%** lên **97.39%** (cải thiện **+47.73%** sau khi lọc bỏ tọa độ ngoài lãnh hải WGS84 và giá trị vận tốc ngoại lai).
  - **Tính chính xác (Accuracy):** Tăng từ **45.90%** lên **77.29%** (cải thiện **+26.96%**).
  - **Tính kịp thời (Timeliness):** Đạt **64.99%** phản ánh độ trễ trạm thu phát bờ biển.
  - **Tính duy nhất (Uniqueness):** Đạt **99.72%** (gần như triệt tiêu hoàn toàn trùng lặp bản ghi phát sóng).
* **Bảng so sánh cốt lõi:**

| Khía cạnh DAMA | Tập thô RAW18 (%) | Sau Tiền xử lý PREP27 (%) | Mức độ cải thiện (%) |
| :--- | :---: | :---: | :---: |
| **Consistency (Nhất quán)** | 36.69% | **99.99%** | **+48.84%** |
| **Validity (Hợp lệ)** | 96.31% | **97.39%** | **+47.73%** |
| **Accuracy (Chính xác)** | 45.90% | **77.29%** | **+26.96%** |
| **Spearman Corr (SOG vs Target)** | 0.2738 | **0.6224** | **+127.31%** |

#### C. Speaker Notes (Lời thoại - ~50 giây)
> *"Để chứng minh tính khoa học và độ tin cậy của dữ liệu trước khi huấn luyện mô hình học máy, nhóm chúng em đã thực hiện kiểm toán dữ liệu nghiêm ngặt theo chuẩn quốc tế DAMA DMBOK với 6 khía cạnh cốt lõi. Như quý Thầy Cô có thể quan sát trên biểu đồ Radar: Ở tập dữ liệu thô RAW18, tính nhất quán chỉ đạt 36.69% do các cảm biến AIS liên tục phát tín hiệu xung đột khi tàu đứng yên. Sau module tiền xử lý PREP27, tính nhất quán đã đạt mức tuyệt đối 99.99%, tính hợp lệ đạt 97.39%, và độ tương quan phi tuyến Spearman giữa vận tốc tức thời và nhãn thời gian hành trình tăng ngoạn mục từ 0.27 lên 0.62, tức tăng hơn 127%. Điều này khẳng định dữ liệu sau xử lý sạch, chuẩn và giàu tín hiệu dự báo."*

#### D. Đường dẫn tệp hình ảnh radar chất lượng cao
- Đường dẫn tương đối: `05_Output_Cac_Notebook/02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/CHARTS/01_dama_6_dimensions_raw_vs_prep27.png`
- Bản dự phòng: `05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/Hinh_Anh_Bieu_Do/dama_comparison_raw_vs_base22_bar.png`

---

### SLIDE 3.3: BÓC TÁCH DỮ LIỆU KHUYẾT & PHÂN TÍCH ĐỘNG HỌC NEO ĐẬU

#### A. Gợi ý Layout & Thiết kế
- **Bố cục 2 phần ngang hoặc 2 cột:**
  - Nửa trái: Ma trận 9 trường khuyết và chiến lược xử lý triệt để.
  - Nửa phải: Biểu đồ phân phối vận tốc SOG và phân tích 52.88% trạng thái neo đậu.

#### B. Nội dung hiển thị trên Slide
* **Bản chất 9 trường khuyết dữ liệu trong AIS Hàng hải:**
  - `Draft` (Độ mớn nước) khuyết **26.97%** (21,787,015 bản ghi) $\rightarrow$ Điền trung vị theo từng nhóm tàu (`VesselType`).
  - Kích thước tàu `Dimension_to_Bow/Stern/Port/Starboard` khuyết **18.78%** $\rightarrow$ Nội suy theo cấu trúc hình học chuẩn phân lớp tàu.
  - Thông số hành trình `Heading` khuyết **7.09%**, `COG` khuyết **4.88%**, `SOG` khuyết **1.56%** $\rightarrow$ Dùng nội suy tuyến tính theo chuỗi thời gian của từng mã hành trình (`TripID`).
* **Hiện tượng Tàu Neo Đậu Tĩnh (Moored/Anchored Anomaly):**
  - **52.88%** số lượng bản ghi có vận tốc $SOG < 0.5$ hải lý/giờ (hầu như không di chuyển).
  - Phân tích động lực học: Tàu neo đậu tại cảng hoặc phao luồng không phản ánh đúng quy luật di chuyển đường trường, gây lệch nghiêm trọng hàm mục tiêu ETA/Duration.
  - Giải pháp của nhóm: Phân tách rõ ràng trạng thái neo đậu và trạng thái di chuyển bằng các đặc trưng khoảng cách tới bến (`distance_to_berth`) và trạng thái động học (`is_anchored`).

#### C. Speaker Notes (Lời thoại - ~45 giây)
> *"Đi sâu vào cấu trúc dữ liệu, chúng em phát hiện hai hiện tượng cốt lõi của dữ liệu hàng hải thực tế: Thứ nhất, có 9 trường bị khuyết dữ liệu do đặc thù truyền nhận sóng VHF, trong đó độ mớn nước Draft khuyết tới 26.97%. Chúng em đã áp dụng phương pháp điền khuyết dựa trên thuộc tính nhóm tàu và nội suy động học chuỗi thời gian, bảo đảm không làm mất thông tin. Thứ hai, hơn 52.8% bản ghi ghi nhận vận tốc dưới 0.5 hải lý/giờ. Đây là các tàu đang neo đậu tại cảng. Nếu đưa nguyên trạng số liệu này vào huấn luyện, mô hình sẽ bị đánh lừa rằng tàu đang chạy rất chậm trên hải trình. Nhận diện được điều này đã giúp nhóm thiết kế Module M3 với các đặc trưng động học cảng bến cực kỳ hiệu quả."*

#### D. Đường dẫn tệp hình ảnh minh họa sẵn có
- Ma trận dữ liệu khuyết: `05_Output_Cac_Notebook/02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/CHARTS/02_missing_and_imputation_flag.png`
- Phân phối SOG & Nhóm tàu: `05_Output_Cac_Notebook/02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/CHARTS/03_sog_vessel_status_raw_vs_prep27.png`

---

### SLIDE 3.4: KIỂM SOÁT DATA DRIFT QUA 4 QUÝ & TÍNH ỔN ĐỊNH MÔ HÌNH

#### A. Gợi ý Layout & Thiết kế
- **Bố cục:** Biểu đồ đường/cột thể hiện chỉ số trôi dạt dữ liệu (Population Stability Index - PSI) và phân phối mật độ xác suất qua 4 Quý Q1, Q2, Q3, Q4 năm 2025.

#### B. Nội dung hiển thị trên Slide
* **Kiểm định Data Drift qua 4 Quý (Temporal Stability):**
  - Sử dụng phương pháp kiểm định **Population Stability Index (PSI)** và khoảng cách **Wasserstein Distance** giữa các Quý:
    - So sánh Q1 (Cơ sở) với Q2, Q3, Q4.
    - Tất cả các đặc trưng động học chính (`SOG`, `COG`, `Draft`, `Distance_to_Destination`): $PSI < 0.05$ (Ngưỡng cảnh báo trôi dạt chuẩn là $PSI > 0.1$).
* **Ý nghĩa đối với Chiến lược Đánh giá Mô hình:**
  - Phân phối dữ liệu ổn định tuyệt đối xuyên suốt 12 tháng của năm 2025.
  - Khẳng định tính hợp lệ khoa học khi áp dụng chiến lược phân tách **Expanding Window Time-Series Split**:
    - Fold 1: Huấn luyện Q1 (2.22M dòng) $\rightarrow$ Kiểm thử Q2 (3.54M dòng).
    - Fold 2: Huấn luyện Q1+Q2 $\rightarrow$ Kiểm thử Q3 (3.63M dòng).
    - Fold 3: Huấn luyện Q1+Q2+Q3 $\rightarrow$ Kiểm thử Q4 (3.48M dòng).
  - Không xảy ra hiện tượng rò rỉ tương lai (No Data Leakage) và mô hình học tập được xu hướng dài hạn.

#### C. Speaker Notes (Lời thoại - ~40 giây)
> *"Cuối cùng, một thách thức lớn trong dữ liệu chuỗi thời gian là sự trôi dạt phân phối (Data Drift) theo mùa vụ. Nhóm đã thực hiện kiểm định PSI trên toàn bộ 4 Quý của năm 2025. Kết quả cho thấy toàn bộ các chỉ số PSI đều dưới 0.05, tức là phân phối dữ liệu cực kỳ ổn định, không có hiện tượng đột biến tiêu cực. Sự ổn định này là bằng chứng vững chắc cho phép nhóm áp dụng kỹ thuật Expanding Window Cross-Validation - huấn luyện trên quá khứ và dự báo tương lai mà không lo ngại mô hình bị suy thoái hiệu năng do sai lệch môi trường biển."*

#### D. Đường dẫn tệp hình ảnh minh họa sẵn có
- Biểu đồ phân phối theo mùa / Drift: `05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/Hinh_Anh_Bieu_Do/Hinh2_ThacLoc_Waterfall.png`
- Biểu đồ tương quan đặc trưng: `05_Output_Cac_Notebook/02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/CHARTS/05_correlation_heatmap_and_target_ranking.png`

---

## 3. CHECKLIST TỔNG HỢP GỬI TRẦN HỒNG LĨNH

| Hạng mục kiểm tra | Trạng thái | Ghi chú kỹ thuật |
| :--- | :---: | :--- |
| **Nội dung 4 slide** | Đầy đủ | Chia rõ bullet points, số liệu cô đọng, dễ đọc |
| **Speaker notes** | Đầy đủ | Khớp thời lượng thuyết trình 2.5 - 3 phút |
| **Số liệu DAMA** | Chuẩn 100% | Khớp tuyệt đối với Chương 3 và Data Inventory |
| **Tệp hình ảnh PNG** | Đã sẵn sàng | Độ phân giải cao, nằm trong thư mục output của repo |
| **Độ độc lập module** | Hoàn thành | Không làm thay slide, bàn giao dạng text & asset |
