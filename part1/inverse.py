from fractions import Fraction
from determinant import determinant
import numpy as np

def inverse(A):
    n = len(A)
    assert all(len(row) == n for row in A), "inverse() chỉ áp dụng cho ma trận vuông!"

    # ── Kiểm tra khả nghịch ─────────────────────────────────────────────
    # Tính det để kiểm tra khả nghịch - det = 0
    det = determinant(A)
    if det == 0:
        print("Ma trận suy biến (det = 0) --> không tồn tại ma trận nghịch đảo!")
        return None

    # ── Tạo ma trận ghép [A | I_n] ─────────────────────────────────────
    # Mỗi hàng: n phần tử từ A + n phần tử từ I (hàng i của I có 1 ở cột i)
    I = [[Fraction(1) if i == j else Fraction(0) for j in range(n)]
        for i in range(n)]
    M = [
        [Fraction(A[i][j]) for j in range(n)] + I[i]
        for i in range(n)
    ]

    # ── Gauss–Jordan: khử xuôi và khử ngược ────────────────────────────
    for k in range(n):

        # 1. Partial Pivoting: tìm hàng có |M[i][k]| lớn nhất từ k xuống
        max_row = k
        for i in range(k + 1, n):
            if abs(M[i][k]) > abs(M[max_row][k]):
                max_row = i

        if M[max_row][k] == 0:
            # Kiểm tra suy biến lần 2
            print("Ma trận suy biến — không thể tính nghịch đảo!")
            return None

        # 2. Hoán đổi hàng k với hàng max_row (nếu cần)
        if max_row != k:
            M[k], M[max_row] = M[max_row], M[k]

        # 3. Chuẩn hóa hàng k: chia toàn hàng cho pivot M[k][k]
        #    Mục đích: pivot trở thành 1
        pivot = M[k][k]
        for j in range(2 * n):
            M[k][j] /= pivot

        # 4. Khử tất cả hàng khác (cả hàng TRÊN lẫn hàng DƯỚI)
        #    Đây là điểm khác Gauss thường — Gauss–Jordan khử cả 2 chiều
        #    để đưa phần trái về ma trận đơn vị I
        for i in range(n):
            if i == k:
                continue   # bỏ qua hàng k vừa chuẩn hóa
            factor = M[i][k]
            if factor == 0:
                continue
            for j in range(2 * n):
                M[i][j] -= factor * M[k][j]
            M[i][k] = Fraction(0)   # gán thẳng để tránh sai số nhỏ lẻ

    # ── Lấy phần bên phải: đó chính là A⁻¹ ────────────────────────────
    # Sau khi biến đổi xong: M = [I | A⁻¹]
    # Ta cắt lấy n cột cuối của mỗi hàng
    A_inv = [[str(M[i][n + j]) for j in range(n)] for i in range(n)]
    return A_inv


#Kiểm thử
if __name__ == "__main__":
    def run_test(name, A):
        print(f"\n=== {name} ===")
        print(f"Ma tran A: {A}")
        inv = inverse(A)
        if inv:
            print("Ma tran nghich dao A^-1:")
            for row in inv:
                print(row)
                
    # Case 1: Ma trận 2x2 cơ bản
    run_test("CASE 1: MA TRAN 2x2", [[4, 7], [2, 6]])

    # Case 2: Ma trận 3x3
    run_test("CASE 2: MA TRAN 3x3", [[1, 2, 3], [0, 1, 4], [5, 6, 0]])

    # Case 3: Ma trận đơn vị (nghịch đảo là chính nó)
    run_test("CASE 3: MA TRAN DON VI", [[1, 0], [0, 1]])

    # Case 4: Ma trận suy biến (det = 0)
    run_test("CASE 4: MA TRAN SUY BIEN", [[1, 2], [2, 4]])

    # Case 5: Ma trận 1x1
    run_test("CASE 5: MA TRAN 1x1", [[5]])