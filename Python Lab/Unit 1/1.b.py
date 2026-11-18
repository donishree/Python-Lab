"""
Program 1(b) - Lab Exercise 2 – Variables, operators, input/output
Source: Python Lab Report
"""

# Lab Exercise 2: Variables, operators and input/output

name = input("Enter your name: ")
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print(f"\nHello, {name}!")

# Arithmetic operators
print(f"Addition        : {a} + {b} = {a + b}")
print(f"Subtraction     : {a} - {b} = {a - b}")
print(f"Multiplication  : {a} * {b} = {a * b}")
div = a / b if b != 0 else 'undefined'
print(f"Division        : {a} / {b} = {div}")
floor = a // b if b != 0 else 'undefined'
print(f"Floor division  : {a} // {b} = {floor}")
print(f"Modulus         : {a} % {b} = {a % b if b != 0 else 'undefined'}")
print(f"Power           : {a} ** {b} = {a ** b}")

# Relational and logical operators
print("a > b  :", a > b)
print("a == b :", a == b)
print("Both a and b positive:", a > 0 and b > 0)

# Assignment operator and type()
a += 10
print("After a += 10, a =", a)
print("Type of a:", type(a), "| Type of name:", type(name))
