from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map
squared = list(map(lambda x: x**2, numbers))
print("Squared:", squared)

# filter
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even:", even)

# reduce
total = reduce(lambda x, y: x + y, numbers)
print("Sum:", total)

# Other built-in functions
print("Length:", len(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sum:", sum(numbers))