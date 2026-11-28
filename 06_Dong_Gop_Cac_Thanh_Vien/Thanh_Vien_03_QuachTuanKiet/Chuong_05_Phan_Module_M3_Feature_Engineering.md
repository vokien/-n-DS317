# BÁO CÁO ĐÓNG GÓP HỌC THUẬT CHƯƠNG 5:
## PHẦN MODULE M3 - KỸ THUẬT CHẾ TÁC ĐẶC TRƯNG MỚI (FEATURE ENGINEERING) VÀ ĐÁNH GIÁ BÓC TÁCH (ABLATION STUDY) TRÊN ENGINE V2

- **Học phần:** DS317 - Khai phá dữ liệu trong doanh nghiệp (UIT - ĐHQG-HCM)
- **Đề tài:** Dự báo thời điểm cập cảng của tàu biển thay thế ETA tự khai báo (*Prediction of Vessel Port Arrival Time Replacing Self-Reported ETA*)
- **Thành viên phụ trách:** **Quách Tuấn Kiệt** (MSSV: **24520911**) - Kỹ sư Dữ liệu & Phụ trách Module M3
- **Tệp kết quả nguồn Engine v2:** `03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md` và `05_Output_Cac_Notebook/07_Runner_Song_Song_1_Baseline_M1_M2_M3/results/m3_features_*`
- **Tệp đối chiếu Engine v1:** `03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/Bao_cao_Modules/Bao_cao_Thuc_nghiem_Module_M3_Ablation_Study.docx`

---

## 1. MỤC TIÊU VÀ NGUYÊN TẮC THỰC NGHIỆM MODULE M3

Trong kiến trúc tổng thể 7 Module của đồ án DS317, **Module M3 (Tạo đặc trưng mới / Feature Engineering)** đóng vai trò trung tâm trong việc chuyển đổi các tín hiệu cảm biến thô (tọa độ GPS, vận tốc SOG, hướng di chuyển COG) thành các đại lượng vật lý mang tính động lực học hàng hải (Nautical Dynamics). 

### 1.1. Nguyên tắc bóc tách khoa học (Ablation Protocol)
- **Nguyên tắc "Cố định 6 Module, chỉ thử nghiệm 1 Module":** Toàn bộ các module khác được giữ nguyên trạng thái mặc định (M1: Clean & Partition, M2: Nội suy cơ bản, M4: Chưa nạp thời tiết RTMA, M5: IdentityPassthrough, M6: Target Log Transform, M7: Mặc định). Mọi sự cải thiện về sai số đều hoàn toàn bắt nguồn từ các đặc trưng mới được bổ sung ở M3.
- **Cam kết Zero Data Leakage tuyệt đối:** Toàn bộ 20 đặc trưng mới được vector hóa nghiêm ngặt nội trong từng chuyến đi (`trip_id`). Tại điểm bắt đầu của mỗi chuyến ($t=0$), các giá trị sai phân gia tốc và tốc độ đổi hướng được gán mặc định bằng 0.0, giá trị trung bình trượt được gán bằng chính vận tốc khởi hành $SOG[0]$. Tuyệt đối không sử dụng thông tin tương lai (No Look-Ahead Leakage).
- **Giao thức thẩm định đa tầng (Multi-tier Expanding Window 3 Folds):**
  - **Fold 1 (Q1 $\to$ Q2):** Huấn luyện trên Q1 (1,832,455 dòng) $\to$ Đánh giá trên Q2 (3,543,951 dòng).
  - **Fold 2 (Q1+Q2 $\to$ Q3):** Huấn luyện trên Q1+Q2 (4,046,198 dòng) $\to$ Đánh giá trên Q3 (3,632,498 dòng).
  - **Fold 3 (Q1+Q2+Q3 $\to$ Q4):** Huấn luyện trên Q1+Q2+Q3 (6,282,714 dòng) $\to$ Đánh giá trên Q4 (3,482,238 dòng).
  - Đánh giá song song trên 2 tầng dữ liệu: Tầng toàn cục (`All` ~ 3.55M dòng/fold) và Tầng tác nghiệp cận bến (`LE_168h` $\le 7$ ngày, chiếm **78.61%** dữ liệu, ~2.79M dòng/fold).

