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
