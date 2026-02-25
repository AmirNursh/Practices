# math.py

# Import modules
import math      # mathematical functions
import random    # random number generation

numbers = [4, -7, 15, 2.7]

# ---------- Built-in Functions ----------

# Find minimum value
print("Min:", min(numbers))

# Find maximum value
print("Max:", max(numbers))

# Get absolute value
print("Absolute value of -7:", abs(-7))

# Round number
print("Rounded 2.7:", round(2.7))

# Power function
print("2 power 3:", pow(2, 3))


# ---------- math Module Functions ----------

# Square root
print("Square root of 16:", math.sqrt(16))

# Round up
print("Ceil 4.3:", math.ceil(4.3))

# Round down
print("Floor 4.9:", math.floor(4.9))

# Trigonometric function
print("Sin(pi/2):", math.sin(math.pi / 2))

# Mathematical constants
print("PI:", math.pi)
print("E:", math.e)


# ---------- random Module ----------

# Random float between 0 and 1
print("Random float:", random.random())

# Random integer between 1 and 10
print("Random integer 1-10:", random.randint(1, 10))

# Random element from list
print("Random choice:", random.choice(numbers))

# Shuffle list randomly
random.shuffle(numbers)
print("Shuffled list:", numbers)
