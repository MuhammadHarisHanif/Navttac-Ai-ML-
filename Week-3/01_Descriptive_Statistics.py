

# NAVTTC AI/ML - Week 3
# Descriptive Statistics

import statistics

data = [10, 20, 20, 30, 40, 50]

# Example 1: Mean
print("Mean =", statistics.mean(data))

# Example 2: Median
print("Median =", statistics.median(data))

# Example 3: Mode
print("Mode =", statistics.mode(data))

# Example 4: Variance
print("Variance =", statistics.variance(data))

# Example 5: Standard Deviation
print("Standard Deviation =", statistics.stdev(data))

# Example 6: Minimum and Maximum
print("Minimum =", min(data))
print("Maximum =", max(data))

# Example 7: Range
print("Range =", max(data) - min(data))

# Example 8: Percentile using sorted data
sorted_data = sorted(data)
print("Sorted Data =", sorted_data)

# Example 9: Correlation coefficient
# Two variables with a positive relationship
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

correlation = statistics.correlation(x, y)
print("Correlation =", correlation)
