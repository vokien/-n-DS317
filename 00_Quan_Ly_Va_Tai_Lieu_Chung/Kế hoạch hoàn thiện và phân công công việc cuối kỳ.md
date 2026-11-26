# Kế Hoạch Hoàn Thiện và Phân Công Công Việc Cuối Kỳ - Nhóm 03 (DS317.R11)

- **Học phần:** DS317 - Khai phá dữ liệu trong doanh nghiệp (UIT)
- **Đề tài:** Dự báo thời điểm cập cảng của tàu biển thay thế ETA tự khai báo (*Prediction of Vessel Port Arrival Time Replacing Self-Reported ETA*)
- **Kho lưu trữ chuẩn:** `DS317_DoAn_Nhom03_TongHop/` | **Thư mục nộp bài chuẩn 8 phần:** [`DS317_R11_Nhom03_HoSoNopDoAn/`](../DS317_R11_Nhom03_HoSoNopDoAn/README.md)
- **Phạm vi tài liệu này:** Chốt hiện trạng kho lưu trữ, liệt kê đầy đủ các hạng mục thiếu/sai lệch từ rà soát đối chiếu với [`DS317_Yeu_cau_noi_dung_do_an.pdf`](../DS317_Yeu_cau_noi_dung_do_an.pdf), và **phân công ngay giai đoạn Kỹ thuật, Thực nghiệm & Demo** cho 7 thành viên. Các phần **Báo cáo cuối kỳ, Slide bảo vệ và Phân vai thuyết trình** được giữ lại cho giai đoạn sau (**chưa phân công**).

---

## Mục 0: Cập Nhật Trạng Thái Vừa Xử Lý Gần Nhất (Tránh Làm Trùng Việc Đã Xong)

Để các thành viên nắm đúng phiên bản mới nhất trên nhánh `main` và không thực hiện lại các đầu việc đã hoàn thành:

1. **Đã xóa bỏ các tệp lỗi / số liệu Engine v1 hoặc tệp trung gian gây nhiễu:**
   - Xóa `03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Giai_Thich_Chenh_Lech_So_Lieu_Phan_Tang_168h.md` (sẽ viết lại bằng phân tích lỗi có kiểm chứng từ dự đoán thật sau khi chạy lại Runner).
   - Xóa `03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Bao_cao_Modules/Bao_cao_Thuc_nghiem_Ablation_Module_M7_LeSyLiem.md` (dùng số liệu Engine v1 cũ).
   - Xóa `table_4_3_dama_comparison_raw_vs_base22.csv`, `old_numbers_verification.csv`, và `Huong_dan_cap_nhat_BaiTapVeNha.md` trong `04_So_Lieu_Kiem_Ke_Va_Bieu_Do/So_Lieu_Sau_Chay_Lai/`.
2. **Đã sửa sạch sai lệch số liệu trên các tệp README:**
   - Cập nhật [`README.md`](../README.md): chuẩn hóa `256,935,254` bản ghi thô sau chia (`01_ban_tho_18_thuoc_tinh`) so với `320,776,922` bản ghi trước chia (`pre-split`), và kiểm kê chuẩn tệp thô (`31` tệp `.csv.zst` + `1` tệp `.zip` + `1` tệp `.tif` = `33` tệp, tổng `13.15 GB`).
   - Cập nhật [`BT1_Xac_Dinh_Bai_Toan/README.md`](../01_Bai_Tap_Ve_Nha_Chinh_Thuc/BT1_Xac_Dinh_Bai_Toan/README.md), [`BT2_Do_Luong_Chat_Luong_Du_Lieu/README.md`](../01_Bai_Tap_Ve_Nha_Chinh_Thuc/BT2_Do_Luong_Chat_Luong_Du_Lieu/README.md), và [`BT3_Thuyet_Minh_De_Tai/README.md`](../01_Bai_Tap_Ve_Nha_Chinh_Thuc/BT3_Thuyet_Minh_De_Tai/README.md) (mục 2 cập nhật DAMA 6 chiều `RAW18` vs `Base22` và Pearson `r = +0.2589 -> +0.50971`).
