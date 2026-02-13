import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    mod_a = np.sqrt(np.dot(a, a))
    mod_b = np.sqrt(np.dot(b, b))
    if mod_a == 0 or mod_b == 0:
        return 0
    else:
        cosine = np.dot(a, b)/mod_a/mod_b
        return cosine
    # pass