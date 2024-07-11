import numpy as np

array = np.random.randint(1, 100, size=5)  

mean_value = np.mean(array)
median_value = np.median(array)
std_deviation = np.std(array)

print("Random Array:", array)
print("Mean:", mean_value)
print("Median:", median_value)
print("Standard Deviation:", std_deviation)
