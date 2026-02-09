import numpy as np

def t_test_one_sample(x, mu0):
    """
    Compute one-sample t-statistic.
    """
    # Write code here
    s = np.sqrt(np.sum((x-np.average(x))**2)/(len(x) - 1))
    t = (np.average(x) - mu0)/(s/np.sqrt(len(x)))
    return t
    # pass