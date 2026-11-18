"""
Program 1(a) - Lab Exercise 1 – Basic Python program
Source: Python Lab Report
"""

# Lab Exercise 1: Basic Python program
# Demonstrates print(), comments, variables, data types and indentation

print("Hello, World!")
print("Welcome to Python Programming Lab")

# Variables and data types
name = "Python"         # string
version = 3.12          # float
year_released = 1991    # integer
is_popular = True       # boolean

print("Language      :", name)
print("Version       :", version)
print("Released in   :", year_released)
print("Is it popular?", is_popular)

# type() shows the data type of each variable
print(type(name), type(version), type(year_released), type(is_popular))

# Indentation defines a block of code
for i in range(1, 4):
    print("This is line number", i)
