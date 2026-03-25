import numpy as np
from collections import Counter

def mean_median_mode(x):
    x = np.array(x)
    m1 = np.mean(x)
    m2 = np.median(x)
    c = Counter(x)
    max_fre = max(c.values())
    lst = [num for num, value in c.items() if value == max_fre]
    return m1, m2, min(lst)

x = [1, 2, 3, 4, 5]
print(mean_median_mode(x))