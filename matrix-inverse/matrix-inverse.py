import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    # row_count = len(A)
    # col_count = len(A[0])
    A  = np.array(A)
    n = A.shape[0]
    if A.ndim != 2 or A.shape[0] != A.shape[0]:
        return None
    try:
        A_inv = np.linalg.inv(A)
        identity = np.eye(n)
        error = np.linalg.norm(A @ A_inv - identity)
        if error < 1e-7:
            return A_inv
        else:
            return None
    except np.linalg.LinAlgError:
        return None

    # pass
