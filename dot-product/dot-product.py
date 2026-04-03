import numpy as np

def dot_product(x, y):
    x = np.array(x)
    y = np.array(y)
    return np.dot(x, y)

    x = [1, 2, 3]
    y = [4, 5, 6]
    print(dot_product(x, y))