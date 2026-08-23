import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Return the expected value of the discrete distribution.
    """
    # Write code here
    x = np.asarray(x)
    p = np.asarray(p)
    e = np.dot(x,p)
    return float(e)
    # pass