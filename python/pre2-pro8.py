def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for char in s:
        if char.lower() in vowels: 
            count += 1

    return count

string = input("Enter a string: ") 
num_vowels = count_vowels(string)
print(f"Number of vowels in the string: {num_vowels}")