3. **Đã nâng cấp mã nguồn thực nghiệm & kiểm kê (đang chờ chạy lại trên Kaggle):**
   - Nâng cấp [`DS317_Runner_Song_Song_1_Baseline_M1_M2_M3.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/02_Runner_Song_Song_Chinh_Thuc_v2/DS317_Runner_Song_Song_1_Baseline_M1_M2_M3.ipynb) và [`DS317_Runner_Song_Song_2_M4_M5_M6_M7.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/02_Runner_Song_Song_Chinh_Thuc_v2/DS317_Runner_Song_Song_2_M4_M5_M6_M7.ipynb): tách `eval_meta_fold{1,2,3}.parquet` + `pred_*.parquet` nén `zstd`, xuất sidecar `*_meta.json` kèm trọng số trong `saved_models/`, và đóng gói `runner{1,2}_saved_models.zip` tách riêng khỏi `runner{1,2}_results.zip` (an toàn dưới trần `20 GB` của Kaggle).
   - Nâng cấp [`DS317_02_Kham_Pha_Kiem_Ke_Chat_Luong.ipynb`](../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_02_Kham_Pha_Kiem_Ke_Chat_Luong.ipynb) để xuất đầy đủ số liệu cho cả bản thô (`01_ban_tho_18_thuoc_tinh`) và bản 26 đặc trưng (`03_ban_tien_xu_ly_27_thuoc_tinh`).
   - **Lưu ý phụ thuộc:** 3 notebook trên đã sẵn sàng trên Git, hiện **đang chờ Nhóm trưởng chạy lại trên Kaggle** để sinh tệp trọng số, `detailed_predictions/` và bảng DAMA 26 đặc trưng mới.
4. **Đã khởi tạo khung 8 thư mục nộp bài chuẩn:**
   - Thư mục [`DS317_R11_Nhom03_HoSoNopDoAn/`](../DS317_R11_Nhom03_HoSoNopDoAn/README.md) đã có đủ 8 thư mục con (`01_BaoCao/` đến `08_QuanLyNhom/`).

---

## PHẦN A: CÁC NỘI DUNG & TIÊU CHÍ CHƯA HOÀN THÀNH (BẮT BUỘC BỔ SUNG)

### 1. Nhóm sản phẩm bàn giao bắt buộc (Chiếm 100% điểm A4)

| STT | Hạng mục bắt buộc (theo quy định môn học) | Tỷ trọng / Vai trò | Thư mục đích | Trạng thái hiện tại / Quyết định điều phối |
| :-: | :--- | :--- | :--- | :--- |
| 1 | **Chương trình Demo Web/App tương tác (`app.py`)** (kết nối trọng số thật, tích hợp BI Dashboard & dự báo ETA) | **50%** điểm sản phẩm A4 | `03_SourceCode/` & `07_Demo/` | **Chưa có (0%)** - Đã phân công **Đỗ Văn Lộc** (Mục C) |
| 2 | **Chạy lại Runner 1, Runner 2 & `DS317_02` trên Kaggle** để lấy Trọng số (`saved_models`), `detailed_predictions/*.parquet` và số liệu DAMA 26 đặc trưng | Đầu vào bắt buộc cho Demo, SHAP, Kiểm định & Phân tích lỗi | `05_Model/` & `06_Results/` | **Đã nâng cấp code, chờ chạy Kaggle** - Đã phân công **Võ Đình Kiên** (Mục C) |
| 3 | **Báo cáo Đồ án Cuối kỳ 7 Chương** (`.docx` & `.pdf`, 30-50 trang) | **30%** điểm sản phẩm A4 | `01_BaoCao/` | **Chưa có (0%)** - **Để làm sau, chưa phân công** (Mục D) |
| 4 | **Bộ Slide Bảo vệ Cuối kỳ 10 phần** (`.pptx` & `.pdf`) | **20%** điểm sản phẩm A4 | `02_Slides/` | **Chưa có (0%)** - **Để làm sau, chưa phân công** (Mục D) |
| 5 | **Bộ dữ liệu mẫu chạy Demo & `requirements.txt`** (1,000-5,000 dòng đầy đủ 27 đặc trưng + RTMA, kèm hướng dẫn cài đặt môi trường) | Điều kiện nghiệm thu Demo & tái lập mã nguồn | `04_Data/` & `03_SourceCode/` | **Chưa có (0%)** - Đã phân công **Quách Tuấn Kiệt** (dữ liệu mẫu) & **Võ Đình Kiên** (`requirements.txt`) (Mục C) |

### 2. Nhóm tiêu chí Kỹ thuật, Biểu đồ & Học thuật còn thiếu hoàn toàn (0%)

1. **Kiểm định ý nghĩa thống kê chính thức (Statistical Significance Testing):**
   - Hiện mới có trung bình MAE/RMSE qua 3 fold; chưa có kiểm định `Wilcoxon signed-rank test`, `Diebold-Mariano test` hoặc `Paired Bootstrap` (ví dụ 2,000 lần) kèm `p-value` trên dự đoán từng bản ghi giữa Baseline `B0` và các mô hình/biến thể tốt nhất.
