#Sample Variance & Standard Deviation

Compute unbiased sample variance and standard deviation using Bessel's correction.


Formula :

    var = sum[(x - mean)] / (n - 1)
    std = sqrt(var)


Requirements :


    Return tuple: (var, std)
    Both values: scalar floats
    Use Bessel correction (divide by n-1)
    Vectorized implementation
