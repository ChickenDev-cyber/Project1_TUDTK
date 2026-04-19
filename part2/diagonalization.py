import math as mth
import numpy as np
from fractions import Fraction


def back_substitution(U, c):
    n_rows = len(U)
    n_cols = len(U[0])
    
    r = 0
    for i in range(n_rows):
        if any(abs(float(val)) > 1e-5 for val in U[i]):
            r += 1
            
    for i in range(r, n_rows):
        if abs(float(c[i])) > 1e-5:
            return None
            
    pivot_cols = []
    for i in range(r):
        for j in range(n_cols):
            if abs(float(U[i][j])) > 1e-5:
                pivot_cols.append(j)
                break
                
    free_cols = [j for j in range(n_cols) if j not in pivot_cols]

    x_expr = [{} for _ in range(n_cols)]
    
    for j in free_cols:
        x_expr[j] = {'const': Fraction(0), j: Fraction(1)}
        
    for i in range(r - 1, -1, -1):
        p = pivot_cols[i]
        expr = {'const': c[i]}
        
        for j in range(p + 1, n_cols):
            if abs(float(U[i][j])) > 1e-5:
                for key, val in x_expr[j].items():
                    expr[key] = expr.get(key, Fraction(0)) - U[i][j] * val
                    
        for key in expr:
            expr[key] = (expr[key] / U[i][p]).limit_denominator(10**8)
            
        x_expr[p] = expr

    if r < n_cols:
        return x_expr 
    else:
        return [x_expr[j]['const'] for j in range(n_cols)]

def gaussian_eliminate(A, b):
    n = len(A)
    m = len(A[0])

    M = [[Fraction(val).limit_denominator(10**8) for val in row] + [Fraction(b[i]).limit_denominator(10**8)] for i, row in enumerate(A)]
    s = 0
    r = 0 

    for c_idx in range(m):
        if r >= n:
            break

        p = r
        for i in range(r + 1, n):
            if abs(M[i][c_idx]) > abs(M[p][c_idx]):
                p = i

        if abs(float(M[p][c_idx])) < 1e-5:
            for i in range(r, n):
                M[i][c_idx] = Fraction(0)
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

    x = back_substitution(U, c_result)
    
    return M, x, s

def rank_and_basis(A):
    n_rows = len(A)
    n_cols = len(A[0])
    
    M_aug, _, _ = gaussian_eliminate(A, [0] * n_rows)
    
    U = [row[:n_cols] for row in M_aug]
    
    pivot_indices = []
    for i in range(n_rows):
        for j in range(n_cols):
            if abs(float(U[i][j])) > 1e-5: 
                pivot_indices.append((i, j))
                break
                
    rank = len(pivot_indices)
    
    row_basis = [[str(val) for val in U[i]] for i, _ in pivot_indices]
    
    col_basis = []
    for _, j in pivot_indices:
        column_from_A = [str(A[i][j]) for i in range(n_rows)]
        col_basis.append(column_from_A)
    
    null_basis = []
    if rank < n_cols:
        pivot_cols = [j for i, j in pivot_indices]
        free_cols = [j for j in range(n_cols) if j not in pivot_cols]
        
        for free_j in free_cols:
            special_solution = [Fraction(0)] * n_cols
            special_solution[free_j] = Fraction(1)

            for i, k in reversed(pivot_indices):
                sum_ax = sum(U[i][j] * special_solution[j] for j in range(k + 1, n_cols))
                val = -sum_ax / U[i][k]
                special_solution[k] = val.limit_denominator(10**8)
            
            null_basis.append([str(val.limit_denominator(10**8)) for val in special_solution])
    
    return {
        "rank": rank,
        "row_basis": row_basis,
        "col_basis": col_basis,
        "null_basis": null_basis
    }

def InitMatrix(n, m):
    Res = []
    for i in range(n):
        row_zeros = [0.0] * m
        Res.append(row_zeros)
    return Res

def DotProduct(v, u):
    res = 0.0
    for i in range(len(v)):
        res += float(v[i]) * float(u[i])
    return res

