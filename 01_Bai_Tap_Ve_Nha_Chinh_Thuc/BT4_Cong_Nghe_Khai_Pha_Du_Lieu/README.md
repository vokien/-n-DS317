# BÀI TẬP VỀ NHÀ 4: CÔNG NGHỆ KHAI PHÁ DỮ LIỆU
**Môn học:** DS317 - Khai phá dữ liệu trong doanh nghiệp  
**Căn cứ:** Nội dung Chương 6 (Mô hình hóa và Thuật toán KPDL) và Chương 7 (Đánh giá và Triển khai mô hình)  

---

## 1. Mục Tiêu Bài Tập

Bài tập về nhà 4 tập trung vào việc thiết kế giải pháp công nghệ khai phá dữ liệu toàn diện cho bài toán dự báo thời gian tàu cập cảng (ETA), bao gồm:
1. **Phân loại phương thức học máy:** Khảo sát, phân loại và lựa chọn các thuật toán phù hợp với cấu trúc dữ liệu chuỗi thời gian bảng (Tabular Time-Series).
2. **Thiết lập hệ thống độ đo đánh giá:** Phân định rõ ràng giữa độ đo kỹ thuật toán học ($MAE$, $RMSE$, $R^2$) và độ đo nghiệp vụ kinh doanh cảng biển ($Asymmetric Loss$, chi phí lưu tàu $Demurrage$).
3. **Xây dựng kịch bản thực nghiệm chuẩn mực:** Áp dụng cơ chế phân chia dữ liệu theo thời gian ($Time-based Split$) và thiết kế kịch bản nghiên cứu thành phần ($Ablation Study$) để đánh giá đóng góp của từng bước tiền xử lý.
4. **Lập kế hoạch giám sát mô hình trong vận hành:** Thiết kế cơ chế theo dõi trôi dạt dữ liệu ($Data Drift$ qua chỉ số $PSI$), suy giảm độ chính xác ($Model Drift$) và chu kỳ tái huấn luyện ($Retraining Cadence$).

---

## 2. Cấu Trúc Tệp Tin trong Thư Mục

| STT | Tên tệp tin | Định dạng | Dung lượng | Nội dung chính |
| :-: | :--- | :---: | :-: | :--- |
| 1 | `Phân loại phương thức học của các thuật toán dự kiến.docx` | Word | ~8 KB | Phân loại các thuật toán theo phương thức học có giám sát ($Supervised Learning$), so sánh ưu nhược điểm giữa mô hình tuyến tính (Ridge), cây quyết định tăng cường độ dốc (LightGBM, XGBoost, CatBoost), mạng nơ-ron sâu (MLP/Bi-LSTM), và phương pháp không tham số ($Conformal Prediction$). |
| 2 | `Liệt kê các độ đo đánh giá và xác định các độ đo đánh giá dự kiến sử dụng.docx` | Word | ~28 KB | Phân tích chi tiết công thức toán học, ý nghĩa thực tế và căn cứ lựa chọn các độ đo đánh giá: $MAE$, $RMSE$, $MedAE$, $R^2$, $MAPE$, tỷ lệ dự báo sớm/trễ, và hàm chi phí bất đối xứng. |
| 3 | `Liệt kê các độ đo đánh giá và xác định các độ đo đánh giá dự kiến sử dụng.pdf` | PDF | ~235 KB | Bản xuất PDF chính thức của tài liệu độ đo đánh giá. |
| 4 | `Kịch bản thực nghiệm.docx` | Word | ~851 KB | Thiết kế kịch bản thực nghiệm chi tiết: quy trình phân chia dữ liệu không rò rỉ ($Time-based Split$ Q1-Q3 Train/Val vs Q4 Eval), kiểm định chéo $K-Fold$ theo thời gian, ma trận thực nghiệm Ablation Study 7 Module, và quy trình ghi nhận tham số/kết quả. |
| 5 | `Kế hoạch giám sát mô hình.docx` | Word | ~13 KB | Chiến lược MLOps theo dõi mô hình sau triển khai: giám sát chỉ số độ trôi phân phối $PSI$ (Population Stability Index), ngưỡng cảnh báo trôi dạt dữ liệu ($PSI > 0.25$), giám sát độ trễ tính toán, và quy trình tự động kích hoạt tái huấn luyện định kỳ. |

