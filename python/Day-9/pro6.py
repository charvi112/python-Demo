class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_details(self):
        print(f"Car make: {self.make}")
        print(f"Car model: {self.model}")
        print(f"Car year: {self.year}")

my_car = Car("Honda", "City", 2024)
my_car.display_details()
