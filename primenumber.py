def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Calculate factorial of a number."""
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Input from user
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"Factorial of {num} is {factorial(num)}")
else:
    print(f"{num} is not a prime number.")
