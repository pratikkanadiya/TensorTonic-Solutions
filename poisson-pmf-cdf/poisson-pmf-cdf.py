import numpy as np

def poisson_pmf_cdf(lam, k):
    if k == 0:
        log_fact_k = 0
    else:
        log_fact_k = np.sum(np.log(np.arange(1, k + 1)))
        
    x = (-lam) + k * np.log(lam) - log_fact_k
    pmf = np.exp(x)

    cdf = 0
    for i in range(0, k + 1):
        if i == 0:
            log_fact_i = 0
        else:
            log_fact_i = np.sum(np.log(np.arange(1, i + 1)))
        
        y = (-lam) + i * np.log(lam) - log_fact_i 
        cdf += np.exp(y)


    return pmf, cdf

lam = 3
k = 2
print(poisson_pmf_cdf(lam, k)) 