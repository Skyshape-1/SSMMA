from mat_oper_SSMMA import mat_add, mat_sub, hor_comb, vert_comb
from padding_and_unpadding import padding_noret, unpadding_noret

# Goal: Implement SSMMA to perform matrix multiplication between two n by n matrices,
#       i.e. X*Y = Z 
    # Input: Two n by n matrices
    # Output: One n by n matrix

# Representation: 
# Every matrix will be represented by a list of lists (for pratical sake)

# Wrapper function #
# Goal: to perform padding on the input matrices and then call the SSMMA function
def wrapper(inputX, inputY):
    # Check if the input matrices are square
    if len(inputX) != len(inputX[0]) or len(inputY) != len(inputY[0]):
        raise ValueError("Input matrices must be square.")
    
    ori_dims = len(inputX)
    # Do padding on the input matrices
    padding_noret(inputX)
    padding_noret(inputY)
    # Call the SSMMA function
    res = SSMMA(inputX, inputY)
    # Unpadding the result
    unpadding_noret(res, ori_dims)
    return res

# Main Function #
# Input: Two n by n matrices (where n must be a power of 2, else requires padding )
# Output: One n by n matrix
def SSMMA(X, Y):
    if len(X) == 1:
        return [[X[0][0]*Y[0][0]]]
    else:
        subcol_X = mat_split(X)
        subcol_Y = mat_split(Y)
        X_A, X_B, X_C, X_D = subcol_X[0], subcol_X[1], subcol_X[2], subcol_X[3]
        Y_A, Y_B, Y_C, Y_D = subcol_Y[0], subcol_Y[1], subcol_Y[2], subcol_Y[3]
        # Seven Recursive calls
        P1 = SSMMA(X_A, mat_sub(Y_B, Y_D))
        P2 = SSMMA(mat_add(X_A, X_B), Y_D)
        P3 = SSMMA(mat_add(X_C, X_D), Y_A)
        P4 = SSMMA(X_D, mat_sub(Y_C, Y_A))
        P5 = SSMMA(mat_add(X_A, X_D), mat_add(Y_A, Y_D))
        P6 = SSMMA(mat_sub(X_B, X_D), mat_add(Y_C, Y_D))
        P7 = SSMMA(mat_sub(X_A, X_C), mat_add(Y_A, Y_B))

        # Additions between sub matrices

        Z_A = mat_sub(mat_add(P5, P4), mat_sub(P2, P6))
        Z_B = mat_add(P1, P2)
        Z_C = mat_add(P3, P4)
        Z_D = mat_sub(mat_add(P1, P5), mat_add(P3, P7))
        upper, lower = hor_comb(Z_A, Z_B), hor_comb(Z_C, Z_D)
        Z = vert_comb(upper, lower)
        return Z

# Helper function #
# Goal: to extract sub matrices 
# Input: a matrix (guaranteed n is even)
# Output: four submatrices of oder n/2
def sub_mat(mat, col_from, col_end, row_from, row_end):    
    res = []
    for i in range(row_from, row_end):
        row = []
        for j in range(col_from, col_end):
            row.append(mat[i][j])
        res.append(row)
    return res

# Helper function II #
# Input: A matrix of order n
# Output: Four submatrices all of order n/2
def mat_split(mat):
    n = len(mat)
    topleft, topright, lowleft, lowright = sub_mat(mat, 0, n//2, 0, n//2), \
        sub_mat(mat, n//2, n, 0, n//2), \
        sub_mat(mat, 0, n//2, n//2, n), \
        sub_mat(mat, n//2, n, n//2, n)
    
    return (topleft, topright, lowleft, lowright)


def SSMMA_test_case():
    X = [
    [1, 2, 3, 1, 11],
    [4, 5, 6, 2, 12],
    [7, 8, 9, 3, 13],
    [10,11,12,4, 7],
    [13,14,15,5, 8]
]
    Y = [
    [10, 9, 8, 10, 7],
    [8, 8, 7, 9, 5],
    [4, 3, 2, 8, 6],
    [1, 0, 1, 7, 13],
    [0, 1, 2, 3, 4]
]
    
    Z = [
    [39, 45, 51, 92, 92],
    [106, 106, 105, 183, 163],
    [173, 167, 159, 274, 234],
    [240, 221, 199, 344, 277],
    [307, 282, 253, 435, 348]
    ]
    print("Input Matrices:")
    res = wrapper(X, Y)
    print(res)
    print("Expected Output:")
    print(Z)
    print("Test Passed!" if res == Z else "Test Failed!")

SSMMA_test_case()