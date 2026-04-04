import numpy as np

def euclidean_distance(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    
    if x.shape != y.shape:
        raise ValueError(f"Shape mismatch: {x.shape} vs {y.shape}")
    
    return float(np.sqrt(np.sum((x - y) ** 2)))

x = [3, 4]
y = [0, 0]
print(euclidean_distance(x, y))
