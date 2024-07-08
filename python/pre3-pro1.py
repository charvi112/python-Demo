def check_number(number):
    if number > 0:
        return "The number is positive."
    elif number < 0:
        return "The number is negative."
    else:
        return "The number is zero."

number = float(input("Enter a number: "))
result = check_number(number)
print(result)
