# super_function.py

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}")

class Student(Person):
    def __init__(self, name, grade):
        # Call parent constructor using super()
        super().__init__(name)
        self.grade = grade

    def introduce(self):
        # Call parent method
        super().introduce()
        print(f"I am in grade {self.grade}")

student1 = Student("Alice", 10)
student1.introduce()
