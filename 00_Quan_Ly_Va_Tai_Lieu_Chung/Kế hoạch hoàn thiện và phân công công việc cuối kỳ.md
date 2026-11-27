# Kế Hoạch Hoàn Thiện và Phân Công Công Việc Cuối Kỳ - Nhóm 03 (DS317.R11)

- **Học phần:** DS317 - Khai phá dữ liệu trong doanh nghiệp (UIT - ĐHQG-HCM)
- **Đề tài:** Dự báo thời điểm cập cảng của tàu biển thay thế ETA tự khai báo (*Prediction of Vessel Port Arrival Time Replacing Self-Reported ETA*)
- **Kho lưu trữ chuẩn:** `DS317_DoAn_Nhom03_TongHop/` | **Thư mục nộp bài chuẩn 8 phần:** [`DS317_R11_Nhom03_HoSoNopDoAn/`](../DS317_R11_Nhom03_HoSoNopDoAn/README.md)
- **Kho output tập trung các notebook:** [`05_Output_Cac_Notebook/`](../05_Output_Cac_Notebook/README.md)
- **Khu vực không gian làm việc của 7 thành viên:** [`06_Dong_Gop_Cac_Thanh_Vien/`](../06_Dong_Gop_Cac_Thanh_Vien/README.md)
- **Phạm vi tài liệu này:** Cập nhật hiện trạng thực tế mới nhất sau khi đã hoàn tất 100% việc chạy thực nghiệm và quy tập kết quả đầu ra tập trung; cung cấp bản đồ tra cứu tệp nguồn chuẩn hóa (số liệu, tham số, trọng số) cho toàn nhóm; giải thích bản chất khoa học - kỹ thuật về sai số giữa Lab 3 và Engine v2; xác lập cơ chế phân quyền thư mục làm việc Git cho 7 thành viên; và phân công chi tiết 7 chương Báo cáo cuối kỳ, Slide, Demo Web và Hồ sơ nghiệm thu.

---

## PHẦN A: CÁC NỘI DUNG VÀ TIÊU CHÍ TRỌNG TÂM CẦN HOÀN THIỆN

### 1. Bảng theo dõi tiến độ các sản phẩm bàn giao bắt buộc (Chiếm 100% điểm A4)

| STT | Hạng mục bắt buộc (theo quy định môn học) | Tỷ trọng / Vai trò | Thư mục đích | Trạng thái hiện tại | Người phụ trách chính |
| :---: | :--- | :--- | :--- | :--- | :--- |
| 1 | **Chương trình Demo Web/App tương tác (`app.py`)** (kết nối trọng số thật, tích hợp BI Dashboard & dự báo ETA) | **50%** điểm sản phẩm A4 | `03_SourceCode/` & `07_Demo/` | **Đang xây dựng** (Đã có sẵn trọng số mô hình và số liệu DAMA để tích hợp) | **Đỗ Văn Lộc** |
| 2 | **Báo cáo Đồ án Cuối kỳ 7 Chương** (`.docx` & `.pdf`, 30-50 trang) | **30%** điểm sản phẩm A4 | `01_BaoCao/` | **Đang triển khai viết** (Đã có đầy đủ số liệu thực nghiệm Engine v2 và phân công chi tiết 7 chương) | **Cả nhóm** (Võ Đình Kiên chủ trì) |
| 3 | **Bộ Slide Bảo vệ Cuối kỳ 10 phần** (`.pptx` & `.pdf`) | **20%** điểm sản phẩm A4 | `02_Slides/` | **Đang triển khai thiết kế** (Đã chốt bố cục 10 phần chuẩn môn học) | **Cả nhóm** (Đỗ Văn Lộc chủ trì) |
| 4 | **Bộ dữ liệu mẫu chạy Demo & `requirements.txt`** (1,000-5,000 dòng đầy đủ 27 đặc trưng + RTMA, kèm hướng dẫn tái lập) | Điều kiện nghiệm thu Demo & chấm mã nguồn | `04_Data/` & `03_SourceCode/` | **Đang hoàn thiện** (Đã có schema và tệp tiền xử lý mẫu để trích xuất) | **Quách Tuấn Kiệt** (Data mẫu) & **Võ Đình Kiên** (`requirements.txt`) |

---

### 2. Nhóm tiêu chí Kỹ thuật, Biểu đồ & Học thuật chuyên sâu (Sẵn sàng triển khai từ dữ liệu có sẵn)

