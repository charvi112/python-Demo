import csv

csv_file = 'C:\python\Day-8\data.csv'

data = []

with open(csv_file, 'r', newline='') as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        print(f"Name: {row[0]}, Age: {row[1]}, City: {row[2]}")
        data.append(row)