2. **Biểu đồ Chương 4 & Chương 5 chuẩn cho Engine v2 (`DPI >= 300`):**
   - Thư mục biểu đồ hiện có mới dừng ở EDA/DAMA và BT5; còn thiếu toàn bộ biểu đồ Engine v2: sơ đồ kiến trúc Engine v2 + BI Dashboard, biểu đồ so sánh 7 mô hình theo tầng `All / LE_168h / GT_168h`, biểu đồ Delta Ablation `M1-M7`, biểu đồ `PICP_90` vs `MPIW` (M7), biểu đồ `AsymCost` / Business ROI (M6), và biểu đồ phân tích residual theo phân tầng `168h`.
3. **Ứng dụng BI Dashboard chạy được thực tế:**
   - Trong `04_So_Lieu_Kiem_Ke_Va_Bieu_Do/Hinh_Anh_Bieu_Do_Chung/` mới có ảnh mockup tĩnh `Hinh_PL1_Mockup_Demo_Streamlit.png`, chưa có mã nguồn Dashboard BI chạy được (giám sát chất lượng dữ liệu 6 chiều DAMA, cảnh báo Data Drift PSI/JSD, theo dõi hành trình tàu và hiệu năng mô hình).
4. **Phân tích lỗi Case Study có kiểm chứng (Error Analysis):**
   - Sau khi xóa bản cũ sai cơ chế, hiện chưa có bảng Case Study mẫu tàu/MMSI thật có residual lớn nhất ở cả 2 tầng `<= 168h` và `> 168h` kèm đối chiếu `Dist_To_Berth_NM`, `sog`, `vessel_type` từ `eval_meta_fold3.parquet` + `pred_*_fold3.parquet`.
5. **Tuân thủ Pháp lý & Đạo đức AI:**
   - Chưa có tài liệu rà soát tuân thủ **Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15**, **Luật Dữ liệu 60/2024/QH15** (cơ chế ẩn danh hóa định danh `MMSI` -> `Vessel_Hash_ID`), và mục **Khai báo sử dụng AI** theo chuẩn liêm chính học thuật.
6. **Hồ sơ Quản lý Nhóm cuối kỳ (`08_QuanLyNhom/`):**
   - Chưa có Nhật ký thực nghiệm tổng hợp, Scope Changelog (lý giải điều chỉnh phạm vi từ Engine v1 sang Engine v2), Biên bản họp nhóm giai đoạn sau Lab 3, và Bảng tự đánh giá đóng góp % của 7 thành viên cho giai đoạn cuối kỳ.

---

## PHẦN B: CÁC NỘI DUNG CÓ THỂ LÀM TỐT HƠN & LỖI VÊNH SỐ LIỆU CẦN XỬ LÝ

### 1. Trạng thái khắc phục các sai lệch số liệu

- **Các điểm đã xử lý dứt điểm (đã hoàn tất trong kho lưu trữ):**
  - Đã xóa `Giai_Thich_Chenh_Lech_So_Lieu_Phan_Tang_168h.md` để làm lại từ dữ liệu dự đoán thật của Engine v2.
  - Đã xóa `Bao_cao_Thuc_nghiem_Ablation_Module_M7_LeSyLiem.md` dùng số liệu Engine v1 cũ.
  - Đã sửa đồng bộ các số liệu DAMA/tương quan/kiểm kê trong `README.md` gốc và `BT1` -> `BT3/README.md`.
- **Các điểm còn tồn đọng cần đối chiếu khi tổng hợp sau này:**
  - 03 báo cáo Word trong [`03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Bao_cao_Modules/`](../03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Bao_cao_Modules/) (`Bao_cao_Thuc_nghiem_Module_M3_Ablation_Study.docx`, `BaoCao_M5.docx`, `Bao_cao_Thuc_nghiem_Module_M6.docx`) hiện vẫn đang lưu **số liệu Engine v1 cũ** (chưa khớp với bảng Engine v2 trong [`Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md`](../03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md)). Cần đối chiếu số liệu Engine v2 mới trước khi đưa vào Chương 5 Báo cáo cuối kỳ.
  - Tài liệu [`Lab3_DS317.R11_Nhom03_ThuyetMinh.docx`](../01_Bai_Tap_Ve_Nha_Chinh_Thuc/BT3_Thuyet_Minh_De_Tai/Lab3_DS317.R11_Nhom03_ThuyetMinh.docx) (Bảng 10.1) ghi mốc đối chứng `15.79h` thuộc hồ sơ Lab 3 cũ (trên phạm vi dữ liệu khác Engine v2); khi viết Chương 5 Báo cáo cuối kỳ cần chú thích rõ bối cảnh mốc cũ và đối chiếu sang hệ quy chiếu Engine v2 (`LE_168h` MAE `21.64h - 24.94h`, `All` MAE `110.12h - 114.85h`).

