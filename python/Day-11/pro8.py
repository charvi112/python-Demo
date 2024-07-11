import numpy as np

list_of_lists = [
    [2,4,6],
    [3,7,8],
    [1,5,9]
]

array_2d = np.array(list_of_lists)
row_sums = np.sum(array_2d, axis=1)
column_sums = np.sum(array_2d, axis=0)

print("2D Array:")
print(array_2d)
print("Sum of elements in each row:", row_sums)
print("Sum of elements in each column:", column_sums)