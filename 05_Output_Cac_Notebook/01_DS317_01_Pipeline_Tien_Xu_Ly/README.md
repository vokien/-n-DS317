# Kết Quả Đầu Ra: Pipeline Tiền Xử Lý Dữ Liệu (`01_DS317_01_Pipeline_Tien_Xu_Ly/`)

Thư mục này lưu trữ cấu trúc kết quả đầu ra từ notebook tiền xử lý cốt lõi [`DS317_01_Pipeline_Tien_Xu_Ly_Du_Lieu.ipynb`](../../02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/01_Pipeline_Tien_Xu_Ly_Va_BTVN/DS317_01_Pipeline_Tien_Xu_Ly_Du_Lieu.ipynb).

---

## 1. Mục Đích và Vai Trò Kỹ Thuật

Notebook `DS317_01` thực hiện quy trình xử lý dữ liệu lớn (Big Data Pipeline) 2-Pass trên `256.94M` bản tin tàu biển NOAA AIS năm 2025. Thư mục này tổ chức kết quả theo 3 phiên bản dữ liệu tiến triển:
1. **Bản thô 18 thuộc tính (`01_ban_tho_18_thuoc_tinh/`):** Dữ liệu sau khi trích xuất 18 trường thông tin chuẩn từ USCG NOAA AIS.
2. **Bản nền tảng 22 thuộc tính (`02_ban_nen_tang_22_thuoc_tinh/`):** Dữ liệu sạch sau Pass 1 (khử trùng lặp 7 ngày, lọc neo đậu $status \notin \{1,5\}$, lọc trôi dạt $sog \ge 1.0$ kn, điền khuyết Group Median 3 cấp, bổ sung 4 biến động học). Đạt `92,681,850` bản ghi sạch.
3. **Bản tiền xử lý 27 thuộc tính (`03_ban_tien_xu_ly_27_thuoc_tinh/`):** Dữ liệu hoàn chỉnh sau Pass 2 (tính toán cự ly hình học Haversine đến bến `Dist_To_Berth_NM`, trích xuất chu kỳ thời gian và thời điểm cập bến `ata_time`).

---

## 2. Cấu Trúc Thư Mục và Quy Tắc Quản Trị Tệp Lớn

```text
01_DS317_01_Pipeline_Tien_Xu_Ly/
├── 01_ban_tho_18_thuoc_tinh/         <- Quản lý q1..q4.parquet (bản thô 18 cột)
├── 02_ban_nen_tang_22_thuoc_tinh/    <- Quản lý q1..q4.parquet (bản sạch 22 cột)
├── 03_ban_tien_xu_ly_27_thuoc_tinh/  <- Quản lý q1..q4.parquet (bản chuẩn 27 cột)
├── artifacts/                        <- Lưu trữ metadata cấu hình pipeline
└── README.md
```

> [!NOTE]
> **Quy định quản lý tệp nhị phân lớn trên Git:**
> - Các tệp dữ liệu bảng dạng `.parquet` của cả 3 phiên bản có dung lượng từ 500 MB đến 2.5 GB mỗi quý, vượt quá ngưỡng giới hạn 100 MB của GitHub.
> - Căn cứ tệp cấu hình [`.gitignore`](../../.gitignore), các tệp `.parquet` được bảo vệ không đẩy lên GitHub và được lưu trữ trên nền tảng đám mây **Kaggle Datasets** và **Google Drive Nhóm 03**.
> - Chi tiết liên kết tải và mã checksum SHA-256 được công bố tại [`04_Data/README.md`](../../DS317_R11_Nhom03_HoSoNopDoAn/04_Data/README.md).

---

## 3. Phân Công Trách Nhiệm

- **Võ Đình Kiên:** Trực tiếp lập trình và thực thi pipeline 2-Pass trên Kaggle Kernel.
- **Quách Tuấn Kiệt:** Kiểm tra tính toàn vẹn của schema dữ liệu qua từng pass.
