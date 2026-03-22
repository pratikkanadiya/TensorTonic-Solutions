import numpy as np

def percentiles(x, q):
    x = np.array(x)
    q = np.array(q)
    return np.percentile(x, q, method='linear')
    
x = [1, 2, 3, 4]
q = [25, 50, 75]

print(percentiles(x, q))
    