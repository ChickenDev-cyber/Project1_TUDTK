import math as mth
import numpy as np
from fractions import Fraction

#--- Sử dụng từ Part1 để tìm ma trận P ---
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

def gaussian_elimination(A, b, tol=1e-7):
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
            # Cần ép về float để dùng hàm abs() cho an toàn
            if abs(float(M[i][c_idx])) > abs(float(M[p][c_idx])):
                p = i

        # --- SỬA TẠI ĐÂY: Thêm bộ lọc sai số ---
        # Nếu Pivot tìm được nhỏ hơn sai số, coi như cột này toàn số 0
        if abs(float(M[p][c_idx])) < tol:
            for i in range(r, n):
                M[i][c_idx] = Fraction(0) # Ép về 0 tuyệt đối để tránh dội sai số
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

def rank_and_basis(A):
    n_rows = len(A)
    n_cols = len(A[0])
    
    # Khử Gauss để tìm ma trận bậc thang M
    M_aug, _, _ = gaussian_elimination(A, [0] * n_rows)
    
    # Tách ma trận hệ số U từ ma trận bổ sung M_aug
    U = [row[:n_cols] for row in M_aug]
    
    pivot_indices = []
    for i in range(n_rows):
        for j in range(n_cols):
            if U[i][j] != 0: 
                pivot_indices.append((i, j))
                break
            
    rank = len(pivot_indices)
    
    # 1. Row Basis: Các dòng chứa pivot của ma trận bậc thang U
    row_basis = []
    for i, j in pivot_indices:
        row_basis.append([str(val) for val in U[i]])
        
    # 2. Column Basis: PHẢI lấy cột tương ứng ở ma trận GỐC A
    col_basis = []
    for _, j in pivot_indices:
        # Lấy cột j của ma trận A ban đầu
        column_from_A = [str(A[i][j]) for i in range(n_rows)]
        col_basis.append(column_from_A)
    
    # 3. Null Basis (Cơ sở không gian nghiệm Ax = 0)
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
    Res = []
    for i in range(n):
        row_zeros = [0.0] * m
        Res.append(row_zeros)
    return Res

#---Dùng QR cho trường hợp n <= 5----
def DotProduct(v, u):
    res = 0.0
    for i in range(len(v)):
        res += v[i] * u[i]
    return res

# Tính độ dài 1 vecto
def LengthOfVector(v):
    return mth.sqrt(DotProduct(v, v))

# Hàm liệu có là vector 0
def isVec0(v):
    for i in range(len(v)):
        if v[i] != 0:
            return False
    return True

# Phân rã QR bằng Gram-Schmidt
def decomposite(A):
    n = len(A)  # hàng
    m = len(A[0]) # cột
    Q1 = InitMatrix(n, m)    
    R1 = InitMatrix(m, m)

    Q = [] # Các vector  q = trưc chuẩn
    V = [] # Các vector  v = trực giao
    for j in range(m):
        u_j = [] # Lấy vector  cột j của ma trận A
        v_j = [] # Tìm vector v thứ j (Hay còn gọi là trực giao)
        for i in range(n):
            u_j.append(A[i][j])
            v_j.append(A[i][j])

        #Không được tồn tại vector 0
        if (isVec0(v_j) == True):
            print("Vector v hiện tại là vector 0")
            return [],[]
        
        # Tìm trực giao
        for i in range(j):
            v_i = V[i]
            HeSo = DotProduct(u_j, v_i) / DotProduct(v_i, v_i)
            for row in range(len(v_j)):
                v_j[row] -= HeSo * v_i[row]
            #Tính R1 trực tiếp
            R1[i][j] = DotProduct(u_j, v_i) / mth.sqrt(DotProduct(v_i, v_i))
        
        # Chuẩn Hóa 
        V.append(v_j)
        q_temp = []
        DoDai = LengthOfVector(v_j)

        # Đường chéo chính của R chính là độ dài của V[j]
        R1[j][j] = DotProduct(u_j, V[j]) / mth.sqrt(DotProduct(V[j], V[j]))

        # Gán vào list các Q (Trực Chuẩn)
        for row in range(len(v_j)):
            q_temp.append(v_j[row] / DoDai)
        Q.append(q_temp)
    
    # Tính Q1
    for j in range(m):
        for i in range(n):
            Q1[i][j] = Q[j][i]

    return Q1, R1

# Tạo ma trận đơn vị I
def get_identity(n):
    return [[1.0 if i == j else 0.0 for j in range(n)] for i in range(n)]

# Ma trận A - lamda*I
def subtract_lambda_I(A, lam):
    n = len(A)
    # Làm tròn trị riêng lam đến 10 chữ số để triệt tiêu sai số float
    lam_clean = round(float(lam), 10) 
    
    Res = []
    for i in range(n):
        row = []
        for j in range(n):
            # Làm tròn kết quả phép trừ trước khi đưa vào hệ thống Fraction
            val = float(A[i][j]) - (lam_clean if i == j else 0.0)
            row.append(round(val, 10)) 
        Res.append(row)
    return Res

