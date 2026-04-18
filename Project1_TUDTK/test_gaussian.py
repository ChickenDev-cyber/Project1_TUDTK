from gaussian import gaussian_elimination, verify_solution

def test_gaussian():
    print("===== TEST GAUSSIAN ELIMINATION =====")

    # Test 1: nghiệm duy nhất
    A1 = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
    b1 = [8, -11, -3]
    print("Input A1:", A1)
    print("Input b1:", b1)
    M, x, s = gaussian_elimination(A1, b1)
    print("Test 1 - Unique solution:")
    print("x =", x)
    verify_solution(A1, x, b1)
    print("-" * 40)

    # Test 2: vô số nghiệm
    A2 = [[1, 2, 3], [2, 4, 6]]
    b2 = [5, 10]
    print("Input A2:", A2)
    print("Input b2:", b2)
    M, x, s = gaussian_elimination(A2, b2)
    print("Test 2 - Infinite solutions:")
    print("Result =", x)
    print("-" * 40)

    # Test 3: vô nghiệm
    A3 = [[1, 1], [1, 1]]
    b3 = [2, 3]
    print("Input A3:", A3)
    print("Input b3:", b3)
    M, x, s = gaussian_elimination(A3, b3)
    print("Test 3 - No solution:")
    print("Result =", x)
    print("-" * 40)


if __name__ == "__main__":
    test_gaussian()