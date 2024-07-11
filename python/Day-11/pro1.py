import numpy as np

my_list = [3,6,2,7,5]

my_array = np.array(my_list)
add_result = my_array + 5
print("Addition Result:", add_result)

mul_result = my_array * 2
print("Multiplication Result:", mul_result)

square_result = np.square(my_array)
print("Square Result:", square_result)
