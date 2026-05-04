# lambda_with_map.py

numbers = [1, 2, 3, 4, 5]

# Using map with lambda to square numbers
squared = list(map(lambda x: x * x, numbers))

print("Original:", numbers)
print("Squared:", squared)
