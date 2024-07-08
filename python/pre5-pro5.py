def count(s):
    words = s.split()
    return len(words)

s = input("Enter a sentence: ")
print(f'number of words in the sentence is: {count(s)}')
