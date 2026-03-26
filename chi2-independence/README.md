#Chi-Square Test

Given an r×c contingency table C, compute the chi-square test statistic and expected frequency table for testing independence.


Chi-Square Test for Independence:


Test Statistic    :    chi2 = sum((O - E)^2 / E)


Expected Frequencies    :    E = rowi * coli / total


Requirements :
    
    Return tuple: (chi2, expected)
    chi2: scalar float
    expected: NumPy array (same shape as C)
    Vectorized computation (no nested loops)

Code : 

  use np.sum(arr, axis = 1/0) sum od arr row and col wise and find total

  np.outer() : 
      The outer product takes two 1D arrays (vectors) and produces a matrix where:
      Each element is the product of one element from the first array and one from the second.
