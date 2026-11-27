# Kế Hoạch Hoàn Thiện và Phân Công Công Việc Cuối Kỳ - Nhóm 03 (DS317.R11)

- **Học phần:** DS317 - Khai phá dữ liệu trong doanh nghiệp (UIT - ĐHQG-HCM)
- **Đề tài:** Dự báo thời điểm cập cảng của tàu biển thay thế ETA tự khai báo (*Prediction of Vessel Port Arrival Time Replacing Self-Reported ETA*)
- **Kho lưu trữ chuẩn:** `DS317_DoAn_Nhom03_TongHop/` | **Thư mục nộp bài chuẩn 8 phần:** [`DS317_R11_Nhom03_HoSoNopDoAn/`](../DS317_R11_Nhom03_HoSoNopDoAn/README.md)
- **Kho output tập trung các notebook:** [`05_Output_Cac_Notebook/`](../05_Output_Cac_Notebook/README.md)
- **Khu vực không gian làm việc của 7 thành viên:** [`06_Dong_Gop_Cac_Thanh_Vien/`](../06_Dong_Gop_Cac_Thanh_Vien/README.md)
- **Phạm vi tài liệu này:** Cập nhật hiện trạng thực tế mới nhất sau khi đã hoàn tất 100% việc chạy thực nghiệm và quy tập kết quả đầu ra tập trung; cung cấp bản đồ tra cứu tệp nguồn chuẩn hóa (số liệu, tham số, trọng số) và đường link Kaggle Output trực tiếp cho toàn nhóm; giải thích bản chất khoa học - kỹ thuật về sai số giữa Lab 3 và Engine v2 cùng phân tích chuyên sâu 3 nhóm thời gian chân trời <= 168h; xác lập cơ chế phân quyền thư mục làm việc Git cho 7 thành viên; và phân công chi tiết 7 chương Báo cáo cuối kỳ, Slide, Demo Web và Hồ sơ nghiệm thu.

---

## MỤC 0: HIỆN TRẠNG MỚI NHẤT - NỀN TẢNG THỰC NGHIỆM VÀ ĐƯỜNG LINK TẢI KAGGLE OUTPUT

Nhóm đã hoàn tất 100% việc huấn luyện và kiểm thử thực nghiệm trên môi trường điện toán đám mây Kaggle với cấu hình phân tán 2x GPU Tesla T4 (DDP). Toàn bộ sản phẩm đầu ra đã được đóng gói hoàn chỉnh, cung cấp đường link chi tiết để tải trọng số mô hình, bộ tham số cấu hình và kết quả dự đoán chi tiết của từng mẫu (sample-level predictions):

