from fractions import Fraction
from gaussian import gaussian_eliminate
import numpy as np
import io
from contextlib import redirect_stdout

def determinant(A):
    n = len(A)
    # Kiểm tra A phải là ma trận vuông
    assert all(len(row) == n for row in A), "Chỉ áp dụng cho ma trận vuông!"
    b_zero = [0] * n
    with redirect_stdout(io.StringIO()):
        M, _, s = gaussian_eliminate(A, b_zero)
    
    # lấy tích của chúng = det của U
    det = Fraction((-1) ** s)
    for i in range(n):
        det *= M[i][i]
    return det
