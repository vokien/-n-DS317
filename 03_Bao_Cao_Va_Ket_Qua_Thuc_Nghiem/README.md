# Báo Cáo và Kết Quả Thực Nghiệm (`03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/`)

Thư mục này là nơi quy tập các tài liệu phân tích, báo cáo chuyên đề học thuật và văn bản tổng hợp toàn diện kết quả thực nghiệm của **Nhóm 03 (Lớp DS317.R11)** cho đề tài **Dự báo Thời gian Đến Cảng (Vessel ETA Prediction)**.

---

## 1. Mục Đích và Vai Trò trong Đồ Án

1. **Tổng hợp tri thức thực nghiệm:** Chuyển hóa hàng trăm bảng số liệu và tham số thô từ `05_Output_Cac_Notebook/` thành các nhận định khoa học, phân tích định lượng có kiểm chứng và luận cứ kỹ thuật vững chắc.
2. **Cơ sở dữ liệu cho Báo cáo 7 Chương cuối kỳ:** Đóng vai trò là nguồn tham khảo nội dung cốt lõi để các thành viên tổng hợp nên Chương 4 (Kỹ thuật Khai phá Dữ liệu Đề xuất) và Chương 5 (Kết quả Thực nghiệm và Thảo luận) của Báo cáo Đồ án Cuối kỳ.
3. **Lưu trữ báo cáo chuyên đề:** Tập hợp các báo cáo nghiên cứu sâu độc lập về từng module thành phần (M3 Tạo đặc trưng, M5 Lựa chọn đặc trưng, M6 Hàm mất mát bất đối xứng).

---

## 2. Cấu Trúc Tệp Tin và Chi Tiết Nội Dung

```text
03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem/
├── Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md  <- Văn bản phân tích tổng hợp cốt lõi (97.5 KB)
├── Bao_cao_Modules/                                  <- Báo cáo chuyên đề Word các module
│   ├── Bao_cao_Thuc_nghiem_Module_M3_Ablation_Study.docx
│   ├── BaoCao_M5.docx
│   └── Bao_cao_Thuc_nghiem_Module_M6.docx
└── README.md                                         <- Tài liệu hướng dẫn thư mục
```

### Chi Tiết Từng Tệp Tin:

| STT | Tên tệp tin | Định dạng | Dung lượng | Nội dung phân tích chính |
| :-: | :--- | :---: | :-: | :--- |
| 1 | `Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md` | Markdown | ~97.5 KB | **Văn bản tổng hợp toàn diện Engine v2:**<br>• Phân tích hiệu quả Baseline B0 và chuỗi 7 Module thực nghiệm (M1-M7).<br>• Bảng đối chiếu số liệu 7 thuật toán qua 3 phân tầng thời gian (`All`, `LE_168h`, `GT_168h`).<br>• Giải thích cơ chế triệt tiêu trễ tàu từ Asymmetric Loss M6 và độ phủ tin cậy Conformal M7.<br>• Kiểm định ý nghĩa thống kê ($p < 0.001$) và bài toán quy đổi tài chính doanh nghiệp USD ($ROI$). |
| 2 | [`Bao_cao_Modules/`](Bao_cao_Modules/README.md) | Thư mục | - | Chứa 3 báo cáo chuyên đề Word chi tiết về Module M3, M5, M6 (kèm lưu ý chuẩn hóa dữ liệu từ Engine v1 sang Engine v2). |

---

## 3. Lưu Ý Quan Trọng về Phiên Bản Số Liệu (Engine v1 vs Engine v2)

Căn cứ theo văn bản chỉ đạo tại [`00_Quan_Ly_Va_Tai_Lieu_Chung/Kế hoạch hoàn thiện và phân công công việc cuối kỳ.md`](../00_Quan_Ly_Va_Tai_Lieu_Chung/K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md):
- **Nguồn số liệu chuẩn duy nhất (Source of Truth):** Toàn bộ số liệu chính thức phục vụ nghiệm thu đồ án được trích xuất từ kho lưu trữ [`05_Output_Cac_Notebook/`](../05_Output_Cac_Notebook/README.md) (đặc biệt là 2 thư mục `07_Runner_Song_Song_1_Baseline_M1_M2_M3/results/` và `08_Runner_Song_Song_2_M4_M5_M6_M7/results/`).
- **Các báo cáo chuyên đề cũ trong `Bao_cao_Modules/`:** Một số bảng số liệu trong 3 tệp Word cũ còn lưu số liệu của đợt chạy Engine v1 ban đầu. Khi đưa vào Báo cáo 7 chương cuối kỳ, các thành viên phụ trách **bắt buộc phải lấy số liệu mới nhất của Engine v2** đã được chuẩn hóa trong tệp `Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md`.

---

## 4. Phân Công Trách Nhiệm Thành Viên

- **Võ Đình Kiên:** Chủ trì biên soạn văn bản `Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md`, rà soát tính nhất quán giữa số liệu thực nghiệm và kết luận phân tích.
- **Quách Tuấn Kiệt:** Soạn thảo báo cáo chuyên đề Module M3 (Tạo đặc trưng tương tác).
- **Nguyễn Hữu Bảo Lộc:** Soạn thảo báo cáo chuyên đề Module M5 (Lựa chọn đặc trưng MI và biến đổi log1p).
- **Trần Hồng Lĩnh:** Soạn thảo báo cáo chuyên đề Module M6 (Hàm mất mát bất đối xứng).
- **Lê Sỹ Liêm:** Cung cấp số liệu kiểm định thống kê và bài toán quy đổi tài chính USD bổ sung vào báo cáo tổng hợp.

---

## 5. Hướng Dẫn Sử Dụng và Trích Xuất

- Khi viết **Chương 4 (Phương pháp đề xuất)**: Trích xuất các phân tích lý thuyết và thiết kế kiến trúc từ `Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md` và các báo cáo trong `Bao_cao_Modules/`.
- Khi viết **Chương 5 (Kết quả thực nghiệm)**: Sao chép các bảng tổng hợp số liệu phân tầng (`All`, `LE_168h`, `GT_168h`), bảng so sánh Delta Ablation và nhận xét chuyên sâu từ tệp `Tong_Hop_Ket_Qua_Thuc_Nghiem_Ablation_7_Module.md`.
