def frequent(lst):

    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    

    max_freq = max(frequency.values())
    

    most_frequent = [key for key, value in frequency.items() if value == max_freq]
    
    return most_frequent

lst = [2,5,4,3,4,5,7,7,7,1,2,2]
print(frequent(lst))  