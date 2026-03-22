#What Are Percentiles?

  A percentile indicates the relative standing of a value within a dataset.

  The pth percentile is a value below which p percent of the data falls.

Example: 

  If your test score is at the 90th percentile, you scored higher than 90% of test-takers.

  Percentiles are used to understand distributions, identify outliers, and compare values across different scales.

#Formal Definition :

  The pth percentile (where 0 <= p <= 100) is a value xp such that :

   --> at least p% of the data is <= xp
 
   --> at least (100 - p)% of the data is >= xp

   Note: Different methods exist for computing percentiles, especially when the percentile falls between data points.

#Computing Percentiles: Basic Method

Step 1: Sort the data in ascending order

Step 2: Calculate the rank position:
                L = (P / 100) * (N + 1)
                
  where p is the percentile and n is the sample size.

Step 3:

  If L is an integer, the percentile is the value at position L

  If L is not an integer, interpolate between adjacent values
