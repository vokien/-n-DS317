# Kế Hoạch Hoàn Thiện và Phân Công Công Việc Cuối Kỳ - Nhóm 03 (DS317.R11)

- **Học phần:** DS317 - Khai phá dữ liệu trong doanh nghiệp (UIT - ĐHQG-HCM)
- **Đề tài:** Dự báo thời điểm cập cảng của tàu biển thay thế ETA tự khai báo (*Prediction of Vessel Port Arrival Time Replacing Self-Reported ETA*)
- **Kho lưu trữ chuẩn:** `DS317_DoAn_Nhom03_TongHop/` | **Thư mục nộp bài chuẩn 8 phần:** [`DS317_R11_Nhom03_HoSoNopDoAn/`](../DS317_R11_Nhom03_HoSoNopDoAn/README.md)
- **Kho output tập trung các notebook:** [`05_Output_Cac_Notebook/`](../05_Output_Cac_Notebook/README.md)
- **Khu vực không gian làm việc của 7 thành viên:** [`06_Dong_Gop_Cac_Thanh_Vien/`](../06_Dong_Gop_Cac_Thanh_Vien/README.md)

---

## PHẦN A: CÁC NỘI DUNG VÀ TIÊU CHÍ TRỌNG TÂM CẦN HOÀN THIỆN

### 1. Bảng theo dõi tiến độ các sản phẩm bàn giao bắt buộc (Chiếm 100% điểm A4)

|  STT  | Hạng mục bắt buộc (theo quy định môn học)                                                                                                                                                                                      | Tỷ trọng / Vai trò                        | Thư mục đích                  | Trạng thái hiện tại                                                                                  | Người phụ trách chính                                                                            |
| :---: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------- | :---------------------------- | :--------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
|   1   | **Chương trình Demo Web/App tương tác (`app.py`)** (kết nối trọng số thật, tích hợp BI Dashboard & dự báo ETA)                                                                                                                 | **50%** điểm sản phẩm A4                  | `03_SourceCode/` & `07_Demo/` | **Đang xây dựng** (Đã có sẵn trọng số mô hình và số liệu DAMA để tích hợp)                           | **Đỗ Văn Lộc**                                                                                   |
|   2   | **Báo cáo Đồ án Cuối kỳ 7 Chương** (`.docx` & `.pdf`, 30-50 trang)                                                                                                                                                             | **30%** điểm sản phẩm A4                  | `01_BaoCao/`                  | **Đang triển khai viết** (Đã có đầy đủ số liệu thực nghiệm Engine v2 và phân công chi tiết 7 chương) | **Cả nhóm** (Võ Đình Kiên chủ trì)                                                               |
|   3   | **Bộ Slide Bảo vệ Cuối kỳ 10 phần** (`.pptx` & `.pdf`)                                                                                                                                                                         | **20%** điểm sản phẩm A4                  | `02_Slides/`                  | **Đang triển khai thiết kế** (Đã chốt bố cục 10 phần chuẩn môn học)                                  | **Trần Hồng Lĩnh** chủ trì toàn bộ (Cả nhóm cung cấp nội dung theo phân công)                    |
|   4   | **Bộ dữ liệu mẫu chạy Demo & `requirements.txt`** (1,000-5,000 dòng có phân bổ đại diện đủ 3 nhóm chân trời thời gian `< 24h`, `24h - 72h`, `72h - 168h` trong mốc <= 168h, đầy đủ 27 đặc trưng + RTMA, kèm hướng dẫn tái lập) | Điều kiện nghiệm thu Demo & chấm mã nguồn | `04_Data/` & `03_SourceCode/` | **Đang hoàn thiện** (Đã có schema và tệp tiền xử lý mẫu để trích xuất)                               | **Quách Tuấn Kiệt** (Data mẫu & Tái lập code) & **Võ Đình Kiên** (`requirements.txt` & Đóng gói) |

---

### 2. Nhóm tiêu chí Kỹ thuật, Biểu đồ & Học thuật chuyên sâu (Sẵn sàng triển khai từ dữ liệu có sẵn)

1. **Kiểm định ý nghĩa thống kê chính thức (Statistical Significance Testing) & Phân rã Thống kê 3 Nhóm Chân trời:**
   - **Hiện trạng:** Đã có số liệu chi tiết qua 3 Fold của 7 mô hình và 13 biến thể trong `05_Output_Cac_Notebook/07_Runner_Song_Song_1_Baseline_M1_M2_M3/results/` và `08_Runner_Song_Song_2_M4_M5_M6_M7/results/`.
   - **Yêu cầu hoàn thiện:** Thực hiện kiểm định `Wilcoxon signed-rank test`, `Diebold-Mariano test` hoặc `Paired Bootstrap` (2,000 lần lặp) kèm tính toán giá trị `p-value` so sánh giữa Baseline B0 và các mô hình tốt nhất (CatBoost, XGBoost, LightGBM, M6 Asymmetric, M7 Conformal). Đồng thời, tính toán kiểm định thống kê và xây dựng Bảng quy đổi giá trị kinh tế / Business ROI cảng biển phân rã chi tiết theo 3 nhóm chân trời thời gian (`< 24h`, `24h - 72h`, `72h - 168h`). Phụ trách: **Lê Sỹ Liêm** (độc lập phụ trách toàn bộ).
