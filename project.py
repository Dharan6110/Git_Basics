# a = int(input("Enter a Value :______"))
# b = int(input("Enter a Value :______"))

# c = a**b

# print(f"The value of {a}**{b} is", c)

def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

# Example: Generate the first 10 Fibonacci numbers
n = 10
result = fibonacci(n)
print(f"Fibonacci series of first {n} numbers: {result}")
