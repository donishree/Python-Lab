"""
Program 4(c) - Lab Exercise 3 – CSV-based payroll management system
Source: Python Lab Report
"""

# Lab Exercise 3: CSV-based payroll management system
import csv

# Sample employee file created by the program
employees = [["EmpID", "Name", "Basic"], ["E01", "Asha", "50000"],
             ["E02", "Ravi", "42000"], ["E03", "Meena", "60000"]]
with open("employees.csv", "w", newline="") as f:
    csv.writer(f).writerows(employees)

bonus_percent = float(input("Enter bonus percentage: "))
payroll = []
try:
    with open("employees.csv", newline="") as f:
        for row in csv.DictReader(f):
            basic = float(row["Basic"])
            hra, da, tax = 0.20 * basic, 0.10 * basic, 0.10 * basic
            bonus = basic * bonus_percent / 100
            net = basic + hra + da + bonus - tax
            payroll.append([row["EmpID"], row["Name"], basic, hra, da,
                            bonus, tax, net])
except (FileNotFoundError, ValueError) as error:
    print("Error while reading employee data:", error)
else:
    header = ["EmpID", "Name", "Basic", "HRA", "DA", "Bonus", "Tax",
              "Net"]
    with open("payroll.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(payroll)

    print("\n" + "".join(f"{h:<8}" for h in header))
    for r in payroll:
        nums = "".join(f"{v:<8.0f}" for v in r[2:])
        print(f"{r[0]:<8}{r[1]:<8}" + nums)
    print("\nTotal payout:", sum(r[7] for r in payroll))
    print("Payroll saved to payroll.csv")
