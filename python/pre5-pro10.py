def union(list1, list2):
    return list(set(list1) | set(list2))

list1 = [1,4,7,8,9]
list2 = [4,7,6,2,1]
result = union(list1, list2)
print(result)
