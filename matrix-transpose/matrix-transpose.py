import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    # pass
    transpose_matrix = []
    # list_1 = []
    for i in range(len(A[0])):
        list_1 = []
        for j in range(len(A)):
            list_1.append(A[j][i])
        transpose_matrix.append(list_1)


    return np.asarray(transpose_matrix)