1. **Kiểm định ý nghĩa thống kê chính thức (Statistical Significance Testing):**
   - **Hiện trạng:** Đã có số liệu chi tiết qua 3 Fold của 7 mô hình và 13 biến thể trong `05_Output_Cac_Notebook/07_Runner_Song_Song_1_Baseline_M1_M2_M3/results/` và `08_Runner_Song_Song_2_M4_M5_M6_M7/results/`.
   - **Yêu cầu hoàn thiện:** Thực hiện kiểm định `Wilcoxon signed-rank test`, `Diebold-Mariano test` hoặc `Paired Bootstrap` (2,000 lần lặp) kèm tính toán giá trị `p-value` so sánh giữa Baseline B0 và các mô hình tốt nhất (CatBoost, XGBoost, LightGBM, M6 Asymmetric, M7 Conformal). Phụ trách: **Lê Sỹ Liêm**.
2. **Biểu đồ Chương 4 & Chương 5 chuẩn Engine v2 (`DPI >= 300`):**
   - **Hiện trạng:** Thư mục `06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/Hinh_Anh_Bieu_Do/` và `02_DS317_02.../CHARTS/` đã có 30 biểu đồ chuẩn cho EDA và BTVN.
   - **Yêu cầu hoàn thiện:** Thiết kế bổ sung các biểu đồ Engine v2 cho Chương 4 và Chương 5: sơ đồ kiến trúc Engine v2 tích hợp BI Dashboard, biểu đồ so sánh 7 mô hình theo phân tầng (`All`, `LE_168h`, `GT_168h`), biểu đồ Delta Ablation `M1-M7`, biểu đồ phân tích sai số residual theo phân tầng 168h. Phụ trách: **Huỳnh Chí Kiên**.
3. **Giải thích mô hình chuyên sâu bằng SHAP (`SHAP Summary Plot` & `SHAP Beeswarm Plot`):**
   - **Hiện trạng:** Đã có đầy đủ trọng số mô hình trong gói `runner1_saved_models.zip` và `runner2_saved_models.zip` (hoặc giải nén trong `05_Model/`).
   - **Yêu cầu hoàn thiện:** Nạp mô hình tốt nhất (CatBoost/XGBoost/LightGBM) cùng bộ dữ liệu kiểm thử để trích xuất SHAP values, vẽ `SHAP Summary Plot` và `SHAP Beeswarm Plot` giải thích mức độ ảnh hưởng của `Dist_To_Berth_NM`, `sog`, các biến tương tác M3 và thời tiết RTMA M4. Phụ trách: **Huỳnh Chí Kiên**.
4. **Phân tích lỗi Case Study có kiểm chứng (Error Analysis):**
   - **Hiện trạng:** Đã có bảng số liệu đánh giá chi tiết theo từng chuyến đi và phân tầng thời gian.
   - **Yêu cầu hoàn thiện:** Trích xuất các trường hợp tàu biển thật (kèm định danh `MMSI`, loại tàu, vận tốc `sog`, khoảng cách `Dist_To_Berth_NM`) có sai số residual lớn nhất ở cả 2 tầng `<= 168h` và `> 168h`, phân tích nguyên nhân vật lý/hàng hải, viết tài liệu **Giải thích phân tầng 168h mới** thay thế bản cũ đã xóa. Phụ trách: **Trần Hồng Lĩnh**.
5. **Quy đổi Tài chính USD / Business ROI và Đánh giá Mất mát Bất đối xứng (M6/M7):**
   - **Hiện trạng:** Đã có kết quả thực nghiệm M6 Asymmetric Loss (`m6_asym_*`) và M7 Conformal Prediction (`m7_conformal_*`).
   - **Yêu cầu hoàn thiện:** Xây dựng bảng quy đổi tài chính thực tế cho doanh nghiệp cảng biển: tham chiếu đơn giá nhân công bốc xếp ILWU (56.85 USD/giờ), chi phí thuê tàu theo ngày (15,800 - 90,500 USD/ngày), định lượng khoản tiết kiệm USD khi giảm tỷ lệ dự báo sớm (`Underprediction_pct`) từ M6 và độ tin cậy từ khoảng dự báo M7 Conformal (`PICP_90` vs `MPIW`). Phụ trách: **Lê Sỹ Liêm** & **Trần Hồng Lĩnh**.
