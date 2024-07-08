def pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    s = s.lower()
    return alphabet <= set(s)

test_string = "hello world"
if pangram(test_string):
    print(f'"{test_string}" is a pangram.')
else:
    print(f'"{test_string}" is not a pangram.')
