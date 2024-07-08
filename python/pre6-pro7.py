words = ["apple", "banana", "orange", "mango"]

longest_word = ""
max_length = 0

for word in words:
    if len(word) > max_length:
        longest_word = word
        max_length = len(word)

print(f"Longest word: {longest_word}, Length: {max_length}")
