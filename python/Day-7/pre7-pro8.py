def average(dicts, key):
    total = sum(d[key] for d in dicts)
    count = len(dicts)
    return total / count

items = [
    {'name': 'item1', 'value': 24},
    {'name': 'item2', 'value': 40},
    {'name': 'item3', 'value': 65}
]

average = average(items, 'value')
print("The average value is:", average) 
