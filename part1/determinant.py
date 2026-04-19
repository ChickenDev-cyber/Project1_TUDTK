from fractions import Fraction
from gaussian import gaussian_elimination
import numpy as np
import io
from contextlib import redirect_stdout

def determinant(A):
    n = len(A)
    # Kiểm tra A phải là ma trận vuông
    assert all(len(row) == n for row in A), "Chỉ áp dụng cho ma trận vuông!"
    b_zero = [0] * n
    with redirect_stdout(io.StringIO()):
        M, _, s = gaussian_elimination(A, b_zero)
    
    # Ta chỉ lấy n cột đầu của đường chéo.
    # lấy tích của chúng = det của U
    det = Fraction((-1) ** s)
    for i in range(n):
        det *= M[i][i]
    return det

if __name__ == "__main__":
    def run_test(name, A):
        print(f"=== {name} ===")
        print(f"Ma tran: {A}")
        det = determinant(A)
        print(f"Dinh thuc tinh duoc: {det} ({float(det)})")
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
