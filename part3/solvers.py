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
    A = [[float(val) for val in row] for row in A]
    b = [float(val) for val in b]
    
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    # 2. Phân rã LU
    for i in range(n):
        # Tính U[i][k]
        for k in range(i, n):
            # Tính sum(L[i][j] * U[j][k]) bằng vòng lặp thuần
            sum_lu = 0.0
            for j in range(i):
                sum_lu += L[i][j] * U[j][k]
            U[i][k] = A[i][k] - sum_lu

        # Tính L[k][i]
        for k in range(i + 1, n):
            sum_lu = 0.0
            for j in range(i):
                sum_lu += L[k][j] * U[j][i]
            
            if abs(U[i][i]) < 1e-12: return [] # Tránh chia cho 0
            L[k][i] = (A[k][i] - sum_lu) / U[i][i]

    # 3. Thế tiến: Ly = b
    y = [0.0] * n
    for i in range(n):
        sum_ly = 0.0
        for j in range(i):
            sum_ly += L[i][j] * y[j]
        y[i] = b[i] - sum_ly

    # 4. Thế lùi: Ux = y
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        sum_ux = 0.0
        for j in range(i + 1, n):
            sum_ux += U[i][j] * x[j]
        x[i] = (y[i] - sum_ux) / U[i][i]

    return x

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

def verify_solution(A, b, x, method_name):
    """
    Kiểm chứng nghiệm x bằng cách tính Ax và so sánh với b.
    """
    if not x:
        print(f"   [{method_name}] KIỂM CHỨNG: BỎ QUA (Không có nghiệm hợp lệ)")
        return

    try:
        A_np = np.array(A, dtype=float)
        b_np = np.array(b, dtype=float)
        x_np = np.array(x, dtype=float)
        
        # Tái tạo b: Ax = b_reconstructed
        b_reconstructed = np.dot(A_np, x_np)
        
        # Kiểm tra sai số
        if np.allclose(b_np, b_reconstructed, atol=1e-4):
            print(f"   [{method_name}] KIỂM CHỨNG: THÀNH CÔNG (Ax ≈ b)")
        else:
            sai_so = np.max(np.abs(b_np - b_reconstructed))
            print(f"   [{method_name}] KIỂM CHỨNG: CẢNH BÁO SAI SỐ (Độ lệch tối đa: {sai_so:.2e})")
            
    except Exception as e:
        print(f"   [{method_name}] KIỂM CHỨNG: LỖI TOÁN HỌC ({e})")


def run_tests(test_cases):
    """
    Hàm chạy kiểm thử hàng loạt các hệ phương trình
    """
    for idx, test in enumerate(test_cases, 1):
        A = test['A']
        b = test['b']
        
        print("=" * 65)
        print(f"TEST CASE {idx}: {test.get('name', 'Không tên')}")
        print("Ma trận hệ số (A):")
        for row in A:
            print(f"  {[round(val, 4) for val in row]}")
        print(f"Vector hằng số (b): {b}")
        print("-" * 65)

        # --- 1. PHƯƠNG PHÁP KHỬ GAUSS ---
        print("1. Phương pháp Khử Gauss:")
        try:
            # Truyền bản sao của A và b để tránh làm thay đổi ma trận gốc
            x_gauss = solve_gauss([row[:] for row in A], b[:])
            if x_gauss:
                print("   Nghiệm:", [round(val, 5) for val in x_gauss])
            verify_solution(A, b, x_gauss, "Gauss")
        except Exception as e:
            print(f"   [Gauss] LỖI: {e}")

        print()

        # --- 2. PHƯƠNG PHÁP LU ---
        print("2. Phương pháp Phân rã LU:")
        try:
            x_lu = solve_lu([row[:] for row in A], b[:])
            if x_lu:
                print("   Nghiệm:", [round(val, 5) for val in x_lu])
            verify_solution(A, b, x_lu, "LU")
        except Exception as e:
            print(f"   [LU] LỖI: {e}")

        print()

        # --- 3. PHƯƠNG PHÁP GAUSS-SEIDEL ---
        print("3. Phương pháp Gauss-Seidel:")
        try:
            if not IsStrictlyDiagonallyDominant(A):
                print("   [!] Cảnh báo: Ma trận không chéo trội ngặt, có thể hội tụ chậm hoặc phân kỳ.")
            
            x_gs = solve_gauss_seidel([row[:] for row in A], b[:])
            if x_gs:
                print("   Nghiệm:", [round(val, 5) for val in x_gs])
            verify_solution(A, b, x_gs, "Gauss-Seidel")
        except Exception as e:
            print(f"   [Gauss-Seidel] LỖI: {e}")

        print("=" * 65 + "\n")


if __name__ == "__main__":
    test_cases = [
        {
            "name": "TEST 1: Hệ 3x3 Chéo trội ngặt",
            "A": [
                [4.0,  1.0, -1.0],
                [1.0,  5.0,  2.0],
                [-1.0, 1.0,  6.0]
            ],
            "b": [1.0, 0.0, 10.0]
        },
        {
            "name": "TEST 2: Hệ 4x4 Chéo trội ngặt ",
            "A": [
                [10.0, -1.0,  2.0,  0.0],
                [-1.0, 11.0, -1.0,  3.0],
                [ 2.0, -1.0, 10.0, -1.0],
                [ 0.0,  3.0, -1.0,  8.0]
            ],
            "b": [14.0, 30.0, 26.0, 35.0]
        },
        {
            "name": "TEST 3: Hệ 3x3 KHÔNG chéo trội (Gauss-Seidel phân kỳ/thất bại, Gauss & LU giải tốt)",
            "A": [
                [1.0, 4.0, 1.0],
                [2.0, 1.0, 3.0],
                [3.0, 2.0, 1.0]
            ],
            "b": [5.0, 2.0, 7.0]
        },
        {
            "name": "TEST 4: Hệ 3x3 Số thập phân lẻ (Kiểm tra sai số dấu phẩy động)",
            "A": [
                [2.5, 0.5, 1.0],
                [0.2, 3.5, 0.8],
                [0.1, 0.3, 4.2]
            ],
            "b": [2.5, -0.45, 6.2]
        },
        {
            "name": "TEST 5: Phần tử đầu tiên trên đường chéo bằng 0 (LU sẽ lỗi, Gauss có pivoting sẽ sống)",
            "A": [
                [0.0, 2.0, 3.0],
                [4.0, 5.0, 6.0],
                [7.0, 8.0, 0.0]
            ],
            "b": [13.0, 32.0, 23.0]
        }
    ]

    # Khởi chạy toàn bộ 5 tests
    run_tests(test_cases)