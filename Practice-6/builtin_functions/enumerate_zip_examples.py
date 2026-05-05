names = ["Amir", "Ali", "Aruzhan"]
scores = [90, 85, 95]

# enumerate
for index, name in enumerate(names):
    print(index, name)

# zip
for name, score in zip(names, scores):
    print(name, score)

# sorted
sorted_scores = sorted(scores)
print(sorted_scores)

# type checking
x = "123"
print(type(x))

# type conversion
number = int(x)
print(number)
print(type(number))