---

## 2. CƠ SỞ TOÁN HỌC VÀ ĐỘNG LỰC HỌC CỦA 20 ĐẶC TRƯNG MỚI (5 NHÓM ĐẶC TRƯNG)

Module M3 thiết kế chính xác 20 đặc trưng mới, phân chia thành 5 nhóm chuyên biệt:

### Bảng 5.1: Danh mục đặc tả toán học và cơ sở vật lý hàng hải của 20 đặc trưng Module M3

| Nhóm đặc trưng | Tên đặc trưng | Đơn vị | Công thức giải tích / Định nghĩa | Ý nghĩa động lực học hàng hải |
| :--- | :--- | :---: | :--- | :--- |
| **Nhóm 1: Berth Kinematics**<br>(7 đặc trưng) | `bearing_to_berth` | độ (deg) | $\text{arctan2}(\sin\Delta\lambda\cos\phi_2, \cos\phi_1\sin\phi_2 - \sin\phi_1\cos\phi_2\cos\Delta\lambda)$ | Góc phương vị trắc địa đường vòng lớn từ vị trí hiện tại tới cầu bến đích. |
| | `approach_cos` | $[-1, 1]$ | $\cos(COG - \text{bearing\_to\_berth})$ | Mức độ thẳng hướng tới bến (+1: đâm thẳng về bến, -1: đi ngược hướng bến). |
| | `approach_sin` | $[-1, 1]$ | $\sin(COG - \text{bearing\_to\_berth})$ | Mức độ trôi dạt lệch hướng (+1: lệch phải, -1: lệch trái). |
| | `v_closing` | knot | $SOG \cdot \cos(COG - \text{bearing\_to\_berth})$ | **Vận tốc tiếp cận hướng tâm:** Thành phần tốc độ thực tế rút ngắn cự ly đến cầu cảng. |
| | `v_cross` | knot | $SOG \cdot \sin(COG - \text{bearing\_to\_berth})$ | **Vận tốc lệch ngang:** Thành phần vận tốc trôi vuông góc với trục tiếp cận bến. |
| | `delta_lon` | độ | $\text{dest\_lon} - \text{current\_lon}$ | Độ lệch kinh độ trực giao tới đích. |
| | `delta_lat` | độ | $\text{dest\_lat} - \text{current\_lat}$ | Độ lệch vĩ độ trực giao tới đích. |
| **Nhóm 2: Hydrodynamics**<br>(5 đặc trưng) | `drift_cos` | $[-1, 1]$ | $\cos(Heading - COG)$ | Góc dạt dọc vỏ tàu (Leeway angle dọc) do tác động của dòng chảy. |
| | `drift_sin` | $[-1, 1]$ | $\sin(Heading - COG)$ | Góc dạt ngang vỏ tàu do tác động của gió và sóng biển. |
| | `wetted_surface_proxy` | m² | $2.56 \cdot \sqrt{\text{Length} \cdot \text{Width} \cdot \text{Draft}}$ | Diện tích mặt ướt vỏ tàu theo công thức thực nghiệm Mumford (phản ánh lực cản ma sát). |
| | `slenderness_ratio` | không thứ nguyên | $\text{Length} / \sqrt{\text{Width} \cdot \text{Draft}}$ | Hệ số thon dài thân tàu (tỷ số chiều dài trên diện tích mặt cắt ngang ngập nước). |
| | `block_draft_ratio` | m | $C_b \cdot \text{Draft}$ | Chiều sâu chìm hiệu dụng của khối thể tích choán nước tàu. |
| **Nhóm 3: Nonlinear ETA**<br>(3 đặc trưng) | `eta_kinematic_hours` | giờ | $\text{Dist\_To\_Berth\_KM} / (SOG \cdot 1.852 + \epsilon)$ | Thời gian ETA lý thuyết tuyến tính dựa trên vận tốc mặt đất hiện tại. |
| | `eta_closing_hours` | giờ | $\text{Dist\_To\_Berth\_KM} / (\max(v_{\text{closing}}, 0.5) \cdot 1.852 + \epsilon)$ | **Thời gian ETA tiếp cận thực tế:** Dựa trên tốc độ rút ngắn khoảng cách hướng bến. |
| | `log_dist_to_berth` | $\ln(\text{km})$ | $\ln(1 + \max(\text{Dist\_To\_Berth\_KM}, 0))$ | Biến đổi logarit khoảng cách giúp nén phân phối đuôi dài, hỗ trợ mô hình tuyến tính và MLP. |
| **Nhóm 4: Differentials**<br>(3 đặc trưng) | `acc_sog` | knot/h | $\Delta SOG / \Delta t$ (clipped $[-20, 20]$) | Gia tốc dọc tức thời: Nhận diện giai đoạn tàu hãm tốc cập bến hoặc tăng tốc hành trình. |
| | `rot_approx` | deg/min | $\Delta COG / \Delta t$ (chuẩn hóa góc quay $[-180, 180]$) | Tốc độ đổi hướng hành hải xấp xỉ (Rate of Turn Proxy). |
| | `dist_rate_ratio` | $[-3, 3]$ | $(\Delta \text{dist} / \Delta t) / (SOG \cdot 1.852 + \epsilon)$ | Tỷ số giữa tốc độ rút ngắn khoảng cách và tốc độ di chuyển thực tế. |
| **Nhóm 5: Rolling Stats**<br>(2 đặc trưng) | `sog_rolling_mean_3` | knot | $\text{Mean}(SOG[t-2:t])$ nội trong chuyến | Vận tốc trung bình trượt 3 bước thời gian: Lọc nhiễu cảm biến GPS và sóng biển ngắn hạn. |
| | `sog_rolling_std_3` | knot | $\text{Std}(SOG[t-2:t])$ nội trong chuyến | Độ biến động vận tốc: Đo lường mức độ bất ổn hành trình do thời tiết hoặc luồng lạch. |

