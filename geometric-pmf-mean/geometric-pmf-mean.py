import numpy as np

def geometric_pmf_mean(k, p):
    k = np.array(k)
    pmf = np.pow(1 - p, k - 1) * p 
    mean = 1 / p
    return pmf, mean
    

k = [1, 2, 3]
p = 0.2
print(geometric_pmf_mean(k, p))