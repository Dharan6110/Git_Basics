# a = int(input("Enter a Value :______"))
# b = int(input("Enter a Value :______"))

# c = a**b

# print(f"The value of {a}**{b} is", c)

# def fibonacci(n):
#     fib_series = [0, 1]
#     while len(fib_series) < n:
#         fib_series.append(fib_series[-1] + fib_series[-2])
#     return fib_series

# # Example: Generate the first 10 Fibonacci numbers
# n = 10
# result = fibonacci(n)
# print(f"Fibonacci series of first {n} numbers: {result}")

def sum_arrays(array1, array2):
    result = []
    for element1, element2 in zip(array1, array2):
        result.append(element1 + element2)
    return result

# Example: Sum of two arrays
array1 = [1, 2, 3, 4]
array2 = [5, 6, 7, 8]

result = sum_arrays(array1, array2)
print(f"Sum of arrays: {result}")

