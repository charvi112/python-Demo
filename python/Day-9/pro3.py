class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

name = input("Enter the student's name: ")
age = int(input("Enter the student's age: "))
grades = input("Enter the student's grades:")


student1 = Student(name, age, grades)

student1.display_info()
