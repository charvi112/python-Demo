def Merge(dict1, dict2): 
    s = dict1 | dict2
    return s 
 
dict1 = {'x': 3, 'y': 5} 
dict2 = {'a': 7, 'b': 9} 
dict3 = Merge(dict1, dict2) 
print(dict3)

