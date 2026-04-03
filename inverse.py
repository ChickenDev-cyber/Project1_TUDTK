from fractions import Fraction
from determinant import determinant


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

