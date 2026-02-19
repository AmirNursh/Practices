# return_values.py

# Function that returns a value
def multiply(a, b):
    return a * b

# Function returning multiple values
def calculate(a, b):
    return a + b, a - b

result = multiply(4, 5)
print("Multiplication:", result)

sum_result, diff_result = calculate(10, 3)
print("Sum:", sum_result)
print("Difference:", diff_result)