2. **Biểu đồ Chương 4 & Chương 5 chuẩn Engine v2 (`DPI >= 300`) Phân rã theo 3 Nhóm Chân trời:**
   - **Hiện trạng:** Thư mục `06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/Hinh_Anh_Bieu_Do/` và `02_DS317_02.../CHARTS/` đã có 30 biểu đồ chuẩn cho EDA và BTVN.
   - **Yêu cầu hoàn thiện:** Thiết kế bổ sung các biểu đồ Engine v2 cho Chương 4 và Chương 5: sơ đồ kiến trúc Engine v2 tích hợp BI Dashboard, biểu đồ so sánh 7 mô hình theo phân tầng (`All`, `LE_168h`, `GT_168h`), biểu đồ Delta Ablation `M1-M7`. Đặc biệt, thiết kế biểu đồ phân bố sai số (Residual / Error Distribution) và sai số tuyệt đối trung bình MAE theo 3 nhóm thời gian (`< 24h`, `24h - 72h`, `72h - 168h`) cho Chương 5; cung cấp toàn bộ biểu đồ chất lượng cao cho Trần Hồng Lĩnh dựng slide. Phụ trách: **Huỳnh Chí Kiên**.
3. **Giải thích mô hình chuyên sâu bằng SHAP (`SHAP Summary Plot` & `SHAP Beeswarm Plot`):**
   - **Hiện trạng:** Đã có đầy đủ trọng số mô hình trong gói `runner1_saved_models.zip` và `runner2_saved_models.zip` (hoặc giải nén trong `05_Model/`).
   - **Yêu cầu hoàn thiện:** Nạp mô hình tốt nhất (CatBoost/XGBoost/LightGBM) cùng bộ dữ liệu kiểm thử để trích xuất SHAP values, vẽ `SHAP Summary Plot` và `SHAP Beeswarm Plot` giải thích mức độ ảnh hưởng của `Dist_To_Berth_NM`, `sog`, các biến tương tác M3 và thời tiết RTMA M4. Phụ trách: **Huỳnh Chí Kiên**.
4. **Phân tích lỗi Case Study có kiểm chứng theo 3 Nhóm Chân trời Nghiệp vụ Hàng hải (Error Analysis):**
   - **Hiện trạng:** Đã có bảng số liệu đánh giá chi tiết theo từng chuyến đi và phân tầng thời gian.
   - **Yêu cầu hoàn thiện:** Trích xuất các trường hợp tàu biển thật (kèm định danh `MMSI`, loại tàu, vận tốc `sog`, khoảng cách `Dist_To_Berth_NM`) có sai số residual lớn nhất ở cả 2 tầng `<= 168h` và `> 168h` từ `detailed_predictions/*.parquet`. Thực hiện phân tích lỗi dạng Case Study chi tiết theo 3 nhóm thời gian trong mốc chân trời <= 168h (`LE_168h`), giải thích cơ chế sai số khi tàu từ ngoài khơi tiến dần vào gần cảng:
     * **Nhóm Siêu ngắn hạn / Cận cảng (`< 24h` / Dưới 1 ngày):** Giai đoạn tàu tiếp cận luồng hoa tiêu, phao số 0, vùng neo đậu chờ bến. Ý nghĩa nghiệp vụ: Bố trí hoa tiêu hàng hải, tàu lai dắt (tugboat), cầu bến cập tức thời, rà soát xung đột an toàn luồng lạch.
     * **Nhóm Ngắn hạn / Duyên hải (`24h - 72h` / 1 đến 3 ngày):** Giai đoạn tàu chạy ven bờ, tiếp cận vùng nước cảng. Ý nghĩa nghiệp vụ: Lập kế hoạch giải phóng bãi container bốc dỡ, điều động nhân công cẩu giàn STS, xếp dỡ sà lan và xe trung chuyển nội địa.
     * **Nhóm Trung hạn / Ngoài khơi (`72h - 168h` / 3 đến 7 ngày):** Giai đoạn tàu hành trình ngoài biển mở, chịu ảnh hưởng thời tiết/sóng gió hải lưu RTMA. Ý nghĩa nghiệp vụ: Kế hoạch tổng thể tiếp nhận tàu mẹ của cảng, tối ưu hóa khung giờ cập bến (berth window), giảm chi phí phạt lưu tàu (demurrage).
       Viết tài liệu **Giải thích phân tầng 168h khoa học** thay thế bản cũ đã xóa. Phụ trách: **Trần Hồng Lĩnh**.
5. **Quy đổi Tài chính USD / Business ROI và Đánh giá Mất mát Bất đối xứng (M6/M7):**
   - **Hiện trạng:** Đã có kết quả thực nghiệm M6 Asymmetric Loss (`m6_asym_*`) và M7 Conformal Prediction (`m7_conformal_*`).
   - **Yêu cầu hoàn thiện:** Xây dựng bảng quy đổi tài chính thực tế cho doanh nghiệp cảng biển phân rã theo 3 nhóm chân trời thời gian: tham chiếu đơn giá nhân công bốc xếp ILWU (56.85 USD/giờ), chi phí thuê tàu theo ngày (15,800 - 90,500 USD/ngày), định lượng khoản tiết kiệm USD khi giảm tỷ lệ dự báo sớm (`Underprediction_pct`) từ M6 và độ tin cậy từ khoảng dự báo M7 Conformal (`PICP_90` vs `MPIW`).
   - **Phân định rõ ràng trách nhiệm:** **Lê Sỹ Liêm** độc lập phụ trách toàn bộ mô hình kinh tế / Bảng quy đổi tài chính USD / Business ROI cảng biển và Module M7 Conformal Prediction; **Trần Hồng Lĩnh** chỉ viết phần thực nghiệm Module M6 Asymmetric Loss (đã giảm tải cho Hồng Lĩnh).
