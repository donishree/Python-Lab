"""
Program 1(d) - Mini Project – Unit Converter
Source: Python Lab Report
"""

# Mini Project: Unit Converter (length, temperature, weight, time)

print("========== UNIT CONVERTER ==========")

# Length: kilometres -> metres, centimetres, miles
km = float(input("Enter distance in kilometres: "))
print(f"{km} km = {km * 1000:.2f} m = {km * 100000:.2f} cm "
      f"= {km * 0.621371:.2f} miles")

# Temperature: Celsius -> Fahrenheit, Kelvin
celsius = float(input("\nEnter temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
print(f"{celsius} C = {fahrenheit:.2f} F = {kelvin:.2f} K")

# Weight: kilograms -> grams, pounds
kg = float(input("\nEnter weight in kilograms: "))
print(f"{kg} kg = {kg * 1000:.2f} g = {kg * 2.20462:.2f} lb")

# Time: hours -> minutes, seconds
hours = float(input("\nEnter time in hours: "))
print(f"{hours} hours = {hours * 60:.0f} min = {hours * 3600:.0f} sec")

# Currency: INR -> USD (fixed sample rate)
rate = 0.012
inr = float(input("\nEnter amount in INR: "))
print(f"Rs. {inr:.2f} = $ {inr * rate:.2f} (at 1 INR = {rate} USD)")

print("\nThank you for using the Unit Converter!")
