"""
Program 2(c) - Lab Exercise 3 – Fibonacci series using recursion
Source: Python Lab Report
"""

# Lab Exercise 3: Fibonacci series using recursion

def fibonacci(n):
    """Return the n-th Fibonacci number (0, 1, 1, 2, 3, 5, ...)."""
    if n <= 1:                 # base cases: fib(0) = 0, fib(1) = 1
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)   # recursive case

terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive integer.")
else:
    print(f"Fibonacci series with {terms} term(s):")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()

    # lambda function to find the sum of the series
    series_sum = lambda count: sum(fibonacci(i) for i in range(count))
    print("Sum of the series =", series_sum(terms))
