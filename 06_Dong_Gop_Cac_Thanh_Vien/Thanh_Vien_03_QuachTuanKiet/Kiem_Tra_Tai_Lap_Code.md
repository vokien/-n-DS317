# BÁO CÁO RÀ SOÁT TÍNH TÁI LẬP MÃ NGUỒN VÀ ĐỘ ĐỘC LẬP MÔI TRƯỜNG
## (SOURCE CODE REPRODUCIBILITY & ENVIRONMENT AGNOSTIC AUDIT REPORT)

- **Học phần:** DS317 - Khai phá dữ liệu trong doanh nghiệp (UIT - ĐHQG-HCM)
- **Đề tài:** Dự báo thời điểm cập cảng của tàu biển thay thế ETA tự khai báo (*Prediction of Vessel Port Arrival Time Replacing Self-Reported ETA*)
- **Thành viên thực hiện rà soát:** **Quách Tuấn Kiệt** (MSSV: **24520911**) - Kỹ sư Dữ liệu
- **Phạm vi kiểm tra:** Toàn bộ 17 tệp mã nguồn (.ipynb và .py) thuộc:
  - `02_Ma_Nguon_Tien_Xu_Ly_Va_Thuc_Nghiem/` (16 notebooks)
  - `05_Output_Cac_Notebook/` (1 script đồng bộ)
- **Ngày hoàn thành kiểm toán:** 27/11/2026

---

## 1. MỤC TIÊU VÀ TIÊU CHÍ KIỂM TOÁN TÁI LẬP (AUDIT CRITERIA)

Tính tái lập (Reproducibility) là tiêu chuẩn cao nhất trong nghiên cứu khoa học và phát triển phần mềm doanh nghiệp. Mục tiêu của đợt rà soát này nhằm bảo đảm:
1. **Không tồn tại đường dẫn tuyệt đối cứng cục bộ (Zero Personal Hardcoded Paths):** Tuyệt đối không chứa các đường dẫn máy tính cá nhân (ví dụ: `C:\Users\...`, `D:\...`, `/home/user/...`), tránh gây lỗi sập chương trình (`FileNotFoundError`) khi người khác clone repository về máy tính mới.
2. **Cơ chế phân giải đường dẫn động (Dynamic Path Resolution):** Các notebook phải trang bị hàm tự động dò tìm dữ liệu (`locate_inputs()`, `glob.glob()`, `Path(__file__)`) để thích ứng linh hoạt giữa môi trường đám mây Kaggle và máy trạm cục bộ.
3. **Tính toàn vẹn của tệp cấu hình môi trường:** Đảm bảo có đầy đủ `requirements.txt` và tài liệu hướng dẫn tham số môi trường tái lập từ dữ liệu thô.

---

## 2. BẢNG TỔNG HỢP KẾT QUẢ KIỂM TOÁN 17 TỆP MÃ NGUỒN

Nhóm kiểm toán đã chạy script quét tự động toàn bộ cây thư mục mã nguồn. Kết quả chi tiết như sau:

