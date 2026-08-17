def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    i = 0
    
    while i < steps:
        df = 2*a*x0+b
        x0 = x0-lr*df
        i = i + 1
    return x0
    # pass