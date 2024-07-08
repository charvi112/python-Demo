def vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


test_string = "Hello, good morning how are you?"
print(f'number of vowels in "{test_string}" is {vowels(test_string)}.')