### 2. Các điểm chuyên sâu nâng cấp để đạt mức 9.0-10.0

1. **Giải thích mô hình bằng SHAP (`SHAP Summary Plot` & `SHAP Beeswarm Plot`):**
   - Thực hiện phân tích đóng góp đặc trưng SHAP trên mô hình tốt nhất của Engine v2 (`CatBoost` / `XGBoost` / `LightGBM` nạp từ `05_Model/`) để làm rõ tác động của `Dist_To_Berth_NM`, `sog`, biến tương tác M3, thời tiết RTMA M4.
2. **Bảng Quy đổi Tài chính USD / ROI cụ thể cho cảng biển:**
   - Quy đổi mức giảm MAE tầng `<= 168h` và mức giảm tỷ lệ dự báo sớm (`Underprediction_pct`) ở M6 sang chi phí vận hành thực tế (tham chiếu đơn giá nhân công bốc xếp ILWU `56.85 USD/giờ` và chi phí thuê tàu `15,800-90,500 USD/ngày` đã nêu trong bối cảnh bài toán).
3. **Chuẩn hóa định dạng `.docx` & Phân vai Thuyết trình 7 người (làm sau):**
   - Khi soạn thảo Báo cáo cuối kỳ (`01_BaoCao/`), thống nhất dấu chấm thập phân `.`, sử dụng dấu gạch ngang chuẩn ASCII `-` thay cho ký tự `en-dash (U+2013)` hoặc `em-dash (U+2014)`, đánh số Caption Bảng/Hình liên tục, và xây dựng kịch bản thuyết trình chia đều cho cả 7 thành viên.

---

## PHẦN C: BẢNG PHÂN CÔNG CHI TIẾT CHO 7 THÀNH VIÊN NHÓM 03 (Giai đoạn Kỹ thuật, Thực nghiệm & Demo - Thực hiện ngay)

**Nguyên tắc kế thừa:** Mỗi thành viên tiếp nhận đúng đầu việc phù hợp với chuỗi BTVN (`BT1-BT5`) và Module (`M1-M7`) đã thực hiện.

**Thứ tự phụ thuộc thực thi:**
- **Đợt 1 (Mở khóa dữ liệu & trọng số):** **Võ Đình Kiên** chạy lại `Runner 1`, `Runner 2` và `DS317_02` trên Kaggle để cấp `05_Model/`, `detailed_predictions/*.parquet` và DAMA 26 đặc trưng; song song **Nguyễn Hữu Bảo Lộc** chuẩn hóa tài liệu Pháp lý/Đạo đức AI và **Đỗ Văn Lộc** dựng khung `Streamlit` + `BI Dashboard`.
- **Đợt 2 (Phân tích sâu từ trọng số & dự đoán thật):** Ngay khi có `05_Model/` và `detailed_predictions/`, **Quách Tuấn Kiệt**, **Huỳnh Chí Kiên**, **Lê Sỹ Liêm**, **Trần Hồng Lĩnh** đồng loạt trích xuất bộ mẫu Demo, chạy SHAP, kiểm định thống kê, tính ROI USD, kiểm chứng Case Study lỗi 168h và xuất trọn bộ biểu đồ Engine v2 (`DPI >= 300`); **Đỗ Văn Lộc** ghép trọng số thật + bộ mẫu Demo vào app hoàn chỉnh và quay video dự phòng.

