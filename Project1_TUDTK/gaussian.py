from fractions import Fraction
import numpy as np

def back_substitution(U, c):
    n_rows = len(U)
    n_cols = len(U[0])
    
    pivot_indices = []
    for i in range(n_rows):
        for j in range(n_cols):
            if U[i][j] != 0:
                pivot_indices.append((i, j))
                break
    
    if len(pivot_indices) < n_cols:
        return ("He phuong trinh da cho co vo so nghiem")
    
    x = [Fraction(0)] * n_cols
    for i, k in reversed(pivot_indices):
        sum_ax = sum(U[i][j] * x[j] for j in range(k + 1, n_cols))
        x[k] = (c[i] - sum_ax) / U[i][k]
    
    return [str(val) for val in x]
    

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
            print(f"Khong co pivot tai cot {c_idx}.")
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

    for i in range(r, n):
        if c_result[i] != 0:
            return M, "He phuong trinh vo nghiem", s

    x = back_substitution(U, c_result)
    
    return M, x, s

def verify_solution(A, x, b):
    if x is None or isinstance(x, str):
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
        
