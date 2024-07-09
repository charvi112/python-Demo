def common(set1, set2):
    return bool(set1 & set2)

set1 = {3,6,9,4}
set2 = {6,5,4}

if common(set1, set2):
    print("The sets have common elements.")
else:
    print("The sets do not have any common elements.")
