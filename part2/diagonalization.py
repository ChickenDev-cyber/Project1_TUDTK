import math as mth
import numpy as np
from fractions import Fraction

def back_substitution(U, c):
    n_rows = len(U)
    n_cols = len(U[0])
    
    r = sum(1 for i in range(n_rows) if any(val != 0 for val in U[i]))
    
    for i in range(r, n_rows):
        if c[i] != 0:
            print("-> Vô nghiệm.")
            return None
            
    pivot_cols = []
    for i in range(r):
        for j in range(n_cols):
            if U[i][j] != 0:
                pivot_cols.append(j)
                break
                
    free_cols = [j for j in range(n_cols) if j not in pivot_cols]

    if r < n_cols:
        print("-> Vô số nghiệm. Nghiệm tổng quát:")
    
    x_expr = [{} for _ in range(n_cols)]
    
    for j in free_cols:
        x_expr[j] = {'const': Fraction(0), j: Fraction(1)}
        
    for i in range(r - 1, -1, -1):
        p = pivot_cols[i]
        expr = {'const': c[i]}
        
        for j in range(p + 1, n_cols):
            if U[i][j] != 0:
                for key, val in x_expr[j].items():
                    expr[key] = expr.get(key, Fraction(0)) - U[i][j] * val
                    
        for key in expr:
            expr[key] /= U[i][p]
            
        x_expr[p] = expr

    # In kết quả nghiệm
    for j in range(n_cols):
        terms = []
        const_val = x_expr[j].get('const', Fraction(0))
        has_free_var = False
        
        for k in free_cols:
            if k in x_expr[j] and x_expr[j][k] != 0:
                has_free_var = True
                coeff = x_expr[j][k]
                sign = "+" if coeff > 0 else "-"
                abs_coeff = abs(coeff)
                coeff_str = "" if abs_coeff == 1 else f"{abs_coeff}*"
                terms.append(f"{sign} {coeff_str}t{k+1}") 
        
        if not has_free_var:
            print(f"  x{j+1} = {const_val}")
        else:
            expr_str = " ".join(terms)
            if const_val != 0:
                expr_str = f"{const_val} " + expr_str
            else:
                if expr_str.startswith("+ "):
                    expr_str = expr_str[2:]
                elif expr_str.startswith("- "):
                    expr_str = "-" + expr_str[2:]
            print(f"  x{j+1} = {expr_str}")

    return None if r < n_cols else [x_expr[j]['const'] for j in range(n_cols)]

def gaussian_elimination(A, b, tol=1e-4):
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
            if abs(float(M[i][c_idx])) > abs(float(M[p][c_idx])):
                p = i

        # Xử lý sai số float
        if abs(float(M[p][c_idx])) < tol:
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
    n_rows, n_cols = len(A), len(A[0])
    M_aug, _, _ = gaussian_elimination(A, [0] * n_rows)
    U = [row[:n_cols] for row in M_aug]
    
    pivot_indices = []
    for i in range(n_rows):
        for j in range(n_cols):
            if U[i][j] != 0: 
                pivot_indices.append((i, j))
                break
                
    rank = len(pivot_indices)
    
    row_basis = [[str(val) for val in U[i]] for i, _ in pivot_indices]
    col_basis = [[str(A[i][j]) for i in range(n_rows)] for _, j in pivot_indices]
    
    null_basis = []
    if rank < n_cols:
        pivot_cols = [j for i, j in pivot_indices]
        free_cols = [j for j in range(n_cols) if j not in pivot_cols]
        
        for free_j in free_cols:
            special_solution = [Fraction(0)] * n_cols
            special_solution[free_j] = Fraction(1)

            for i, k in reversed(pivot_indices):
                sum_ax = sum(U[i][j] * special_solution[j] for j in range(k + 1, n_cols))
                special_solution[k] = -sum_ax / U[i][k]
            
            null_basis.append([str(val) for val in special_solution])
    
    return {
        "rank": rank,
        "row_basis": row_basis,
        "col_basis": col_basis,
        "null_basis": null_basis
    }

def InitMatrix(n, m):
    return [[0.0] * m for _ in range(n)]

def DotProduct(v, u):
    return sum(v[i] * u[i] for i in range(len(v)))

def LengthOfVector(v):
    return mth.sqrt(DotProduct(v, v))

def isVec0(v):
    return all(val == 0 for val in v)

# Phân rã QR (Gram-Schmidt)
def decomposite(A):
    n, m = len(A), len(A[0])
    Q1 = InitMatrix(n, m)    
    R1 = InitMatrix(m, m)

    Q, V = [], []
    
    for j in range(m):
        u_j = [A[i][j] for i in range(n)]
        v_j = [A[i][j] for i in range(n)]

        if isVec0(v_j):
            print("Lỗi: Xuất hiện vector 0 trong quá trình trực giao.")
            return [], []
        
        for i in range(j):
            v_i = V[i]
            he_so = DotProduct(u_j, v_i) / DotProduct(v_i, v_i)
            for row in range(len(v_j)):
                v_j[row] -= he_so * v_i[row]
            R1[i][j] = DotProduct(u_j, v_i) / mth.sqrt(DotProduct(v_i, v_i))
        
        V.append(v_j)
        do_dai = LengthOfVector(v_j)

        R1[j][j] = DotProduct(u_j, V[j]) / mth.sqrt(DotProduct(V[j], V[j]))

        q_temp = [v_j[row] / do_dai for row in range(len(v_j))]
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
    return [[round(float(A[i][j]) - (lam_clean if i == j else 0.0), 10) for j in range(n)] for i in range(n)]

