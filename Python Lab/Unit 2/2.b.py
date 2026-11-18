"""
Program 2(b) - Lab Exercise 2 – Prime number and factorial programs
Source: Python Lab Report
"""

# Lab Exercise 2: Prime number and factorial programs

def is_prime(n):
    """Return True if n is a prime number."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Return n! using a loop."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Prime check
num = int(input("Enter a number to check prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# Prime numbers in a range
limit = int(input("Print prime numbers up to: "))
print("Prime numbers:", end=" ")
for n in range(2, limit + 1):
    if is_prime(n):
        print(n, end=" ")
print()

# Factorial
value = int(input("\nEnter a number to find factorial: "))
if value < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {value} = {factorial(value)}")
