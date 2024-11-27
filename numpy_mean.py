import numpy as np 
# Given dataset for basic statistical calculations 
data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]) 
# Calculate mean, median, and standard deviation 
mean_value = np.mean(data) 
median_value = np.median(data) 
std_deviation = np.std(data) 
print("Mean:", mean_value) 
print("Median:", median_value) 
print("Standard Deviation:", std_deviation) 
# Two sets of data for correlation coefficient calculation 
data_set_1 = np.array([1, 2, 3, 4, 5]) 
data_set_2 = np.array([10, 20, 30, 40, 50]) 
# Compute correlation coefficient 
correlation_coefficient = np.corrcoef(data_set_1, data_set_2)[0, 1] 
print("Correlation Coefficient:", correlation_coefficient) 