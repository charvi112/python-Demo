def sum_positive(numbers):
    return sum(number for number in numbers if number > 0)

numbers = [6, -4, 32, 13, -8, 23,0,34,19]
result = sum_positive(numbers)
print(f"The sum of all positive numbers is: {result}")
