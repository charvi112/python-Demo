def count_words(sentence):
    words = sentence.split()  
    return len(words)         


sentence = input("Enter a sentence: ")  
word_count = count_words(sentence)  
print("The number of words in the sentence is:", word_count)  
