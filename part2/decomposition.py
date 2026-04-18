import math as mth
import numpy as np

# TÍNH TÍCH VÔ HƯỚNG 
def DotProduct(v, u):
    res = 0.0
    for i in range(len(v)):
        res += v[i] * u[i]
    return res

# TÍNH LENGTH VETCOR
def LengthOfVector(v):
    return mth.sqrt(DotProduct(v, v))

# KHỞI TẠO
def InitMatrix(n, m):
    Res = []
    for i in range(n):
        row_zeros = []
        for j in range(m):
            row_zeros.append(0.0)
        Res.append(row_zeros)
    return Res

# HÀM A^(T)
def TransposeMatrix(A):
    n = len(A)
    m = len(A[0])
    Res = InitMatrix(m, n)
    for i in range(n):
        for j in range(m):
            Res[j][i] = A[i][j]
    return Res

# HHAM NHÂN MA TRẬN
def MultiplyMatrix(A, B):
    n = len(A)
    m = len(A[0])
    p = len(B[0])
    Res = InitMatrix(n, p)
    for i in range(n):
        for j in range(p):
            for k in range(m):
                Res[i][j] += A[i][k] * B[k][j]
    return Res

# JACOBI: Tìm Trị riêng và Vector riêng cho ma trận đối xứng
def JacobiEigen(M, num0=1e-9, max_iter=100):
    n = len(M)
    V = InitMatrix(n, n)
    # Khởi tạo V là ma trận đơn vị
    for i in range(n):
        V[i][i] = 1.0

    for iteration in range(max_iter):
        max_val = 0.0
        p, q = 0, 0
        # Tìm phần tử ngoài đường chéo có trị tuyệt đối lớn nhất
        for i in range(n):
            for j in range(i + 1, n):
                if abs(M[i][j]) > max_val:
                    max_val = abs(M[i][j])
                    p = i
                    q = j

        # Nếu các phần tử ngoài đường chéo đã xấp xỉ 0 thì dừng
        if max_val < num0:
            break

        # Tính góc xoay theta
        if M[p][p] == M[q][q]:
            theta = mth.pi / 4.0
        else:
            theta = 0.5 * mth.atan(2.0 * M[p][q] / (M[p][p] - M[q][q]))

        cos_t = mth.cos(theta)
        sin_t = mth.sin(theta)

        # Cập nhật ma trận M (chỉ tính lại các hàng/cột bị ảnh hưởng)
        M_pp = cos_t**2 * M[p][p] - 2*sin_t*cos_t*M[p][q] + sin_t**2 * M[q][q]
        M_qq = sin_t**2 * M[p][p] + 2*sin_t*cos_t*M[p][q] + cos_t**2 * M[q][q]
        M[p][q] = M[q][p] = 0.0
        M[p][p] = M_pp
        M[q][q] = M_qq

        for i in range(n):
            if i != p and i != q:
                M_ip = cos_t * M[i][p] - sin_t * M[i][q]
                M_iq = sin_t * M[i][p] + cos_t * M[i][q]
                M[i][p] = M[p][i] = M_ip
                M[i][q] = M[q][i] = M_iq

        # Cập nhật ma trận Vector riêng V
        for i in range(n):
            V_ip = cos_t * V[i][p] - sin_t * V[i][q]
            V_iq = sin_t * V[i][p] + cos_t * V[i][q]
            V[i][p] = V_ip
            V[i][q] = V_iq

    eigenvalues = []
    for i in range(n):
        eigenvalues.append(M[i][i])
        
    return eigenvalues, V

