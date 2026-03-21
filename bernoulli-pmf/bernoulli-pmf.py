import numpy as np

def bernoulli_pmf_and_moments(x, p):
    x = np.array(x)
    q = 1 - p
    result = np.where(x == 1, p, q)
    return result, p, p*q

x = [0, 1, 1]
p = 0.3
pmf, mean, var = bernoulli_pmf_and_moments(x, p)
print(f"PMF : {pmf}")
print(f"Mean : {mean}")
print(f"variance : {var}")