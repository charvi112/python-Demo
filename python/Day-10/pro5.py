class Animal:
    def __init__(self, name):
        self.name = name

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

class Fish(Animal):
    def __init__(self, name):
        super().__init__(name)

bird = Bird("Peacock")
fish = Fish("Goldfish")

print(f"Bird name: {bird.name}") 
print(f"Fish name: {fish.name}") 
