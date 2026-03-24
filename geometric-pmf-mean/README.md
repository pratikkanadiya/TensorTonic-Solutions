#Geometric Probability Mass Function & Mean


Compute the Probability Mass Function (PMF) and Mean of a Geometric distribution.
The Geometric distribution models the number of trials $k$ needed to get the first success in repeated Bernoulli trials with probability of success $p$.


P(K = x) = (1 - p)^k-1 * p for k = 1, 2, 3 ...


mean = 1/p


Function Arguments :


k: list or array - Number of trials integers (k ≥ 1)


p: float - Probability of success (0 < p ≤ 1)


Examples


Input: k = [1, 2, 3] p = 0.5


Output: (array([0.5, 0.25, 0.125]), 2.0)
