def unique(strings):
    common = set(strings[0])
    
    for s in strings[1:]:
        common &= set(s)
    
    return common

strings = ["good","morning","hello"]
result = unique(strings)
print(result)  