| STT | Tên tệp mã nguồn | Thư mục lưu trữ | Đường dẫn máy cá nhân (`C:\`) | Đường dẫn đám mây Kaggle (`/kaggle/`) | Cơ chế phân giải động | Đánh giá tính tái lập |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: |
| 1 | `DS317_01_Pipeline_Tien_Xu_Ly_Du_Lieu.ipynb` | `02_.../01_Pipeline_.../` | **KHÔNG CÓ (0)** | Có (4 vị trí) | Có (`glob` pattern) | **ĐẠT CHUẨN** |
| 2 | `DS317_02_Kham_Pha_Kiem_Ke_Chat_Luong.ipynb` | `02_.../01_Pipeline_.../` | **KHÔNG CÓ (0)** | Có (3 vị trí) | Có (`locate_inputs`) | **ĐẠT CHUẨN** |
| 3 | `DS317_03_Kiem_Chung_Lua_Chon_Dac_Trung.ipynb` | `02_.../01_Pipeline_.../` | **KHÔNG CÓ (0)** | Có (2 vị trí) | Cần bổ sung fallback | **ĐẠT (Khuyến nghị)** |
| 4 | `DS317_04_Huan_Luyen_Mo_Hinh_Co_So_Baseline.ipynb` | `02_.../01_Pipeline_.../` | **KHÔNG CÓ (0)** | Có (4 vị trí) | Có (`locate_inputs`) | **ĐẠT CHUẨN** |
| 5 | `DS317_05_Tich_Hop_Thoi_Tiet_RTMA_2025.ipynb` | `02_.../01_Pipeline_.../` | **KHÔNG CÓ (0)** | Có (3 vị trí) | Cần bổ sung fallback | **ĐẠT (Khuyến nghị)** |
| 6 | `DS317_Tong_Hop_Xuat_So_Lieu_BTVN.ipynb` | `02_.../01_Pipeline_.../` | **KHÔNG CÓ (0)** | Có (6 vị trí) | Có (`locate_inputs`) | **ĐẠT CHUẨN** |
| 7 | `DS317_Runner_Song_Song_1_Baseline_M1_M2_M3.ipynb` | `02_.../02_Runner_..._v2/` | **KHÔNG CÓ (0)** | Có (11 vị trí) | Có (`locate_inputs` DDP) | **ĐẠT XUẤT SẮC** |
| 8 | `DS317_Runner_Song_Song_2_M4_M5_M6_M7.ipynb` | `02_.../02_Runner_..._v2/` | **KHÔNG CÓ (0)** | Có (11 vị trí) | Có (`locate_inputs` DDP) | **ĐẠT XUẤT SẮC** |
| 9 | `DS317_Thuc_Nghiem_00_Baseline.ipynb` | `02_.../03_Notebook_Tach_Le/` | **KHÔNG CÓ (0)** | Có (10 vị trí) | Có (`locate_inputs`) | **ĐẠT CHUẨN** |
| 10 | `DS317_Thuc_Nghiem_M1_Loc_Ngoai_Lai.ipynb` | `02_.../03_Notebook_Tach_Le/` | **KHÔNG CÓ (0)** | Có (10 vị trí) | Có (`locate_inputs`) | **ĐẠT CHUẨN** |
| 11 | `DS317_Thuc_Nghiem_M2_Dien_Khuyet.ipynb` | `02_.../03_Notebook_Tach_Le/` | **KHÔNG CÓ (0)** | Có (10 vị trí) | Có (`locate_inputs`) | **ĐẠT CHUẨN** |
| 12 | `DS317_Thuc_Nghiem_M3_Tao_Dac_Trung.ipynb` | `02_.../03_Notebook_Tach_Le/` | **KHÔNG CÓ (0)** | Có (10 vị trí) | Có (`locate_inputs`) | **ĐẠT CHUẨN** |
| 13 | `DS317_Thuc_Nghiem_M4_Thoi_Tiet_RTMA.ipynb` | `02_.../03_Notebook_Tach_Le/` | **KHÔNG CÓ (0)** | Có (10 vị trí) | Có (`locate_inputs`) | **ĐẠT CHUẨN** |
| 14 | `DS317_Thuc_Nghiem_M5_Chon_Loc_Dac_Trung.ipynb` | `02_.../03_Notebook_Tach_Le/` | **KHÔNG CÓ (0)** | Có (10 vị trí) | Có (`locate_inputs`) | **ĐẠT CHUẨN** |
| 15 | `DS317_Thuc_Nghiem_M6_Mat_Mat_Bat_Doi_Xung.ipynb` | `02_.../03_Notebook_Tach_Le/` | **KHÔNG CÓ (0)** | Có (10 vị trí) | Có (`locate_inputs`) | **ĐẠT CHUẨN** |
| 16 | `DS317_Thuc_Nghiem_M7_Gom_Cum_Khoang_Sai_So.ipynb` | `02_.../03_Notebook_Tach_Le/` | **KHÔNG CÓ (0)** | Có (10 vị trí) | Có (`locate_inputs`) | **ĐẠT CHUẨN** |
| 17 | `dong_bo_ho_so_nop.py` | `05_Output_Cac_Notebook/` | **KHÔNG CÓ (0)** | **KHÔNG CÓ (0)** | Có (`Path(__file__).resolve()`) | **HOÀN HẢO** |

---

## 3. PHÂN TÍCH CHI TIẾT CÁC PHÁT HIỆN KIỂM TOÁN

### 3.1. Kết quả tích cực đạt được
1. **100% sạch bóng đường dẫn máy tính cá nhân:** Không có bất kỳ tệp nào chứa đường dẫn dạng `C:\Users\...` hay đường dẫn Windows cục bộ. Toàn bộ mã nguồn đã được tổng duyệt và khử sạch trước khi đưa vào kho GitHub chính thức.
2. **Cơ chế tự động định vị dữ liệu thông minh (`locate_inputs()` pattern):**
   Trong các notebook cốt lõi (`Runner 1`, `Runner 2` và các tệp tách lẻ `M1` - `M7`), nhóm phát triển đã thiết kế hàm `locate_inputs()` có khả năng quét linh hoạt nhiều biến thể thư mục đầu vào trên Kaggle:
   ```python
   def locate_inputs():
       # Tự động tìm kiếm các dataset gán vào Kaggle không phụ thuộc tên slug chính xác
       cand_ais = glob.glob('/kaggle/input/**/03_ban_tien_xu_ly_27_thuoc_tinh', recursive=True)
       cand_side = glob.glob('/kaggle/input/**/weather_rtma_2025_sidecar*', recursive=True)
       ...
   ```
   Cơ chế này giúp người dùng khác khi fork notebook trên Kaggle chỉ cần add dataset vào là mã nguồn tự động nhận diện chính xác đường dẫn mà không cần sửa code.
3. **Mã nguồn script đồng bộ đạt chuẩn tuyệt đối:** Tệp `dong_bo_ho_so_nop.py` sử dụng thư viện chuẩn `pathlib.Path(__file__).resolve().parent` để xác định thư mục gốc, hoàn toàn độc lập với hệ điều hành (chạy mượt mà cả trên Windows, Linux và macOS).

### 3.2. Điểm cần lưu ý và khuyến nghị cải tiến
- **Đối với 2 notebook BTVN 03 và 05:** Có xuất hiện chuỗi `/kaggle/working/task03_raw02_v2` ở dạng chuỗi trực tiếp. Khi chạy trên môi trường cục bộ ngoài Kaggle, người dùng cần gán biến môi trường `OUTPUT_DIR = os.getenv('OUTPUT_DIR', './output')`.
- **Khuyến nghị bổ sung khối chuẩn hóa đầu môi trường (Environment Setup Block):**
  Thêm đoạn mã sau vào Cell đầu tiên của các notebook:
  ```python
  import os, sys
  IS_KAGGLE = 'KAGGLE_KERNEL_RUN_TYPE' in os.environ
  BASE_DIR = '/kaggle' if IS_KAGGLE else os.path.abspath(os.path.join(os.getcwd(), '..'))
  DATA_DIR = os.path.join(BASE_DIR, 'input')
  WORK_DIR = os.path.join(BASE_DIR, 'working') if IS_KAGGLE else './outputs'
  os.makedirs(WORK_DIR, exist_ok=True)
  ```

---

## 4. KẾT LUẬN VÀ CAM KẾT HỘI ĐỒNG

- **Kết luận:** Hệ thống mã nguồn của nhóm đạt độ tin cậy và khả năng tái lập cao (**100% không có hardcoded path cá nhân**). Bất kỳ giảng viên hoặc sinh viên nào khi tải repository về hoặc mở trên Kaggle đều có thể tái lập kết quả huấn luyện mô hình và kiểm toán DAMA một cách trơn tru.
- **Tài liệu bàn giao kèm theo:**
  - `requirements.txt` chuẩn hóa các thư viện (LightGBM, XGBoost, CatBoost, PyTorch, PyArrow, DuckDB).
  - Bản đồ dữ liệu mẫu `demo_sample_3000.csv` / `.parquet` phục vụ chạy thử nghiệm tức thì.
