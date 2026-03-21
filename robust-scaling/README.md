#Robust Scaling

Robust scaling normalizes features using statistics that are robust to outliers: the median and the interquartile range (IQR). 
Unlike standard scaling (which uses mean and standard deviation), a single extreme outlier does not distort the scaling. 
This makes robust scaling the preferred normalization method when data contains outliers that should not influence the scale.

Given a list of values, scale each value using the formula below. 
If the IQR is zero, return (value - median) without dividing.

Formula : Xscaled = (X - median) / IQR 


#When to Use Robust Scaling

Good for:
Data with known or suspected outliers
Distributions with heavy tails
Real-world measurements prone to errors
When outlier removal is undesirable or infeasible

Less suitable for:
Clean data without outliers (standard scaling is simpler)
When exact [0, 1] range is required (use min-max)
Very small datasets where percentile estimates are unreliable
