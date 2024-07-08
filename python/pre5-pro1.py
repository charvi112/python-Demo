def palindrome(s):
    s=s.replace(" "," ").lower()
    return s==s[::-1]

test_string = "good morning ,how are you?"
if palindrome(test_string):
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')
