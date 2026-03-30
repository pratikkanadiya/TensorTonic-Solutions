import numpy as np

def bootstrap_mean(x, n_bootstrap=1000, ci=0.95, rng=None):
    x = np.array(x)
    N = len(x)
    
    if rng is None:
        rng = np.random.default_rng()
        
    indices = rng.integers(0, N, size=(n_bootstrap, N))
    samples = x[indices]
    boot_means = samples.mean(axis=1)
    
    alpha = (1 - ci) / 2
    lower = np.quantile(boot_means, alpha)
    upper = np.quantile(boot_means, 1 - alpha)
    
    return boot_means, lower, upper


x = [1, 2, 3, 4]
rng = np.random.default_rng(42)

print(bootstrap_mean(x, 1000, 0.9, rng))