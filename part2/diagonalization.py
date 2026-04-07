import math as mth
import numpy as np

def InitMatrix(n, m):
    Res = []
    for i in range(n):
        row_zeros = [0.0] * m
        Res.append(row_zeros)
    return Res

def CheckDefective(A, eigenvalues, sai_so=1e-6):
    n = len(A)
    A_np = np.array(A)
    
    # Lấy danh sách các trị riêng duy nhất kiểm tra
    unique_eigenvalues = np.unique(np.round(eigenvalues, 8)) 
    
    for lamda in unique_eigenvalues:
        #  Đếm xem lamda xuất hiện mấy lần trong eigenvalues
        AM = np.sum(np.isclose(eigenvalues, lamda, atol=sai_so))
        
        if AM > 1: # Chỉ cần kiểm tra nếu là nghiệm kép/bội
            # Tính ma trận (A - lamda*I)
            A_minus_lamdaI = A_np - lamda * np.eye(n)
            
            # Bội hình học (GM) = n - hạng của ma trận (A - lamda*I)
            rank = np.linalg.matrix_rank(A_minus_lamdaI, tol=sai_so)
            GM = n - rank
            
            if GM < AM:
                return True # không đủ vecto riêng tương ứng trị riêng
    return False

def SolveEigenFullFast(A):
    # Ở đây ta dùng .eig để lấy cả eigenvalues và eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    n = len(A)
    A_final = InitMatrix(n, n)
    
    for i in range(n):
        # ĐIỀU KIỆN: Kiểm tra nếu là số phức
        if np.iscomplex(eigenvalues[i]):
            print("Thất bại: Tồn tại giá trị riêng phức => Là không có thể tạo chéo hóa")
            return [], []
        
        # Lấy phần thực và điền vào đường chéo
        A_final[i][i] = float(eigenvalues[i].real)

    # ĐIỀU KIỆN: Kiểm tra (nghiệm kép, defective)
    if CheckDefective(A, eigenvalues):
        print("Thất bại: Ma trận nghiệm kép, không đủ không gian vector riêng.")
        return [], []

    P_matrix = eigenvectors.real.tolist()

    print("Ma trận có thể chéo hóa.")
    return A_final, P_matrix

if __name__ == "__main__":
    # A = [
    #     [1, 3, 3],
    #     [-3, -5, -3],
    #     [3, 3, 1]
    # ]

    # A = [[3, 1, 0], 
    #      [0, 3, 0], 
    #      [0, 0, 5]]

    A = [
        [3, -2],
        [4, -1]
    ]


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
            print([round(val, 4) for val in row])