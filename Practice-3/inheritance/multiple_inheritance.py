# multiple_inheritance.py

class Father:
    def skills(self):
        print("Gardening, Carpentry")

class Mother:
    def skills(self):
        print("Cooking, Painting")

# Child inherits from both parents
class Child(Father, Mother):
    def show_skills(self):
        print("Child inherits:")
        Father.skills(self)
        Mother.skills(self)

child1 = Child()
child1.show_skills()
