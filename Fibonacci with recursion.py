def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
num = int(input("Enter a positive integer to get the Fibonacci number at that position: "))
result = fibonacci(num)
print(f"The Fibonacci number at position {num} is: {result}")
# This code defines a recursive function to compute the Fibonacci number at a given position.


def fibonacci_sequence(n):
    sequence = []
    for i in range(1, n + 1):
        sequence.append(fibonacci(i))
    return sequence 
num = int(input("Enter a positive integer to get the Fibonacci sequence up to that position: "))
result = fibonacci_sequence(num)
print(f"The Fibonacci sequence up to position {num} is: {result}")
# This code generates the Fibonacci sequence up to the nth position using the recursive fibonacci function.