6. **Tuân thủ Pháp lý & Đạo đức AI:**
   - **Yêu cầu hoàn thiện:** Rà soát và hoàn thiện tài liệu tuân thủ **Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15**, **Luật Dữ liệu 60/2024/QH15**, cơ chế ẩn danh `MMSI` -> `Vessel_Hash_ID`, và soạn thảo bản **Khai báo sử dụng AI** minh bạch theo chuẩn liêm chính học thuật kèm danh mục trích dẫn IEEE `references.bib`. Phụ trách: **Nguyễn Hữu Bảo Lộc**.
7. **Hồ sơ Quản lý Nhóm cuối kỳ (`08_QuanLyNhom/`):**
   - **Yêu cầu hoàn thiện:** Hoàn thiện Nhật ký thực nghiệm tổng hợp, Scope Changelog (lý giải điều chỉnh từ Engine v1 sang Engine v2), tập hợp Biên bản họp nhóm giai đoạn sau Lab 3 và Bảng tự đánh giá đóng góp % của 7 thành viên. Phụ trách: **Đỗ Văn Lộc**.

---

## PHẦN B: PHÂN TÍCH BẢN CHẤT KHOA HỌC & KỸ THUẬT VỀ SỰ KHÁC BIỆT SAI SỐ (LAB 3: 15.79h vs. ENGINE V2: 21.64h - 24.94h)

Một câu hỏi cốt lõi thường được đặt ra trong các buổi phản biện trước Hội đồng Đồ án:

> *"Tại sao ở Lab 3 mô hình cơ sở Ridge Regression đạt MAE 15.79h, nhưng khi nâng cấp mô hình toàn diện lên Engine v2 với các thuật toán SOTA (CatBoost, LightGBM, XGBoost, ST-GNN, PatchTST) thì sai số phân tầng cốt lõi lại ghi nhận ở mức 21.64h - 24.94h?"*

Các thành viên nhóm cần nắm vững 4 nguyên nhân khoa học và kỹ thuật nền tảng sau đây để giải thích mạch lạc, tự tin và thuyết phục:

```
+---------------------------------------------------------------------------------------------------------+
|                  BẢN CHẤT SỰ THAY ĐỔI HỆ QUY CHIẾU THỰC NGHIỆM (PARADIGM SHIFT)                         |
+---------------------------------------------------------------------------------------------------------+
|   LAB 3 (Thuyết minh ban đầu)                   |   ENGINE V2 (Hệ thống thực nghiệm chuẩn hóa)          |
|   - Chia ngẫu nhiên / Cửa sổ hẹp                |   - Out-of-Time Walk-Forward 3 Folds                  |
|   - Dữ liệu bị cắt cúp: Target <= 168h          |   - Toàn dải hành trình liên tục (Full Voyage)        |
|   - Dummy MAE = 27.23h (Mẫu nhỏ, gần bờ)        |   - Dummy MAE All = 129.20h - 156.47h                 |
|   - MAE 15.79h chiếm > 58% dải mục tiêu         |   - Phân tầng LE_168h MAE = 21.64h - 24.94h (~13%)    |
|   - Tồn tại rò rỉ dữ liệu (Temporal Leakage)    |   - Triệt tiêu 100% rò rỉ dữ liệu (Zero Leakage)      |
|   - Tối ưu L2 MSE đối xứng thông thường         |   - Tối ưu Custom Asymmetric Loss (Phạt sớm w=2.5)    |
+---------------------------------------------------------------------------------------------------------+
```

### 1. Chiến lược phân chia dữ liệu (Data Splitting Protocol) & Triệt tiêu Rò rỉ Chuỗi Thời gian (Data Leakage)

- **Ở Lab 3:** Dữ liệu thử nghiệm ban đầu vô tình chịu ảnh hưởng của hiện tượng **Rò rỉ Chuỗi Thời gian (Temporal Data Leakage)**: Cùng một định danh tàu (`mmsi`) hoặc cùng một chuyến hải trình (`trip_id`) xuất hiện đan xen ở cả tập Train và Test. Với tần suất phát tín hiệu AIS dày đặc (2-10 giây/bản tin), khi mô hình học thấy vị trí tàu lúc 10:00 ở tập Train, mô hình chỉ cần "nội suy" hoặc ghi nhớ quỹ đạo là có thể đoán chính xác thời điểm cập cảng lúc 10:05 ở tập Test. Kết quả là mốc `MAE = 15.79h` mang tính **"lạc quan ảo" (over-optimistic)**, không phản ánh năng lực khái quát hóa thực tế.
- **Ở Engine v2:** Nhóm thiết lập giao thức **Out-of-Time Time-based Walk-Forward Expanding Window 3 Folds** nghiêm ngặt nhất (Fold 1: Train Q1 -> Test Q2; Fold 2: Train Q1-Q2 -> Test Q3; Fold 3: Train Q1-Q3 -> Blind Test Q4). Toàn bộ các chuyến tàu vượt biên quý (`TRAIN_CROSSING_EXCLUDED`) đều bị loại bỏ, bảo đảm tính thuần khiết 100% (`TRAIN_PURE`, `TEST_PURE`). Mô hình trong Engine v2 bắt buộc phải suy luận trên những con tàu hoàn toàn mới trong tương lai mà nó chưa từng gặp, triệt tiêu hoàn toàn hiện tượng học vẹt.