---

## 3. BẢNG TỔNG HỢP MASTER ABLATION STUDY MODULE M3 TRÊN ENGINE V2

Trong khuôn khổ thực nghiệm Engine v2, Module M3 đã thực hiện tổng cộng **126 lượt chạy huấn luyện và kiểm thử** (6 biến thể M3 × 7 mô hình x 3 Folds), bao quát cả 3 họ mô hình:
1. **Họ Cây tăng áp Gradient Boosting (GBDT):** CatBoost, LightGBM, XGBoost.
2. **Họ Mạng nơ-ron học sâu chuỗi thời gian (Deep Time-Series):** Bi-LSTM, PatchTST, Temporal Fusion Transformer (TFT).
3. **Họ Mạng nơ-ron đồ thị không - thời gian (Spatio-Temporal Graph):** Spatio-Temporal Graph Neural Network (ST-GNN).

### Bảng 5.2: Bảng tổng hợp Master Ablation Study Module M3 trên Engine v2 (Trung bình 3 Fold)

| Biến thể (Số Feats) | Mô hình | MAE `All` (h) | $\Delta\text{MAE}$ vs B0 | RMSE `All` (h) | $R^2$ `All` | AsymCost (w=2.5) | PICP `All` (%) | `LE_168h` MAE (h) | $\Delta\text{LE}_{168}$ MAE | `LE_168h` $R^2$ | Train (s) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| `EXP1_G1` (27)   | Bi-LSTM      |   111.9606    |     -1.1547 (-1.02%)     |    271.4138    |   0.0304    |   183,496.3219   |    86.1224     |      23.3933      |      -0.5025 (-2.10%)       |     0.0445      |   76.4300   |
| `EXP1_G1` (27)   | CatBoost     |   110.2058    |   **-3.5457 (-3.12%)**   |  **266.8379**  | **0.0627**  | **177,375.5740** |    86.5146     |      23.5466      |      -1.3468 (-5.41%)       |     0.1221      | **11.9733** |
| `EXP1_G1` (27)   | LightGBM     |   111.1134    |     -2.8292 (-2.48%)     |    268.3554    |   0.0521    |   179,426.4216   |    86.5679     |      23.7801      |      -0.9188 (-3.72%)       |     0.0885      |   51.2333   |
| `EXP1_G1` (27)   | PatchTST     |   113.0030    |     -1.8505 (-1.61%)     |    272.9989    |   0.0190    |   185,994.8338   |    86.5159     |      23.3776      |      -0.4026 (-1.69%)       |     0.0437      |   83.2500   |
| `EXP1_G1` (27)   | ST-GNN       |   110.7295    |     -2.8430 (-2.50%)     |    269.1011    |   0.0468    |   180,386.3739   |  **86.9869**   |      23.3466      |    **-1.5977 (-6.41%)**     |     0.0567      |   67.0900   |
| `EXP1_G1` (27)   | TFT          |   114.0201    |     -0.4537 (-0.40%)     |    274.9479    |   0.0048    |   188,787.4665   |    86.0071     |    **22.9302**    |      -1.3156 (-5.43%)       |   **0.1314**    |   87.2733   |
| `EXP1_G1` (27)   | **XGBoost**  | **110.1231**  |     -3.1194 (-2.75%)     |    267.1126    |   0.0610    |   177,665.4546   |    86.2438     |      23.5078      |      -0.8450 (-3.47%)       |     0.0664      |   17.4900   |
| `EXP2_G2` (25)   | Bi-LSTM      |   113.4734    |     +0.3581 (+0.32%)     |    272.3603    |   0.0231    |   184,437.6971   |    86.3537     |      24.5923      |      +0.6965 (+2.91%)       |     -0.0807     |   88.7633   |
| `EXP2_G2` (25)   | CatBoost     |   113.4954    |     -0.2561 (-0.23%)     |    272.5444    |   0.0220    |   184,917.8168   |  **86.8698**   |      24.7887      |      -0.1047 (-0.42%)       |     0.0174      | **12.3000** |
| `EXP2_G2` (25)   | LightGBM     |   114.0610    |     +0.1184 (+0.10%)     |    273.7049    |   0.0142    |   186,593.4475   |    86.8096     |      24.8615      |      +0.1626 (+0.66%)       |     0.0234      |   57.0667   |
| `EXP2_G2` (25)   | PatchTST     |   115.4661    |     +0.6126 (+0.53%)     |    277.5750    |   -0.0137   |   192,342.7889   |    85.0723     |    **23.8933**    |      +0.1131 (+0.48%)       |   **0.0430**    |   73.6733   |
| `EXP2_G2` (25)   | **ST-GNN**   | **113.2051**  |   **-0.3674 (-0.32%)**   |  **270.7018**  | **0.0360**  | **182,032.7875** |    85.2542     |      25.5897      |      +0.6454 (+2.59%)       |     -0.1012     |   60.9633   |
| `EXP2_G2` (25)   | TFT          |   114.8900    |     +0.4162 (+0.36%)     |    275.4272    |   0.0012    |   189,037.9055   |    86.1348     |      24.3531      |      +0.1073 (+0.44%)       |     -0.0270     |   94.0200   |
| `EXP2_G2` (25)   | XGBoost      |   113.8321    |     +0.5896 (+0.52%)     |    273.7052    |   0.0144    |   186,559.9256   |    86.5081     |      24.5478      |      +0.1950 (+0.80%)       |     -0.0106     |   14.9900   |
| `EXP3_G3` (23)   | Bi-LSTM      |   112.1035    |     -1.0118 (-0.89%)     |    271.2193    |   0.0322    |   182,967.8484   |    85.7516     |      23.7005      |      -0.1953 (-0.82%)       |     -0.0119     |   85.6633   |
| `EXP3_G3` (23)   | **CatBoost** | **111.3310**  |   **-2.4205 (-2.13%)**   |  **268.9697**  | **0.0478**  | **180,251.0904** |  **86.9920**   |      23.8602      |    **-1.0332 (-4.15%)**     |     0.0966      | **13.9167** |
| `EXP3_G3` (23)   | LightGBM     |   112.3611    |     -1.5815 (-1.39%)     |    270.9238    |   0.0341    |   183,009.3393   |    86.6185     |      24.0150      |      -0.6839 (-2.77%)       |   **0.1164**    |   45.6767   |
| `EXP3_G3` (23)   | PatchTST     |   115.6201    |     +0.7666 (+0.67%)     |    276.6720    |   -0.0079   |   190,891.3356   |    86.0821     |      24.8673      |      +1.0871 (+4.57%)       |     -0.0529     |   82.1233   |
| `EXP3_G3` (23)   | ST-GNN       |   111.9303    |     -1.6422 (-1.45%)     |    269.5399    |   0.0439    |   180,708.8080   |    85.7521     |      24.2895      |      -0.6548 (-2.63%)       |     -0.0346     |   63.0633   |
| `EXP3_G3` (23)   | TFT          |   113.1234    |     -1.3504 (-1.18%)     |    271.8615    |   0.0273    |   183,995.8606   |    85.7791     |      24.4103      |      +0.1645 (+0.68%)       |     -0.0925     |   94.5000   |
| `EXP3_G3` (23)   | XGBoost      |   111.3336    |     -1.9089 (-1.69%)     |    269.3867    |   0.0451    |   180,820.8371   |    86.6625     |    **23.6696**    |      -0.6832 (-2.81%)       |     0.0707      |   14.9833   |
| `EXP4_G4` (23)   | Bi-LSTM      |   112.3439    |     -0.7714 (-0.68%)     |    271.7358    |   0.0286    |   183,901.5607   |    85.8510     |      23.4983      |      -0.3975 (-1.66%)       |     -0.0227     |   76.4667   |
| `EXP4_G4` (23)   | CatBoost     |   111.7516    |     -1.9999 (-1.76%)     |    269.3558    |   0.0450    |   180,756.1810   |  **86.7538**   |      23.9557      |    **-0.9377 (-3.77%)**     |   **0.1266**    | **11.5300** |
| `EXP4_G4` (23)   | LightGBM     |   112.1114    |     -1.8312 (-1.61%)     |    270.1725    |   0.0393    |   181,862.0655   |    86.5899     |      24.0897      |      -0.6092 (-2.47%)       |     0.0943      |   54.2200   |
| `EXP4_G4` (23)   | PatchTST     |   114.6597    |     -0.1938 (-0.17%)     |    275.7996    |   -0.0011   |   189,987.6759   |    86.0110     |    **23.4203**    |      -0.3599 (-1.51%)       |     0.0684      |   75.5000   |
| `EXP4_G4` (23)   | ST-GNN       |   112.0198    |     -1.5527 (-1.37%)     |    269.3434    |   0.0452    |   180,479.3044   |    85.8270     |      24.8705      |      -0.0738 (-0.30%)       |     -0.0029     |   56.1600   |
| `EXP4_G4` (23)   | TFT          |   113.9537    |     -0.5201 (-0.45%)     |    274.2343    |   0.0110    |   187,815.2479   |    86.2327     |      23.7308      |      -0.5150 (-2.12%)       |     0.0708      |   87.5533   |
| `EXP4_G4` (23)   | **XGBoost**  | **110.8377**  |   **-2.4048 (-2.12%)**   |  **268.5120**  | **0.0512**  | **179,515.6117** |    86.6748     |      23.5712      |      -0.7816 (-3.21%)       |     0.0697      |   16.9733   |
| `EXP5_G5` (22)   | Bi-LSTM      |   113.3465    |     +0.2312 (+0.20%)     |    274.5535    |   0.0085    |   188,005.4386   |    86.3564     |    **23.4157**    |      -0.4801 (-2.01%)       |     0.0659      |   72.8333   |
| `EXP5_G5` (22)   | CatBoost     |   113.5715    |     -0.1800 (-0.16%)     |    272.5146    |   0.0225    |   184,986.0684   |    86.8329     |      24.7594      |      -0.1340 (-0.54%)       |     0.0541      | **12.8067** |
| `EXP5_G5` (22)   | LightGBM     |   114.1194    |     +0.1768 (+0.16%)     |    273.9875    |   0.0123    |   187,079.1114   |  **86.8871**   |      24.8049      |      +0.1060 (+0.43%)       |     0.0532      |   37.5967   |
| `EXP5_G5` (22)   | PatchTST     |   114.6294    |     -0.2241 (-0.20%)     |    275.2374    |   0.0032    |   189,033.6767   |    86.0909     |      24.3031      |      +0.5229 (+2.20%)       |     -0.0038     |   77.1100   |
| `EXP5_G5` (22)   | **ST-GNN**   | **112.9135**  |   **-0.6590 (-0.58%)**   |  **271.2052**  | **0.0329**  | **183,234.3997** |    86.0830     |      24.5525      |      -0.3918 (-1.57%)       |     0.0119      |   57.3100   |
| `EXP5_G5` (22)   | TFT          |   115.1756    |     +0.7018 (+0.61%)     |    276.4600    |   -0.0056   |   190,854.8066   |    86.1249     |      23.5774      |    **-0.6684 (-2.76%)**     |   **0.1088**    |   88.1800   |
| `EXP5_G5` (22)   | XGBoost      |   112.9967    |     -0.2458 (-0.22%)     |    272.8304    |   0.0208    |   185,422.9456   |    86.6218     |      24.3109      |      -0.0419 (-0.17%)       |     0.0140      |   15.9833   |
| `EXP6_ALL` (40)  | Bi-LSTM      |   111.7751    |     -1.3402 (-1.18%)     |    270.0705    |   0.0398    |   181,562.5188   |    86.0480     |      24.1947      |      +0.2989 (+1.25%)       |     -0.0121     |   73.0733   |
| `EXP6_ALL` (40)  | **CatBoost** | **110.1599**  |   **-3.5916 (-3.16%)**   |  **266.9477**  | **0.0618**  | **177,457.6599** |  **86.9670**   |      23.5338      |    **-1.3596 (-5.46%)**     |   **0.1097**    | **13.7967** |
| `EXP6_ALL` (40)  | LightGBM     |   110.9315    |     -3.0111 (-2.64%)     |    268.3328    |   0.0524    |   179,294.8520   |    86.5476     |      23.6693      |      -1.0296 (-4.17%)       |     0.0745      |   56.3933   |
| `EXP6_ALL` (40)  | PatchTST     |   115.0399    |     +0.1864 (+0.16%)     |    275.5185    |   0.0011    |   189,538.3510   |    85.7882     |      24.1771      |      +0.3969 (+1.67%)       |     0.0073      |   88.9733   |
| `EXP6_ALL` (40)  | ST-GNN       |   112.4021    |     -1.1704 (-1.03%)     |    270.1966    |   0.0398    |   182,036.6081   |    86.2523     |      24.4496      |      -0.4947 (-1.98%)       |     0.0252      |   55.1367   |
| `EXP6_ALL` (40)  | TFT          |   113.7918    |     -0.6820 (-0.60%)     |    274.3537    |   0.0093    |   187,832.0134   |    86.1761     |      23.4513      |      -0.7945 (-3.28%)       |     0.0657      |   93.0233   |
| `EXP6_ALL` (40)  | XGBoost      |   110.1945    |     -3.0480 (-2.69%)     |    267.6365    |   0.0572    |   178,394.6650   |    86.2252     |    **23.2125**    |      -1.1403 (-4.68%)       |     0.0875      |   25.1967   |
---

