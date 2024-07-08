def count(elements):
    occurrence = {}
    
    for element in elements:
        if element in occurrence:
            occurrence[element] += 1
        else:
            occurrence[element] = 1
            
    return occurrence


elements = [2,6,3,4,4,6,8,8,7]
occurrences = count(elements)
print(occurrences) 
