# BÀI TẬP VỀ NHÀ 2: ĐO LƯỜNG VÀ GIÁM SÁT ĐỘ ĐO CHẤT LƯỢNG DỮ LIỆU
**Môn học:** DS317 - Khai phá dữ liệu trong doanh nghiệp  
**Căn cứ:** Nội dung Chương 4 (Chất lượng dữ liệu), tiêu chuẩn DAMA-DMBOK và ISO 8000  

---

## 1. Mục tiêu bài tập
- Cài đặt đo lường định lượng 6 khía cạnh chất lượng dữ liệu ở mức hạt dữ liệu (Data Grain: mức bản ghi, mức thuộc tính, mức chuyến tàu).
- Đo lường và kiểm toán thực chứng 6 chiều DAMA trên **Tập dữ liệu thô (Raw Data - 256,935,254 dòng)** nhằm phát hiện khiếm khuyết, vi phạm logic và mâu thuẫn nghiệp vụ thực tế.
- Giám sát chất lượng dữ liệu theo trục thời gian phân rã qua 4 Quý (Q1 - Q4 năm 2025) nhằm kiểm soát rủi ro trôi dạt dữ liệu (Data Drift).
- Thiết lập bảng đối chiếu Trước vs Sau tiền xử lý (Dữ liệu thô vs Bản Nền tảng 22 cột) để chứng minh hiệu quả làm sạch và tính tất yếu của pipeline tiền xử lý.

---

## 2. Kết quả đo lường định lượng 6 chiều DAMA trên Dữ liệu thô (256.94M dòng)

| STT | Chiều chất lượng | Tiêu chí & Phương pháp đo lường | Kết quả thực tế (Dữ liệu thô 2025) | Đánh giá đạt chuẩn |
|:---:|:---|:---|:---|:---:|
| 1 | **Tính đầy đủ (Completeness)** | Đo tỷ lệ không khuyết ở mức bản ghi (18 cột) và mức từng thuộc tính | • Mức bản ghi: **93.5626%** (240,395,409 / 256,935,254 bản ghi đủ 18 cột)<br>• Mức thuộc tính: **99.5467%** (khuyết chính: heading 3.17%, draft 2.10%, width 1.07%, cargo 0.64%) | **KHÔNG ĐẠT** (Mức bản ghi < 95.0%) |
| 2 | **Tính nhất quán (Consistency)** | Thẩm định 4 ràng buộc logic nghiệp vụ chéo ($1.0 \le sog \le 40.0$, $0 < Target \le 168h$, $status \notin \{1,5\}$, thời gian nhân quả) | Chỉ đạt **36.6940%** (94,279,701 / 256,935,254 bản ghi); vi phạm 63.31% do tàu neo đậu status 1, 5, trôi dạt sog < 1 kn, hoặc Target_Hours > 168h | **KHÔNG ĐẠT** (Vi phạm logic hàng hải) |
| 3 | **Tính chính xác (Accuracy)** | Đo vận tốc biểu kiến $v_{implied} \ge 1.62$ kn, cự ly theo nhóm tàu, bến trong US và tương quan Pearson | Mức hạt mẫu: **45.9011%** (117,936,010 / 256,935,254 dòng); Tương quan Pearson thô rất yếu $r = +0.2589$ do nhiễu neo đậu và trôi dạt | **KHÔNG ĐẠT** (Động học thô yếu) |
| 4 | **Tính kịp thời (Timeliness)** | Kiểm tra độ phủ 365/365 ngày của năm 2025 và cửa sổ tác nghiệp hữu dụng $(0, 168h]$ | Đạt **64.9956%** (166,996,581 / 256,935,254 dòng); 100% thuộc năm 2025 nhưng 35.00% phát quá sớm trước cập bến (> 7 ngày) | **KHÔNG ĐẠT** (Ngoài cửa sổ 7 ngày) |
| 5 | **Tính hợp lệ (Validity)** | Thẩm định miền giá trị theo ITU-R M.585 (MMSI), WGS84, dải vật lý vận tốc và kích thước thân vỏ | Đạt **96.3052%** (247,442,006 / 256,935,254 bản ghi hợp lệ trên toàn dải thuộc tính) | **ĐẠT** (Vượt chuẩn DAMA >= 95.0%) |
| 6 | **Tính duy nhất (Uniqueness)** | Kiểm tra trùng lặp bản tin theo cặp khóa kép (mmsi, base_date_time) | Đạt **99.7228%** (256,223,135 dòng duy nhất; chỉ 0.2772% trùng lặp trạm bờ VHF của USCG) | **ĐẠT** (Vượt chuẩn DAMA >= 99.0%) |

---

## 3. Giám sát chất lượng dữ liệu thô theo trục thời gian (4 Quý năm 2025)