### 2. Chân trời dự báo & Hiện tượng Cắt cúp Cửa sổ (Prediction Horizon & Truncation Bias)

- **Ở Lab 3:** Dữ liệu bị gọt giũa và cắt cúp cứng trong cửa sổ ngắn ($0 < \text{Target\_Hours} \le 168\text{h}$), trong đó các bản tin gần bờ và gần luồng hoa tiêu (Pilot Station) với cự ly ngắn chiếm tỷ trọng áp đảo. Bằng chứng rõ nhất là mô hình ngây thơ Dummy Regressor ở Lab 3 chỉ có $MAE = 27.23\text{h}$ (trung vị của tập dữ liệu chỉ quanh 25-30h). Do đó, sai số `15.79h` thực chất chiếm tới hơn **58%** giá trị trung vị của tập dữ liệu đó.
- **Ở Engine v2:** Nhóm giữ nguyên **toàn dải chân trời hành trình liên tục (Full Voyage Horizon)** không cắt cúp nhân tạo, bao gồm cả các hành trình xa khơi vượt đại dương hàng nghìn hải lý (chân trời dự báo lên đến hàng trăm giờ, Dummy MAE toàn cục lên tới `129.20h - 156.47h`). Khi phân tầng đánh giá chuyên biệt trên nhóm $\le 168\text{h}$ (`LE_168h`, chiếm 78.61% tập kiểm thử), các tàu phân bố đều từ 0 đến 168 giờ với cự ly hàng trăm hải lý ngoài biển mở. Mức sai số `21.64h - 24.94h` trên phân tầng này chỉ chiếm **12.8% - 14.8%** chân trời dự báo, phản ánh năng lực dự báo thực chiến và có độ tin cậy vượt trội trong điều độ cầu bến.

### 3. Quy mô dữ liệu, Tính toàn diện & Trôi dạt Phân phối Mùa vụ (Scale & Concept Drift)

- **Ở Lab 3:** Thử nghiệm trên tập mẫu con nhỏ, lọc bớt các điều kiện hành hải phức tạp.
- **Ở Engine v2:** Xử lý trực tiếp toàn bộ **320.78 triệu bản ghi thô pre-split** (`256.94M` `RAW18`), tinh chế thành **92.68 triệu bản ghi sạch** (`Base22`/`Prep27`), bao phủ trọn vẹn **11,632 tàu thương mại độc nhất** trên toàn bộ lãnh hải Hoa Kỳ (Đại Tây Dương, Thái Bình Dương, Vịnh Mexico, Alaska). Tập kiểm thử Blind Test Quý 4 chịu trọn vẹn sự biến động thời tiết khắc nghiệt của mùa đông (gió bão cấp 8-10, sóng biển $>4\text{m}$, hiện tượng trôi dạt và giảm tốc chờ bến kéo dài). Mức sai số `21.64h - 24.94h` phản ánh đúng thực tế khắc nghiệt ngoài đại dương.

### 4. Đánh đổi Hàm mục tiêu Nghiệp vụ Bất đối xứng (Asymmetric Loss Trade-off)

- **Ở Lab 3:** Ridge Regression tối ưu hóa sai số bình phương đối xứng ($L_2$ Loss), phạt lỗi dự báo sớm và dự báo trễ như nhau.
- **Ở Engine v2:** Nhóm triển khai Module M6 với **Custom Asymmetric Loss** (phạt nặng trường hợp dự báo tàu đến sớm gấp $w=2.5$ lần so với tàu đến trễ, vì tàu đến sớm sẽ khiến cảng chưa kịp bố trí cầu bến, công nhân cẩu bãi nhàn rỗi tiêu tốn hàng nghìn USD/giờ). Về mặt toán học (biên Pareto), khi ép mô hình triệt tiêu dự báo sớm (giảm `Underprediction_pct` từ 50% xuống mức an toàn), mô hình chủ động chấp nhận tăng nhẹ MAE đối xứng quanh mốc `21.64h - 24.94h` để đạt mục tiêu kinh tế tối thượng: **tiết kiệm hàng triệu USD chi phí vận hành cho doanh nghiệp cảng**.

---

## PHẦN C: BẢN ĐỒ TRA CỨU TỆP NGUỒN, LINK TẢI KAGGLE VÀ KHÔNG GIAN LÀM VIỆC CỦA 7 THÀNH VIÊN

### 1. Tra Cứu Tệp Nguồn & Đường Link Tải Kaggle Output Trực Tiếp

Toàn bộ các tệp số liệu thực nghiệm, siêu tham số và trọng số mô hình đã được đồng bộ hóa và lưu trữ tại 2 nguồn: kho lưu trữ GitHub cục bộ và nền tảng điện toán đám mây Kaggle:

