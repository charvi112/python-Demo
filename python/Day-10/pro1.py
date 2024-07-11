class Animal:
    def sound(self):
        return ""

class Dog(Animal):
    def sound(self):
        return "Bark!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog()
cat = Cat()

print("Dog says:", dog.sound())
print("Cat says:", cat.sound())
