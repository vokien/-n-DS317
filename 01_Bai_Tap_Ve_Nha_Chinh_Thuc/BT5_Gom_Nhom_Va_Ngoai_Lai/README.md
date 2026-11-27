# BÀI TẬP VỀ NHÀ 5: GOM NHÓM VÀ XÁC ĐỊNH NGOẠI LAI DỮ LIỆU AIS
**Môn học:** DS317 - Khai phá dữ liệu trong doanh nghiệp  
**Căn cứ:** Nội dung Chương 8 (Phân tích gom nhóm) và Chương 10 (Phát hiện điểm ngoại lai)  

---

## 1. Mục Tiêu Bài Tập

Bài tập về nhà 5 giải quyết hai bài toán học máy không giám sát cốt lõi trên dữ liệu tự động nhận dạng tàu biển NOAA AIS:
1. **Phân tích gom nhóm tàu thuyền ($Clustering$):** Phân đoạn các hành vi hành hải, đặc trưng thân vỏ và kiểu vận hành của tàu thành các cụm có ý nghĩa thực tế mà không cần nhãn định sẵn; xác định số cụm tối ưu $k$ qua các độ đo nội bộ ($Silhouette$, $Calinski-Harabasz$, $Davies-Bouldin$) và thẩm định qua các độ đo bên ngoài ($Purity$, $Entropy$, $Adjusted Rand Index$).
2. **Phát hiện và phân loại ngoại lai ($Outlier Detection$):** Nhận diện 3 dạng bất thường hàng hải chính:
   - *Ngoại lai điểm (Point Anomaly):* Tọa độ GPS nhảy cóc, vận tốc $sog > 40$ knots, mớn nước $draft$ âm.
   - *Ngoại lai ngữ cảnh (Contextual Anomaly):* Vận tốc quá thấp khi đang ở luồng chính, dừng đỗ bất thường giữa luồng lạch.
   - *Ngoại lai tập thể (Collective Anomaly):* Chuỗi hành trình quay vòng hoặc sai lệch hướng liên tục.
3. **Làm giàu dữ liệu ($Data Enrichment$):** Tạo các đặc trưng cụm hành vi và chỉ số bất thường để bổ trợ cho bài toán dự báo thời gian cập cảng (ETA).

---

## 2. Cấu Trúc Tệp Tin trong Thư Mục

Thư mục bao gồm văn bản báo cáo chính thức, mã nguồn thực thi và thư mục con lưu trữ 20 tệp kết quả thực nghiệm:

```text
BT5_Gom_Nhom_Va_Ngoai_Lai/
├── BT5 - Gom nhóm và xác định ngoại lai dữ liệu AIS.docx      <- Báo cáo chính thức 3.19 MB
├── DS317 BT5 Thực nghiệm gom nhóm và xác định ngoại lai.ipynb   <- Notebook thực nghiệm Jupyter
├── DS317_BT5_Chay_Thuc_Nghiem_Va_Xuat_So_Lieu.py              <- Script Python tự động hóa
├── Tai_Lieu_Tham_Khao_Nguong_Ngoai_Lai.md                     <- Tài liệu tham khảo ngưỡng vật lý
├── Đề xuất ý tưởng làm giàu dữ liệu Chương 8 và Chương 10.docx <- Đề xuất ứng dụng Chương 8 & 10
└── Ket_Qua_Thuc_Nghiem/                                       <- 20 tệp sản phẩm thực nghiệm
    ├── ais_sample_clustering_outlier.parquet                  <- Dữ liệu mẫu gán nhãn cụm/ngoại lai
    ├── kmeans_best_model.joblib                               <- Trọng số mô hình KMeans tối ưu
    ├── scaler_clustering.joblib                               <- Trọng số chuẩn hóa dữ liệu
    ├── luat_cay_quyet_dinh_giai_thich_cum.txt                 <- Bộ luật cây quyết định giải thích cụm
    ├── 11 file bảng biểu đo lường (.csv)                      <- Xem chi tiết bảng bên dưới
    └── 5 file biểu đồ chất lượng cao (.png)                   <- Xem chi tiết biểu đồ bên dưới
```

### Danh Mục 11 Tệp Bảng Biểu Số Liệu (`Ket_Qua_Thuc_Nghiem/*.csv`):