| Hạng mục tài nguyên                    | Thí nghiệm Runner 1 (B0, M1, M2, M3)                                                           | Thí nghiệm Runner 2 (M4, M5, M6, M7)                                                               | Ghi chú & Thư mục đích trong workspace                                                          |
| :------------------------------------- | :--------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------- |
| **Đường link Kaggle Output trực tiếp** | [4 Thí nghiệm đầu (Kaggle Output)](https://www.kaggle.com/code/kienvo134/4-th-nghi-m-u/output) | [4 thí nghiệm cuối (Kaggle Output)](https://www.kaggle.com/code/kienvo134/4-th-nghi-m-cu-i/output) | Tải trực tiếp kết quả chạy từ Kaggle Kernel                                                     |
| **Gói nén trọng số mô hình**           | `runner1_saved_models.zip` (72.98 MB, 273 files)                                               | `runner2_saved_models.zip` (74.40 MB, 273 files)                                                   | Giải nén vào `05_Output_Cac_Notebook/07_.../saved_models/` và `08_.../saved_models/`            |
| **Bảng số liệu kết quả thực nghiệm**   | 42 file CSV (`results/`)                                                                       | 42 file CSV (`results/`)                                                                           | Đã đồng bộ sẵn trong `05_Output_Cac_Notebook/` và `DS317_R11_Nhom03_HoSoNopDoAn/06_Results/`    |
| **Tham số & siêu tham số cấu hình**    | 273 file JSON + 1 CSV (`parameters/`)                                                          | 273 file JSON + 1 CSV (`parameters/`)                                                              | Đã đồng bộ sẵn trong `05_Output_Cac_Notebook/` và `DS317_R11_Nhom03_HoSoNopDoAn/05_Model/`      |
| **Kết quả dự đoán chi tiết từng mẫu**  | `detailed_predictions/*.parquet`                                                               | `detailed_predictions/*.parquet`                                                                   | Tải từ Kaggle Output, đặt vào `05_Output_Cac_Notebook/07_.../detailed_predictions/` và `08_...` |

### 2. Không Gian Làm Việc Của 7 Thành Viên Trên GitHub (`06_Dong_Gop_Cac_Thanh_Vien/`)

Nhằm bảo đảm tính độc lập, tránh xung đột mã nguồn (merge conflicts) và minh bạch hóa tỷ lệ đóng góp của từng cá nhân, nhóm thiết lập 7 thư mục làm việc cá nhân riêng biệt tại [`06_Dong_Gop_Cac_Thanh_Vien/`](../06_Dong_Gop_Cac_Thanh_Vien/README.md):

|  STT  | Thành viên & MSSV                   | Vai trò chuyên trách                      | Nhiệm vụ trọng tâm trong đồ án                                                                                                                      | Đường dẫn thư mục cá nhân                                   | Tệp hướng dẫn riêng                                                                                                |
| :---: | :---------------------------------- | :---------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
|   1   | **Võ Đình Kiên** *(24520893)*       | Nhóm trưởng, Quản trị dự án & Kiến trúc   | Chủ trì Chương 1 & Chương 5, Module M4 RTMA, Báo cáo rủi ro Big Data, duyệt học thuật, xuất bản DOCX/PDF & đóng gói ZIP                             | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_01_VoDinhKien/`      | [`Thanh_Vien_01_VoDinhKien/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_01_VoDinhKien/README.md)           |
|   2   | **Đỗ Văn Lộc** *(24520977)*         | Thư ký, Kỹ sư Demo Web `app.py` & MLOps   | Chủ trì Chương 6, toàn bộ Web Streamlit `app.py`, video demo <= 3 phút, ảnh mockup cho Slide (không làm slide), biên bản & % đóng góp               | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_02_DoVanLoc/`        | [`Thanh_Vien_02_DoVanLoc/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_02_DoVanLoc/README.md)               |
|   3   | **Quách Tuấn Kiệt** *(24520911)*    | Kỹ sư Dữ liệu mẫu & Chất lượng DAMA       | Chủ trì Chương 3, Module M3, rà soát tính tái lập mã nguồn (Code Reproducibility), trích xuất bộ dữ liệu mẫu demo 1,000 - 5,000 dòng                | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_03_QuachTuanKiet/`   | [`Thanh_Vien_03_QuachTuanKiet/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_03_QuachTuanKiet/README.md)     |
|   4   | **Huỳnh Chí Kiên** *(24520880)*     | Chuyên viên EDA, Biểu đồ & XAI (SHAP)     | Chủ trì Chương 4, Module M1 & M2 trong Chương 5, thiết kế trọn bộ biểu đồ DPI >= 300 Engine v2 (Residual, SHAP, Delta Ablation) cho Báo cáo & Slide | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_04_HuynhChiKien/`    | [`Thanh_Vien_04_HuynhChiKien/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_04_HuynhChiKien/README.md)       |
|   5   | **Nguyễn Hữu Bảo Lộc** *(24520983)* | Chuyên viên SOTA IEEE & Đạo đức AI        | Chủ trì Chương 2 & Chương 7, Module M5 trong Chương 5, chuẩn hóa IEEE `references.bib`, Báo cáo Tuân thủ Pháp lý & Phụ lục Khai báo sử dụng AI      | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_05_NguyenHuuBaoLoc/` | [`Thanh_Vien_05_NguyenHuuBaoLoc/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_05_NguyenHuuBaoLoc/README.md) |
|   6   | **Lê Sỹ Liêm** *(24520951)*         | Chuyên viên Kiểm định Thống kê & ROI Cảng | Module M7 Conformal trong Chương 5, toàn bộ Kiểm định Thống kê chính thức (Wilcoxon, DM, Bootstrap), toàn bộ Mô hình Kinh tế / Business ROI cảng    | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_06_LeSyLiem/`        | [`Thanh_Vien_06_LeSyLiem/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_06_LeSyLiem/README.md)               |
|   7   | **Trần Hồng Lĩnh** *(24520970)*     | Chủ trì toàn bộ Slide Bảo vệ, Kỹ sư ML    | Chủ trì toàn bộ 10 phần Slide (`02_Slides/`), Baseline B0 & Module M6 trong Chương 5, phân tích lỗi Case Study có kiểm chứng theo 3 nhóm thời gian  | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_07_TranHongLinh/`    | [`Thanh_Vien_07_TranHongLinh/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_07_TranHongLinh/README.md)       |

