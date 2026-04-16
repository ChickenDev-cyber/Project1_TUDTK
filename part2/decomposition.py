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

def verify_solution(A, U, Sigma, V_T):
    print("KIỂM CHỨNG KẾT QUẢ PHÂN RÃ SVD BẰNG NUMPY")

    try:
        A_np = np.array(A, dtype=float)
        U_np = np.array(U, dtype=float)
        Sigma_np = np.array(Sigma, dtype=float)
        VT_np = np.array(V_T, dtype=float)
        
        A_reconstructed = np.dot(np.dot(U_np, Sigma_np), VT_np)
        
        # Kiểm tra sai số
        if np.allclose(A_np, A_reconstructed, atol=1e-5):
            print("KẾT QUẢ: THÀNH CÔNG")
            print("Nhận xét: Thuật toán SVD tự cài đặt hoạt động chính xác. Ma trận tái tạo khớp với ma trận gốc.")
        else:
            print("KẾT QUẢ: CẢNH BÁO SAI SỐ")
            sai_so = np.max(np.abs(A_np - A_reconstructed))
            print(f"Nhận xét: Kết quả tái tạo SVD bị lệch. Độ lệch tối đa: {sai_so}")
            
    except Exception as e:
        print(f"KẾT QUẢ: LỖI QUÁ TRÌNH KIỂM CHỨNG ({e})")

if __name__ == "__main__":

    # ============NHẬP VÀO TỪ BÀN PHÍM =========
    # print("Nhập vào không gian R^(n): ", end="")
    # n = int(input())
    # print("Nhập vào số vector: ", end="")
    # n_vector = int(input())

    # A = InitMatrix(n, n_vector)
    # for i in range(n):
    #     print("Nhập vào vector thứ " + str(i + 1))
    #     for j in range(n_vector):
    #         print("Phần tử thứ " + str(j + 1) + ": ", end="")
    #         A[i][j] = float(input()) 

    # ===========NHẬP VÀO BẰNG CÁCH TỰ KHỞI TẠO==========
    # A = [
    #     [1, 1],
    #     [0, 1],
    #     [-1, 1]
    # ]


    A = [
        [3, 2, 2],
        [2, 3, -2]
    ]

    # A = [
    #     [1, 2, 3],
    #     [2, 4, 6],
    #     [-1, -2, -3]
    # ]
    
    # ========== XỬ LÝ ========
    print("\nMa trận A:")
    for i in A:
        print([round(val, 4) for val in i])

    # PHÂN RÃ
    U, Sigma, V_T = decomposite_SVD(A)

    print("\n--- PHÂN RÃ SVD (A = U * Sigma * V^T) ---")

    print("\nMa trận U:")
    for row in U:
        print([round(val, 4) for val in row])

    print("\nMa trận Sigma:")
    for row in Sigma:
        print([round(val, 4) for val in row])

    print("\nMa trận V^(T):")
    for row in V_T:
        print([round(val, 4) for val in row])

    # KIỂM CHỨNG
    verify_solution(A, U, Sigma, V_T)