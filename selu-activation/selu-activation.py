import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """

    x = np.asarray(x, dtype=np.float64)
    # x[pos_mask] = lam * x[pos_mask]
    # x[neg_mask] = lam * alpha * (np.exp(x[neg_mask]) - 1)
    # np.where
    return np.round(lam * np.where(x > 0, x, alpha * (np.exp(x) - 1)), 4).tolist()
