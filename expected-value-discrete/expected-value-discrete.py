import numpy as np

def expected_value_discrete(x, p):
    x = np.array(x)
    p = np.array(p)
    
    if x.shape != p.shape:
        raise ValueError("x and p must have same length")
    
    if not np.allclose(np.sum(p), 1, atol=1e-6):
        raise ValueError("Probabilities must sum to 1")
    
    return float(np.sum(x * p))

x = [1, 2, 3]
p = [0.2, 0.5, 0.3]

print(expected_value_discrete(x, p))
