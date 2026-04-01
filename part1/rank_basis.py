from fractions import Fraction
from gaussian import gaussian_elimination

def rank_and_basis(A):
    n_rows = len(A)
    n_cols = len(A[0])
    
    M, _, _ = gaussian_elimination(A, [0] * n_rows)
    pivot_indices = []
    for i in range(n_rows):
        for j in range(n_cols):
            if M[i][j] != 0:
                pivot_indices.append((i, j))
                break
            
    rank = len(pivot_indices)
    row_basis = []
    for i, j in pivot_indices:
        row_basis.append([str(val) for val in M[i][:n_cols]])
        
    col_basis = []
    for _, j in pivot_indices:
        col_basis.append([str(M[i][j]) for i in range(n_rows)])
    
    null_basis = []
    if rank < n_cols:
        pivot_cols = [j for i, j in pivot_indices]
        free_cols = [j for j in range(n_cols) if j not in pivot_cols]
        
        for free_j in free_cols:
            special_solution = [Fraction(0)] * n_cols
            special_solution[free_j] = Fraction(1)

            for i, k in reversed(pivot_indices):
                sum_ax = sum(M[i][j] * special_solution[j] for j in range(k + 1, n_cols))
                special_solution[k] = -sum_ax / M[i][k]
            
            null_basis.append([str(val) for val in special_solution])
    
    return {
        "rank": rank,
        "row_basis": row_basis,
        "col_basis": col_basis,
        "null_basis": null_basis
    }