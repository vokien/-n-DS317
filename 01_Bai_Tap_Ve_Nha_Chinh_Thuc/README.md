# HỆ THỐNG BÀI TẬP VỀ NHÀ (BTVN) MÔN HỌC DS317
**Môn học:** DS317 - Khai phá dữ liệu trong doanh nghiệp (Data Mining for Enterprise)  
**Đơn vị:** Khoa Khoa học và Kỹ thuật Thông tin - Trường Đại học Công nghệ Thông tin (ĐHQG-HCM)  
**Nhóm sinh viên thực hiện:** Nhóm 03 - Lớp DS317.R11  

---

## 1. Cấu trúc tổng thể các đợt BTVN

Thư mục này tổ chức toàn bộ các bài tập về nhà theo từng giai đoạn tiến trình học phần môn học, kết nối chặt chẽ từ khâu xác định bài toán, đo lường chất lượng dữ liệu, bảo vệ thuyết minh đề tài đến thiết kế công nghệ khai phá dữ liệu và phát hiện ngoại lai.

Các file có quy định mẫu tên bắt buộc theo mẫu hướng dẫn của môn học (Đề xuất đề tài BT1 và Thuyết minh đề tài BT3) được đặt chính xác theo định dạng quy chuẩn; các file còn lại được đặt tên tiếng Việt có dấu với khoảng trắng tự nhiên:

```text
Bài tập về nhà/
├── BT1 - Xác định bài toán khai phá dữ liệu/
│   ├── Bước 1 - Rà soát tài sản dữ liệu.xlsx
│   ├── Bước 2 - Xác định bối cảnh và nhu cầu doanh nghiệp.docx
│   ├── Bước 3 - Chuyển bài toán nghiệp vụ thành bài toán KPDL.docx
│   ├── Bước 4 - Thẩm định tính khả thi.docx
│   ├── DS317.R11_Nhom03_DeXuat.docx                   <- Định dạng mẫu quy định
│   └── README.md
├── BT2 - Đo lường và giám sát độ đo chất lượng dữ liệu/
│   ├── BT - Đo lường và giám sát độ đo chất lượng dữ liệu.docx
│   ├── BT - Đo lường và giám sát độ đo chất lượng dữ liệu.pdf
│   ├── DS317 - Đo lường giám sát chất lượng 6 khía cạnh.ipynb
│   ├── DS317 C4 - Mẫu hướng dẫn giáo viên.ipynb
│   ├── Hình ảnh biểu đồ/
│   │   ├── Hình 1 - Phân phối Target Hours.png
│   │   ├── Hình 2 - Phân tán Dist vs Target.png
│   │   ├── Hình 3 - Biểu đồ hộp SOG Draft Cargo vs Tanker.png
│   │   └── Hình 4 - Mật độ địa không gian.png
│   └── README.md
├── BT3 - Thuyết minh đề tài (Ver 1)/
│   ├── Lab3_DS317.R11_Nhom03_ThuyetMinh.docx         <- Định dạng mẫu quy định
│   ├── Lab3_DS317.R11_Nhom03_ThuyetMinh.pdf          <- Định dạng mẫu quy định
│   ├── Lab3_DS317.R11_Nhom03_DataInventory.xlsx      <- Định dạng mẫu quy định
│   ├── Lab3_DS317.R11_Nhom03_Code.ipynb              <- Định dạng mẫu quy định
│   ├── Lab3_DS317.R11_Nhom03_Slides.pdf              <- Định dạng mẫu quy định
│   ├── Lab3_DS317.R11_Nhom03_PhanCong.docx           <- Định dạng mẫu quy định
│   ├── Lab3_DS317.R11_Nhom03_PhanCong.pdf            <- Định dạng mẫu quy định
│   ├── Lab3 DS317.R11 Nhóm 03 - Kịch bản thuyết trình 15 phút.docx
│   ├── Lab3 DS317.R11 Nhóm 03 - Kịch bản thuyết trình 15 phút.pdf
│   ├── Lab3 DS317.R11 Nhóm 03 - Thuyết minh gốc.docx
│   ├── Nội dung gốc thuyết minh đề tài.docx
│   ├── Lab3 DS317 Nhóm 03 - Cũ.zip
│   └── README.md
├── BT4 - Công nghệ khai phá dữ liệu/
│   ├── Kế hoạch giám sát mô hình.docx
│   ├── Kịch bản thực nghiệm.docx
│   ├── Liệt kê các độ đo đánh giá và xác định các độ đo đánh giá dự kiến sử dụng.docx
│   ├── Liệt kê các độ đo đánh giá và xác định các độ đo đánh giá dự kiến sử dụng.pdf
│   └── Phân loại phương thức học của các thuật toán dự kiến.docx
└── BT5 - Gom nhóm và xác định ngoại lai/
    └── DS317 Nhóm 03 - Đề xuất phát hiện outlier AIS.docx
```

---

## 2. Tóm tắt nội dung từng đợt BTVN

### [BT1 - Xác định bài toán khai phá dữ liệu](BT1_Xac_Dinh_Bai_Toan/README.md)
- **Nội dung:** Thực hiện 4 bước của Giai đoạn tiền đề (Chương 3): Bước 1 Rà soát tài sản dữ liệu (Data Inventory), Bước 2 Xác định bối cảnh và nhu cầu của doanh nghiệp, Bước 3 Chuyển bài toán nghiệp vụ thành bài toán khai phá dữ liệu, và Bước 4 Thẩm định tính khả thi.
- **Sản phẩm chính:** Bản đề xuất đề tài [`DS317.R11_Nhom03_DeXuat.docx`](BT1_Xac_Dinh_Bai_Toan/DS317.R11_Nhom03_DeXuat.docx) (chuẩn mẫu quy định `<MãLớp>_<TênNhóm>_DeXuat`).

