import numpy as np

def sample_var_std(x):
    x = np.array(x)
    n = len(x)
    mean = np.mean(x)
    var = np.sum((x - mean) ** 2) / (n - 1)
    std = np.sqrt(var)
    return var, std

x = [1, 2, 3]