import numpy as np

def chi2_independence(C):
    c = np.array(C)
    sr = np.sum(c, axis = 1)
    sc = np.sum(c, axis = 0)
    total = np.sum(c)
    e = np.outer(sr, sc)
    expected = e / total
    chi2 = np.sum((c - expected) ** 2 / expected)
    return chi2, expected

c = [[10, 20], [20, 10]]
print(chi2_independence(c))