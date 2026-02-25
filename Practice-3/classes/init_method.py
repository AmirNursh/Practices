# init_method.py

class Car:
    def __init__(self, brand, year):
        # Constructor method
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"Car: {self.brand}, Year: {self.year}")

car1 = Car("Toyota", 2022)
car1.display_info()