| Chiều chất lượng DAMA | Quý 1 (Q1) | Quý 2 (Q2) | Quý 3 (Q3) | Quý 4 (Q4) | Toàn năm 2025 |
|:---|:---:|:---:|:---:|:---:|:---:|
| **1. Completeness (Mức bản ghi)** | 93.82% | 92.97% | 93.66% | 94.00% | **93.56%** |
| **   Completeness (Mức thuộc tính)** | 99.59% | 99.48% | 99.55% | 99.58% | **99.55%** |
| **2. Consistency (Tính nhất quán)** | 30.51% | 35.36% | 42.16% | 41.15% | **36.69%** |
| **3. Accuracy (Tính chính xác động học)** | 37.60% | 45.10% | 52.82% | 50.86% | **45.90%** |
| **4. Timeliness (Tính kịp thời tác nghiệp)** | 58.03% | 61.19% | 71.76% | 72.91% | **65.00%** |
| **5. Validity (Tính hợp lệ dải vật lý)** | 97.27% | 95.78% | 95.70% | 96.44% | **96.31%** |
| **6. Uniqueness (Tính duy nhất)** | 99.97% | 99.95% | 99.26% | 99.59% | **99.72%** |
| **Khối lượng quan trắc thô (N_raw)** | 72.36M (28.16%) | 75.61M (29.43%) | 61.65M (23.99%) | 47.32M (18.42%) | **256.94M (100.0%)** |

---

## 4. Bảng đối chiếu chất lượng Trước vs Sau tiền xử lý (Dữ liệu thô vs Bản Nền tảng 22)

| STT | Chiều chất lượng DAMA | Bản thô (Trước tiền xử lý) | Bản Nền tảng 22 (Sau tiền xử lý) | Chênh lệch | Đánh giá đạt chuẩn |
|:---:|:---|:---:|:---:|:---:|:---|
| 1 | **1. Completeness (Mức bản ghi)** | 93.56% | 100.00% (21 cột sạch 0 null) | +6.44% | **ĐẠT** (Điền khuyết Group Median 3 cấp) |
| 2 | **2. Consistency (Tính nhất quán)** | 36.69% | 100.00% (92.68M dòng thỏa mãn) | +63.31% | **ĐẠT** (Loại bỏ neo đậu status 1,5 & trôi dạt) |
| 3 | **3. Accuracy (Tính chính xác)** | 45.90% | 92.73% toàn năm (Q1-Q3: 100%, Q4: 70.9%) | +46.82% | **ĐẠT** (Pearson r tăng từ +0.2589 lên +0.5097) |
| 4 | **4. Timeliness (Tính kịp thời)** | 65.00% | 100.00% (365/365 ngày trọn vẹn) | +35.00% | **ĐẠT** (Giới hạn cửa sổ tác nghiệp <= 168h) |
| 5 | **5. Validity (Tính hợp lệ)** | 96.31% | 100.00% (Khớp schema PyArrow & vật lý) | +3.69% | **ĐẠT** (Lọc bỏ tọa độ ngoại lai & kích thước âm) |
| 6 | **6. Uniqueness (Tính duy nhất)** | 99.72% | 100.00% (Khử sạch hoàn toàn trùng lặp) | +0.28% | **ĐẠT** (SlidingBatchDeduplicator 7 ngày) |

---

## 5. Danh mục tài liệu và sản phẩm bàn giao

- [`BT - Đo lường và giám sát độ đo chất lượng dữ liệu.docx`](BT%20-%20%C4%90o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20gi%C3%A1m%20s%C3%A1t%20%C4%91%E1%BB%99%20%C4%91o%20ch%E1%BA%A5t%20l%C6%B0%E1%BB%A3ng%20d%E1%BB%AF%20li%E1%BB%87u.docx) (và [`BT - Đo lường và giám sát độ đo chất lượng dữ liệu.pdf`](BT%20-%20%C4%90o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20gi%C3%A1m%20s%C3%A1t%20%C4%91%E1%BB%99%20%C4%91o%20ch%E1%BA%A5t%20l%C6%B0%E1%BB%A3ng%20d%E1%BB%AF%20li%E1%BB%87u.pdf)): Báo cáo hoàn chỉnh về phương pháp, kết quả đo lường và ma trận đối chiếu.
- Notebook tính toán và trích xuất:
  - [`DS317 - Đo lường giám sát chất lượng 6 khía cạnh.ipynb`](DS317%20-%20%C4%90o%20l%C6%B0%E1%BB%9Dng%20gi%C3%A1m%20s%C3%A1t%20ch%E1%BA%A5t%20l%C6%B0%E1%BB%A3ng%206%20kh%C3%ADa%20c%E1%BA%A1nh.ipynb)
  - `DS317 C4 - Mẫu hướng dẫn giáo viên.ipynb` (lưu trữ ngoài repo)
- Thư mục biểu đồ dùng chung trong repo: [`04_So_Lieu_Kiem_Ke_Va_Bieu_Do/Hinh_Anh_Bieu_Do_Chung/`](../../04_So_Lieu_Kiem_Ke_Va_Bieu_Do/Hinh_Anh_Bieu_Do_Chung) (đã quy chuẩn từ thư mục `Hình ảnh biểu đồ/` gốc) chứa:
  - `Hình 1 - Phân phối Target Hours.png`
  - `Hình 2 - Phân tán Dist vs Target.png`
  - `Hình 3 - Biểu đồ hộp SOG Draft Cargo vs Tanker.png`
  - `Hình 4 - Mật độ địa không gian.png`
