from fractions import Fraction
import numpy as np

def back_substitution(U, c, r):
    n_rows = len(U)
    n_cols = len(U[0])
    
    # 1. Kiểm tra Vô nghiệm trước
    for i in range(r, n_rows):
        if c[i] != 0:
            print("He phuong trinh Vo nghiem.")
            return None
            
    # 2. Tìm các cột Pivot (Biến cơ sở)
    pivot_cols = []
    for i in range(r):
        for j in range(n_cols):
            if U[i][j] != 0:
                pivot_cols.append(j)
                break
                
    # Các cột không phải pivot là Biến tự do
    free_cols = [j for j in range(n_cols) if j not in pivot_cols]

    if r < n_cols:
        print("He phuong trinh co Vo so nghiem. Nghiem tong quat:")
    
    # Biểu diễn nghiệm dưới dạng dictionary: x[j] = {'const': gia_tri, index_bien_tu_do: he_so, ...}
    x_expr = [{} for _ in range(n_cols)]
    
    # Khởi tạo cho các biến tự do (VD: x2 = 1*t2)
    for j in free_cols:
        x_expr[j] = {'const': Fraction(0), j: Fraction(1)}
        
    # Thế ngược để tìm các biến cơ sở
    for i in range(r - 1, -1, -1):
        p = pivot_cols[i]
        expr = {'const': c[i]}
        
        for j in range(p + 1, n_cols):
            if U[i][j] != 0:
                # Trừ đi U[i][j] * x_expr[j]
                for key, val in x_expr[j].items():
                    expr[key] = expr.get(key, Fraction(0)) - U[i][j] * val
                    
        # Chia cho phần tử pivot
        for key in expr:
            expr[key] /= U[i][p]
            
        x_expr[p] = expr

    # 3. In kết quả nghiệm dưới dạng phương trình tham số
    for j in range(n_cols):
        terms = []
        const_val = x_expr[j].get('const', Fraction(0))
        has_free_var = False
        
        for k in free_cols:
            if k in x_expr[j] and x_expr[j][k] != 0:
                has_free_var = True
                coeff = x_expr[j][k]
                sign = "+" if coeff > 0 else "-"
                abs_coeff = abs(coeff)
                # Nếu hệ số là 1 hoặc -1 thì ẩn số 1 đi cho đẹp (vd: t2 thay vì 1*t2)
                coeff_str = "" if abs_coeff == 1 else f"{abs_coeff}*"
                terms.append(f"{sign} {coeff_str}t{k+1}") 
        
        if not has_free_var:
            print(f"  x{j+1} = {const_val}")
        else:
            expr_str = " ".join(terms)
            if const_val != 0:
                expr_str = f"{const_val} " + expr_str
            else:
                # Cắt bỏ dấu "+" hoặc "-" thừa ở đầu chuỗi nếu không có hằng số
                if expr_str.startswith("+ "):
                    expr_str = expr_str[2:]
                elif expr_str.startswith("- "):
                    expr_str = "-" + expr_str[2:]
            print(f"  x{j+1} = {expr_str}")

    # Trả về kết quả tùy theo trường hợp
    if r < n_cols:
        # Nếu vô số nghiệm, có thể trả về x_expr để sau này dùng, 
        # nhưng ở đây trả về None để hàm verify_solution hiện tại không bị lỗi.
        return None 
    else:
        # Nếu nghiệm duy nhất, convert x_expr thành mảng Fraction bình thường
        return [x_expr[j]['const'] for j in range(n_cols)]
    

