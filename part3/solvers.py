import numpy as np

# THÀNH VIÊN 1: PHƯƠNG PHÁP KHỬ GAUSS
def solve_gauss(A, b):
    """
    Giải hệ Ax = b bằng phương pháp khử Gauss (có partial pivoting).
    Đầu vào: Ma trận A (numpy array 2D), vector b (numpy array 1D)
    Đầu ra: vector nghiệm x (numpy array 1D)
    """
    # ... Code thuật toán của Thành viên 1 ở đây ...
    # Nhớ phải có bước đổi chỗ hàng (pivoting) để tránh chia cho 0
    # return x

#PHƯƠNG PHÁP PHÂN RÃ LU
def solve_lu(A, b):
    """
    Giải hệ Ax = b bằng phân rã LU.
    """
    # Bước 1: Phân rã A thành L và U
    # ... Code tìm L, U ...
    
    # Bước 2: Giải Ly = b (Thế tiến)
    # ...
    
    # Bước 3: Giải Ux = y (Thế lùi)
    # ...
    # return x

# Kiểm tra ma trận chéo trội
def IsStrictlyDiagonallyDominant(A):
    n = len(A)
    for i in range(n):
        diag_val = abs(A[i][i])
        off_diag_sum = 0.0
        for j in range(n):
            if i != j:
                off_diag_sum += abs(A[i][j])
        
        # Nếu có bất kỳ hàng nào mà phần tử chéo không đủ lớn -> Không chéo trội
        if diag_val <= off_diag_sum:
            return False
    return True

# PHƯƠNG PHÁP LẶP GAUSS-SEIDEL
def solve_gauss_seidel(A, b, tol=1e-6, max_iter=1000):

    "vài lưu ý sống còn cho Project của bạn:Chia cho 0: Nếu a[i][i] = 0$, code sẽ bị lỗi ngay. "
    "Trong thực tế, người ta thường dùng Partial Pivoting (đổi hàng) để đưa phần tử lớn nhất lên đường chéo trước khi lặp."
    
    # Bước 1 : Kiểm tra điều kiện hội tụ
    if not IsStrictlyDiagonallyDominant(A):
        print("Cảnh báo: Ma trận không chéo trội hàng. Thuật toán có thể không hội tụ!")
        return []

    n = len(A)
    x = [0.0] * n
    
    for k in range(max_iter):
        # Lưu lại nghiệm cũ 
        x_old = list(x)
        
        for i in range(n):
            sigma = 0.0
            for j in range(n):
                if j != i: #Nếu j != i có nghĩa là khác nghiệm đang cần thay thì cộng dồn
                    sigma += A[i][j] * x[j]
            
            # Cập nhật x[i] trực tiếp vào mảng, tìm nghiệm xi (lấy const - phương trình, chuyển vế)
            x[i] = (b[i] - sigma) / A[i][i]
            
        # Bước 2: Kiểm tra điều kiện dừng (Sai số Euclid hoặc Max tuyệt đối)
        # Tính chuẩn L2 của (x_new - x_old)
        error = np.linalg.norm(np.array(x) - np.array(x_old))
        
        # Kiểm tra hội tụ mỗi vòng lặp, xem độ lệch gần bằng 0 hay chưa.
        if error < tol: 
            print(f"Hội tụ sau {k+1} vòng lặp.")
            return x
            
    print("Không hội tụ sau số lần lặp tối đa.")
    return x

if __name__ == "__main__":
    A_test = np.array([
        [4.0, -1.0,  0.0],
        [-1.0, 4.0, -1.0],
        [ 0.0, -1.0, 4.0]
    ])
    b_test = np.array([3.0, 2.0, 3.0])
    
    print("Nghiệm kỳ vọng (Lý thuyết): [1. 1. 1.]\n")

    # KHỬ GAUSS
    try:
        x_gauss = solve_gauss(A_test.copy(), b_test.copy())
        print("1. Nghiệm Khử Gauss:   ", x_gauss)
    except Exception as e:
        print("1. Khử Gauss LỖI:      ", e)

    # PHÂN RÃ LU
    try:
        x_lu = solve_lu(A_test.copy(), b_test.copy())
        print("2. Nghiệm Phân rã LU:  ", x_lu)
    except Exception as e:
        print("2. Phân rã LU LỖI:     ", e)

    # GAUSS-SEIDEL
    try:
        x_gs = solve_gauss_seidel(A_test.copy(), b_test.copy())
        print("3. Nghiệm Gauss-Seidel:", np.round(x_gs, 5)) # Round 5 chữ số
    except Exception as e:
        print("3. Gauss-Seidel LỖI:   ", e)