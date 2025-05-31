# Helper #
def is_power_of_two(n):
    while n > 1:
        rem = n % 2
        if rem != 0:
            return False    
        n = n / 2
    return True


def padding_noret(mat): # Test pending

    n = len(mat)
    while not is_power_of_two(n):
        n += 1
    for i in range(n):
        if i < len(mat):
                while len(mat[i]) < n:
                    mat[i].append(0)
        else:
            zerorow = [0]*n
            mat.append(zerorow)

def unpadding_noret(mat, m):
    
    for i in range(m):
        mat[i] = mat[i][:m]
    
    del mat[m:]


# create test cases for padding and unpadding
def primary_test_case():
    mat = [[1, 2, 3], [3, 4, 5], [6, 7, 8]]
    print("Test Case: Padding and Unpadding")
    print("Original Matrix:")
    print(mat)
    
    padding_noret(mat)
    print("Padded Matrix:")
    print(mat)
    
    unpadding_noret(mat, 3)
    print("Unpadded Matrix:")
    print(mat)

primary_test_case()