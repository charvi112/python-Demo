import numpy as np
def sort(numbers):
    np_array = np.array(numbers)
    sorted_array = np.sort(np_array)
    return sorted_array

numbers = [4,6,9,2,7,25,17]
sorted_numbers = sort(numbers)
print(sorted_numbers)