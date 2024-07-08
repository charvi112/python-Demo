def intersection(list1, list2):
    return list(set(list1) & set(list2))

words1 = ["aman", "meet", "tirth", "binal", "chiya", "veer", "rivi"]
words2 = ["meet", "binal", "veer", "rahul"]

intersection_words = intersection(words1, words2)
print(intersection_words)