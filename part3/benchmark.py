import time
import numpy as np
import solvers as sv
import math

def manual_norm(v):
    return math.sqrt(sum(x**2 for x in v))

def mat_vec_mult(A, x):
    n = len(A)
    result = [0.0] * n
    for i in range(n):
        result[i] = sum(A[i][j] * x[j] for j in range(len(x)))
    return result

def vec_sub(v1, v2):
    return [x - y for x, y in zip(v1, v2)]

def generate_hilbert_matrix(n):
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1.0 / (i + j + 1)
    return H

def generate_spd_matrix(n):
    # Tạo ma trận đối xứng xác định dương 
    A = np.random.rand(n, n)
    return np.dot(A, A.T) + n * np.eye(n)

#    Đo thời gian chạy trung bình (5 lần) và tính sai số tương đối của thuật toán.  
def generate_diagonally_dominant_matrix(n):
    A = np.random.rand(n, n)
    row_sums = np.sum(np.abs(A), axis=1)
    np.fill_diagonal(A, row_sums + 1.0)
    return A


# Hàm tính toán thời gian trung bình và sai số tương đối.
def run_experiment(solver_func, A, b, num_runs=5):
    total_time = 0.0
    x_hat = None
    
    if hasattr(A, 'tolist'): A = A.tolist()
    if hasattr(b, 'tolist'): b = b.tolist()
    
    for _ in range(num_runs):
        A_copy = [row[:] for row in A]
        b_copy = b[:]
        
        start_time = time.time()
        x_hat = solver_func(A_copy, b_copy) 
        total_time += (time.time() - start_time)
        
    avg_time = total_time / num_runs
    
    if x_hat is None or len(x_hat) == 0:
        x_hat = [0.0] * len(b)
    # Bước 1: Tính vector Ax = A * x_hat
    Ax = mat_vec_mult(A, x_hat)
    
    # Bước 2: Tính vector hiệu số: diff = Ax - b
    diff = vec_sub(Ax, b)
    
    # Bước 3: Tính sai số tương đối: ||Ax - b|| / ||b||
    norm_diff = manual_norm(diff)
    norm_b = manual_norm(b)
    
    # Tránh lỗi chia cho 0 
    relative_error = (norm_diff / norm_b) if norm_b != 0 else norm_diff
    
    return avg_time, relative_error

def benchmark_performance(solvers_dict, n_values=[50, 100, 200, 500, 1000]):
    results = {name: {'time': [], 'error': []} for name in solvers_dict.keys()}
    results['n'] = n_values

    print("="*50)
    print("BẮT ĐẦU ĐO THỜI GIAN THỰC THI (YÊU CẦU 2)")
    print("="*50)
    
    for n in n_values:
        print(f"\nĐang xử lý ma trận kích thước n = {n}...")
        
        A = generate_diagonally_dominant_matrix(n)
        
        x_true = np.ones(n)
        b = np.dot(A, x_true)

        for name, solver_func in solvers_dict.items():
            try:
                avg_time, rel_error = run_experiment(solver_func, A, b, num_runs=5)
                
                results[name]['time'].append(avg_time)
                results[name]['error'].append(rel_error)
                print(f"[{name}] Time: {avg_time:.6f}s | Error: {rel_error:.2e}")
                
            except Exception as e:
                print(f"[{name}] Lỗi khi giải n={n}: {e}")
                results[name]['time'].append(None)
                results[name]['error'].append(None)
                
    return results

def benchmark_stability(solvers_dict, n=10):    
    print("\n--- BẮT ĐẦU PHÂN TÍCH ỔN ĐỊNH SỐ ---")
    
    A_hilbert = generate_hilbert_matrix(n)
    A_spd = generate_spd_matrix(n) 
    
    x_true = np.ones(n)
    b_hilbert = np.dot(A_hilbert, x_true)
    b_spd = np.dot(A_spd, x_true)

    stability_results = {}

    for name, solver_func in solvers_dict.items():
        print(f"\n* Đang test độ ổn định của: {name}")
        
        # Test ma trận SPD (Tốt)
        try:
            _, error_spd = run_experiment(solver_func, A_spd, b_spd, num_runs=1)
            print(f"  -> Sai số SPD (Tốt): {error_spd:.2e}")
        except Exception as e:
            error_spd = None
            print(f"  -> Lỗi khi giải SPD: {e}")

        # Test ma trận Hilbert (Xấu)
        try:
            _, error_hilbert = run_experiment(solver_func, A_hilbert, b_hilbert, num_runs=1)
            print(f"  -> Sai số Hilbert (Xấu): {error_hilbert:.2e}")
        except Exception as e:
            error_hilbert = None
            print(f"  -> Lỗi giải Hilbert (Đã bị tràn số/Không hội tụ): {e}")

        # Lưu lại kết quả
        stability_results[name] = {
            'spd_error': error_spd,
            'hilbert_error': error_hilbert
        }
        
    return stability_results 