def set(set1, set2):
    union = set1 | set2 
    intersection = set1 & set2  
    difference = set1 - set2  
    
    return union, intersection, difference

set1 = {6,3,9,2,5}
set2 = {3,5,2,1,7}

union, intersection, difference = set(set1, set2)

print("Union:", union)  
print("Intersection:", intersection)  
print("Difference:", difference) 
