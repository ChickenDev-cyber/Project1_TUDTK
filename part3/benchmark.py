import time
import numpy as np

def generate_hilbert_matrix(n):
    # Tạo ma trận Hilbert H_ij = 1 / (i + j + 1) do index Python bắt đầu từ 0
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1.0 / (i + j + 1)
    return H

def generate_spd_matrix(n):
    # Tạo ma trận đối xứng xác định dương (Symmetric Positive Definite)
    A = np.random.rand(n, n)
    return np.dot(A, A.T) + n * np.eye(n)

def run_experiment(solver_func, A, b, num_runs=5):
    """
    Đo thời gian chạy trung bình (5 lần) và tính sai số tương đối của thuật toán.
    """
    total_time = 0.0
    x_hat = None
    
    for _ in range(num_runs):
        # Phải copy() để tránh thuật toán làm biến đổi ma trận gốc ở các lần lặp sau
        A_copy = A.copy()
        b_copy = b.copy()
        
        start_time = time.time()
        x_hat = solver_func(A_copy, b_copy) 
        total_time += (time.time() - start_time)
        
    avg_time = total_time / num_runs
    
    # Tính sai số tương đối: ||A*x_hat - b||_2 / ||b||_2
    relative_error = np.linalg.norm(np.dot(A, x_hat) - b) / np.linalg.norm(b)
    
    return avg_time, relative_error