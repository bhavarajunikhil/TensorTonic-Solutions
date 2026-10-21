import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    output = {}
    x_2 = x - np.mean(x)
    output["variance"] = float(np.dot(x_2, x_2)/(len(x)-1))
    output["standard_deviation"] = float(np.sqrt(np.dot(x_2, x_2)/(len(x)-1)))
    return output
    # pass