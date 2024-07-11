import csv
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def display_info(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")

def read_employees_from_csv(file_path):
    employees = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader) 
        for row in csv_reader:
            employee = Employee(row[0], row[1], row[2])
            employees.append(employee)
    return employees

file_path = 'C:\python\Day-9\employee.csv'  

employees = read_employees_from_csv(file_path)
for emp in employees:
    emp.display_info()
