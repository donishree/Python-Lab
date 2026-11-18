"""
Program 3(d) - Mini Project – Attendance Tracker
Source: Python Lab Report
"""

# Mini Project: Attendance Tracker
from datetime import date, timedelta

students = ["Asha", "Ravi", "Meena", "Kiran", "Sana"]
attendance = {}          # date string -> set of present students

days = int(input("Number of class days to record: "))
for d in range(days):
    day = (date.today() + timedelta(days=d)).strftime("%d-%m-%Y")
    present = set()
    print(f"\nAttendance for {day}")
    for student in students:
        if input(f"  Is {student} present? (y/n): ").lower() == "y":
            present.add(student)
    attendance[day] = present

print("\n========== ATTENDANCE REPORT ==========")
for student in students:
    attended = sum(1 for p in attendance.values() if student in p)
    percent = attended / days * 100 if days else 0
    status = "Eligible" if percent >= 75 else "Shortage"
    print(f"{student:<8}{attended}/{days} days {percent:6.1f}%  {status}")

all_days = set(students)
for present in attendance.values():
    all_days &= present      # set intersection
print("\nPresent on all days:", sorted(all_days) if all_days else "None")
absent_once = set(students) - all_days
print("Absent at least once:", sorted(absent_once))