### [BT2 - Đo lường và giám sát độ đo chất lượng dữ liệu](BT2_Do_Luong_Chat_Luong_Du_Lieu/README.md)
- **Nội dung:** Cài đặt tính 6 khía cạnh chất lượng dữ liệu theo chuẩn DAMA DMBOK và ISO 8000 ở mức hạt dữ liệu trên 256.94 triệu dòng thô NOAA AIS 2025 (và 92.68M dòng Bản Nền tảng 22); phân rã theo trục thời gian 4 Quý (Q1 - Q4) và trực quan hóa xu hướng chất lượng bằng biểu đồ.
- **Sản phẩm chính:** Báo cáo [`BT - Đo lường và giám sát độ đo chất lượng dữ liệu.docx`](BT2_Do_Luong_Chat_Luong_Du_Lieu/BT%20-%20%C4%90o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20gi%C3%A1m%20s%C3%A1t%20%C4%91%E1%BB%99%20%C4%91o%20ch%E1%BA%A5t%20l%C6%B0%E1%BB%A3ng%20d%E1%BB%AF%20li%E1%BB%87u.docx) & [`.pdf`](BT2_Do_Luong_Chat_Luong_Du_Lieu/BT%20-%20%C4%90o%20l%C6%B0%E1%BB%9Dng%20v%C3%A0%20gi%C3%A1m%20s%C3%A1t%20%C4%91%E1%BB%99%20%C4%91o%20ch%E1%BA%A5t%20l%C6%B0%E1%BB%A3ng%20d%E1%BB%AF%20li%E1%BB%87u.pdf) và Notebook tính toán [`DS317 - Đo lường giám sát chất lượng 6 khía cạnh.ipynb`](BT2_Do_Luong_Chat_Luong_Du_Lieu/DS317%20-%20%C4%90o%20l%C6%B0%E1%BB%9Dng%20gi%C3%A1m%20s%C3%A1t%20ch%E1%BA%A5t%20l%C6%B0%E1%BB%A3ng%206%20kh%C3%ADa%20c%E1%BA%A1nh.ipynb).

### [BT3 - Thuyết minh đề tài (Ver 1)](BT3_Thuyet_Minh_De_Tai/README.md)
- **Nội dung:** Hồ sơ Thuyết minh đề tài chính thức (Lab 3), ứng dụng toàn diện kết quả bài tập Chương 4 (Mục 5.1: 6 chiều chất lượng dữ liệu) và bài tập Chương 5 (Mục 5.2: Khám phá dữ liệu chuyên sâu EDA/BI) cho phần "Kết quả nghiên cứu sơ khởi".
- **Sản phẩm chính:** Bộ hồ sơ 5 tệp chuẩn mẫu quy định `Lab3_<MãLớp>_<TênNhóm>_<LoạiSảnPhẩm>`: [`Lab3_DS317.R11_Nhom03_ThuyetMinh.docx`](BT3_Thuyet_Minh_De_Tai/Lab3_DS317.R11_Nhom03_ThuyetMinh.docx) & [`.pdf`](BT3_Thuyet_Minh_De_Tai/Lab3_DS317.R11_Nhom03_ThuyetMinh.pdf), [`DataInventory.xlsx`](BT3_Thuyet_Minh_De_Tai/Lab3_DS317.R11_Nhom03_DataInventory.xlsx), [`Code.ipynb`](BT3_Thuyet_Minh_De_Tai/Lab3_DS317.R11_Nhom03_Code.ipynb), [`Slides.pdf`](BT3_Thuyet_Minh_De_Tai/Lab3_DS317.R11_Nhom03_Slides.pdf) và [`PhanCong.docx`](BT3_Thuyet_Minh_De_Tai/Lab3_DS317.R11_Nhom03_PhanCong.docx) & [`.pdf`](BT3_Thuyet_Minh_De_Tai/Lab3_DS317.R11_Nhom03_PhanCong.pdf).

### [BT4 - Công nghệ khai phá dữ liệu](BT4_Cong_Nghe_Khai_Pha_Du_Lieu)
- **Nội dung:** Ứng dụng nội dung Chương 6 và 7 để phân loại phương thức học thuật toán, liệt kê các độ đo đánh giá hồi quy AI, xác định các độ đo đánh giá dự kiến sử dụng, xây dựng kịch bản thực nghiệm và kế hoạch giám sát mô hình.
- **Sản phẩm chính:** Các tài liệu phân tích kỹ thuật, kịch bản thực nghiệm và kế hoạch giám sát mô hình (giữ tiếng Việt tự nhiên).

### [BT5 - Gom nhóm và xác định ngoại lai](BT5_Gom_Nhom_Va_Ngoai_Lai)
- **Nội dung:** Đề xuất phương pháp phân cụm và phát hiện hành vi bất thường, ngoại lai hành hải của tàu thuyền trên dữ liệu quỹ đạo AIS.
- **Sản phẩm chính:** Bản đề xuất `DS317 Nhóm 03 - Đề xuất phát hiện outlier AIS.docx` (bản lưu trữ ngoài repo; xem bản chính thức trong repo tại [`BT5 - Gom nhóm và xác định ngoại lai dữ liệu AIS.docx`](BT5_Gom_Nhom_Va_Ngoai_Lai/BT5%20-%20Gom%20nh%C3%B3m%20v%C3%A0%20x%C3%A1c%20%C4%91%E1%BB%8Bnh%20ngo%E1%BA%A1i%20lai%20d%E1%BB%AF%20li%E1%BB%87u%20AIS.docx)).