| STT | Thành viên & MSSV | Nền tảng BTVN & Module đã làm | Nhiệm vụ chi tiết giai đoạn Kỹ thuật, Thực nghiệm & Demo | Sản phẩm bàn giao & Thư mục đích |
| :-: | :--- | :--- | :--- | :--- |
| 1 | **Võ Đình Kiên** (`24520893` - Nhóm trưởng) | Master Pipeline, Big Data/PyArrow, `M4 RTMA`, quản lý Repo & MLOps | 1. Chạy lại `Runner 1`, `Runner 2` và `DS317_02` trên Kaggle; thu thập `runner{1,2}_results.zip`, `runner{1,2}_saved_models.zip`, `eval_meta_fold*.parquet` + `pred_*_fold3.parquet`.<br>2. Tạo `requirements.txt` & hướng dẫn tái lập môi trường.<br>3. Chủ trì Nhật ký thực nghiệm tổng hợp, `Scope Changelog`, và Bảng tổng hợp 7 mô hình Engine v2. | - `05_Model/` (trọng số + `*_meta.json`)<br>- `06_Results/` (CSV + `detailed_predictions/`)<br>- `03_SourceCode/requirements.txt` & README tái lập<br>- `08_QuanLyNhom/` (Experiment Log, Scope Changelog) |
| 2 | **Đỗ Văn Lộc** (`24520977` - Thư ký) | Mockup Web Demo Mục 9, `M2 Điền khuyết`, độ đo nghiệp vụ | 1. Lập trình **Ứng dụng Web Demo Streamlit (`app.py`)** kết hợp **BI Dashboard tương tác** (giám sát CLDL 6 chiều DAMA, cảnh báo Data Drift PSI/JSD, suy luận ETA từ trọng số thật trong `05_Model/`, diễn giải điều độ cảng).<br>2. Soạn kịch bản demo và quay **Video màn hình dự phòng (`<= 3` phút)**.<br>3. Tập hợp Biên bản họp nhóm giai đoạn sau Lab 3 và Bảng tự đánh giá đóng góp % của 7 thành viên. | - `03_SourceCode/app.py` (hoặc module Demo)<br>- `07_Demo/` (code Demo, hướng dẫn chạy, video `<= 3` phút)<br>- `08_QuanLyNhom/` (Meeting Minutes, Bảng đánh giá % 7 thành viên) |
| 3 | **Quách Tuấn Kiệt** (`24520911`) | Data Inventory 7 tiêu chí, 6 chiều DAMA BT2, `M3 Feature Creation` | 1. Trích xuất **Bộ dữ liệu mẫu chạy Demo** (`1,000-5,000` bản ghi đầy đủ 27 đặc trưng + RTMA khớp schema để app Demo chạy `< 3` giây).<br>2. Tổng hợp kết quả chạy mới của `DS317_02` (DAMA 6 chiều Trước/Sau đồng nhất công thức + Từ điển 27 thuộc tính) làm đầu vào tab BI Monitoring của Demo và đối chiếu số liệu M3 sang Engine v2. | - `04_Data/` (tệp mẫu Demo + Data Dictionary 27 cột + link dữ liệu lớn)<br>- `06_Results/` (bảng DAMA 18 vs 27 cột từ `DS317_02` + bảng đối chiếu M3 Engine v2) |
| 4 | **Huỳnh Chí Kiên** (`24520880`) | Biểu đồ EDA `DPI >= 300`, Tiền xử lý, `M1 Ngoại lai`, phối hợp SHAP | 1. Chạy **SHAP (`SHAP Summary Plot`, `SHAP Beeswarm Plot`)** trên mô hình tốt nhất của Engine v2 (`CatBoost` / `XGBoost` / `LightGBM` nạp từ `05_Model/`).<br>2. Thiết kế trọn bộ **Biểu đồ Chương 4 & Chương 5 chuẩn `DPI >= 300` cho Engine v2**: Kiến trúc Engine v2 + BI Dashboard, So sánh 7 mô hình (`All / LE_168h / GT_168h`), Delta Ablation `M1-M7`, Biểu đồ phân tích lỗi/residual và phân tầng `168h`. | - `06_Results/` (bộ ảnh biểu đồ SHAP + Chương 4 & 5 `DPI >= 300` và mã nguồn vẽ biểu đồ trong `03_SourceCode/`) |
| 5 | **Nguyễn Hữu Bảo Lộc** (`24520983`) | Khảo sát SOTA, trích dẫn IEEE `references.bib`, `M5 Chọn lọc MI & log1p` | 1. Nghiên cứu và chuẩn hóa tài liệu **Tuân thủ Pháp lý & Đạo đức AI** (Luật Bảo vệ dữ liệu cá nhân `91/2025/QH15`, Luật Dữ liệu `60/2024/QH15`, cơ chế ẩn danh hóa `MMSI` -> `Vessel_Hash_ID`) và soạn khung **Khai báo sử dụng AI**.<br>2. Đối chiếu và cập nhật số liệu **M5 (`MI12`, `log1p`)** từ Engine v2 phục vụ tổng hợp báo cáo sau này. | - Tài liệu Pháp lý, Đạo đức AI & Khai báo AI (lưu tại `08_QuanLyNhom/` hoặc `00_Quan_Ly_Va_Tai_Lieu_Chung/` để ghép vào `01_BaoCao/`)<br>- Bảng đối chiếu M5 Engine v2 trong `06_Results/` |
| 6 | **Lê Sỹ Liêm** (`24520951`) | Time-based Split, giám sát PSI BT4, `M7 Conformal`, độ đo kỹ thuật & nghiệp vụ | 1. Thực hiện **Kiểm định ý nghĩa thống kê chính thức & Kiểm tra độ ổn định Engine v2**: chạy `Wilcoxon signed-rank test`, `Diebold-Mariano test` / `Paired Bootstrap 2,000 lần` (`p-value`) trên `detailed_predictions/*.parquet` giữa `B0` và các mô hình/biến thể tốt nhất, kèm phân tích ổn định 3-Fold.<br>2. Xuất **Biểu đồ Conformal `PICP_90` vs `MPIW`** (`m7_ablation_intervals_comparison.png` chuẩn Engine v2) và xây dựng **Bảng Quy đổi Tài chính USD / ROI cụ thể cho cảng biển** (đơn giá ILWU `56.85 USD/h`, thuê tàu `15,800-90,500 USD/ngày`, mức giảm Early Prediction M6 & MAE `<= 168h`). | - `06_Results/` (bảng CSV/MD kết quả kiểm định thống kê `p-value`, phân tích 3-Fold, ảnh `m7_ablation_intervals_comparison.png`, Bảng quy đổi USD/ROI)<br>- Script kiểm định trong `03_SourceCode/` |
| 7 | **Trần Hồng Lĩnh** (`24520970`) | Baseline & GBDT, `M6 Asymmetric Loss`, phối hợp SHAP Error Analysis | 1. Thực hiện **Phân tích lỗi dạng Case Study có kiểm chứng (Error Analysis)** trực tiếp từ `eval_meta_fold3.parquet` + `pred_*_fold3.parquet` (trích mẫu tàu/`MMSI` thật có residual lớn nhất ở cả tầng `<= 168h` và `> 168h`, kiểm tra `Dist_To_Berth_NM`, `sog`, `vessel_type`), viết lại tài liệu **Giải thích phân tầng 168h mới** thay thế bản cũ đã xóa.<br>2. Xuất **Biểu đồ Business ROI / `AsymCost` M6** và đối chiếu số liệu M6 từ Engine v2. | - `03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/` & `06_Results/` (bài phân tích lỗi Case Study + Giải thích phân tầng 168h mới từ dữ liệu thật, biểu đồ ROI/`AsymCost` M6, bảng đối chiếu M6 Engine v2) |

