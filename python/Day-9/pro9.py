class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2  

    def circumference(self):
        return 2 * 3.14 * self.radius  

radius = 8
circle = Circle(radius)

print(f"Radius of the circle: {circle.radius}")
print(f"Area of the circle: {circle.area():.2f}")
print(f"Circumference of the circle: {circle.circumference():.2f}")
