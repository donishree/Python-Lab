"""
Program 5(c) - Lab Exercise 3 – Dice simulator using random module
Source: Python Lab Report
"""

# Lab Exercise 3: Dice simulator using random module
import random
import numpy as np

print("========== DICE SIMULATOR ==========")
dice_count = int(input("Number of dice to roll each time: "))
rolls = int(input("Number of rolls: "))

totals = []
for i in range(1, rolls + 1):
    throw = [random.randint(1, 6) for _ in range(dice_count)]
    totals.append(sum(throw))
    print(f"Roll {i}: {throw} -> total = {sum(throw)}")

# Frequency of each total using a dictionary
frequency = {}
for t in totals:
    frequency[t] = frequency.get(t, 0) + 1

print("\nFrequency of totals:")
for value in sorted(frequency):
    print(f"  {value:>2} : {'*' * frequency[value]} ({frequency[value]})")

# NumPy gives quick statistics on the results
results = np.array(totals)
print(f"\nAverage total : {results.mean():.2f}")
print(f"Highest total : {results.max()}")
print(f"Lowest total  : {results.min()}")