# Chuyển vị ma trận P_cols (thay cho .T)
def transpose_list(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

# --- BỔ SUNG CHÉO HÓA ---
def MultiplyMatrix(A, B): #Nhân 2 Ma Trận
    n = len(A)
    m = len(B[0])
    p = len(B)
    Res = InitMatrix(n, m)
    for i in range(n):
        for j in range(m):
            for k in range(p):
                Res[i][j] += A[i][k] * B[k][j]
    return Res

def CheckConvergence(A, sai_so=1e-4):
    n = len(A)
    for i in range(n):
        for j in range(i): # Chỉ xét các phần tử dưới đường chéo (j < i)
            if abs(A[i][j]) > sai_so:
                return False
    return True

def CheckDefective_QR(A, sai_so=1e-6):
    n = len(A)
    gia_tri_rieng = [A[i][i] for i in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            if abs(gia_tri_rieng[i] - gia_tri_rieng[j]) < sai_so: 
                if abs(A[i][j]) > sai_so: 
                    return True
    return False

def CheckDefective_Eigvals(A, eigenvalues, sai_so=1e-6):
    n = len(A)
    # Làm tròn trị riêng để gom nhóm chính xác
    rounded_eigs = [round(float(val.real), 8) for val in eigenvalues]
    unique_vals = sorted(list(set(rounded_eigs)))
    
    for lamda in unique_vals:
        AM = rounded_eigs.count(lamda) # Số bội đại số
        
        if AM > 1:
            # subtract_lambda_I đã được xử lý làm tròn ở vòng trước
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
            print("Tồn tại vector 0")
            return [] 
        A_k = MultiplyMatrix(R, Q)
        
    if not CheckConvergence(A_k):
        print("Thất bại: Ma trận có giá trị riêng là số phức")
        return [] 
        
    if CheckDefective_QR(A_k):
        print("Thất bại: Tồn tại nghiệm kép, có thể nói là ko đủ không gian")
        return []
        
    print("Ma trận chéo hóa hợp lệ trên tập số thực.")
    return A_k


def SolveEigenFullFast(A):
    n = len(A)
    A_final = InitMatrix(n, n)
    P_cols = []

    if (n <= 5): #Dùng QR_Loop
        matrix_result = QR_Loop(A, 500)
        if not matrix_result:
            return [], []
        
        # Lấy các trị riêng từ đường chéo chính của ma trận kết quả
        eigen_list = [matrix_result[i][i] for i in range(n)]
        
        for i in range(n):
            A_final[i][i] = eigen_list[i]
        
        eigenvalues = eigen_list
    else: 
        # Dùng hàm kiểm tra theo điều kiện của hàm
        eigenvalues = np.linalg.eigvals(A)

        # Thay đoạn kiểm tra số phức:
        for i in range(n):
            # Dùng thuộc tính .imag của Python thay cho np.iscomplex
            if abs(eigenvalues[i].imag) > 1e-9: 
                print("Thất bại: Tồn tại giá trị riêng phức...")
                return [], []
            A_final[i][i] = float(eigenvalues[i].real)
            
            # Lấy phần thực và điền vào đường chéo
            A_final[i][i] = float(eigenvalues[i].real)

        # ĐIỀU KIỆN: Kiểm tra (nghiệm kép, defective)
        if CheckDefective_Eigvals(A, eigenvalues):
            print("Thất bại: Ma trận nghiệm kép, không đủ không gian vector riêng.")
            return [], []
        
    # Tìm P
    unique_vals = sorted(list(set(round(val.real, 8) for val in eigenvalues)))
    for lam in unique_vals:
        # Thay thế phép trừ NumPy bằng hàm tự viết
        A_minus_lamI = subtract_lambda_I(A, lam)
        res = rank_and_basis(A_minus_lamI)
        for vec in res['null_basis']:
            P_cols.append([float(Fraction(v)) for v in vec])

    if len(P_cols) < n:
        print("Thất bại: Không đủ vector riêng.")
        return [], []

    # Thay .T.tolist() bằng hàm transpose_manual
    P_matrix = transpose_list(P_cols)

    print("Ma trận có thể chéo hóa.")
    return A_final, P_matrix

if __name__ == "__main__":
    A = [
        [1, 3, 3],
        [-3, -5, -3],
        [3, 3, 1]
    ]

    # A = [[3, 1, 0], 
    #      [0, 3, 0], 
    #      [0, 0, 5]]

    # A = [
    #     [3, -2],
    #     [4, -1]
    # ]

    # A = [
    #     [0, -2, 0, 0, 0, 0],
    #     [2,  0, 0, 0, 0, 0],
    #     [0,  0, 1, -3, 0, 0],
    #     [0,  0, 3,  1, 0, 0],
    #     [0,  0, 0,  0, 5, -4],
    #     [0,  0, 0,  0, 4,  5]
    # ]

    # A = [
    #     [4, 1, 0, 0, 0, 0],
    #     [1, 4, 1, 0, 0, 0],
    #     [0, 1, 4, 1, 0, 0],
    #     [0, 0, 1, 4, 1, 0],
    #     [0, 0, 0, 1, 4, 1],
    #     [0, 0, 0, 0, 1, 4]
    # ]

    # A = [
    #     [2, 1, 0, 0, 0, 0],
    #     [1, 2, 1, 0, 0, 0],
    #     [0, 1, 2, 1, 0, 0],
    #     [0, 0, 1, 2, 1, 0],
    #     [0, 0, 0, 1, 2, 1],
    #     [0, 0, 0, 0, 1, 2]
    # ]

    print("Ma trận ban đầu:")
    for row in A: print([round(val, 4) for val in row])
    
    # Gọi hàm để lấy cả D và P
    D, P = SolveEigenFullFast(A)
    
    if D and P:
        print("\nMa Trận chéo hóa (D):")
        for row in D:
            print([round(val, 4) for val in row])
            
        print("\nMa Trận vector riêng (P):")
        for row in P:
            # Chỉ cần dòng này để in từng hàng của P
            print([round(v, 4) for v in row])