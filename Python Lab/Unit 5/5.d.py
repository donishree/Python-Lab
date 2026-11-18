"""
Program 5(d) - Mini Project – Retail sales dashboard using CSV and matplotlib
Source: Python Lab Report
"""

# Mini Project: Retail Sales Dashboard using CSV and matplotlib
import csv
import numpy as np
import matplotlib.pyplot as plt

# Sample sales data (Month, Category, Units, Price) saved as a CSV file
data = [("Jan", "Electronics", 12, 1500), ("Jan", "Grocery", 80, 60),
        ("Jan", "Clothing", 35, 400), ("Feb", "Electronics", 15, 1500),
        ("Feb", "Grocery", 95, 60), ("Feb", "Clothing", 30, 400),
        ("Mar", "Electronics", 20, 1500), ("Mar", "Grocery", 70, 60),
        ("Mar", "Clothing", 50, 400)]
with open("sales.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Month", "Category", "Units", "Price"])
    writer.writerows(data)

# Read the CSV file and calculate revenue
month_rev = {"Jan": 0, "Feb": 0, "Mar": 0}
cat_rev, units, revenues = {}, [], []
with open("sales.csv", newline="") as f:
    for row in csv.DictReader(f):
        revenue = int(row["Units"]) * float(row["Price"])
        month_rev[row["Month"]] += revenue
        cat = row["Category"]
        cat_rev[cat] = cat_rev.get(cat, 0) + revenue
        units.append(int(row["Units"]))
        revenues.append(revenue)

# Dashboard with three charts (black and white style)
fig, ax = plt.subplots(1, 3, figsize=(15, 4))
ax[0].plot(list(month_rev), list(month_rev.values()), marker="o",
           color="black")
ax[0].set_title("Monthly Revenue (Line)")
ax[1].bar(list(cat_rev), list(cat_rev.values()), color="gray",
          edgecolor="black")
ax[1].set_title("Revenue by Category (Bar)")
ax[2].scatter(units, revenues, color="black")
ax[2].set_title("Units vs Revenue (Scatter)")
ax[2].set_xlabel("Units sold")
plt.tight_layout()
plt.savefig("dashboard.png")
plt.show()

print("Total revenue :", np.sum(revenues))
print("Best category :", max(cat_rev, key=cat_rev.get))
