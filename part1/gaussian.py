from fractions import Fraction
import numpy as np

def back_substitution(U, c):
    n_rows = len(U)
    n_cols = len(U[0])
    
    r = 0
    for i in range(n_rows):
        if any(val != 0 for val in U[i]):
            r += 1
    
    for i in range(r, n_rows):
        if c[i] != 0:
            print("He phuong trinh Vo nghiem.")
            return None
            
    pivot_cols = []
    for i in range(r):
        for j in range(n_cols):
            if U[i][j] != 0:
                pivot_cols.append(j)
                break
                
    free_cols = [j for j in range(n_cols) if j not in pivot_cols]

    if r < n_cols:
        print("He phuong trinh co Vo so nghiem. Nghiem tong quat:")
    
    x_expr = [{} for _ in range(n_cols)]
    
    for j in free_cols:
        x_expr[j] = {'const': Fraction(0), j: Fraction(1)}
        
    for i in range(r - 1, -1, -1):
        p = pivot_cols[i]
        expr = {'const': c[i]}
        
        for j in range(p + 1, n_cols):
            if U[i][j] != 0:
                for key, val in x_expr[j].items():
                    expr[key] = expr.get(key, Fraction(0)) - U[i][j] * val
                    
        for key in expr:
            expr[key] /= U[i][p]
            
        x_expr[p] = expr

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
                coeff_str = "" if abs_coeff == 1 else f"{abs_coeff}*"
                terms.append(f"{sign} {coeff_str}t{k+1}") 
        
        if not has_free_var:
            print(f"  x{j+1} = {const_val}")
        else:
            expr_str = " ".join(terms)
            if const_val != 0:
                expr_str = f"{const_val} " + expr_str
            else:
                if expr_str.startswith("+ "):
                    expr_str = expr_str[2:]
                elif expr_str.startswith("- "):
                    expr_str = "-" + expr_str[2:]
            print(f"  x{j+1} = {expr_str}")

    if r < n_cols:
        return x_expr 
    else:
        return [x_expr[j]['const'] for j in range(n_cols)]

def gaussian_eliminate(A, b):
    n = len(A)
    m = len(A[0])

    M = [[Fraction(val).limit_denominator(10**8) for val in row] + [Fraction(b[i]).limit_denominator(10**8)] for i, row in enumerate(A)]
    s = 0
    r = 0 

    for c_idx in range(m):
        if r >= n:
            break

        p = r
        for i in range(r + 1, n):
            if abs(M[i][c_idx]) > abs(M[p][c_idx]):
                p = i

        if abs(float(M[p][c_idx])) < 1e-8:
            for i in range(r, n):
                M[i][c_idx] = Fraction(0)
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

    x = back_substitution(U, c_result)
    
    return M, x, s

def verify_solution(A, x, b):
    if x is None: 
        print("Khong co nghiem de kiem chung.")
        return
    
    try:
        A_np = np.array(A, dtype=float)
        b_np = np.array(b, dtype=float)
        
        if isinstance(x[0], dict):
            n_cols = len(x)
            
            free_vars = set()
            for x_dict in x:
                for key in x_dict:
                    if key != 'const':
                        free_vars.add(key)
            
            x_p = np.array([float(x[i].get('const', Fraction(0))) for i in range(n_cols)])
            if not np.allclose(np.dot(A_np, x_p), b_np, atol=1e-5):
                print("-> SAI: Phan hang so (nghiem rieng) khong khop!")
                return
            
            for k in free_vars:
                v_k = np.array([float(x[i].get(k, Fraction(0))) for i in range(n_cols)])
                zeros = np.zeros(len(b))
                if not np.allclose(np.dot(A_np, v_k), zeros, atol=1e-5):
                    print(f"-> SAI: Vector he so cua bien tu do t{k+1} khong khop voi khong gian Null!")
                    return
                    
            print("-> Verify OK: Nghiem tong quat hoan toan CHINH XAC.")

        else:
            x_np = np.array([float(Fraction(val)) for val in x], dtype=float)
            ax_res = np.dot(A_np, x_np)
            if np.allclose(ax_res, b_np, atol=1e-5):
                print("-> Verify OK: Nghiem duy nhat CHINH XAC.")
            else:
                print("-> SAI: Nghiem duy nhat khong chinh xac.")
            
    except Exception as e:
        print(f"Da xay ra loi khi kiem chung nghiem: {e}")
        
def run_tests(test_cases):
    for idx, test in enumerate(test_cases, 1):
        A = test['A']
        b = test['b']
        
        print("=" * 65)
        print(f"TEST CASE {idx}: {test['name']}")
        print("Ma trận hệ số (A):")
        for row in A:
            print(f"  {row}")
        print(f"Vector hằng số (b): {b}")
        print("-" * 65)

        try:
            result = gaussian_eliminate([row[:] for row in A], b[:])
            
            if result is None:
                verify_solution(A, None, b)
            else:
                M, x, s = result

                if x is not None:
                    if isinstance(x[0], dict):
                        print(f"   Số lần hoán vị hàng (s): {s}")
                        print("   Nghiệm x: [Dạng phương trình tổng quát]")
                    else:
                        formatted_x = ", ".join([str(v) for v in x])
                        print(f"   Số lần hoán vị hàng (s): {s}")
                        print(f"   Nghiệm x: [{formatted_x}]")
                    
                    verify_solution(A, x, b)
                else:
                    print("   => Hệ vô nghiệm, không có nghiệm để kiểm chứng.")
                
        except Exception as e:
            print(f"   [Gauss] LỖI CHƯƠNG TRÌNH: {e}")

        print("=" * 65 + "\n")