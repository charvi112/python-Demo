def find(list1, list2):
    common_elements = []
    for item in list1:
        if item in list2 and item not in common_elements:
            common_elements.append(item)
    return common_elements

list1 = [2,4,7,8,3]
list2 = [1,5,8,3,9]
common_elements = find(list1, list2)
print(common_elements)  
