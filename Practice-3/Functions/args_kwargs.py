# args_kwargs.py

# Using *args
def print_numbers(*args):
    for number in args:
        print("Number:", number)

# Using **kwargs
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_numbers(1, 2, 3, 4)

print_details(name="John", age=25, country="USA")
