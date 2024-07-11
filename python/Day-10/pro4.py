class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

class Engineer(Employee):
    def __init__(self, name, salary, field):
        super().__init__(name, salary)
        self.field = field

manager = Manager("Raj", 10000, "HR")
engineer = Engineer("chirag", 25000, "Software")

print("Manager:", manager.name, manager.salary, manager.department) 
print("Engineer:", engineer.name, engineer.salary, engineer.field) 