def LengthOfVector(v):
    return mth.sqrt(DotProduct(v, v))

def isVec0(v):
    for i in range(len(v)):
        if abs(float(v[i])) > 1e-5:
            return False
    return True

def decomposite(A):
    n = len(A)
    m = len(A[0])
    Q1 = InitMatrix(n, m)    
    R1 = InitMatrix(m, m)

    Q = [] 
    V = [] 
    for j in range(m):
        u_j = [] 
        v_j = [] 
        for i in range(n):
            u_j.append(float(A[i][j]))
            v_j.append(float(A[i][j]))

        if isVec0(v_j) == True:
            return [], []
        
        for i in range(j):
            v_i = V[i]
            HeSo = DotProduct(u_j, v_i) / DotProduct(v_i, v_i)
            for row in range(len(v_j)):
                v_j[row] -= HeSo * v_i[row]
            R1[i][j] = DotProduct(u_j, v_i) / mth.sqrt(DotProduct(v_i, v_i))
        
        V.append(v_j)
        q_temp = []
        DoDai = LengthOfVector(v_j)
        
        if DoDai < 1e-5:
            return [], []

        R1[j][j] = DotProduct(u_j, V[j]) / mth.sqrt(DotProduct(V[j], V[j]))

        for row in range(len(v_j)):
            q_temp.append(v_j[row] / DoDai)
        Q.append(q_temp)
    
    for j in range(m):
        for i in range(n):
            Q1[i][j] = Q[j][i]

    return Q1, R1