---

## 3. Luồng Dữ Liệu và Quan Hệ Kỹ Thuật

```text
[BTVN BT2: 6 Chiều DAMA] & [BTVN BT3: Thuyết Minh Đề Tài]
                       │
                       ▼
    ┌────────────────────────────────────────┐
    │  BT4: Thiết Kế Công Nghệ Khai Phá      │
    │  - Phương thức học & Lựa chọn thuật toán│
    │  - Hệ thống độ đo (Kỹ thuật + Nghiệp vụ)│
    │  - Kịch bản thực nghiệm Ablation Study │
    │  - Kế hoạch giám sát Data/Model Drift  │
    └──────────────────┬─────────────────────┘
                       │
                       ▼
[02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/02_Runner_Song_Song_Chinh_Thuc_v2]
                       │ (Thực thi huấn luyện 7 mô hình x 13 biến thể x 3 fold)
                       ▼
[05_Output_Cac_Notebook/07_Runner_... & 08_Runner_...] -> [06_Results/]
```

- **Đầu vào:** Bảng dữ liệu tiền xử lý từ `01_Pipeline_Tien_Xu_Ly_Va_BTVN`, các thuộc tính động học và không gian hàng hải.
- **Đầu ra:** Bản đặc tả kỹ thuật và khung kịch bản làm cơ sở trực tiếp để lập trình 2 Runner song song (`DS317_Runner_Song_Song_1_Baseline_M1_M2_M3.ipynb` và `DS317_Runner_Song_Song_2_M4_M5_M6_M7.ipynb`).

---

## 4. Phân Công Trách Nhiệm Thành Viên

- **Lê Sỹ Liêm:** Chủ trì xây dựng hệ thống độ đo đánh giá, thiết kế công thức $Asymmetric Loss$, $Conformal Prediction$ và kế hoạch giám sát chỉ số trôi dữ liệu $PSI$.
- **Trần Hồng Lĩnh:** Chủ trì phân loại phương thức học thuật toán, đối chiếu ưu thế thuật toán GBDT và xây dựng kịch bản thực nghiệm cơ sở.
- **Võ Đình Kiên:** Thẩm định kịch bản thực nghiệm, đảm bảo tính khả thi về mặt kỹ thuật trên môi trường tính toán đám mây Kaggle.

---

## 5. Hướng Dẫn Sử Dụng và Tra Cứu

- **Tham khảo độ đo:** Đọc [`Liệt kê các độ đo đánh giá và xác định các độ đo đánh giá dự kiến sử dụng.pdf`](Li%E1%BB%87t%20k%C3%AA%20c%C3%A1c%20%C4%91%E1%BB%99%20%C4%91o%20%C4%91%C3%A1nh%20gi%C3%A1%20v%C3%A0%20x%C3%A1c%20%C4%91%E1%BB%8Bnh%20c%C3%A1c%20%C4%91%E1%BB%99%20%C4%91o%20%C4%91%C3%A1nh%20gi%C3%A1%20d%E1%BB%B1%20ki%E1%BA%BFn%20s%E1%BB%AD%20d%E1%BB%A5ng.pdf) khi viết Báo cáo Chương 2 và Chương 4.
- **Tham khảo kịch bản:** Đọc [`Kịch bản thực nghiệm.docx`](K%E1%BB%8Bch%20b%E1%BA%A3n%20th%E1%BB%B1c%20nghi%E1%BB%87m.docx) để nắm rõ cơ chế phân chia Time-based Split phục vụ phân tích kết quả ở Chương 5.
- **Tham khảo giám sát:** Đọc [`Kế hoạch giám sát mô hình.docx`](K%E1%BA%BF%20ho%E1%BA%A1ch%20gi%C3%A1m%20s%C3%A1t%20m%C3%B4%20h%C3%ACnh.docx) phục vụ xây dựng Chương 6 (Triển khai và MLOps).
