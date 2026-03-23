import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    q = 1 - p
    pmf = comb(n, k) * np.pow(p, k) * np.pow(q, n - k)
    cdf = 0
    for i in range(0, k + 1):
        c1 = comb(n, i) * np.pow(p, i) * np.pow(q, n - i)
        cdf += c1

    return pmf, cdf
        

n = 5
p = 0.5
k = 2
cdf, pmf = binomial_pmf_cdf(n, p, k)
print(f"CDF : {cdf}")
print(f"PMF : {pmf}")