def get_identity(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

def subtract_lambda_I(A, lam):
    n = len(A)
    lam_clean = round(float(lam), 10) 
    
    Res = []
    for i in range(n):
        row = []
        for j in range(n):
            val = float(A[i][j]) - (lam_clean if i == j else 0.0)
            row.append(round(val, 10)) 
        Res.append(row)
    return Res

def transpose_list(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def MultiplyMatrix(A, B):
    n = len(A)
    m = len(B[0])
    p = len(B)
    Res = InitMatrix(n, m)
    for i in range(n):
        for j in range(m):
            for k in range(p):
                Res[i][j] += float(A[i][k]) * float(B[k][j])
    return Res

def CheckConvergence(A, tol=1e-5):
    n = len(A)
    for i in range(n):
        for j in range(i):
            if abs(float(A[i][j])) > tol:
                return False
    return True

def CheckDefective_QR(A, tol=1e-6):
    n = len(A)
    gia_tri_rieng = [float(A[i][i]) for i in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if abs(gia_tri_rieng[i] - gia_tri_rieng[j]) < tol: 
                if abs(float(A[i][j])) > tol: 
                    return True
    return False

def CheckDefective_Eigvals(A, eigenvalues, tol=1e-6):
    n = len(A)
    rounded_eigs = [round(float(val.real), 8) for val in eigenvalues]
    unique_vals = sorted(list(set(rounded_eigs)))
    
    for lamda in unique_vals:
        AM = rounded_eigs.count(lamda)
        
        if AM > 1:
            A_minus_lamdaI = subtract_lambda_I(A, lamda)
            res_temp = rank_and_basis(A_minus_lamdaI)
            rank = res_temp['rank']
            GM = n - rank 
            
            if GM < AM:
                return True
    return False

def QR_Loop(A, iterations=100):
    A_k = A
    for step in range(iterations):
        Q, R = decomposite(A_k)
        if not Q or not R:
            return [] 
        A_k = MultiplyMatrix(R, Q)
        
    if not CheckConvergence(A_k):
        return [] 
        
    if CheckDefective_QR(A_k):
        return []
        
    return A_k

def SolveEigenFullFast(A):
    n = len(A)
    A_final = InitMatrix(n, n)
    P_cols = []

    if (n <= 5):
        matrix_result = QR_Loop(A, 500)
        if not matrix_result:
            return [], []
        
        eigen_list = [matrix_result[i][i] for i in range(n)]
        
        for i in range(n):
            A_final[i][i] = eigen_list[i]
        
        eigenvalues = eigen_list
    else: 
        eigenvalues = np.linalg.eigvals(A)

        for i in range(n):
            if abs(eigenvalues[i].imag) > 1e-9: 
                return [], []

        if CheckDefective_Eigvals(A, eigenvalues):
            return [], []
        
    A_final = InitMatrix(n, n)
    P_cols = []
    col_idx = 0 
    
    unique_vals = sorted(list(set(round(val.real, 6) for val in eigenvalues)), reverse=True)
    
    for lam in unique_vals:
        A_minus_lamI = subtract_lambda_I(A, lam)
        res = rank_and_basis(A_minus_lamI)
        
        for vec in res['null_basis']:
            P_cols.append([float(Fraction(v)) for v in vec])
            A_final[col_idx][col_idx] = float(lam)
            col_idx += 1

    if len(P_cols) < n:
        return [], []

    P_matrix = transpose_list(P_cols)

    return A_final, P_matrix

def verify_solution(A, D, P):
    try:
        A_np = np.array(A, dtype=float)
        D_np = np.array(D, dtype=float)
        P_np = np.array(P, dtype=float)
        
        P_inv = np.linalg.inv(P_np)
        A_reconstructed = np.dot(np.dot(P_np, D_np), P_inv)
        
        if np.allclose(A_np, A_reconstructed, atol=1e-5):
            print("KẾT QUẢ: THÀNH CÔNG")
            print("Nhận xét: Kết quả thuật toán tự cài đặt chính xác. Ma trận tái tạo khớp với ma trận gốc.")
        else:
            print("KẾT QUẢ: CẢNH BÁO SAI SỐ")
            sai_so = np.max(np.abs(A_np - A_reconstructed))
            print(f"Nhận xét: Kết quả tái tạo bị lệch so với ma trận gốc. Độ lệch tối đa: {sai_so}")
            
    except np.linalg.LinAlgError:
        print("KẾT QUẢ: LỖI TOÁN HỌC")
        print("Chi tiết: Ma trận P không khả nghịch, không thể thực hiện kiểm chứng.")
    except Exception as e:
        print(f"KẾT QUẢ: LỖI HỆ THỐNG ({e})")

def run_tests(test_cases):
    for idx, A in enumerate(test_cases, 1):
        print("=" * 60)
        print(f"TEST CASE {idx}:")
        print("Ma trận ban đầu (A):")
        for row in A: 
            print([round(val, 4) for val in row])
        
        print("\n")
        D, P = SolveEigenFullFast(A)
        
        if D and P:
            print("Ma Trận chéo hóa (D):")
            for row in D:
                print([round(val, 4) for val in row])
                
            print("\nMa Trận vector riêng (P):")
            for row in P:
                print([round(v, 4) for v in row])
                
            print("\n[Đang kiểm chứng...]")
            verify_solution(A, D, P)
        else:
            print("=> Không thể kiểm chứng vì quá trình chéo hóa thất bại (Không đủ điều kiện).")
            
        print("=" * 60 + "\n")

if __name__ == "__main__":
    test_cases = [
        [
            [1, 3, 3],
            [-3, -5, -3],
            [3, 3, 1]
        ],
        [
            [3, 1, 0], 
            [0, 3, 0], 
            [0, 0, 5]
        ],
        [
            [3, -2],
            [4, -1]
        ],
        [
            [4, 1, 0, 0, 0, 0],
            [1, 4, 1, 0, 0, 0],
            [0, 1, 4, 1, 0, 0],
            [0, 0, 1, 4, 1, 0],
            [0, 0, 0, 1, 4, 1],
            [0, 0, 0, 0, 1, 4]
        ],
        [
            [2, 1, 0, 0, 0, 0],
            [1, 2, 1, 0, 0, 0],
            [0, 1, 2, 1, 0, 0],
            [0, 0, 1, 2, 1, 0],
            [0, 0, 0, 1, 2, 1],
            [0, 0, 0, 0, 1, 2]
        ]
    ]

    run_tests(test_cases)