from rank_basis import rank_and_basis

def test_rank_basis():
    print("===== TEST RANK & BASIS =====")

    # Test 1: rank thấp hơn số cột
    A1 = [
        [1, 2, 3],
        [2, 4, 6],
        [1, 1, 1]
    ]
    print("Input A1:", A1)

    result = rank_and_basis(A1)
    print("Test 1:")
    print("Rank =", result["rank"])

    print("Row basis:")
    for row in result["row_basis"]:
        print(row)

    print("Column basis:")
    for col in result["col_basis"]:
        print(col)

    print("Null space basis:")
    for vec in result["null_basis"]:
        print(vec)

    print("-" * 40)

    # Test 2 (full rank)
    A2 = [
        [1, 2],
        [3, 4]
    ]
    print("Input A2:", A2)

    result = rank_and_basis(A2)

    print("Test 2 (Full rank):")
    print("Rank =", result["rank"])
    print("Null space basis:", result["null_basis"])
    print("-" * 40)

    # Test 3 (rank thấp hơn)
    A3 = [
        [1, 2, 3, 4],
        [2, 4, 6, 8]
    ]
    print("Input A3:", A3)

    result = rank_and_basis(A3)

    print("Test 3:")
    print("Rank =", result["rank"])

    print("Null space basis:")
    for vec in result["null_basis"]:
        print(vec)

    print("-" * 40)


if __name__ == "__main__":
    test_rank_basis()