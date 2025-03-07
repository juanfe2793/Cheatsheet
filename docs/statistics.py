from scipy.stats import ttest_rel

# Define the two sets of data
data1 = [99.57, 99.79, 99.86, 99.60]
data2 = [99.94, 99.49, 99.94, 99.98]

# Perform the paired t-test
t_stat, p_value = ttest_rel(data1, data2)

# Print the results
print("T-statistic: %s" % t_stat)
print("P-value: %s" % p_value)
