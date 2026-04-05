import numpy as np

def matrix_trace(A):
    A = np.array(A)
    if(A.shape[0] == A.shape[1]):
        trace = 0
        for i in range(A.shape[0]):
            trace += A[i][i]

    return trace
x = [[1, 2], [3, 4]]
print(matrix_trace(x))