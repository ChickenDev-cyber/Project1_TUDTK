from fractions import Fraction
from gaussian import gaussian_elimination
import numpy as np

def determinant(A):
    n = len(A)
    # Kiểm tra A phải là ma trận vuông
    assert all(len(row) == n for row in A), "Chỉ áp dụng cho ma trận vuông!"
    # Gọi gaussian_elimination với b = [0,...,0] (ta chỉ cần M và s, không quan tâm đến nghiệm x ở đây)
    b_zero = [0] * n
    M, _, s = gaussian_elimination(A, b_zero)
    # M trả về là list of lists, mỗi hàng có n+1 phần tử (n phần từ A, 1 phần tử từ b). Ta chỉ lấy n cột đầu của đường chéo.
    # M[i][i] là pivot của hàng i sau khi khử → lấy tích của chúng = det của U
    det = Fraction((-1) ** s)
    for i in range(n):
        det *= M[i][i]
    return det

def verify_solution(A, custom_det):
    print("\n[KIEM CHUNG VOI NUMPY]")
    try:
        A_np = np.array(A, dtype=float)
        numpy_det = np.linalg.det(A_np)
        
        # Chuyển custom_det (Fraction) sang float để so sánh
        custom_det_float = float(custom_det)
        
        if np.isclose(custom_det_float, numpy_det, atol=1e-9):
            print(f"Ket qua: CHINH XAC")
            print(f"Custom: {custom_det_float} | NumPy: {round(numpy_det, 4)}")
        else:
            print(f"Ket qua: SAI LECH")
            print(f"Custom: {custom_det_float} | NumPy: {numpy_det}")
    except Exception as e:
        print(f"Loi kiem chung: {e}")

# Kiểm chứng
if __name__ == "__main__":
    def run_test(name, A):
        print(f"=== {name} ===")
        print(f"Ma tran: {A}")
        det = determinant(A)
        print(f"Dinh thuc tinh duoc: {det} ({float(det)})")
        verify_solution(A, det)
        print("-" * 30)

    # Case 1: Ma trận 2x2 cơ bản
    run_test("CASE 1: MA TRAN 2x2", [[1, 2], [3, 4]])

    # Case 2: Ma trận 3x3
    run_test("CASE 2: MA TRAN 3x3", [[6, 1, 1], [4, -2, 5], [2, 8, 7]])

    # Case 3: Ma trận suy biến (Dòng 3 = Dòng 1 + Dòng 2)
    run_test("CASE 3: MA TRAN SUY BIEN (DET=0)", [[1, 2, 3], [4, 5, 6], [5, 7, 9]])

    # Case 4: Ma trận đơn vị
    run_test("CASE 4: MA TRAN DON VI", [[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # Case 5: Ma trận 4x4
    run_test("CASE 5: MA TRAN 4x4", [
        [1, 0, 2, -1],
        [3, 0, 0, 5],
        [2, 1, 4, -3],
        [1, 0, 5, 0]
    ])