---

## PHẦN D: PHÂN CÔNG CHI TIẾT 7 CHƯƠNG BÁO CÁO VÀ CÁC SẢN PHẨM CUỐI KỲ

### 1. Ma trận phân công Báo cáo Đồ án Cuối kỳ 7 Chương (30-50 trang)

| Chương báo cáo | Tên chương nội dung                                               | Thành viên chủ trì & phối hợp                                                                               | Nội dung cốt lõi cần hoàn thành                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Nguồn số liệu chính thức                                                                                                                                                     |
| :------------: | :---------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  **Chương 1**  | **Mở đầu & Bối cảnh Nghiệp vụ Cảng biển**                         | **Võ Đình Kiên** *(Chủ trì)* & **Đỗ Văn Lộc** *(Phối hợp)*, **Nguyễn Hữu Bảo Lộc** *(Tiểu mục 1.4 SOTA)*    | Bối cảnh logistics hàng hải, chi phí trễ/sớm ETA, chi phí lưu tàu Demurrage (15,000 - 30,000 USD/ngày), đơn giá bốc dỡ ILWU (56.85 USD/h), mục tiêu SMART, đối chuẩn 6 bài báo SOTA quốc tế (Springer, Elsevier).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `00_Quan_Ly_Va_Tai_Lieu_Chung/` & tệp `TongQuan_RelatedWork_ETA_6BaiBao_v2.xlsx`                                                                                             |
|  **Chương 2**  | **Cơ sở Lý thuyết & Pháp lý Dữ liệu Hàng hải**                    | **Nguyễn Hữu Bảo Lộc** *(Chủ trì)* & **Lê Sỹ Liêm** *(Phối hợp toán học/thuật toán)*                        | Cơ sở lý thuyết 7 thuật toán học máy (Ridge, RF, ET, LightGBM, XGBoost, CatBoost, MLP); chuẩn chất lượng dữ liệu DAMA-DMBOK và ISO 8000; cơ sở toán học hàm mất mát bất đối xứng Asymmetric Loss và khoảng tin cậy Conformal Prediction; khung pháp trị dữ liệu hàng hải.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `00_Quan_Ly_Va_Tai_Lieu_Chung/`, `TongQuan_RelatedWork_ETA_6BaiBao_v2.xlsx`, `Dinh_nghia_ham_toan_hoc.docx`                                                                  |
|  **Chương 3**  | **Khám phá & Kiểm kê Chất lượng Dữ liệu DAMA**                    | **Quách Tuấn Kiệt** *(Chủ trì)* & **Huỳnh Chí Kiên** *(Phối hợp biểu đồ)*                                   | Kiểm kê 7 tiêu chí NOAA AIS 2025, từ điển 27 thuộc tính, đo lường chất lượng 6 chiều DAMA-DMBOK trên 256.94M bản ghi `RAW18` vs 92.68M bản ghi sạch `Prep27`, phân tích tương quan Pearson ($r = +0.50971$), giám sát độ trôi dữ liệu Data Drift qua 4 Quý (Q1-Q4).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `05_Output_Cac_Notebook/02_DS317_02_Kham_Pha_DAMA_26_Dac_Trung/`, `06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/DAMA/`                                                                |
|  **Chương 4**  | **Thiết kế & Huấn luyện Mô hình Khai phá Dữ liệu**                | **Huỳnh Chí Kiên** *(Chủ trì)* & **Lê Sỹ Liêm** *(Phối hợp độ đo & 3 nhóm)*, **Võ Đình Kiên** *(Kiến trúc)* | Thiết kế kiến trúc 2-Pass Rolling Stream, Time-based Split 3 Folds ngăn rò rỉ dữ liệu, phát biểu bài toán ETA, định nghĩa hàm mất mát Custom Asymmetric Loss, thiết kế phân tầng 3 nhóm chân trời thời gian (`< 24h`, `24h - 72h`, `72h - 168h`), thiết kế chuỗi thực nghiệm 7 mô hình.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | `02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/02_Runner_Song_Song_Chinh_Thuc_v2/`, `Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md`                                              |
|  **Chương 5**  | **Kết quả Thực nghiệm, Đánh giá Mô hình & Bài toán Kinh tế Cảng** | **Võ Đình Kiên** *(Chủ trì & tổng hợp)* cùng 6 thành viên chuyên trách từng phân hệ                         | Đối chuẩn Baseline B0 trên 7 mô hình, Ablation Study 7 Module (M1-M7), kiểm định thống kê chính thức, phân tích SHAP XAI, phân tích lỗi Case Study chi tiết theo 3 nhóm chân trời thời gian (`< 24h`, `24h - 72h`, `72h - 168h`), và bài toán quy đổi tài chính Business ROI cảng biển. Phân công cụ thể: • **Trần Hồng Lĩnh:** Baseline B0 & Module M6 (Asymmetric Loss); Case Study lỗi 3 nhóm thời gian • **Huỳnh Chí Kiên:** Module M1 (Ngoại lai) & M2 (Điền khuyết); trọn bộ biểu đồ DPI >= 300 • **Quách Tuấn Kiệt:** Module M3 (Kỹ thuật đặc trưng biển) • **Võ Đình Kiên:** Module M4 (Thời tiết NOAA RTMA 2025) & Tổng hợp toàn chương • **Nguyễn Hữu Bảo Lộc:** Module M5 (Lựa chọn đặc trưng MI & log1p) • **Lê Sỹ Liêm:** Module M7 (Conformal Prediction); toàn bộ Kiểm định Thống kê (Wilcoxon/DM/Bootstrap); toàn bộ Mô hình Kinh tế / Business ROI cảng | `05_Output_Cac_Notebook/07_Runner_Song_Song_1_Baseline_M1_M2_M3/results/`, `08_Runner_Song_Song_2_M4_M5_M6_M7/results/`, `Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md` |
|  **Chương 6**  | **Triển khai MLOps & BI Dashboard Điều độ Cảng biển**             | **Đỗ Văn Lộc** *(Chủ trì)* & **Quách Tuấn Kiệt** *(Phối hợp dữ liệu mẫu)*                                   | Sơ đồ kiến trúc Web Demo Streamlit `app.py`, kết nối trọng số thật CatBoost/LightGBM/XGBoost, tab giám sát CLDL DAMA tương tác, tab phân bổ cầu bến JIT và phân cấp rủi ro trễ ETA theo 3 nhóm chân trời.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Thư mục `07_Demo/`, `03_SourceCode/app.py`, `04_Data/demo_sample_3000.*`                                                                                                     |
|  **Chương 7**  | **Kết luận, Hạn chế, Đạo đức AI & Hướng Phát triển**              | **Nguyễn Hữu Bảo Lộc** *(Chủ trì)* & **Võ Đình Kiên** *(Phối hợp tổng kết)*                                 | Tổng kết đóng góp đề tài, Báo cáo Tuân thủ Pháp lý (Luật 91/2025/QH15, Luật 60/2024/QH15, cơ chế ẩn danh `MMSI` -> `Vessel_Hash_ID`), Đạo đức AI & Phụ lục Khai báo sử dụng AI minh bạch, các hạn chế kỹ thuật và định hướng mở rộng đề tài.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Tổng hợp toàn bộ các chương, `08_QuanLyNhom/`                                                                                                                                |

