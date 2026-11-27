# Quản Lý Dự Án và Tài Liệu Chung (`00_Quan_Ly_Va_Tai_Lieu_Chung/`)

Thư mục này đóng vai trò là trung tâm quản trị chiến lược, điều phối tiến độ, lưu trữ quy chuẩn học thuật và tài liệu chỉ đạo nghiệp vụ xuyên suốt toàn bộ quá trình thực hiện đồ án môn học **DS317 - Khai phá dữ liệu trong doanh nghiệp** của **Nhóm 03 (Lớp DS317.R11)**.

---

## 1. Mục đích và Vai trò trong Đồ Án

1. **Quản trị tiến độ và phân công:** Định hình lộ trình thực hiện toàn diện qua từng cột mốc (từ BTVN BT1 đến Đồ án cuối kỳ), xác định rõ trách nhiệm cụ thể của 7 thành viên theo thế mạnh chuyên môn.
2. **Quy chuẩn hóa nền tảng toán học & học thuật:** Cung cấp định nghĩa toán học hình thức cho các hàm mất mát, công thức đánh giá, đồng thời khảo sát có hệ thống các công trình khoa học quốc tế liên quan (SOTA) trong lĩnh vực dự báo thời gian tàu cập cảng (ETA).
3. **Chỉ dẫn kỹ thuật và kết nối dữ liệu đám mây:** Hướng dẫn quy trình điều chỉnh, tải và đồng bộ các tập dữ liệu lớn (> 100 MB) từ nền tảng Kaggle và Google Drive về môi trường cục bộ.

---

## 2. Cấu Trúc Tệp Tin và Chi Tiết Nội Dung

| STT | Tên tệp tin | Định dạng | Dung lượng | Mục đích & Nội dung nghiệp vụ |
| :-: | :--- | :---: | :-: | :--- |
| 1 | `Kế hoạch hoàn thiện và phân công công việc cuối kỳ.md` | Markdown | ~41 KB | Văn bản chỉ đạo cốt lõi giai đoạn nước rút: theo dõi 5 sản phẩm bắt buộc (A4), 7 tiêu chí kỹ thuật chuyên sâu, trạng thái khắc phục sai lệch số liệu Engine v2, và bảng phân công chi tiết cho 7 thành viên. |
| 2 | `Phan_cong_kich_ban_thuc_nghiem_7_module.md` | Markdown | ~9 KB | Kế hoạch phân bổ trách nhiệm nghiên cứu và thực thi kịch bản thực nghiệm Ablation 7 Module (M1 đến M7). |
| 3 | `Phan_Cong_Thuyet_Minh_De_Tai.md` | Markdown | ~66 KB | Tài liệu phân công chi tiết công việc chuẩn bị cho đợt bảo vệ Thuyết minh đề tài (Lab 3). |
| 4 | `HuongDan_DieuChinh_Dataset_Tho.md` | Markdown | ~22 KB | Hướng dẫn kỹ thuật xử lý dữ liệu thô NOAA AIS 2025, cơ chế chia phân tầng Train/Eval Q4, và tải dữ liệu từ Google Drive. |
| 5 | `Dinh_nghia_ham_toan_hoc.docx` | Word | ~470 KB | Văn bản chuẩn hóa định nghĩa toán học các hàm mục tiêu, độ đo lỗi hồi quy ($RMSE$, $MAE$, $MedAE$, $R^2$, $MAPE$), hàm mất mát bất đối xứng ($Asymmetric Loss$), và lý thuyết dự báo khoảng $Conformal Prediction$. |
| 6 | `Plan_Ke_Hoach_Tong_The_Do_An.xlsx` | Excel | ~299 KB | Bảng kế hoạch tổng thể đồ án, phân bổ mốc thời gian (WBS, Gantt chart) và trạng thái hoàn thành từng hạng mục. |
| 7 | `TongQuan_RelatedWork_ETA_6BaiBao_v2.xlsx` | Excel | ~46 KB | Ma trận tổng hợp, phân tích và so sánh 6 công trình nghiên cứu SOTA quốc tế về bài toán dự báo ETA hàng hải (phương pháp, tập dữ liệu, độ đo, kết quả). |
| 8 | `Nguon_tham_khao_tien_xu_ly_va_baseline.txt` | Text | ~338 B | Danh mục liên kết tài liệu tham khảo kỹ thuật tiền xử lý dữ liệu AIS và mô hình baseline. |
| 9 | `Nhom_03.txt` | Text | ~84 B | Liên kết Google Drive lưu trữ tập trung dữ liệu lớn, tài nguyên chia sẻ và mô hình nén của Nhóm 03. |

