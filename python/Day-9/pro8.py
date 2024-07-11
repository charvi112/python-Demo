class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")

if __name__ == "__main__":

    person1 = Person("meet", 20, "Ahmedabad")
    person2 = Person("riya", 25, "surat")

    person1.display()
    person2.display()
