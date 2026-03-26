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
