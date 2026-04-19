# Đồ án 1: Ma Trận và Cơ Sở của Tính Toán Khoa Học 🧮

**Môn học:** Toán Ứng Dụng và Thống Kê (MTH00051)  
**Trường:** Đại học Khoa học Tự nhiên, ĐHQG-HCM (FIT-HCMUS)  
**Sinh viên thực hiện:** Trần Công Quang  

---

## 📝 Giới thiệu Đồ án
Dự án tập trung vào việc tự cài đặt và phân tích thực nghiệm các thuật toán Đại số tuyến tính cốt lõi. Mục tiêu không chỉ là tính toán đúng mà còn là hiểu rõ về hiệu năng hệ thống và độ ổn định số học của các thuật toán.

Dự án gồm 3 phần trọng tâm:
1. **Phần 1:** Các ứng dụng của phép khử Gauss (Giải hệ phương trình, tính định thức, nghịch đảo, tìm hạng và cơ sở).
2. **Phần 2:** Phân rã ma trận và trực quan hóa thuật toán bằng thư viện **Manim**.
3. **Phần 3:** Benchmark hiệu năng thời gian $O(n^3)$ và đánh giá sai số trên các ma trận đặc biệt (Hilbert, SPD).

---

## 📂 Sơ đồ Cấu trúc Thư mục
Cây thư mục được tổ chức logic để dễ dàng quản lý mã nguồn và báo cáo:

```text
Project1_TUDTK/
├── part1/                  # Các ứng dụng của phép khử Gauss
│   ├── gaussian.py         # Cài đặt khử Gauss & giải hệ Ax=b
│   ├── determinant.py      # Thuật toán tính định thức
│   ├── inverse.py          # Tìm ma trận nghịch đảo Gauss-Jordan
│   ├── rank_basis.py       # Tìm hạng và cơ sở không gian con
│   └── demo_p1.ipynb       # Notebook chạy thử nghiệm kết quả Phần 1
├── part2/                  # Phân rã ma trận & Hoạt ảnh (Animation)
│   ├── decomposition.py    # Thuật toán LU, QR, SVD
│   └── manim_visual.py     # Script lập trình video bằng Manim
├── part3/                  # Phân tích hiệu năng & Benchmark
│   ├── solvers.py          # Các phương pháp giải hệ (Gauss, LU, Gauss-Seidel)
│   ├── benchmark.py        # Module sinh ma trận và đo thời gian
│   └── analysis.ipynb      # Báo cáo thực nghiệm chuyên sâu & Đồ thị
├── report/                 # Chứa file báo cáo tổng kết định dạng PDF
├── requirements.txt        # Danh sách các thư viện cần thiết
└── README.md
```

---

## ⚙️ Hướng dẫn Cài đặt & Môi trường

Để đảm bảo các thuật toán và phần render video hoạt động chính xác, vui lòng thiết lập môi trường theo các bước sau:

### 1. Yêu cầu Hệ thống (System Requirements)
* **Python:** Phiên bản 3.10 trở lên.
* **FFmpeg:** (Bắt buộc cho Phần 2) Cần được cài đặt trên hệ điều hành và thêm vào biến môi trường `PATH` để Manim có thể xuất video .mp4.
* **LaTeX:** (Khuyến nghị) Cài đặt MiKTeX hoặc TeX Live để Manim render các công thức toán học sắc nét.

### 2. Cài đặt Thư viện Python
Mở Terminal/Command Prompt tại thư mục dự án và chạy lệnh:
```bash
pip install -r requirements.txt
```
*Lưu ý: Các thư viện như Numpy chỉ được sử dụng để sinh dữ liệu và đối chiếu kết quả. Toàn bộ logic giải thuật đều được tự cài đặt thủ công.*

---

## 🚀 Hướng dẫn Chạy Code & Chấm điểm

### 1. Xem kết quả thực nghiệm (Phần 1 & 3)
Cách nhanh nhất để kiểm tra là sử dụng các file **Jupyter Notebook**. Giảng viên có thể mở các file này trực tiếp trong VS Code hoặc Google Colab:
* **Kiểm tra tính đúng đắn:** Mở `part1/demo_p1.ipynb`.
* **Kiểm tra phân tích hiệu năng:** Mở `part3/analysis.ipynb`. Nhấn **"Run All"** để xem đồ thị Log-Log về độ phức tạp $O(n^3)$ và bảng sai số trên ma trận Hilbert.

### 2. Chạy các file Script Python
Nếu muốn chạy trực tiếp qua terminal:
```bash
python part1/gaussian.py
python part3/benchmark.py
```

### 3. Xem và Render video hoạt ảnh (Phần 2)
Video kết quả đã được lưu sẵn trong thư mục `part2/`. Nếu muốn render lại bằng code Manim:
```bash
manim -pql part2/manim_visual.py MatrixScene
```

---

## 📊 Kết luận rút ra từ Đồ án
* **Hiệu năng:** Thực nghiệm chứng minh thời gian chạy của Khử Gauss và LU bám sát đường lý thuyết $O(n^3)$. Khi $n$ tăng gấp đôi, thời gian tăng xấp xỉ 8 lần.
* **Độ ổn định:** Ma trận Hilbert minh chứng cho hiện tượng bùng nổ sai số trên các hệ điều kiện kém (Ill-conditioned), ngay cả khi có Partial Pivoting.
* **Tối ưu:** Gauss-Seidel là lựa chọn tối ưu cho ma trận chéo trội kích thước lớn nhờ độ phức tạp thấp hơn trong điều kiện hội tụ nhanh.

---

## 👥 Thông tin Sinh viên
* **Họ và tên:** Trần Công Quang
* **Khoa:** Công nghệ Thông tin
* **Trường:** ĐH Khoa học Tự nhiên - ĐHQG HCM
