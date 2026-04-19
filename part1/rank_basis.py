from fractions import Fraction
from gaussian import gaussian_elimination
import numpy as np
import io
from contextlib import redirect_stdout

def rank_and_basis(A):
    n_rows = len(A)
    n_cols = len(A[0])
    
    # Khử Gauss để tìm ma trận bậc thang M
    with redirect_stdout(io.StringIO()):
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

# KIỂM THỬ
if __name__ == "__main__":
    def run_test(name, A):
        print(f"\n=== {name} ===")
        res = rank_and_basis(A)
        print(f"Ma tran: {A}")
        print(f"Hang (Rank): {res['rank']}")
        print(f"Co so dong (Row Basis): {res['row_basis']}")
        print(f"Co so cot (Col Basis): {res['col_basis']}")
        print(f"Co so nghiem (Null Basis): {res['null_basis']}")

    # CASE 1: Ma tran vuong du hang
    A1 = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
    run_test("CASE 1: MA TRAN VUONG DU HANG", A1)

    # CASE 2: Ma tran co dong phu thuoc tuyen tinh
    A2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    run_test("CASE 2: MA TRAN PHU THUOC TUYEN TINH", A2)

    # CASE 3: Ma tran chu nhat (Nhieu an hon phuong trinh)
    A3 = [[1, 2, 0, 3], [0, 0, 1, 4]]
    run_test("CASE 3: MA TRAN CHU NHAT (2x4)", A3)

    # CASE 4: Ma tran Zero (Edge Case: Rank = 0)
    A4 = [[0, 0], [0, 0]]
    run_test("CASE 4: MA TRAN ZERO (RANK 0)", A4)

    # CASE 5: Ma tran don vi (Co so la cac vector don vi)
    A5 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    run_test("CASE 5: MA TRAN DON VI", A5)

    # CASE 6: Ma tran chi co 1 dong (Row matrix)
    A6 = [[1, 2, 3, 4]]
    run_test("CASE 6: MA TRAN MOT DONG", A6)

    # CASE 7: Ma tran chi co 1 cot (Column matrix)
    A7 = [[1], [2], [3]]
    run_test("CASE 7: MA TRAN MOT COT", A7)