from mat_oper_SSMMA import mat_negate, mat_add, mat_sub, vert_comb, hor_comb

def test_mat_negate():
    # Test matrix negation
    matrix = [[1, 2], [3, 4]]
    expected = [[-1, -2], [-3, -4]]
    result = mat_negate(matrix)
    test_passed = result == expected and matrix == [[1, 2], [3, 4]]
    print(f"test_mat_negate: {test_passed}")
    return test_passed

def test_mat_add():
    # Test matrix addition
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    result = mat_add(mat1, mat2)
    test_passed = result == expected and mat1 == [[1, 2], [3, 4]] and mat2 == [[5, 6], [7, 8]]
    print(f"test_mat_add: {test_passed}")
    return test_passed

def test_mat_sub():
    # Test matrix subtraction
    mat1 = [[9, 8], [7, 6]]
    mat2 = [[4, 3], [2, 1]]
    expected = [[5, 5], [5, 5]]
    result = mat_sub(mat1, mat2)
    test_passed = result == expected and mat1 == [[9, 8], [7, 6]] and mat2 == [[4, 3], [2, 1]]
    print(f"test_mat_sub: {test_passed}")
    return test_passed

def test_vert_comb():
    # Test vertical combination of matrices
    top = [[1, 2], [3, 4]]
    bottom = [[5, 6], [7, 8]]
    expected = [[1, 2], [3, 4], [5, 6], [7, 8]]
    result = vert_comb(top, bottom)
    test_passed = result == expected and top == [[1, 2], [3, 4]] and bottom == [[5, 6], [7, 8]]
    print(f"test_vert_comb: {test_passed}")
    return test_passed

def test_hor_comb():
    # Test horizontal combination of matrices
    left = [[1, 2], [3, 4]]
    right = [[5, 6], [7, 8]]
    expected = [[1, 2, 5, 6], [3, 4, 7, 8]]
    result = hor_comb(left, right)
    test_passed = result == expected and left == [[1, 2], [3, 4]] and right == [[5, 6], [7, 8]]
    print(f"test_hor_comb: {test_passed}")
    return test_passed

if __name__ == '__main__':
    # Run all tests and count how many passed
    tests = [test_mat_negate, test_mat_add, test_mat_sub, test_vert_comb, test_hor_comb]
    passed = sum(test() for test in tests)
    print(f"\nPassed {passed} out of {len(tests)} tests")