# scale numeric features using min-max scaling.
import numpy as np
def min_max_scaling(data):
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    scaled_data = (data - min_val) / (max_val - min_val)
    return scaled_data

data = np.array([[45, 78, 95],
                  [67, 80, 32],
                  [54, 99, 83]])

scaled_data = min_max_scaling(data)
print("Original data:")
print(data)

print("\nScaled data:")
print(scaled_data)
