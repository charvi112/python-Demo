import numpy as np

data = [3,5,8,4,6,1,9]

array = np.array(data)

mean = np.mean(array)
print(f"Mean: {mean}")

median = np.median(array)
print(f"Median: {median}")

std_dev = np.std(array)
print(f"Standard Deviation: {std_dev}")