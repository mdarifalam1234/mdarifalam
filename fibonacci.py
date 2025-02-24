def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
num = 7
print(f"The {num}th Fibonacci number is {fibonacci(num)}")