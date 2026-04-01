import math as mth
import numpy as np

# HÀM GIÚP PHÂN HÓA
# Tích vô hướng 2 vecto
def DotProduct(v, u):
    res = 0.0
    for i in range(len(v)):
        res += v[i] * u[i]
    return res

# Tính độ dài 1 vecto
def LengthOfVector(v):
    return mth.sqrt(DotProduct(v, v))

# Hàm khởi tạo
def InitMatrix(A, n, m):
    Res = []
    for i in range(n):
        row_zeros = []
        for j in range(m):
            row_zeros.append(0.0)
        Res.append(row_zeros)
    return Res

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
    Q1 = InitMatrix([], n, m)    
    R1 = InitMatrix([], m, m)

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

# --- BỔ SUNG CHÉO HÓA ---
def MultiplyMatrix(A, B): #Nhân 2 Ma Trận
    n = len(A)
    m = len(B[0])
    p = len(B)
    Res = InitMatrix([], n, m)
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

def CheckDefective(A, sai_so=1e-6):
    n = len(A)
    # Lấy các giá trị trên đường chéo
    gia_tri_rieng = [A[i][i] for i in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            # Nếu 2 giá trị riêng bằng nhau (nghiệm kép)
            if abs(gia_tri_rieng[i] - gia_tri_rieng[j]) < sai_so: #
                # Kiểm tra phần tử nằm phía trên có khác 0 không
                if abs(A[i][j]) > sai_so: #Tồn tại lamda xuất hiện n lần (n>2) và sai số khác 0 thì không chéo hóa được.
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
        
    if CheckDefective(A_k):
        print("Thất bại: Tồn tại nghiệm kép, có thể nói là ko đủ không gian")
        return []
        
    print("Ma trận chéo hóa hợp lệ trên tập số thực.")
    return A_k

if __name__ == "__main__":
    #====================NHẬP VÀO MA TRẬN A========
    # Trường hợp chéo hóa được
    A = [
        [1, 3, 3],
        [-3, -5, -3],
        [3, 3, 1]
    ]

    #Trường hợp tồn tại nghiệm kép
    # A = [
    #     [1.0, 1.0],
    #     [0.0, 1.0]
    # ]

    #Trường hợp tồn tại nghiệm phức
    # A = [
    #     [0.0, -1.0],
    #     [1.0, 0.0]
    # ]

    #In ra ma trận ban đầu
    print("Ma trận ban đầu:")
    for row in A:
        print([round(val, 4) for val in row])
    
    A_final = QR_Loop(A, iterations = 100)
    
    # print("\nMa trận P^(-1).A.P lặp 50 lần (gần thành ma trận tam giác):")
    # for row in A_final:
    #     print([round(val, 4) for val in row])

    #Lấy ra các nghiệm riêng
    for i in range(len(A_final)):
        for j in range(len(A_final)):
            if (i != j):
                A_final[i][j] = 0.0

    print("\nMa Trận chéo hóa:")
    for row in A_final:
        print([round(val, 4) for val in row])