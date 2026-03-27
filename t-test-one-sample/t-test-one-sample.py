import numpy as np

def t_test_one_sample(x, mu0):
    x = np.array(x)
    m = np.mean(x)
    n = len(x)
    std = np.sqrt(np.sum((x - m) ** 2) / (n - 1))
    t = (m - mu0) / (std / np.sqrt(n))
    return t
    
x = [2.1,2.4,1.9,2.6,2]
mu0 = 2

print(t_test_one_sample(x, mu0))