# class_variables.py

class Employee:
    company_name = "TechCorp"  # Class variable

    def __init__(self, name):
        self.name = name

emp1 = Employee("Alice")
emp2 = Employee("Bob")

print(emp1.name, "works at", emp1.company_name)
print(emp2.name, "works at", emp2.company_name)
