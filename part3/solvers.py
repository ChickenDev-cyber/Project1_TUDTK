import numpy as np
import math as mth
from fractions import Fraction

def back_substitution(U, c, r):
    n_rows = len(U)
    n_cols = len(U[0])
    epsilon = 1e-12  # Sai số cho phép để so sánh số thực (float)
    
    # Kiểm tra Vô nghiệm trước
    for i in range(r, n_rows):
        if abs(c[i]) > epsilon:  # Thay vì c[i] != 0
            print("Lỗi: Hệ phương trình Vô nghiệm.")
            return None
            
    # Sau khi chắc chắn có nghiệm, mới kiểm tra Vô số nghiệm
    if r < n_cols:
        print("Lỗi: Hệ phương trình có Vô số nghiệm.")
        return None
    
    x_val = [0.0] * n_cols  # Dùng float thay vì Fraction
    
    for i in range(r - 1, -1, -1):
        pivot_col = -1
        row_U = U[i]  # Tối ưu: Lấy sẵn dòng U[i] để truy xuất nhanh hơn
        for j in range(n_cols):
            if abs(row_U[j]) > epsilon:  # Thay vì U[i][j] != 0
                pivot_col = j
                break
        
        if pivot_col != -1:
            # Tối ưu: Tự viết vòng for tính tổng sẽ chạy nhanh hơn sum() trong Python thuần
            sum_ax = 0.0
            for j in range(pivot_col + 1, n_cols):
                sum_ax += row_U[j] * x_val[j]
                
            x_val[pivot_col] = (c[i] - sum_ax) / row_U[pivot_col]
    
    return x_val

# THÀNH VIÊN 1: PHƯƠNG PHÁP KHỬ GAUSS
def solve_gauss(A, b):

    # 2. Thuật toán Khử Gauss chính
    n = len(A)
    m = len(A[0]) if n > 0 else 0

    # Chuyển đổi dữ liệu đầu vào (kể cả numpy array) thành list chứa float (Thay vì Fraction)
    M = [[float(val) for val in row] + [float(b[i])] for i, row in enumerate(A)]
    s = 0
    r = 0 

    for c_idx in range(m):
        if r >= n:
            break

        p = r
        for i in range(r + 1, n):
            # So sánh trị tuyệt đối của float
            if abs(M[i][c_idx]) > abs(M[p][c_idx]):
                p = i

        if abs(M[p][c_idx]) < 1e-12:  # Thay vì kiểm tra == 0
            continue

        if p != r:
            M[r], M[p] = M[p], M[r]
            s += 1

        row_r = M[r]  # Lấy sẵn dòng r làm chuẩn
        for i in range(r + 1, n):
            row_i = M[i]  # Lấy sẵn dòng i cần biến đổi
            f = row_i[c_idx] / row_r[c_idx]
            row_i[c_idx] = 0.0 
            
            # --- TỐI ƯU: TRỪ MẢNG NHANH KHÔNG DÙNG FOR THỨ 3 ---
            slice_i = row_i[c_idx + 1 : m + 1]
            slice_r = row_r[c_idx + 1 : m + 1]
            row_i[c_idx + 1 : m + 1] = [vi - f * vr for vi, vr in zip(slice_i, slice_r)]
        
        r += 1 

    U = [row[:m] for row in M]
    c_result = [row[m] for row in M]

    # Gọi hàm thế ngược
    x_val = back_substitution(U, c_result, r)
    
    # 3. Trả về kết quả
    if x_val is None:
        return [] # Trả về mảng rỗng nếu vô nghiệm/vô số nghiệm
        
    # Không cần bước ép Fraction về lại float nữa vì x_val đã là mảng float sẵn rồi
    return x_val

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
    n = len(A)
    x = [0.0] * n  # Khởi tạo vector nghiệm toàn số 0
    
    # Kiểm tra xem có phần tử 0 trên đường chéo chính không
    for i in range(n):
        if A[i][i] == 0:
            raise ValueError(f"Lỗi: Phần tử A[{i}][{i}] trên đường chéo bằng 0, không thể chia.")

    for k in range(max_iter):
        # Lưu lại nghiệm cũ để tính sai số
        x_old = list(x)
        
        for i in range(n):
            sigma = 0.0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * x[j]
            
            # Cập nhật x[i]
            x[i] = (b[i] - sigma) / A[i][i]
            
        # Tính sai số ||x_new - x_old||_2
        diff = [x[i] - x_old[i] for i in range(n)]
        error = manual_norm(diff)
        
        if error < tol:
            # print(f"Gauss-Seidel: Hội tụ sau {k+1} vòng lặp.")
            return x
            
    print("Gauss-Seidel: Không hội tụ sau số lần lặp tối đa.")
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