def transpose_list(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

def MultiplyMatrix(A, B):
    n, m, p = len(A), len(B[0]), len(B)
    Res = InitMatrix(n, m)
    for i in range(n):
        for j in range(m):
            Res[i][j] = sum(A[i][k] * B[k][j] for k in range(p))
    return Res

def CheckConvergence(A, tol=1e-4):
    for i in range(len(A)):
        for j in range(i):
            if abs(A[i][j]) > tol:
                return False
    return True

def CheckDefective_QR(A, tol=1e-6):
    n = len(A)
    eigvals = [A[i][i] for i in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if abs(eigvals[i] - eigvals[j]) < tol and abs(A[i][j]) > tol: 
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
            GM = n - res_temp['rank']
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
        print("-> Trị riêng phức (Chưa hội tụ).")
        return [] 
        
    if CheckDefective_QR(A_k):
        print("-> Ma trận khuyết (Không đủ vector riêng độc lập tuyến tính).")
        return []
        
    return A_k

def SolveEigenFullFast(A):
    n = len(A)
    A_final = InitMatrix(n, n)
    P_cols = []

    # Giới hạn dùng QR thuần tuý cho ma trận nhỏ
    if n <= 5: 
        matrix_result = QR_Loop(A, 500)
        if not matrix_result:
            return [], []
        
        eigen_list = [matrix_result[i][i] for i in range(n)]
        for i in range(n):
            A_final[i][i] = eigen_list[i]
        eigenvalues = eigen_list
    else: 
        eigenvalues = np.linalg.eigvals(A)

        # Check trị riêng phức
        if any(abs(val.imag) > 1e-9 for val in eigenvalues):
            print("-> Tồn tại giá trị riêng phức.")
            return [], []

        # Check ma trận khuyết
        if CheckDefective_Eigvals(A, eigenvalues):
            print("-> Ma trận khuyết, không chéo hóa được.")
            return [], []
        
    A_final = InitMatrix(n, n)
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
        print("-> Lỗi: Không đủ vector riêng.")
        return [], []

    print("-> Có thể chéo hóa.")
    return A_final, transpose_list(P_cols)

def verify_solution(A, D, P):
    try:
        A_np, D_np, P_np = np.array(A, dtype=float), np.array(D, dtype=float), np.array(P, dtype=float)
        P_inv = np.linalg.inv(P_np)
        
        A_reconstructed = np.dot(np.dot(P_np, D_np), P_inv)
        
        if np.allclose(A_np, A_reconstructed, atol=1e-5):
            print("[OK] Ma trận tái tạo khớp với A gốc.")
        else:
            sai_so = np.max(np.abs(A_np - A_reconstructed))
            print(f"[CẢNH BÁO] Lệch dữ liệu khi tái tạo. Độ lệch max: {sai_so}")
            
    except np.linalg.LinAlgError:
        print("[LỖI] Ma trận P không khả nghịch.")
    except Exception as e:
        print(f"[LỖI] {e}")

def run_tests(test_cases):
    for idx, A in enumerate(test_cases, 1):
        print("-" * 50)
        print(f"TEST CASE {idx}")
        print("Ma trận A:")
        for row in A: 
            print([round(val, 4) for val in row])
        
        print("\n[Đang xử lý...]")
        D, P = SolveEigenFullFast(A)
        
        if D and P:
            print("\nMa trận D (Chéo):")
            for row in D:
                print([round(val, 4) for val in row])
                
            print("\nMa trận P (Vector riêng):")
            for row in P:
                print([round(v, 4) for v in row])
                
            print("\n[Kiểm chứng P * D * P^-1 = A]")
            verify_solution(A, D, P)
        else:
            print("-> Dừng kiểm chứng.")
            
        print("-" * 50 + "\n")

if __name__ == "__main__":
    test_cases = [
        # Ma trận 3x3 bình thường
        [[1, 3, 3], [-3, -5, -3], [3, 3, 1]],
        
        # Ma trận khuyết 3x3
        [[3, 1, 0], [0, 3, 0], [0, 0, 5]],
        
        # Ma trận 2x2 chứa trị riêng phức
        [[3, -2], [4, -1]],
        
        # Ma trận 6x6 tridiagonal 1
        [
            [4, 1, 0, 0, 0, 0],
            [1, 4, 1, 0, 0, 0],
            [0, 1, 4, 1, 0, 0],
            [0, 0, 1, 4, 1, 0],
            [0, 0, 0, 1, 4, 1],
            [0, 0, 0, 0, 1, 4]
        ],
        
        # Ma trận 6x6 tridiagonal 2
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