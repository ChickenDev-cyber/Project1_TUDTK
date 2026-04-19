# Đồ án 1: Ma Trận và Cơ Sở của Tính Toán Khoa Học 🧮

**Môn học:** Toán Ứng Dụng và Thống Kê (MTH00051)  
**Giảng viên hướng dẫn:** Bộ môn Toán - Khoa CNTT  
**Trường:** Đại học Khoa học Tự nhiên, ĐHQG-HCM  
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