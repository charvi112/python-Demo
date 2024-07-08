def sum_of_positive_numbers(numbers):
    return sum(number for number in numbers if number > 0)

numbers = [45, -2, 3, 67, -5, 6]

sum_positive = sum_of_positive_numbers(numbers)
print(f"The sum of all positive numbers is: {sum_positive}")
