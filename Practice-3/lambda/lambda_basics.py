# lambda_basics.py

# Regular function
def square(x):
    return x * x

# Lambda equivalent
square_lambda = lambda x: x * x

print("Regular function:", square(5))
print("Lambda function:", square_lambda(5))
