import numpy as np

def robust_scaling(values):
    y = np.sort(np.array(values))

    def find_median(arr):
        n = len(arr)
        if n == 0:
            return 0
        elif n % 2 != 0:
            return arr[n // 2]
        else:
            return (arr[n // 2] + arr[n // 2 - 1]) / 2

    # Median
    median = find_median(y)

    # Split data
    n = len(y)
    if n % 2 != 0:
        lower = y[:n // 2]
        upper = y[n // 2 + 1:]
    else:
        lower = y[:n // 2]
        upper = y[n // 2:]

    # Quartiles
    Q1 = find_median(lower)
    Q3 = find_median(upper)

    # IQR
    IQR = Q3 - Q1 or 1

    # Apply scaling to ORIGINAL order
    y2 = np.array(values)

    return list((y2 - median) / IQR)


# Test
x = [5, 1, 3, 2, 4]
print(robust_scaling(x))