| STT | Tên bảng CSV | Nội dung và ý nghĩa nghiệp vụ |
| :-: | :--- | :--- |
| 1 | `bang_3_loai_ngoai_lai_hang_hai.csv` | Thống kê tỷ lệ và số lượng bản ghi theo 3 loại ngoại lai: điểm, ngữ cảnh, tập thể. |
| 2 | `bang_chi_so_troi_du_lieu_psi.csv` | Đo lường độ trôi dạt dữ liệu phân cụm giữa các quý qua chỉ số PSI. |
| 3 | `bang_chi_tiet_loai_tau_theo_cum.csv` | Tỷ trọng các loại tàu (Cargo, Tanker, Tug, Passenger) trong từng cụm phát hiện. |
| 4 | `bang_chon_k_cac_do_do_noi_bo.csv` | Kết quả đo Elbow (SSE), Silhouette Score, Davies-Bouldin cho $k \in [2, 10]$. |
| 5 | `bang_danh_gia_ben_ngoai_purity_entropy_ari.csv` | Đánh giá mức độ khớp giữa cụm không giám sát và loại tàu thực tế. |
| 6 | `bang_ho_so_dac_trung_cac_cum.csv` | Hồ sơ trung bình các biến $sog$, $draft$, $length$, $width$, $dist$ của từng cụm. |
| 7 | `bang_mau_canh_bao_ngoai_lai_kem_ly_do.csv` | Mẫu bản tin cảnh báo an toàn hàng hải kèm lý do vi phạm cụ thể cho từng tàu. |
| 8 | `bang_so_sanh_5_tieu_chi_gom_nhom.csv` | So sánh KMeans, DBSCAN, Gaussian Mixture theo 5 tiêu chí kỹ thuật. |
| 9 | `bang_so_sanh_5_tieu_chi_ngoai_lai.csv` | So sánh Isolation Forest, LOF, IQR và Elliptic Envelope theo 5 tiêu chí. |
| 10 | `bang_so_sanh_cac_phuong_phap_gom_nhom.csv` | Tổng hợp thời gian chạy và chất lượng phân cụm của các thuật toán. |
| 11 | `bang_so_sanh_cac_phuong_phap_ngoai_lai.csv` | Đánh giá độ chính xác, tỷ lệ phát hiện và chi phí tính toán phát hiện ngoại lai. |

### Danh Mục 5 Tệp Biểu Đồ Phân Tích (`Ket_Qua_Thuc_Nghiem/*.png`):

| STT | Tên biểu đồ | Ý nghĩa trực quan hóa |
| :-: | :--- | :--- |
| 1 | `Hinh1_Chon_k_Elbow_va_Do_Do_Noi_Bo.png` | Đồ thị Elbow phương sai giải thích và điểm Silhouette xác định $k=4$ tối ưu. |
| 2 | `Hinh2_Truc_Quan_Hoa_Phan_Cum_PCA_2D.png` | Chiếu không gian đặc trưng đa chiều xuống 2 thành phần chính PCA để minh họa phân tách cụm. |
| 3 | `Hinh3_Bieu_Do_Silhouette_Tung_Cum.png` | Biểu đồ Silhouette Plot kiểm tra độ đồng nhất và tình trạng cụm âm (misclassified). |
| 4 | `Hinh4_Heatmap_ZScore_Ho_So_Cum.png` | Bản đồ nhiệt Z-score thể hiện rõ đặc tính định danh của từng cụm (ví dụ: Cụm tàu siêu trường siêu trọng). |
| 5 | `Hinh5_So_Sanh_Diem_Bat_Thuong_Ngoai_Lai.png` | Biểu đồ so sánh phân phối điểm bất thường (Anomaly Score) giữa các phương pháp. |

---

## 3. Luồng Dữ Liệu và Hướng Dẫn Tái Lập

### Luồng Dữ Liệu:
- **Đầu vào:** Tập dữ liệu mẫu đại diện `ais_sample_clustering_outlier.parquet` (trích xuất từ bộ dữ liệu nền tảng 22 thuộc tính với đầy đủ tọa độ, động học và kích thước tàu).
- **Quy trình xử lý:**
  1. Chuẩn hóa đặc trưng bằng RobustScaler/StandardScaler (`scaler_clustering.joblib`).
  2. Chạy thuật toán gom nhóm KMeans phân tách 4 cụm hành vi (`kmeans_best_model.joblib`).
  3. Áp dụng cây quyết định rút trích luật phân cụm tự nhiên (`luat_cay_quyet_dinh_giai_thich_cum.txt`).
  4. Chạy mô hình Isolation Forest kết hợp ngưỡng IQR phát hiện 3 loại ngoại lai.
- **Đầu ra:** 11 bảng số liệu và 5 biểu đồ được lưu tại `Ket_Qua_Thuc_Nghiem/`, đồng thời được trích dẫn trực tiếp vào báo cáo Word `BT5 - Gom nhóm và xác định ngoại lai dữ liệu AIS.docx`.

### Hướng Dẫn Tái Lập Thực Nghiệm:

Để chạy lại toàn bộ quy trình tính toán và tái tạo toàn bộ 16 tệp số liệu và biểu đồ:

```bash
# Di chuyển vào thư mục bài tập
cd "01_Bai_Tap_Ve_Nha_Chinh_Thuc/BT5_Gom_Nhom_Va_Ngoai_Lai"

# Chạy script tự động hóa
python DS317_BT5_Chay_Thuc_Nghiem_Va_Xuat_So_Lieu.py
```

---

## 4. Phân Công Trách Nhiệm Thành Viên

- **Huỳnh Chí Kiên:** Phụ trách tiền xử lý đặc trưng, xây dựng biểu đồ chất lượng cao (Silhouette, PCA, Heatmap) và rà soát ngưỡng ngoại lai IQR.
- **Lê Sỹ Liêm:** Chủ trì đo lường các chỉ số nội bộ/bên ngoài của gom nhóm, phân tích chỉ số độ trôi $PSI$ và đánh giá ngoại lai ngữ cảnh.
- **Võ Đình Kiên:** Thẩm định mã nguồn thực nghiệm `DS317_BT5_Chay_Thuc_Nghiem_Va_Xuat_So_Lieu.py` và đóng gói kết quả.