## 4. ĐỐI CHIẾU SÂU SẮC GIỮA ENGINE V1 VÀ ENGINE V2

Khi so sánh với báo cáo sơ bộ của Engine v1 (`Bao_cao_Thuc_nghiem_Module_M3_Ablation_Study.docx`), Engine v2 đã mang lại những bước tiến học thuật và định lượng vượt bậc:

### Bảng 5.3: Bảng đối chiếu các chỉ số cốt lõi giữa Engine v1 và Engine v2

| Tiêu chí đối chiếu | Phiên bản Engine v1 (Báo cáo cũ) | Phiên bản Engine v2 (Chính thức hiện tại) | Ý nghĩa học thuật & Thực tiễn |
| :--- | :--- | :--- | :--- |
| **Hệ thống mô hình khảo sát** | Chỉ khảo sát 3 mô hình GBDT (`CatBoost`, `LightGBM`, `XGBoost`). | Mở rộng lên **7 mô hình toàn diện** (bổ sung Bi-LSTM, PatchTST, TFT, ST-GNN). | Chứng minh tính tổng quát hóa của đặc trưng M3 trên cả cây quyết định, mạng học sâu và mạng đồ thị. |
| **Phân tầng đánh giá** | Chỉ đo lường MAE gộp toàn cục (`All`). | Đánh giá phân tầng chi tiết: **`All` vs `LE_168h` ($\le 7$ ngày)**. | Làm sáng tỏ hiệu năng thực chiến: Ở tầng tác nghiệp $\le 168$h, MAE giảm từ ~110h xuống chỉ còn **22.9h - 23.5h**. |
| **Hiệu năng EXP1_G1 (CatBoost)** | MAE: 109.9088h, Delta: -3.3808h (-2.98%), Train: 170.6s. | MAE: **110.2058h**, Delta: **-3.5457h (-3.12%)**, Train: **11.97s**. | Tốc độ huấn luyện nhanh gấp **14.2 lần** nhờ tối ưu hóa DDP và GPU Tesla T4; mức giảm MAE tăng từ 3.38h lên 3.55h. |
| **Hiệu năng EXP1_G1 (XGBoost)** | MAE: 110.0758h, Delta: -3.0888h (-2.73%), Train: 109.2s. | MAE: **110.1231h**, Delta: **-3.1194h (-2.75%)**, Train: **17.49s**. | Tốc độ nhanh gấp **6.2 lần**; đạt đỉnh cao nhất toàn cục trên nhóm GBDT. |
| **Hiệu năng TFT & ST-GNN** | Chưa hỗ trợ. | **TFT đạt LE_168h MAE = 22.9302h** ($R^2 = 0.1314$); **ST-GNN giảm -6.41%**. | Mở ra khả năng ứng dụng các mô hình Attention và Graph Neural Network cho luồng lạch hàng hải. |
| **Hiện tượng bão hòa đặc trưng** | Ghi nhận ở EXP6 (+20 feats) gần bằng EXP1 (+7 feats). | Khẳng định vững chắc: EXP1 (27 feats) đạt 110.12h, EXP6 (40 feats) đạt 110.16h. | Cung cấp bằng chứng thực nghiệm quyết định để chuyển giao cho **Module M5** thực hiện chọn lọc đặc trưng (Feature Selection). |

