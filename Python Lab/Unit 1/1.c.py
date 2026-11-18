"""
Program 1(c) - Lab Exercise 3 – Calculator and area calculation
Source: Python Lab Report
"""

# Lab Exercise 3: Simple calculator and area calculation
import math

print("===== SIMPLE CALCULATOR =====")
x = float(input("Enter first number : "))
y = float(input("Enter second number: "))
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")
print(f"{x} * {y} = {x * y}")
print(f"{x} / {y} = {x / y if y != 0 else 'Cannot divide by zero'}")
print(f"{x} % {y} = {x % y if y != 0 else 'Cannot divide by zero'}")
print(f"{x} ** {y} = {x ** y}")
print(f"Square root of {x} = {math.sqrt(x) if x >= 0 else 'undefined'}")

print("\n===== AREA CALCULATION =====")
radius = float(input("Enter radius of the circle: "))
length = float(input("Enter length of the rectangle: "))
breadth = float(input("Enter breadth of the rectangle: "))
base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))

print(f"Area of circle    = {math.pi * radius ** 2:.2f}")
print(f"Area of rectangle = {length * breadth:.2f}")
print(f"Area of triangle  = {0.5 * base * height:.2f}")
print(f"Area of square (side = length) = {length ** 2:.2f}")