1. **4 Thí nghiệm đầu (Runner 1: Baseline B0, M1, M2, M3):**

   - **Kaggle Kernel Output Link:** [4 Thí nghiệm đầu (Kaggle Output)](https://www.kaggle.com/code/kienvo134/4-th-nghi-m-u/output)
   - **Tài nguyên trực tiếp:**
     * **Trọng số mô hình nén (`saved_models.zip`):** Gói nén `runner1_saved_models.zip` (72.98 MB) chứa đầy đủ 273 tệp trọng số (`.pt`, `.cbm`, `.txt`, `.json`) của 7 mô hình x 13 biến thể x 3 Folds (CatBoost, LightGBM, XGBoost, Random Forest, Extra Trees, MLP, Ridge).
     * **Tham số & siêu tham số cấu hình (`parameters/`):** 273 tệp `*_meta.json` chi tiết và tệp tổng hợp `parameters_summary.csv` lưu trữ đầy đủ danh sách đặc trưng đầu vào (`feature_cols`), giá trị trung vị điền khuyết (`fit_medians`), tham số chuẩn hóa (`scaler_mean`, `scaler_std`) và siêu tham số tối ưu.
     * **Số liệu kết quả thực nghiệm (`results/`):** 42 tệp CSV ghi nhận độ lỗi đo lường (`00_baseline_*`, `m1_*`, `m2_*`, `m3_*`, `runner1_master_summary.csv`, `runner1_master_horizons.csv`).
     * **Dự đoán chi tiết từng mẫu (`detailed_predictions/`):** Tệp nén chứa các bảng `.parquet` lưu trữ kết quả dự đoán chi tiết từng bản ghi hành trình phục vụ kiểm toán sai số vi mô theo khoảng cách và thời gian.
2. **4 Thí nghiệm cuối (Runner 2: M4, M5, M6, M7):**

   - **Kaggle Kernel Output Link:** [4 thí nghiệm cuối (Kaggle Output)](https://www.kaggle.com/code/kienvo134/4-th-nghi-m-cu-i/output)
   - **Tài nguyên trực tiếp:**
     * **Trọng số mô hình nén (`saved_models.zip`):** Gói nén `runner2_saved_models.zip` (74.40 MB) chứa đầy đủ 273 tệp trọng số cho các module nâng cao: M4 (Thời tiết hải văn RTMA 2025), M5 (Gom cụm địa lý Geo-Clustering K-Means/DBSCAN), M6 (Hàm mất mát bất đối xứng Asymmetric Loss phạt sớm w=2.5), và M7 (Khoảng tin cậy Conformal Prediction).
     * **Tham số & siêu tham số cấu hình (`parameters/`):** 273 tệp `*_meta.json` chi tiết và tệp `parameters_summary.csv` lưu trữ tham số hàm mất mát bất đối xứng (`asym_alpha`), ngưỡng bao phủ phi tham số (`conformal_q90`), và siêu tham số mô hình phân tầng.
     * **Số liệu kết quả thực nghiệm (`results/`):** 42 tệp CSV chuẩn hóa đo lường độ lỗi kỹ thuật và kinh tế (`m4_*`, `m5_*`, `m6_*`, `m7_*`, `runner2_master_summary.csv`, `runner2_master_horizons.csv`).
     * **Dự đoán chi tiết từng mẫu (`detailed_predictions/`):** Tệp nén `.parquet` lưu trữ giá trị dự đoán điểm, cận trên - cận dưới khoảng tin cậy conformal cho từng bản ghi phục vụ phân tích sai số chuyên sâu.

---

## PHẦN A: CÁC NỘI DUNG VÀ TIÊU CHÍ TRỌNG TÂM CẦN HOÀN THIỆN

### 1. Bảng theo dõi tiến độ các sản phẩm bàn giao bắt buộc (Chiếm 100% điểm A4)

|  STT  | Hạng mục bắt buộc (theo quy định môn học)                                                                                                                                                                                      | Tỷ trọng / Vai trò                        | Thư mục đích                  | Trạng thái hiện tại                                                                                  | Người phụ trách chính                                                  |
| :---: | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------------- | :---------------------------- | :--------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------- |
|   1   | **Chương trình Demo Web/App tương tác (`app.py`)** (kết nối trọng số thật, tích hợp BI Dashboard & dự báo ETA)                                                                                                                 | **50%** điểm sản phẩm A4                  | `03_SourceCode/` & `07_Demo/` | **Đang xây dựng** (Đã có sẵn trọng số mô hình và số liệu DAMA để tích hợp)                           | **Đỗ Văn Lộc**                                                         |
|   2   | **Báo cáo Đồ án Cuối kỳ 7 Chương** (`.docx` & `.pdf`, 30-50 trang)                                                                                                                                                             | **30%** điểm sản phẩm A4                  | `01_BaoCao/`                  | **Đang triển khai viết** (Đã có đầy đủ số liệu thực nghiệm Engine v2 và phân công chi tiết 7 chương) | **Cả nhóm** (Võ Đình Kiên chủ trì)                                     |
|   3   | **Bộ Slide Bảo vệ Cuối kỳ 10 phần** (`.pptx` & `.pdf`)                                                                                                                                                                         | **20%** điểm sản phẩm A4                  | `02_Slides/`                  | **Đang triển khai thiết kế** (Đã chốt bố cục 10 phần chuẩn môn học)                                  | **Cả nhóm** (Đỗ Văn Lộc chủ trì)                                       |
|   4   | **Bộ dữ liệu mẫu chạy Demo & `requirements.txt`** (1,000-5,000 dòng có phân bổ đại diện đủ 3 nhóm chân trời thời gian `< 24h`, `24h - 72h`, `72h - 168h` trong mốc <= 168h, đầy đủ 27 đặc trưng + RTMA, kèm hướng dẫn tái lập) | Điều kiện nghiệm thu Demo & chấm mã nguồn | `04_Data/` & `03_SourceCode/` | **Đang hoàn thiện** (Đã có schema và tệp tiền xử lý mẫu để trích xuất)                               | **Quách Tuấn Kiệt** (Data mẫu) & **Võ Đình Kiên** (`requirements.txt`) |

---

### 2. Nhóm tiêu chí Kỹ thuật, Biểu đồ & Học thuật chuyên sâu (Sẵn sàng triển khai từ dữ liệu có sẵn)

1. **Kiểm định ý nghĩa thống kê chính thức (Statistical Significance Testing) & Phân rã Thống kê 3 Nhóm Chân trời:**
   - **Hiện trạng:** Đã có số liệu chi tiết qua 3 Fold của 7 mô hình và 13 biến thể trong `05_Output_Cac_Notebook/07_Runner_Song_Song_1_Baseline_M1_M2_M3/results/` và `08_Runner_Song_Song_2_M4_M5_M6_M7/results/`.
   - **Yêu cầu hoàn thiện:** Thực hiện kiểm định `Wilcoxon signed-rank test`, `Diebold-Mariano test` hoặc `Paired Bootstrap` (2,000 lần lặp) kèm tính toán giá trị `p-value` so sánh giữa Baseline B0 và các mô hình tốt nhất (CatBoost, XGBoost, LightGBM, M6 Asymmetric, M7 Conformal). Đồng thời, tính toán kiểm định thống kê và xây dựng Bảng quy đổi giá trị kinh tế / Business ROI cảng biển phân rã chi tiết theo 3 nhóm chân trời thời gian (`< 24h`, `24h - 72h`, `72h - 168h`). Phụ trách: **Lê Sỹ Liêm**.
2. **Biểu đồ Chương 4 & Chương 5 chuẩn Engine v2 (`DPI >= 300`) Phân rã theo 3 Nhóm Chân trời:**
   - **Hiện trạng:** Thư mục `06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/Hinh_Anh_Bieu_Do/` và `02_DS317_02.../CHARTS/` đã có 30 biểu đồ chuẩn cho EDA và BTVN.
   - **Yêu cầu hoàn thiện:** Thiết kế bổ sung các biểu đồ Engine v2 cho Chương 4 và Chương 5: sơ đồ kiến trúc Engine v2 tích hợp BI Dashboard, biểu đồ so sánh 7 mô hình theo phân tầng (`All`, `LE_168h`, `GT_168h`), biểu đồ Delta Ablation `M1-M7`. Đặc biệt, thiết kế biểu đồ phân bố sai số (Residual / Error Distribution) và sai số tuyệt đối trung bình MAE theo 3 nhóm thời gian (`< 24h`, `24h - 72h`, `72h - 168h`) cho Chương 5. Phụ trách: **Huỳnh Chí Kiên**.
3. **Giải thích mô hình chuyên sâu bằng SHAP (`SHAP Summary Plot` & `SHAP Beeswarm Plot`):**
   - **Hiện trạng:** Đã có đầy đủ trọng số mô hình trong gói `runner1_saved_models.zip` và `runner2_saved_models.zip` (hoặc giải nén trong `05_Model/`).
   - **Yêu cầu hoàn thiện:** Nạp mô hình tốt nhất (CatBoost/XGBoost/LightGBM) cùng bộ dữ liệu kiểm thử để trích xuất SHAP values, vẽ `SHAP Summary Plot` và `SHAP Beeswarm Plot` giải thích mức độ ảnh hưởng của `Dist_To_Berth_NM`, `sog`, các biến tương tác M3 và thời tiết RTMA M4. Phụ trách: **Huỳnh Chí Kiên**.
4. **Phân tích lỗi Case Study có kiểm chứng theo 3 Nhóm Chân trời Nghiệp vụ Hàng hải (Error Analysis):**
   - **Hiện trạng:** Đã có bảng số liệu đánh giá chi tiết theo từng chuyến đi và phân tầng thời gian.
   - **Yêu cầu hoàn thiện:** Trích xuất các trường hợp tàu biển thật (kèm định danh `MMSI`, loại tàu, vận tốc `sog`, khoảng cách `Dist_To_Berth_NM`) có sai số residual lớn nhất ở cả 2 tầng `<= 168h` và `> 168h`. Thực hiện phân tích lỗi dạng Case Study chi tiết theo 3 nhóm thời gian trong mốc chân trời <= 168h (`LE_168h`), giải thích cơ chế sai số khi tàu từ ngoài khơi tiến dần vào gần cảng:
     * **Nhóm Siêu ngắn hạn / Cận cảng (`< 24h` / Dưới 1 ngày):** Giai đoạn tàu tiếp cận luồng hoa tiêu, phao số 0, vùng neo đậu chờ bến. Ý nghĩa nghiệp vụ: Bố trí hoa tiêu hàng hải, tàu lai dắt (tugboat), cầu bến cập tức thời, rà soát xung đột an toàn luồng lạch.
     * **Nhóm Ngắn hạn / Duyên hải (`24h - 72h` / 1 đến 3 ngày):** Giai đoạn tàu chạy ven bờ, tiếp cận vùng nước cảng. Ý nghĩa nghiệp vụ: Lập kế hoạch giải phóng bãi container bốc dỡ, điều động nhân công cẩu giàn STS, xếp dỡ sà lan và xe trung chuyển nội địa.
     * **Nhóm Trung hạn / Ngoài khơi (`72h - 168h` / 3 đến 7 ngày):** Giai đoạn tàu hành trình ngoài biển mở, chịu ảnh hưởng thời tiết/sóng gió hải lưu RTMA. Ý nghĩa nghiệp vụ: Kế hoạch tổng thể tiếp nhận tàu mẹ của cảng, tối ưu hóa khung giờ cập bến (berth window), giảm chi phí phạt lưu tàu (demurrage).
       Viết tài liệu **Giải thích phân tầng 168h mới** thay thế bản cũ đã xóa. Phụ trách: **Trần Hồng Lĩnh**.
5. **Quy đổi Tài chính USD / Business ROI và Đánh giá Mất mát Bất đối xứng (M6/M7):**
   - **Hiện trạng:** Đã có kết quả thực nghiệm M6 Asymmetric Loss (`m6_asym_*`) và M7 Conformal Prediction (`m7_conformal_*`).
   - **Yêu cầu hoàn thiện:** Xây dựng bảng quy đổi tài chính thực tế cho doanh nghiệp cảng biển phân rã theo 3 nhóm chân trời thời gian: tham chiếu đơn giá nhân công bốc xếp ILWU (56.85 USD/giờ), chi phí thuê tàu theo ngày (15,800 - 90,500 USD/ngày), định lượng khoản tiết kiệm USD khi giảm tỷ lệ dự báo sớm (`Underprediction_pct`) từ M6 và độ tin cậy từ khoảng dự báo M7 Conformal (`PICP_90` vs `MPIW`). Phụ trách: **Lê Sỹ Liêm** & **Trần Hồng Lĩnh**.
6. **Tuân thủ Pháp lý & Đạo đức AI:**
   - **Yêu cầu hoàn thiện:** Rà soát và hoàn thiện tài liệu tuân thủ **Luật Bảo vệ dữ liệu cá nhân**, và soạn thảo mục **Khai báo sử dụng AI** minh bạch theo chuẩn liêm chính học thuật. Phụ trách: **Nguyễn Hữu Bảo Lộc**.
7. **Hồ sơ Quản lý Nhóm cuối kỳ (`08_QuanLyNhom/`):**
   - **Yêu cầu hoàn thiện:** Hoàn thiện Nhật ký thực nghiệm tổng hợp, Scope Changelog (lý giải điều chỉnh từ Engine v1 sang Engine v2), tập hợp Biên bản họp nhóm giai đoạn sau Lab 3 và Bảng tự đánh giá đóng góp % của 7 thành viên. Phụ trách: **Đỗ Văn Lộc**.

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

|  STT  | Thành viên & MSSV                   | Vai trò chuyên trách                      | Đường dẫn thư mục cá nhân                                   | Tệp hướng dẫn riêng                                                                                                |
| :---: | :---------------------------------- | :---------------------------------------- | :---------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
|   1   | **Võ Đình Kiên** *(24520893)*       | Nhóm trưởng, Quản trị dự án & Kiến trúc   | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_01_VoDinhKien/`      | [`Thanh_Vien_01_VoDinhKien/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_01_VoDinhKien/README.md)           |
|   2   | **Đỗ Văn Lộc** *(24520977)*         | Thư ký, Kỹ sư Demo Web `app.py` & Slide   | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_02_DoVanLoc/`        | [`Thanh_Vien_02_DoVanLoc/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_02_DoVanLoc/README.md)               |
|   3   | **Quách Tuấn Kiệt** *(24520911)*    | Kỹ sư Dữ liệu mẫu & Chất lượng DAMA       | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_03_QuachTuanKiet/`   | [`Thanh_Vien_03_QuachTuanKiet/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_03_QuachTuanKiet/README.md)     |
|   4   | **Huỳnh Chí Kiên** *(24520880)*     | Chuyên viên EDA, Biểu đồ & XAI (SHAP)     | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_04_HuynhChiKien/`    | [`Thanh_Vien_04_HuynhChiKien/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_04_HuynhChiKien/README.md)       |
|   5   | **Nguyễn Hữu Bảo Lộc** *(24520983)* | Chuyên viên SOTA IEEE & Đạo đức AI        | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_05_NguyenHuuBaoLoc/` | [`Thanh_Vien_05_NguyenHuuBaoLoc/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_05_NguyenHuuBaoLoc/README.md) |
|   6   | **Lê Sỹ Liêm** *(24520951)*         | Chuyên viên Kiểm định Thống kê & ROI Cảng | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_06_LeSyLiem/`        | [`Thanh_Vien_06_LeSyLiem/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_06_LeSyLiem/README.md)               |
|   7   | **Trần Hồng Lĩnh** *(24520970)*     | Kỹ sư ML/DL, Error Analysis Case Study    | `06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_07_TranHongLinh/`    | [`Thanh_Vien_07_TranHongLinh/README.md`](../06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_07_TranHongLinh/README.md)       |

