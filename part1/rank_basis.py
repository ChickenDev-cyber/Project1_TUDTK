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

if __name__ == "__main__":
    test_cases_rank = [
    ("CASE 1: Ma trận vuông đủ hạng", [[1, 2, 3], [4, 5, 6], [7, 8, 10]]),
    ("CASE 2: Ma trận phụ thuộc tuyến tính", [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    ("CASE 3: Ma trận chữ nhật (2x4)", [[1, 2, 0, 3], [0, 0, 1, 4]]),
    ("CASE 4: Ma trận Zero (rank = 0)", [[0, 0], [0, 0]]),
    ("CASE 5: Ma trận đơn vị", [[1, 0, 0], [0, 1, 0], [0, 0, 1]]),
    ("CASE 6: Ma trận một dòng", [[1, 2, 3, 4]]),
    ("CASE 7: Ma trận một cột", [[1], [2], [3]])
]

    for name, A in test_cases_rank:
        print(f"-------------- {name} --------------")
        print("Ma trận A:")
        for row in A:
            print(f"  {row}")

        res = rank_and_basis(A)
        rank_np = np.linalg.matrix_rank(A)

        print(f"Hạng (của hàm tự định nghĩa): {res['rank']} | Hạng (NumPy): {rank_np}")
        print(f"-> Hạng tính đúng? {res['rank'] == rank_np}")

        print(f"Cơ sở dòng: {res['row_basis']}")
        print(f"Cơ sở cột : {res['col_basis']}")
        print(f"Cơ sở Null: {res['null_basis']}")
        print("\n")