def gaussian_elimination(A, b):
    n = len(A)
    m = len(A[0])

    M = [[Fraction(val) for val in row] + [Fraction(b[i])] for i, row in enumerate(A)]
    s = 0
    r = 0 

    for c_idx in range(m):
        if r >= n:
            break

        p = r
        for i in range(r + 1, n):
            if abs(M[i][c_idx]) > abs(M[p][c_idx]):
                p = i

        if M[p][c_idx] == 0:
            continue

        if p != r:
            M[r], M[p] = M[p], M[r]
            s += 1

        for i in range(r + 1, n):
            f = M[i][c_idx] / M[r][c_idx]
            M[i][c_idx] = Fraction(0) 
            for j in range(c_idx + 1, m + 1):
                M[i][j] -= M[r][j] * f
        
        r += 1 

    U = [row[:m] for row in M]
    c_result = [row[m] for row in M]

    # --- SỬA: Đưa tham số r vào hàm thế ngược để in thông báo ---
    x = back_substitution(U, c_result, r)
    
    return M, x, s

def verify_solution(A, x, b):
    if x is None: 
        print("Khong co nghiem de kiem chung.")
        return
    
    try:
        A_np = np.array(A, dtype=float)
        b_np = np.array(b, dtype=float)
        
        # TRƯỜNG HỢP 1: NGHIỆM TỔNG QUÁT (x là list các dictionary)
        if isinstance(x[0], dict):
            n_cols = len(x)
            
            # Tìm tất cả các index của biến tự do có trong nghiệm
            free_vars = set()
            for x_dict in x:
                for key in x_dict:
                    if key != 'const':
                        free_vars.add(key)
            
            # Điều kiện 1: A * x_p = b (Kiểm tra phần hằng số)
            x_p = np.array([float(x[i].get('const', Fraction(0))) for i in range(n_cols)])
            if not np.allclose(np.dot(A_np, x_p), b_np, atol=1e-9):
                print("-> SAI: Phan hang so (nghiem rieng) khong khop!")
                return
            
            # Điều kiện 2: A * v_i = 0 (Kiểm tra phần vector của từng biến tự do)
            for k in free_vars:
                v_k = np.array([float(x[i].get(k, Fraction(0))) for i in range(n_cols)])
                zeros = np.zeros(len(b))
                if not np.allclose(np.dot(A_np, v_k), zeros, atol=1e-9):
                    print(f"-> SAI: Vector he so cua bien tu do t{k+1} khong khop voi khong gian Null!")
                    return
                    
            print("-> Verify OK: Nghiem tong quat hoan toan CHINH XAC.")

        # TRƯỜNG HỢP 2: NGHIỆM DUY NHẤT (x là list các Fraction bình thường)
        else:
            x_np = np.array([float(Fraction(val)) for val in x], dtype=float)
            ax_res = np.dot(A_np, x_np)
            if np.allclose(ax_res, b_np, atol=1e-9):
                print("-> Verify OK: Nghiem duy nhat CHINH XAC.")
            else:
                print("-> SAI: Nghiem duy nhat khong chinh xac.")
            
    except Exception as e:
        print(f"Da xay ra loi khi kiem chung nghiem: {e}")
        
#Kiem thu
if __name__ == "__main__":
    
    print("NGHIEM DUY NHAT")
    A1 = [[2, 1, -1], 
          [-3, -1, 2], 
          [-2, 1, 2]]
    b1 = [8, -11, -3]
    M1, x1, s1 = gaussian_elimination(A1, b1)
    if x1:
        formatted_x = ", ".join([str(v) for v in x1])
        print(f"Nghiem x: {formatted_x}")
    verify_solution(A1, x1, b1)

    print("\nVO NGHIEM")
    A2 = [[1, 1], 
          [1, 1]]
    b2 = [2, 3]
    gaussian_elimination(A2, b2)

    print("\nVO SO NGHIEM")
    A3 = [[1, 2], 
          [2, 4]]
    b3 = [3, 6]
    gaussian_elimination(A3, b3)

    print("\n NGHIEM PHAN SO ")
    # Ma trận A và vector b của hệ trên
    A4 = [
        [2, 4, 2],
        [4, 2, 2],
        [2, 2, 4]
    ]
    b4 = [2, 4, 6]
    M4, x4, s4 = gaussian_elimination(A4, b4)

    if x4:
        formatted_x = ", ".join([str(v) for v in x4])
        print(f"Nghiem x: {formatted_x}")

        verify_solution(A4, x4, b4)