---

## PHẦN D: PHÂN CÔNG CHI TIẾT 7 CHƯƠNG BÁO CÁO VÀ CÁC SẢN PHẨM CUỐI KỲ

### 1. Ma trận phân công Báo cáo Đồ án Cuối kỳ 7 Chương (30-50 trang)

| Chương báo cáo | Tên chương nội dung                               | Thành viên phụ trách chính                                                                 | Nội dung cốt lõi cần hoàn thành                                                                                                                                                                                                                      | Nguồn số liệu chính thức                                                                                                  |
| :------------: | :------------------------------------------------ | :----------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------ |
|  **Chương 1**  | **Tổng quan và Bối cảnh nghiệp vụ**               | **Đỗ Văn Lộc** *(Chính)* & **Nguyễn Hữu Bảo Lộc** *(SOTA)*                                 | Bối cảnh logistics cảng biển, chi phí trễ/sớm ETA, mục tiêu SMART, tổng quan 6 bài báo SOTA (Springer, Elsevier) và bảng đối sánh quốc tế.                                                                                                           | `00_Quan_Ly_Va_Tai_Lieu_Chung/` & tệp `TongQuan_RelatedWork_ETA_6BaiBao_v2.xlsx`                                          |
|  **Chương 2**  | **Dữ liệu và Đo lường Chất lượng Dữ liệu**        | **Quách Tuấn Kiệt**                                                                        | Kiểm kê 7 tiêu chí NOAA AIS 2025, từ điển 18/22/27 thuộc tính, đo lường chất lượng 6 chiều DAMA-DMBOK trên 256.94M bản ghi `RAW18`.                                                                                                                  | `05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/DAMA/`                                                        |
|  **Chương 3**  | **Phương pháp Tiền xử lý Dữ liệu**                | **Huỳnh Chí Kiên**                                                                         | Kiến trúc 2-Pass Rolling Stream, bộ lọc 3 tầng, Domain-based Imputation (khôi phục khuyết thiếu về 0.00%), chế tác đặc trưng thân vỏ $Area, Volume$.                                                                                                 | `05_Output_Cac_Notebook/06_DS317_Tong_Hop_Xuat_So_Lieu_BTVN/IMPUTE_BENCHMARK/`                                            |
|  **Chương 4**  | **Phương pháp Nghiên cứu & Thiết kế Thực nghiệm** | **Lê Sỹ Liêm**                                                                             | Phát biểu bài toán KPDL, kịch bản Expanding Window 3 Folds, hàm mất mát Custom Asymmetric Loss, các độ đo kỹ thuật và nghiệp vụ ($AsymCost$), thiết kế phân tầng 3 nhóm chân trời thời gian (`< 24h`, `24h - 72h`, `72h - 168h`).                    | `03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md`                                     |
|  **Chương 5**  | **Kết quả Thực nghiệm & Phân tích Đánh giá**      | **Trần Hồng Lĩnh** *(Chủ trì)*, **Huỳnh Chí Kiên**, **Lê Sỹ Liêm**, **Nguyễn Hữu Bảo Lộc** | Đối chuẩn Baseline B0 trên 7 mô hình, Ablation Study 7 Module (M1-M7), giải thích SHAP XAI, kiểm định thống kê $p$-value, phân tích Case Study lỗi phân tầng 3 nhóm thời gian (`< 24h`, `24h - 72h`, `72h - 168h`) và quy đổi ROI kinh tế cảng biển. | `05_Output_Cac_Notebook/07_Runner_Song_Song_1_Baseline_M1_M2_M3/results/` và `08_Runner_Song_Song_2_M4_M5_M6_M7/results/` |
|  **Chương 6**  | **Kiến trúc Ứng dụng & Triển khai Doanh nghiệp**  | **Đỗ Văn Lộc**                                                                             | Sơ đồ kiến trúc Web Demo Streamlit, kịch bản tích hợp hệ thống điều độ cảng biển JIT, các ca sử dụng giao diện và phân cấp rủi ro ETA theo 3 nhóm chân trời.                                                                                         | Thư mục `07_Demo/` và mã nguồn `app.py`                                                                                   |
|  **Chương 7**  | **Kết luận và Hướng phát triển**                  | **Võ Đình Kiên** *(Nhóm trưởng)*                                                           | Tóm tắt các kết quả đạt được, giá trị kinh tế thực tiễn, các hạn chế còn tồn đọng và định hướng mở rộng đề tài trong tương lai.                                                                                                                      | Tổng hợp toàn bộ các chương                                                                                               |

