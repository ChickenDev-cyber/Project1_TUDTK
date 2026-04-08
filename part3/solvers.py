import numpy as np
import math as mth
from fractions import Fraction

def back_substitution(U, c, r):
    n_rows = len(U)
    n_cols = len(U[0])
    
    # Kiểm tra Vô nghiệm trước
    for i in range(r, n_rows):
        if c[i] != 0:
            print("Lỗi: Hệ phương trình Vô nghiệm.")
            return None
            
    # Sau khi chắc chắn có nghiệm, mới kiểm tra Vô số nghiệm
    if r < n_cols:
        print("Lỗi: Hệ phương trình có Vô số nghiệm.")
        return None
    
    x_val = [Fraction(0)] * n_cols
    
    for i in range(r - 1, -1, -1):
        pivot_col = -1
        for j in range(n_cols):
            if U[i][j] != 0:
                pivot_col = j
                break
        
        if pivot_col != -1:
            sum_ax = sum(U[i][j] * x_val[j] for j in range(pivot_col + 1, n_cols))
            x_val[pivot_col] = (c[i] - sum_ax) / U[i][pivot_col]
    
    return x_val

# THÀNH VIÊN 1: PHƯƠNG PHÁP KHỬ GAUSS
def solve_gauss(A, b):

    # 2. Thuật toán Khử Gauss chính
    n = len(A)
    m = len(A[0]) if n > 0 else 0

    # Chuyển đổi dữ liệu đầu vào (kể cả numpy array) thành list chứa Fraction
    M = [[Fraction(val) for val in row] + [Fraction(b[i])] for i, row in enumerate(A)]
    s = 0
    r = 0 

    for c_idx in range(m):
        if r >= n:
            break

        p = r
        for i in range(r + 1, n):
            # So sánh trị tuyệt đối của Fraction
            if abs(M[i][c_idx]) > abs(M[p][c_idx]):
                p = i

        if M[p][c_idx] == 0:
            continue

        if p != r:
            M[r], M[p] = M[p], M[r]
            s += 1

        for i in range(r + 1, n):
            f = M[i][c_idx] / M[r][c_idx]
            M[i][c_idx] = Fraction(0) 
            for j in range(c_idx + 1, m + 1):
                M[i][j] -= M[r][j] * f
        
        r += 1 

    U = [row[:m] for row in M]
    c_result = [row[m] for row in M]

    # Gọi hàm thế ngược
    x_fraction = back_substitution(U, c_result, r)
    
    # 3. Trả về kết quả
    if x_fraction is None:
        return [] # Trả về mảng rỗng nếu vô nghiệm/vô số nghiệm
        
    # Ép Fraction về lại float để in ra cho đẹp và đồng bộ với các phương pháp khác
    return [float(val) for val in x_fraction]

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

# Tính độ lệch
def manual_norm(vector):
    return mth.sqrt(sum(v**2 for v in vector))

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
        diff = [(x[i] - x_old[i]) for i in range(n)]
        error = manual_norm(diff)
        
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