6. **Tuân thủ Pháp lý & Đạo đức AI:**
   - **Yêu cầu hoàn thiện:** Rà soát và hoàn thiện tài liệu tuân thủ **Luật Bảo vệ dữ liệu cá nhân**, và soạn thảo mục **Khai báo sử dụng AI** minh bạch theo chuẩn liêm chính học thuật. Phụ trách: **Nguyễn Hữu Bảo Lộc**.
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

## PHẦN C: KHÔNG GIAN LÀM VIỆC CỦA 7 THÀNH VIÊN TRÊN GITHUB (`06_Dong_Gop_Cac_Thanh_Vien/`)

Nhằm bảo đảm tính độc lập, tránh xung đột mã nguồn (merge conflicts) và minh bạch hóa tỷ lệ đóng góp của từng cá nhân, nhóm thiết lập 7 thư mục làm việc cá nhân riêng biệt tại [`06_Dong_Gop_Cac_Thanh_Vien/`](../06_Dong_Gop_Cac_Thanh_Vien/README.md):

| STT | Thành viên & MSSV | Vai trò chuyên trách | Đường dẫn thư mục cá nhân | Tệp hướng dẫn riêng |
| :-: | :--- | :--- | :--- | :--- |
| 1 | **Võ Đình Kiên** *(24520893)* | Nhóm trưởng, Quản trị dự án & Kiến trúc | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_01_VoDinhKien/` | [`Thanh_Vien_01_VoDinhKien/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_01_VoDinhKien/README.md) |
| 2 | **Đỗ Văn Lộc** *(24520977)* | Thư ký, Kỹ sư Demo Web `app.py` & Slide | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_02_DoVanLoc/` | [`Thanh_Vien_02_DoVanLoc/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_02_DoVanLoc/README.md) |
| 3 | **Quách Tuấn Kiệt** *(24520911)* | Kỹ sư Dữ liệu mẫu & Chất lượng DAMA | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_03_QuachTuanKiet/` | [`Thanh_Vien_03_QuachTuanKiet/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_03_QuachTuanKiet/README.md) |
| 4 | **Huỳnh Chí Kiên** *(24520880)* | Chuyên viên EDA, Biểu đồ & XAI (SHAP) | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_04_HuynhChiKien/` | [`Thanh_Vien_04_HuynhChiKien/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_04_HuynhChiKien/README.md) |
| 5 | **Nguyễn Hữu Bảo Lộc** *(24520983)* | Chuyên viên SOTA IEEE & Đạo đức AI | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_05_NguyenHuuBaoLoc/` | [`Thanh_Vien_05_NguyenHuuBaoLoc/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_05_NguyenHuuBaoLoc/README.md) |
| 6 | **Lê Sỹ Liêm** *(24520951)* | Chuyên viên Kiểm định Thống kê & ROI Cảng | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_06_LeSyLiem/` | [`Thanh_Vien_06_LeSyLiem/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_06_LeSyLiem/README.md) |
| 7 | **Trần Hồng Lĩnh** *(24520970)* | Kỹ sư ML/DL, Error Analysis Case Study | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_07_TranHongLinh/` | [`Thanh_Vien_07_TranHongLinh/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_07_TranHongLinh/README.md) |

---

## PHẦN D: PHÂN CÔNG CHI TIẾT 7 CHƯƠNG BÁO CÁO VÀ CÁC SẢN PHẨM CUỐI KỲ

### 1. Ma trận phân công Báo cáo Đồ án Cuối kỳ 7 Chương (30-50 trang)