---

### 2. Phân công các sản phẩm Kỹ thuật, Slide và Demo bàn giao

1. **Ứng dụng Demo Web Streamlit (`app.py`) (50% điểm sản phẩm A4):**
   - **Đỗ Văn Lộc (Chủ trì):** Xây dựng toàn bộ ứng dụng Web Streamlit (`app.py`), components giao diện, trực quan hóa hải trình, nạp trọng số thật CatBoost/LightGBM/XGBoost từ gói nén `runner*_saved_models.zip`, tích hợp BI Dashboard DAMA 6 chiều, phân bổ cầu bến JIT theo 3 nhóm chân trời, và quay video demo dự phòng (thời lượng <= 3 phút).
   - **Quách Tuấn Kiệt:** Trích xuất bộ dữ liệu mẫu chuẩn (1,000 - 5,000 dòng có phân bổ đại diện đủ cả 3 nhóm thời gian `< 24h`, `24h - 72h`, `72h - 168h` trong mốc <= 168h, schema 39 thuộc tính) phục vụ Demo chạy mượt mà không ngốn tài nguyên.
   - **Võ Đình Kiên:** Kiểm thử môi trường `requirements.txt`, `environment.yml` và đóng gói triển khai.
2. **Bộ Slide Thuyết trình Bảo vệ Cuối kỳ (20% điểm sản phẩm A4 - thư mục `02_Slides/`):**
   - **Trần Hồng Lĩnh (Chủ trì toàn bộ):** Tự tay thiết kế layout đồ họa và dựng hoàn chỉnh cả **10 phần** slide theo cấu trúc chuẩn môn học, xuất bản tệp `DS317_R11_Nhom03_Slides.pptx` và `DS317_R11_Nhom03_Slides.pdf` (tỷ lệ 16:9, thời lượng 15-20 phút).
   - **Các thành viên còn lại:** Chịu trách nhiệm cung cấp nội dung, số liệu, biểu đồ đầu vào đúng hạn cho Trần Hồng Lĩnh tích hợp:
     * **Võ Đình Kiên:** Cung cấp nội dung Phần 1 (Giới thiệu & Bối cảnh) và Phần 4 (Kiến trúc Pipeline); duyệt học thuật tổng thể slide.
     * **Nguyễn Hữu Bảo Lộc:** Cung cấp nội dung Phần 2 (SOTA & Cơ sở Lý thuyết) và Phần 10 (Kết luận, Pháp lý & Đạo đức AI).
     * **Quách Tuách Kiệt:** Cung cấp nội dung Phần 3 (Tài sản Dữ liệu & Kiểm toán 6 Chiều DAMA).
     * **Huỳnh Chí Kiên:** Cung cấp nội dung Phần 5 (Thiết kế Ablation M1-M7) và Phần 7 (SHAP XAI); cung cấp toàn bộ hình ảnh, sơ đồ kiến trúc và biểu đồ chất lượng cao ($DPI \ge 300$).
     * **Lê Sỹ Liêm:** Cung cấp nội dung Phần 6 (Kết Quả Thực Nghiệm & Kiểm Định Thống Kê) và Phần 8 (Tối Ưu Nghiệp Vụ Cảng Biển & ROI).
     * **Đỗ Văn Lộc:** Cung cấp ảnh chụp màn hình mockup/video demo thực tế cho Phần 9 (Demo Web Streamlit & BI Dashboard). Đỗ Văn Lộc **không làm slide**.
