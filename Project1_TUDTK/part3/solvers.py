import numpy as np

# ==========================================
# THÀNH VIÊN 1: PHƯƠNG PHÁP KHỬ GAUSS
# ==========================================
def solve_gauss(A, b):
    """
    Giải hệ Ax = b bằng phương pháp khử Gauss (có partial pivoting).
    Đầu vào: Ma trận A (numpy array 2D), vector b (numpy array 1D)
    Đầu ra: vector nghiệm x (numpy array 1D)
    """
    # ... Code thuật toán của Thành viên 1 ở đây ...
    # Nhớ phải có bước đổi chỗ hàng (pivoting) để tránh chia cho 0
    return x

# ==========================================
# THÀNH VIÊN 2: PHƯƠNG PHÁP PHÂN RÃ LU
# ==========================================
def solve_lu(A, b):
    """
    Giải hệ Ax = b bằng phân rã LU.
    """
    # Bước 1: Phân rã A thành L và U
    # ... Code tìm L, U ...
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Tạo ma trận U
        for k in range(i, n):
            sum_lu = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - sum_lu
            
        if abs(U[i][i]) < 1e-12:  # Kiểm tra nếu U[i][i] gần bằng 0 để tránh chia cho 0
            raise ValueError(f"Phân rã LU thất bại: U[{i}][{i}] gần bằng 0, cần pivoting hoặc kiểm tra lại ma trận A.")
            
        # Tạo ma trận L
        for k in range(i, n):
            if i == k:
                L[i][i] = 1  # Đường chéo chính của L là 1
            else:
                sum_lu = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - sum_lu) / U[i][i] # Chia cho U[i][i] để tính L[k][i], không phải chia cho 0 vì đã kiểm tra ở trên

    
    # Bước 2: Giải Ly = b (Thế tiến)
    # ...
    y = np.zeros(n)
    for i in range(n):
        sum_ly = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - sum_ly) / L[i][i]  


    
    # Bước 3: Giải Ux = y (Thế lùi)
    # ...
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        sum_ux = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - sum_ux) / U[i][i]
    return x

# ==========================================
# THÀNH VIÊN 3: PHƯƠNG PHÁP LẶP GAUSS-SEIDEL
# ==========================================
def solve_gauss_seidel(A, b, tol=1e-6, max_iter=1000):
    """
    Giải hệ Ax = b bằng phương pháp lặp Gauss-Seidel.
    tol: Sai số dừng vòng lặp (tolerance)
    max_iter: Số vòng lặp tối đa để tránh lặp vô hạn
    """
    # Bước 1 (Quan trọng để lấy điểm): Kiểm tra điều kiện hội tụ
    # Ví dụ: Kiểm tra A có phải chéo trội hàng (strictly diagonally dominant) không?
    # Nếu không thỏa mãn, có thể in ra cảnh báo (print)
    
    # Bước 2: Khởi tạo nghiệm ban đầu x0 (thường là vector toàn số 0)
    x = np.zeros_like(b, dtype=np.double)
    
    # Bước 3: Vòng lặp tính x_new từ x_old
    # ... Code lặp của Thành viên 3 ở đây ...
    # Nhớ kiểm tra sai số ||x_new - x|| < tol thì break (dừng lặp)
    
    return x

if __name__ == "__main__":
    A_test = np.array([
        [4.0, -1.0,  0.0],
        [-1.0, 4.0, -1.0],
        [ 0.0, -1.0, 4.0]
    ])
    b_test = np.array([3.0, 2.0, 3.0])
    
    print("=== TEST NHANH CÁC THUẬT TOÁN ===")
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
        
        # Tính Ax để so sánh với b
        b_reconstruct = np.dot(A_test, x_lu) 
        
        # Tính sai số tuyệt đối giữa b và b_reconstruct
        error = np.linalg.norm(b_test - b_reconstruct, ord=np.inf)  #
        
        print("2. Nghiệm Phân rã LU:  ", x_lu)
        print("Vector b tái tạo từ Ax: ", b_reconstruct)
        print("   Sai số ||b - Ax||: ", error)
        
        # Kết luận
        if error < 1e-6:
            print("   Kết luận: Nghiệm LU chính xác (sai số nhỏ).")
        else:
            print("   Kết luận: Nghiệm LU có sai số lớn, cần kiểm tra lại.")
    except Exception as e:
        print("2. Phân rã LU LỖI:     ", e)

    # GAUSS-SEIDEL
    try:
        x_gs = solve_gauss_seidel(A_test.copy(), b_test.copy())
        print("3. Nghiệm Gauss-Seidel:", np.round(x_gs, 5)) # Round 5 chữ số
    except Exception as e:
        print("3. Gauss-Seidel LỖI:   ", e)