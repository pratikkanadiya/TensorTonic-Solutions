import numpy as np

def matrix_transpose(A):
    arr = np.array(A)

    row, col = arr.shape
    transpose = np.zeros((col, row), dtype = int)
    for i in range(row):
        for j in range(col):
            transpose[j][i] = arr[i][j]

    return transpose    
            
y = [[1, 2, 3], [4, 5, 6]]
print(matrix_transpose(y))