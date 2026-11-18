"""
Program 2(d) - Mini Project – OTP Generator
Source: Python Lab Report
"""

# Mini Project: OTP Generator and Verifier
import random

# lambda function that builds an n-digit OTP
generate_otp = lambda n=6: "".join(str(random.randint(0, 9))
                                    for _ in range(n))

def mask_number(phone):
    """Hide the middle digits of a mobile number."""
    return phone[:2] + "*" * (len(phone) - 4) + phone[-2:]

def verify_otp(otp, max_attempts=3):
    """Give the user a limited number of attempts to enter the OTP."""
    for attempt in range(1, max_attempts + 1):
        entered = input(f"Enter OTP (attempt {attempt}/{max_attempts}): ")
        if entered == otp:
            return True
        print("Incorrect OTP.")
    return False

phone = input("Enter your 10-digit mobile number: ")
if len(phone) != 10 or not phone.isdigit():
    print("Invalid mobile number.")
else:
    otp = generate_otp(6)
    print(f"OTP sent to {mask_number(phone)}")
    print(f"(Demo only - your OTP is {otp})")

    if verify_otp(otp):
        print("OTP verified successfully. Login granted!")
    else:
        print("Too many wrong attempts. Account temporarily locked.")