# PHÂN RÃ SVD 
def decomposite_SVD(A):
    n = len(A)      # số hàng
    m = len(A[0])   # số cột

    # Bước 1: Tính M = A^T * A
    A_T = TransposeMatrix(A)
    M = MultiplyMatrix(A_T, A)

    # Bước 2: Tìm Trị riêng và Vector riêng của M (chính là ma trận V)
    eigenvalues, V = JacobiEigen(M)

    # Bước 3: Sắp xếp Trị riêng giảm dần, và đổi chỗ các cột của V tương ứng
    for i in range(len(eigenvalues)):
        for j in range(i + 1, len(eigenvalues)):
            if eigenvalues[i] < eigenvalues[j]:
                eigenvalues[i], eigenvalues[j] = eigenvalues[j], eigenvalues[i]
                # Swap Cột của V
                for row in range(len(V)):
                    V[row][i], V[row][j] = V[row][j], V[row][i]

    # Bước 4: Tạo ma trận Sigma và U
    Sigma = InitMatrix(m, m)
    U = InitMatrix(n, m)

    for j in range(m):
        if eigenvalues[j] < 0:
            eigenvalues[j] = 0.0
            
        sigma_val = mth.sqrt(eigenvalues[j])
        Sigma[j][j] = sigma_val

        # Nếu sigma > 0, tính cột j của U = (A * v_j) / sigma
        if sigma_val > 1e-9:
            # Lấy cột j của V
            v_j = [V[row][j] for row in range(m)]
            
            # Nhân ma trận A với vector v_j
            Av = []
            for row in range(n):
                Av.append(DotProduct(A[row], v_j))
                
            # Chia cho sigma_val và nhét vào cột j của U
            for row in range(n):
                U[row][j] = Av[row] / sigma_val

    # Tính V^T (Transpose của V)
    V_T = TransposeMatrix(V)

    return U, Sigma, V_T

def run_test(name, A):
    import numpy as np
    
    print(f"\n=== {name} ===")
    print("Ma tran A:")
    for row in A: 
        print(row)
        
    # Thuc hien phan ra SVD
    U, Sigma, V_T = decomposite_SVD(A)
    
    print("Ma tran U:")
    for row in U: 
        print([round(val, 4) for val in row])
        
    print("Ma tran Sigma:")
    for row in Sigma: 
        print([round(val, 4) for val in row])
        
    print("Ma tran V^T:")
    for row in V_T: 
        print([round(val, 4) for val in row])

    # Kiem chung voi Numpy
    print("--- Kiem chung Numpy ---")
    try:
        A_np = np.array(A, dtype=float)
        U_np = np.array(U, dtype=float)
        Sigma_np = np.array(Sigma, dtype=float)
        VT_np = np.array(V_T, dtype=float)

        # Tinh U * Sigma * V^T
        A_reconstructed = np.dot(np.dot(U_np, Sigma_np), VT_np)

        if np.allclose(A_np, A_reconstructed, atol=1e-5):
            print("SVD: Thanh cong (A = U * Sigma * V^T)")
        else:
            print("SVD: That bai (Ket qua tai tao bi lech)")
            print(f"Do lech toi da: {np.max(np.abs(A_np - A_reconstructed))}")
    except Exception as e:
        print(f"SVD: That bai (Loi kiem chung: {e})")

if __name__ == "__main__":
    # Case 1: Ma tran 2x2 co ban
    run_test("CASE 1: MA TRAN 2x2", [[4, 7], [2, 6]])

    # Case 2: Ma tran 3x2 (So hang > So cot)
    run_test("CASE 2: MA TRAN 3x2", [
        [1, 1], 
        [0, 1], 
        [-1, 1]
    ])

    # Case 3: Ma tran 2x3 (So hang < So cot)
    run_test("CASE 3: MA TRAN 2x3", [
        [3, 2, 2], 
        [2, 3, -2]
    ])

    # Case 4: Ma tran suy bien (Cac hang ti le voi nhau)
    run_test("CASE 4: MA TRAN SUY BIEN", [
        [1, 2, 3], 
        [2, 4, 6], 
        [-1, -2, -3]
    ])

    # Case 5: Ma tran 1x1
    run_test("CASE 5: MA TRAN 1x1", [[5]])