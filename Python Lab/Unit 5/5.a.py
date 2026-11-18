"""
Program 5(a) - Lab Exercise 1 – Bank account system using OOP
Source: Python Lab Report
"""

# Lab Exercise 1: Bank account system using OOP

class BankAccount:
    def __init__(self, holder, balance=0):    # constructor
        self.holder = holder
        self.__balance = balance                # private (encapsulated)

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount.")
        else:
            self.__balance += amount
            print(f"Deposited {amount:.2f}. New balance: "
                  f"{self.__balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount:.2f}. Balance: {self.__balance:.2f}")

    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):              # inheritance
    def __init__(self, holder, balance=0, rate=4):
        super().__init__(holder, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.get_balance() * self.rate / 100
        print(f"Interest at {self.rate}%: {interest:.2f}")
        self.deposit(interest)

name = input("Account holder name: ")
opening = float(input("Opening balance: "))
account = SavingsAccount(name, opening)
account.deposit(float(input("Amount to deposit: ")))
account.withdraw(float(input("Amount to withdraw: ")))
account.add_interest()
print(f"Final balance of {account.holder}: {account.get_balance():.2f}")