3. **Kiểm định Thống kê & Bảng tính ROI Doanh nghiệp:**
   - **Lê Sỹ Liêm (Độc lập phụ trách toàn bộ):** Chạy script kiểm định Wilcoxon signed-rank, Diebold-Mariano và Paired Bootstrap 2,000 lần ($p < 0.001$) so sánh Baseline B0 với các mô hình tốt nhất; xây dựng Mô hình Kinh tế / Bảng quy đổi giá trị tài chính USD / Business ROI cảng biển phân rã chi tiết theo 3 nhóm chân trời thời gian (`< 24h`, `24h - 72h`, `72h - 168h`), tham chiếu đơn giá ILWU 56.85 USD/giờ và chi phí thuê tàu 15,800 - 90,500 USD/ngày.
4. **Phân tích Lỗi Case Study & Giải thích Phân tầng 3 Nhóm Chân trời:**
   - **Trần Hồng Lĩnh:** Trích xuất các case study tàu biển sai số cực trị từ `detailed_predictions/*.parquet` và hoàn thiện Báo cáo phân tích lỗi dạng Case Study chi tiết theo 3 nhóm thời gian (`< 24h`, `24h - 72h`, `72h - 168h`), giải thích cơ chế sai số vật lý/hàng hải khi tàu từ ngoài khơi tiến dần vào gần cảng; viết tài liệu Giải thích phân tầng 168h khoa học.
5. **SOTA IEEE, Pháp lý Dữ liệu & Đạo đức AI:**
   - **Nguyễn Hữu Bảo Lộc:** Xây dựng danh mục trích dẫn IEEE `references.bib`, soạn thảo Báo cáo Tuân thủ Pháp lý (Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15, Luật Dữ liệu 60/2024/QH15, cơ chế ẩn danh `MMSI` -> `Vessel_Hash_ID`) và bản Phụ lục "Khai báo sử dụng AI" minh bạch.
6. **Rà soát Tính Tái Lập Toàn Bộ Mã Nguồn (Code Reproducibility):**
   - **Quách Tuấn Kiệt:** Kiểm tra khả năng chạy lại trơn tru của toàn bộ các notebook và script trong `05_Output_Cac_Notebook/` và `02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/`, bảo đảm không còn đường dẫn tuyệt đối cứng, lập biên bản `Kiem_Tra_Tai_Lap_Code.md`.
7. **Quản trị Dự án, Báo cáo Rủi ro Big Data & Đóng gói Nghiệm thu:**
   - **Võ Đình Kiên:** Điều phối tiến độ chung, lập Báo cáo rủi ro Big Data khi xử lý 320.78M dòng thô NOAA AIS, tổng biên tập Báo cáo 7 chương (`DS317_R11_Nhom03_BaoCao.docx` & `.pdf`), kiểm soát chất lượng 0 broken link, và đóng gói tệp nén nộp bài `DS317_R11_Nhom03.zip`.
8. **Hồ sơ Quản lý Nhóm cuối kỳ (`08_QuanLyNhom/`):**
   - **Đỗ Văn Lộc:** Hoàn thiện Nhật ký thực nghiệm tổng hợp, Scope Changelog Engine v1 sang Engine v2, tập hợp Biên bản họp nhóm giai đoạn sau Lab 3 và Bảng tự đánh giá % đóng góp của 7 thành viên.

---

## PHẦN E: HƯỚNG DẪN LUỒNG PHỐI HỢP GIT NHÓM (GIT COLLABORATION WORKFLOW)

Để bảo đảm an toàn cho kho lưu trữ, các thành viên cam kết thực hiện đúng quy trình 5 bước:

```
[Nhánh main trên GitHub]
       │
       ├── Bước 1: git checkout main && git pull origin main
       │
       ├── Bước 2: git checkout -b feature/<ten_thanh_vien>
       │
       ├── Bước 3: Làm việc độc quyền trong thư mục 06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_XX_<Ten>/
       │
       ├── Bước 4: git add ... && git commit -m "..." && git push origin feature/<ten_thanh_vien>
       │
       └── Bước 5: Tạo Pull Request (PR) -> Nhóm trưởng review và merge vào hồ sơ nộp bài chuẩn
```

- **Quy tắc bất di bất dịch:**
  1. Tuyệt đối không chỉnh sửa trực tiếp trên nhánh `main`.
  2. Tuyệt đối không commit đè lên thư mục của thành viên khác.
  3. Chỉ sử dụng duy nhất **dấu gạch ngang tiêu chuẩn `-` (ASCII 0x2D)** trong toàn bộ văn bản và tên file; nghiêm cấm dùng các ký tự gạch ngang dài en-dash hoặc em-dash.
  4. Trước khi nộp sản phẩm, kiểm tra kỹ để đảm bảo không tạo ra broken link và không đẩy các file tạm phát sinh vào kho lưu trữ.
