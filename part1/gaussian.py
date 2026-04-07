from fractions import Fraction
import numpy as np

def back_substitution(U, c, r): # Thêm tham số r (rank) 
    n_rows = len(U)
    n_cols = len(U[0])
    
    # --- SỬA: Kiểm tra Vô nghiệm trước ---
    for i in range(r, n_rows):
        if c[i] != 0:
            print("He phuong trinh Vo nghiem.")
            return None
            
    # --- SỬA: Sau khi chac chan co nghiem, moi kiem tra Vo so nghiem ---
    if r < n_cols:
        print("He phuong trinh co Vo so nghiem.")
        return None
    
    x = [Fraction(0)] * n_cols
    
    for i in range(r - 1, -1, -1):
        pivot_col = -1
        for j in range(n_cols):
            if U[i][j] != 0:
                pivot_col = j
                break
        
        if pivot_col != -1:
            sum_ax = sum(U[i][j] * x[j] for j in range(pivot_col + 1, n_cols))
            x[pivot_col] = (c[i] - sum_ax) / U[i][pivot_col]
    
    return x
    

def gaussian_elimination(A, b):
    n = len(A)
    m = len(A[0])

    M = [[Fraction(val) for val in row] + [Fraction(b[i])] for i, row in enumerate(A)]
    s = 0
    r = 0 

    for c_idx in range(m):
        if r >= n:
            break

        p = r
        for i in range(r + 1, n):
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

    # --- SỬA: Đưa tham số r vào hàm thế ngược để in thông báo ---
    x = back_substitution(U, c_result, r)
    
    return M, x, s

def verify_solution(A, x, b):
    if x is None: 
        print("Khong the kiem chung nghiem cua he.")
        return
    
    try:
        A_np = np.array(A, dtype=float)
        b_np = np.array(b, dtype=float)
        x_float = [float(Fraction(val)) for val in x]
        x_np = np.array(x_float, dtype=float)
        
        ax_res = np.dot(A_np, x_np)
        check = np.allclose(ax_res, b_np, atol=1e-9)
        
        if check:
            print("Nghiem da duoc kiem chung thanh cong. Chinh xac.")
        else:
            print("Nghiem khong chinh xac.")
            
    except Exception as e:
        print(f"Da xay ra loi khi kiem chung nghiem: {e}")

#Kiem thu
if __name__ == "__main__":
    
    print("NGHIEM DUY NHAT")
    A1 = [[2, 1, -1], 
          [-3, -1, 2], 
          [-2, 1, 2]]
    b1 = [8, -11, -3]
    M1, x1, s1 = gaussian_elimination(A1, b1)
    if x1:
        formatted_x = ", ".join([str(v) for v in x1])
        print(f"Nghiem x: {formatted_x}")
    verify_solution(A1, x1, b1)

    print("\nVO NGHIEM")
    A2 = [[1, 1], 
          [1, 1]]
    b2 = [2, 3]
    gaussian_elimination(A2, b2)

    print("\nVO SO NGHIEM")
    A3 = [[1, 2], 
          [2, 4]]
    b3 = [3, 6]
    gaussian_elimination(A3, b3)

    print("\n NGHIEM PHAN SO ")
    # Ma trận A và vector b của hệ trên
    A4 = [
        [2, 4, 2],
        [4, 2, 2],
        [2, 2, 4]
    ]
    b4 = [2, 4, 6]
    M4, x4, s4 = gaussian_elimination(A4, b4)

    if x4:
        formatted_x = ", ".join([str(v) for v in x4])
        print(f"Nghiem x: {formatted_x}")

        verify_solution(A4, x4, b4)
