"""
Program 3(b) - Lab Exercise 2 – Student grading system
Source: Python Lab Report
"""

# Lab Exercise 2: Student grading system

def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"

students = {}   # name -> list of marks
count = int(input("Enter number of students: "))
for _ in range(count):
    name = input("\nStudent name: ")
    marks = [float(input(f"  Subject {i + 1} marks: ")) for i in range(3)]
    students[name] = marks

print(f"\n{'Name':<12}{'Total':>8}{'Average':>10}{'Grade':>7}")
print("-" * 37)
for name, marks in students.items():
    total = sum(marks)
    average = total / len(marks)
    grade = get_grade(average)
    print(f"{name:<12}{total:>8.1f}{average:>10.2f}{grade:>7}")

if students:
    topper = max(students, key=lambda n: sum(students[n]))
    print(f"\nTopper: {topper} ({sum(students[topper]):.1f} marks)")
