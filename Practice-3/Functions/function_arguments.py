# function_arguments.py

# Function with positional arguments
def add_numbers(a, b):
    print(f"Sum: {a + b}")

# Function with default argument
def power(base, exponent=2):
    print(f"Result: {base ** exponent}")

add_numbers(5, 3)
power(4)        # Uses default exponent
power(4, 3)     # Overrides default
