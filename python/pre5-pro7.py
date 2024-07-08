def vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

# Test the function
test_string = "Hello, good morning how are you?"
result = vowels(test_string)
print(result)
