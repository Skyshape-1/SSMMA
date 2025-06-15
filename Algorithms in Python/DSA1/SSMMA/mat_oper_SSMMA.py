# Series: Matrix Operations for SSMMA



# Helper function Series: Basic Matrix Operations #
# Assumption: Input matrices are square
# Goal: to perform matrix addition, and subtraction
# Input: Two matrices of the same dimensions
# Output: One matrix of the same dimension
def mat_negate(mat):
    n = len(mat)
    mat2 = deep_copy(mat)
    for i in range(n):
        for j in range(n):
            mat2[i][j] = -mat[i][j]
    return mat2

def mat_add(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print("Matrices must have the same dimensions for addition.")
        return None
    n = len(mat1)
    mat3 = deep_copy(mat1)
    for i in range(n):
        for j in range(n):
            mat3[i][j] = mat3[i][j] + mat2[i][j]
    return mat3

def mat_sub(mat1, mat2):
    return mat_add(mat1, mat_negate(mat2))


# Series: Combinning sub matrices
def vert_comb(top, low):
    return top + low

def hor_comb(left, right):
    res = []
    for i in range(len(left)):
        res.append(left[i] + right[i])
    return res

# Helper Function: deep_copy
def deep_copy(matrix):
    if not matrix:
        return []
    return [row[:] for row in matrix]