| Chương báo cáo | Tên chương nội dung | Thành viên phụ trách chính | Nội dung cốt lõi cần hoàn thành | Nguồn số liệu chính thức |
| :---: | :--- | :--- | :--- | :--- |
| **Chương 1** | **Tổng quan và Bối cảnh nghiệp vụ** | **Đỗ Văn Lộc** *(Chính)* & **Nguyễn Hữu Bảo Lộc** *(SOTA)* | Bối cảnh logistics cảng biển, chi phí trễ/sớm ETA, mục tiêu SMART, tổng quan 6 bài báo SOTA (Springer, Elsevier) và bảng đối sánh quốc tế. | `00_Quan_Ly_Va_Tai_Lieu_Chung/` & tệp `TongQuan_RelatedWork_ETA_6BaiBao_v2.xlsx` |
| **Chương 2** | **Dữ liệu và Đo lường Chất lượng Dữ liệu** | **Quách Tuấn Kiệt** | Kiểm kê 7 tiêu chí NOAA AIS 2025, từ điển 18/22/27 thuộc tính, đo lường chất lượng 6 chiều DAMA-DMBOK trên 256.94M bản ghi `RAW18`. | `05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/DAMA/` |
| **Chương 3** | **Phương pháp Tiền xử lý Dữ liệu** | **Huỳnh Chí Kiên** | Kiến trúc 2-Pass Rolling Stream, bộ lọc 3 tầng, Domain-based Imputation (khôi phục khuyết thiếu về 0.00%), chế tác đặc trưng thân vỏ $Area, Volume$. | `05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/IMPUTE_BENCHMARK/` |
| **Chương 4** | **Phương pháp Nghiên cứu & Thiết kế Thực nghiệm** | **Lê Sỹ Liêm** | Phát biểu bài toán KPDL, kịch bản Expanding Window 3 Folds, hàm mất mát Custom Asymmetric Loss, các độ đo kỹ thuật và nghiệp vụ ($AsymCost$). | `03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md` |
| **Chương 5** | **Kết quả Thực nghiệm & Phân tích Đánh giá** | **Trần Hồng Lĩnh** *(Chủ trì)*, **Huỳnh Chí Kiên**, **Lê Sỹ Liêm**, **Nguyễn Hữu Bảo Lộc** | Đối chuẩn Baseline B0 trên 7 mô hình, Ablation Study 7 Module (M1-M7), giải thích SHAP XAI, kiểm định thống kê $p$-value, phân tích Case Study lỗi phân tầng 168h. | `05_Output_Cac_Notebook/07_Runner_Song_Song_1_Baseline_M1_M2_M3/results/` và `08_Runner_Song_Song_2_M4_M5_M6_M7/results/` |
| **Chương 6** | **Kiến trúc Ứng dụng & Triển khai Doanh nghiệp** | **Đỗ Văn Lộc** | Sơ đồ kiến trúc Web Demo Streamlit, kịch bản tích hợp hệ thống điều độ cảng biển JIT, các ca sử dụng giao diện và phân cấp rủi ro ETA. | Thư mục `07_Demo/` và mã nguồn `app.py` |
| **Chương 7** | **Kết luận và Hướng phát triển** | **Võ Đình Kiên** *(Nhóm trưởng)* | Tóm tắt các kết quả đạt được, giá trị kinh tế thực tiễn, các hạn chế còn tồn đọng và định hướng mở rộng đề tài trong tương lai. | Tổng hợp toàn bộ các chương |

---

### 2. Phân công các sản phẩm Kỹ thuật và Demo bàn giao

1. **Ứng dụng Demo Web Streamlit (`app.py`):**
   - **Đỗ Văn Lộc:** Lập trình giao diện, kết nối model, trực quan hóa bản đồ hải trình và phân bổ cầu bến JIT.
   - **Quách Tuấn Kiệt:** Cung cấp bộ dữ liệu mẫu chuẩn (1,000 - 5,000 dòng).
   - **Võ Đình Kiên:** Kiểm thử môi trường `requirements.txt` và đóng gói triển khai.
2. **Bộ Slide Thuyết trình Bảo vệ Cuối kỳ:**
   - **Đỗ Văn Lộc:** Thiết kế layout đồ họa, cấu trúc 10-12 slides.
   - **Huỳnh Chí Kiên:** Cung cấp toàn bộ biểu đồ và hình ảnh chất lượng cao.
   - **Võ Đình Kiên:** Tổng duyệt nội dung học thuật và speaker notes.
3. **Kiểm định Thống kê & Bảng tính ROI Doanh nghiệp:**
   - **Lê Sỹ Liêm:** Chạy script kiểm định Wilcoxon, Bootstrap 2,000 lần và lập bảng tính ROI tài chính.
4. **Phân tích Lỗi Case Study & Giải thích Phân tầng 168h:**
   - **Trần Hồng Lĩnh:** Trích xuất các case study tàu biển sai số cực trị và hoàn thiện báo cáo phân tích lỗi.
5. **Đạo đức AI & Danh mục IEEE:**
   - **Nguyễn Hữu Bảo Lộc:** Soạn thảo tuyên bố liêm chính AI và chuẩn hóa tệp `references.bib`.

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
