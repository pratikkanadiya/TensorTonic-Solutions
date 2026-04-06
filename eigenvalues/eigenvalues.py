import numpy as np

def calculate_eigenvalues(matrix):
    try:
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                return None
                
        x = np.array(matrix)
        if x.shape[0] == x.shape[1]:
            eigvals = np.linalg.eigvals(x)
            real_part = eigvals.real
            imag_part = eigvals.imag
            indices = np.lexsort((imag_part, real_part))
            return eigvals[indices]
        else:
            return None
    except Exception as e:
        return None


a = [[4, 1], [2, 3]]
print(calculate_eigenvalues(a))