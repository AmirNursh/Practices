# method_overriding.py

class Shape:
    def area(self):
        print("Area calculation not defined")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Method overriding
    def area(self):
        return self.width * self.height

rect = Rectangle(5, 4)
print("Rectangle Area:", rect.area())
