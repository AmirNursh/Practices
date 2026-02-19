# inheritance_basics.py

# Parent class
class Animal:
    def speak(self):
        print("Animal makes a sound")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog1 = Dog()
dog1.speak()  # Inherited method
dog1.bark()   # Child method