---

## 3. Luồng Dữ Liệu và Quan Hệ với Các Phân Hệ Khác

```text
[00_Quan_Ly_Va_Tai_Lieu_Chung]
   │
   ├── Chỉ đạo phân công & quy chuẩn toán học
   │      ├──> [01_Bai_Tap_Ve_Nha_Chinh_Thuc] (Hướng dẫn nội dung nộp BTVN BT1-BT5)
   │      ├──> [02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem] (Định hướng kiến trúc pipeline & 7 module)
   │      └──> [03_Bao_Cao_Va_Ket_Qua_Thuc_Nghiem] (Quy chuẩn cấu trúc báo cáo 7 chương)
   │
   └── Quản lý liên kết lưu trữ đám mây (Kaggle / Google Drive)
          └──> [04_Data] & [05_Model] (Tải dữ liệu mẫu & trọng số mô hình lớn)
```

- **Đầu vào:** Đề cương môn học DS317, barem chấm điểm của giảng viên, các tiêu chuẩn DAMA/ISO 8000, và các bài báo khoa học quốc tế (SOTA).
- **Đầu ra:** Các văn bản phân công, tài liệu quy chuẩn toán học, kế hoạch WBS đóng vai trò là "kim chỉ nam" cho toàn bộ 7 thành viên thực thi code, thực nghiệm, viết báo cáo và bảo vệ đồ án.

---

## 4. Phân Công Trách Nhiệm Thành Viên

Căn cứ văn bản `Kế hoạch hoàn thiện và phân công công việc cuối kỳ.md`, trách nhiệm điều phối thư mục thuộc về:
- **Võ Đình Kiên (Nhóm trưởng):** Chủ trì xây dựng kế hoạch tổng thể, ban hành tài liệu phân công, chuẩn hóa tài liệu kỹ thuật và điều phối chung.
- **Đỗ Văn Lộc (Thư ký):** Phối hợp cập nhật bảng kế hoạch Excel, tổng hợp biên bản họp nhóm và quản lý tiến độ các mốc nộp bài.
- **Tập thể Nhóm 03:** Tuân thủ các quy định học thuật, quy chuẩn toán học và hạn nộp được công bố trong thư mục này.

---

## 5. Hướng Dẫn Sử Dụng và Tra Cứu

1. **Tra cứu kế hoạch nước rút:** Đọc trực tiếp tệp [`Kế hoạch hoàn thiện và phân công công việc cuối kỳ.md`](K%E1%BA%BF%20ho%E1%BA%A1ch%20ho%C3%A0n%20thi%E1%BB%87n%20v%C3%A0%20ph%C3%A2n%20c%C3%B4ng%20c%C3%B4ng%20vi%E1%BB%87c%20cu%E1%BB%91i%20k%E1%BB%B3.md) để nắm rõ phân công chi tiết cho 7 thành viên và trạng thái số liệu Engine v2.
2. **Tra cứu định nghĩa công thức:** Mở tệp [`Dinh_nghia_ham_toan_hoc.docx`](Dinh_nghia_ham_toan_hoc.docx) để lấy công thức chuẩn đưa vào Báo cáo Chương 2 và Chương 4.
3. **Truy cập Google Drive nhóm:** Đọc đường dẫn trong tệp [`Nhom_03.txt`](Nhom_03.txt) để truy cập kho dữ liệu dung lượng lớn.
