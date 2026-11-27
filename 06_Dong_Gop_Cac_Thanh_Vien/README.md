# THƯ MỤC KHÔNG GIAN LÀM VIỆC CỦA 7 THÀNH VIÊN (NHÓM 03 - DS317.R11)

## 1. MỤC ĐÍCH & Ý NGHĨA
Thư mục `06_Dong_Gop_Cac_Thanh_Vien/` được thiết kế nhằm phân quyền không gian làm việc độc lập cho 7 thành viên trong giai đoạn nước rút hoàn thiện Đồ án cuối kỳ.
- **Mục tiêu chính:** Tránh 100% tình trạng xung đột mã nguồn (merge conflicts) trên GitHub khi nhiều thành viên cùng nộp tài liệu, slide, script kiểm định hoặc mã nguồn ứng dụng.
- **Nguyên tắc làm việc:** Mỗi thành viên toàn quyền phát triển sản phẩm trong thư mục riêng của mình. Nhóm trưởng sẽ định kỳ rà soát, kiểm chuẩn chất lượng và merge các sản phẩm đạt tiêu chuẩn vào thư mục nộp bài chuẩn 8 phần [`DS317_R11_Nhom03_HoSoNopDoAn/`](../DS317_R11_Nhom03_HoSoNopDoAn/README.md).

---

## 2. BẢNG CHỈ MỤC THƯ MỤC CÁ NHÂN CỦA 7 THÀNH VIÊN

| STT | Thành viên & MSSV | Vai trò chính | Thư mục làm việc cá nhân | Đường dẫn tương đối | Trạng thái |
| :-: | :--- | :--- | :--- | :--- | :---: |
| 1 | **Võ Đình Kiên** *(24520893)* | Nhóm trưởng, Quản trị dự án, Chủ trì Chương 5 | `Thanh_Vien_01_VoDinhKien/` | [`Thanh_Vien_01_VoDinhKien/README.md`](Thanh_Vien_01_VoDinhKien/README.md) | Sẵn sàng |
| 2 | **Đỗ Văn Lộc** *(24520977)* | Thư ký, Kỹ sư Demo Web `app.py` | `Thanh_Vien_02_DoVanLoc/` | [`Thanh_Vien_02_DoVanLoc/README.md`](Thanh_Vien_02_DoVanLoc/README.md) | Sẵn sàng |
| 3 | **Quách Tuấn Kiệt** *(24520911)* | Chương 2 Dữ liệu & DAMA, Module M3, Tái lập code | `Thanh_Vien_03_QuachTuanKiet/` | [`Thanh_Vien_03_QuachTuanKiet/README.md`](Thanh_Vien_03_QuachTuanKiet/README.md) | Sẵn sàng |
| 4 | **Huỳnh Chí Kiên** *(24520880)* | Biểu đồ Engine v2 & XAI (SHAP) | `Thanh_Vien_04_HuynhChiKien/` | [`Thanh_Vien_04_HuynhChiKien/README.md`](Thanh_Vien_04_HuynhChiKien/README.md) | Sẵn sàng |
| 5 | **Nguyễn Hữu Bảo Lộc** *(24520983)* | SOTA IEEE, `references.bib` & Đạo đức AI | `Thanh_Vien_05_NguyenHuuBaoLoc/` | [`Thanh_Vien_05_NguyenHuuBaoLoc/README.md`](Thanh_Vien_05_NguyenHuuBaoLoc/README.md) | Sẵn sàng |
| 6 | **Lê Sỹ Liêm** *(24520951)* | Kiểm định Thống kê, Phân tích nhóm thời gian & ROI | `Thanh_Vien_06_LeSyLiem/` | [`Thanh_Vien_06_LeSyLiem/README.md`](Thanh_Vien_06_LeSyLiem/README.md) | Sẵn sàng |
| 7 | **Trần Hồng Lĩnh** *(24520970)* | Chủ trì toàn bộ Slide Bảo vệ, Case Study lỗi | `Thanh_Vien_07_TranHongLinh/` | [`Thanh_Vien_07_TranHongLinh/README.md`](Thanh_Vien_07_TranHongLinh/README.md) | Sẵn sàng |

---

## 3. QUY TRÌNH PHỐI HỢP GIT NHÓM (GIT COLLABORATION WORKFLOW)

```
[Nhánh main trên GitHub]
       │
       ├── Tạo nhánh feature riêng: feature/<ten_thanh_vien>
       │      │
       │      ├── Thành viên làm việc, commit & push vào thư mục riêng của mình:
       │      │   06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_XX_<Ten>/
       │      │
       │      └── Mở Pull Request (PR) vào nhánh main
       │
       ├── Nhóm trưởng review PR & kiểm tra tính toàn vẹn (0 broken link, chuẩn PEP 8, dấu '-')
       │
       └── Merge vào main -> Tự động/bán tự động đồng bộ vào DS317_R11_Nhom03_HoSoNopDoAn/
```

### Các lệnh Git mẫu cho từng thành viên:
1. **Trước khi bắt đầu:** Luôn kéo bản mới nhất về máy:
   ```bash
   git checkout main
   git pull origin main
   ```
2. **Tạo nhánh cá nhân:**
   ```bash
   git checkout -b feature/<ten_thanh_vien>
   # Ví dụ: git checkout -b feature/dovanloc
   ```
3. **Thao tác và lưu file:** Chỉ thêm/sửa file trong thư mục của chính mình.
4. **Commit và đẩy lên GitHub:**
   ```bash
   git add 06_Dong_Gop_Cac_Thanh_Vien/Thanh_Vien_XX_<Ten>/
   git commit -m "feat(<ten>): mo ta ngan gon cong viec da hoan thanh"
   git push origin feature/<ten_thanh_vien>
   ```
5. **Mở Pull Request (PR):** Truy cập giao diện GitHub của nhóm, bấm nút **Compare & pull request**, ghi chú các file bàn giao để Nhóm trưởng nghiệm thu.
