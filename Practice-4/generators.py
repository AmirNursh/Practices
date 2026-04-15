# generators.py

# ---------- ITERATOR EXAMPLE ----------

class CountToN:
    # Constructor receives the maximum number
    def __init__(self, n):
        self.n = n  # store the limit

    # __iter__ initializes the iterator
    def __iter__(self):
        self.current = 1  # start counting from 1
        return self

    # __next__ returns the next value in iteration
    def __next__(self):
        if self.current <= self.n:  # check if we reached the limit
            num = self.current      # store current value
            self.current += 1       # increment counter
            return num              # return the value
        else:
            # stop iteration when limit is reached
            raise StopIteration


# ---------- GENERATOR FUNCTION EXAMPLE ----------

def fibonacci(limit):
    # Initial values of Fibonacci sequence
    a, b = 0, 1
    
    # Generate numbers until the limit is reached
    while a <= limit:
        yield a           # yield returns value and pauses function execution
        a, b = b, a + b   # update values


# ---------- GENERATOR EXPRESSION EXAMPLE ----------

# Generator expression that creates squares of numbers from 0 to 9
squares = (x * x for x in range(10))


# ---------- TEST RUN ----------

if __name__ == "__main__":
    print("Iterator example:")
    
    # Create iterator object
    counter = CountToN(5)
    
    # Loop through iterator
    for num in counter:
        print(num)

    print("\nFibonacci generator:")
    
    # Use generator function
    for num in fibonacci(50):
        print(num)

    print("\nGenerator expression (squares):")
    
    # Iterate through generator expression
    for num in squares:
        print(num)
