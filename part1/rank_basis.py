from fractions import Fraction
from gaussian import gaussian_eliminate
import numpy as np
import io
from contextlib import redirect_stdout

def rank_and_basis(A):
    n_rows = len(A)
    n_cols = len(A[0])
    
    # Khử Gauss để tìm ma trận bậc thang M
    with redirect_stdout(io.StringIO()):
        M_aug, _, _ = gaussian_eliminate(A, [0] * n_rows)
    
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