---

### 2. Phân công các sản phẩm Kỹ thuật và Demo bàn giao

1. **Ứng dụng Demo Web Streamlit (`app.py`):**
   - **Đỗ Văn Lộc:** Lập trình giao diện, kết nối model, trực quan hóa bản đồ hải trình và phân bổ cầu bến JIT theo 3 nhóm chân trời.
   - **Quách Tuấn Kiệt:** Trích xuất bộ dữ liệu mẫu chuẩn (1,000 - 5,000 dòng có phân bổ đại diện đủ cả 3 nhóm thời gian `< 24h`, `24h - 72h`, `72h - 168h` trong mốc <= 168h).
   - **Võ Đình Kiên:** Kiểm thử môi trường `requirements.txt` và đóng gói triển khai.
2. **Bộ Slide Thuyết trình Bảo vệ Cuối kỳ:**
   - **Đỗ Văn Lộc:** Thiết kế layout đồ họa, cấu trúc 10-12 slides.
   - **Huỳnh Chí Kiên:** Cung cấp toàn bộ biểu đồ và hình ảnh chất lượng cao (DPI >= 300), bao gồm biểu đồ phân bố sai số residual và MAE theo 3 nhóm thời gian.
   - **Võ Đình Kiên:** Tổng duyệt nội dung học thuật và speaker notes.
3. **Kiểm định Thống kê & Bảng tính ROI Doanh nghiệp:**
   - **Lê Sỹ Liêm:** Chạy script kiểm định Wilcoxon, Paired Bootstrap 2,000 lần ($p < 0.001$) và xây dựng Bảng quy đổi giá trị kinh tế / Business ROI cảng biển phân rã chi tiết theo 3 nhóm chân trời thời gian (`< 24h`, `24h - 72h`, `72h - 168h`).
4. **Phân tích Lỗi Case Study & Giải thích Phân tầng 3 Nhóm Chân trời:**
   - **Trần Hồng Lĩnh:** Trích xuất các case study tàu biển sai số cực trị và hoàn thiện báo cáo phân tích lỗi dạng Case Study chi tiết theo 3 nhóm thời gian (`< 24h`, `24h - 72h`, `72h - 168h`), giải thích cơ chế sai số vật lý/hàng hải khi tàu từ ngoài khơi tiến dần vào gần cảng.
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
