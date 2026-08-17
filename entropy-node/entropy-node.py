import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    unique_values, counts = np.unique(y, return_counts = True)
    prob = counts/len(y)
    print(prob)
    log_prob = np.log2(prob)
    return -np.dot(prob, log_prob)
    # pass