---

## 5. PHÂN TÍCH CHUYÊN SÂU CƠ CHẾ VẬT LÝ VÀ ĐỘNG LỰC HỌC HÀNG HẢI

Từ bảng số liệu thực chứng của Engine v2, ba cơ chế vật lý hàng hải then chốt được khẳng định rõ nét:
1. **Tại sao Nhóm 1 (Berth Kinematics) mang lại bước nhảy vọt lớn nhất (-3.55h MAE, -6.41% LE_168h)?**
   - Trong dữ liệu thô, khoảng cách Euclidean hoặc khoảng cách vòng cung lớn ($Dist$) chỉ cho biết tàu cách cảng bao xa, nhưng không cho biết tàu có đang di chuyển về phía bến hay không.
   - Khi tàu quay đầu né bão, chạy vòng tránh bãi cạn, hoặc chạy theo luồng zíc-zắc, vận tốc $SOG$ vẫn cao nhưng $v_{\text{closing}} = SOG \cdot \cos(COG - \text{bearing})$ có thể âm hoặc bằng 0.
   - Việc trực tiếp cung cấp $v_{\text{closing}}$ và $\text{approach\_cos}$ giúp cây quyết định phân rã ngay lập tức thành phần vận tốc hữu ích và vận tốc trôi dạt ngang ($v_{\text{cross}}$), giảm thiểu gánh nặng tính toán phi tuyến cho mô hình.
