#One-Sample t-Test

Given a sample x and a hypothesized population mean μ₀, compute the one-sample t-statistic.


One-Sample t-Statistic :

  
    t = (x̄ - mu0) / (s / sqrt(n))
    Where: x̄ = sample mean, s = sample standard deviation, n = sample size


Sample standard deviation (Bessel correction):


    s = sqrt(sum((x - mean) ** 2) / (n - 1))


Function Arguments :
    
    x: list or array - Sample observations
    mu0: float - Null hypothesis mean (μ₀)


Requirements :
    
    Return scalar float (t-statistic)
    Must convert x to NumPy array
    Use Bessel correction (n-1 denominator)
    No external statistics libraries
