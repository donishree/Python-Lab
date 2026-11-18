"""
Program 2(a) - Lab Exercise 1 – Number guessing game
Source: Python Lab Report
"""

# Lab Exercise 1: Number guessing game
import random

secret = random.randint(1, 100)   # computer picks a number
max_attempts = 7
attempts = 0

print("===== NUMBER GUESSING GAME =====")
print(f"Guess a number between 1 and 100 ({max_attempts} attempts).")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret:
        print(f"Congratulations! Guessed in {attempts} attempt(s).")
        break
    elif guess < secret:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

    print(f"Attempts left: {max_attempts - attempts}")
else:
    # runs only when the loop ends without 'break'
    print(f"Game over! The secret number was {secret}.")