---

## PHẦN D: CÁC HẠNG MỤC ĐỂ LÀM SAU - CHƯA PHÂN CÔNG

Theo chỉ đạo của Nhóm trưởng, các nội dung tổng hợp trình bày dưới đây **chưa phân công** trong đợt này và sẽ được triển khai ngay sau khi toàn bộ Phần C hoàn tất:

1. **Viết và hợp nhất Báo cáo Đồ án Cuối kỳ 7 Chương (`01_BaoCao/` - `.docx` & `.pdf`, 30-50 trang):**
   - Bao gồm việc tổng hợp kết quả từ Phần C, thay thế toàn bộ số liệu Engine v1 cũ trong các bản `.docx` (`M3`, `M5`, `M6`), chú thích đối chiếu mốc `15.79h` của Lab 3 cũ, chuẩn hóa dấu chấm thập phân `.`, dùng dấu gạch ngang chuẩn `-` (không dùng `en-dash` hay `em-dash`), và đánh số `Table/Figure Caption` thống nhất.
2. **Thiết kế Bộ Slide Bảo vệ Cuối kỳ 10 phần (`02_Slides/` - `.pptx` & `.pdf`):**
   - Đưa toàn bộ kết quả Engine v2, SHAP, kiểm định thống kê, bảng quy đổi USD/ROI và ảnh/video Demo vào bộ slide bảo vệ chuẩn học phần.
3. **Phân vai Thuyết trình 7 thành viên & Kịch bản Q&A phản biện:**
   - Phân chia thời lượng trình bày đồng đều đảm bảo cả 7 thành viên đều thuyết trình trước lớp, kèm danh sách câu hỏi phản biện dự kiến và phương án trả lời.