2. **Hiệu quả bền vững của Nhóm 3 (Nonlinear ETA) và Nhóm 4 (Differentials):**
   - Nhóm 3 đóng vai trò một "điểm neo quy nạp vật lý" (physical inductive bias): Mô hình không cần học tương quan từ đầu mà chỉ cần học phần dư (residual learning) của đại lượng $\text{eta\_closing\_hours}$.
   - Nhóm 4 cung cấp tín hiệu báo trước: Gia tốc âm ($\text{acc\_sog} < 0$) và tốc độ đổi hướng tăng cao ($\text{rot\_approx} > 0$) là dấu hiệu đặc trưng khi tàu giảm tốc để hoa tiêu lên tàu hoặc tiếp cận phao số 0, giúp XGBoost giảm sâu thêm 2.40 giờ MAE.
3. **Tại sao Nhóm 2 (Vỏ tàu) và Nhóm 5 (Rolling) chưa phát huy tối đa ở dạng đơn lẻ?**
   - Nhóm 2 (thủy động lực học vỏ tàu) chỉ phát huy sức mạnh khi có sự tương tác với các yếu tố ngoại sinh (sóng, gió, hải lưu từ Module M4).
   - Nhóm 5 (cửa sổ trượt 3 bước) có độ dài thời gian quá ngắn (vài chục phút) so với tổng hành trình viễn dương (hàng trăm giờ), chỉ phản ánh rung lắc tức thời thay vì xu thế dài hạn.

---

## 6. KHUYẾN NGHỊ VÀ BÀN GIAO SANG CÁC MODULE TIẾP THEO

1. **Bàn giao cho Module M5 (Nguyễn Hữu Bảo Lộc - Lựa chọn đặc trưng):**
   - Đề xuất giữ lại bộ **13 đặc trưng cốt lõi (Core Feature Set):** Toàn bộ Nhóm 1 (7 đặc trưng) + Nhóm 3 (3 đặc trưng) + Nhóm 4 (3 đặc trưng).
   - Loại bỏ hoặc tinh giảm Nhóm 5 (`sog_rolling_mean_3`, `sog_rolling_std_3`) để tiết kiệm bộ nhớ và giảm độ trễ tính toán.
2. **Phối hợp với Module M4 (Mã Gia Kiệt - Thời tiết RTMA 2025):**
   - Tái kích hoạt Nhóm 2 (Thủy động lực học) thông qua việc tạo các đặc trưng tương tác chéo với trường gió ($u_{\text{wind}}, v_{\text{wind}}$) và sóng biển NOAA RTMA.
