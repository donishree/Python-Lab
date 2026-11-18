"""
Program 4(b) - Lab Exercise 2 – Student data manager using files
Source: Python Lab Report
"""

# Lab Exercise 2: Student data manager using files
FILE = "students.txt"

# Sample data written first so that the program can run on its own
with open(FILE, "w") as f:
    f.writelines(["101,Asha,88\n", "102,Ravi,75\n", "103,Meena,92\n"])

def add_student(roll, name, marks):
    with open(FILE, "a") as f:                  # append mode
        f.write(f"{roll},{name},{marks}\n")

def view_students():
    with open(FILE, "r") as f:
        print(f"{'Roll':<8}{'Name':<12}{'Marks'}")
        for line in f:
            roll, name, marks = line.strip().split(",")
            print(f"{roll:<8}{name:<12}{marks}")

def search_student(roll):
    with open(FILE, "r") as f:
        for line in f:
            if line.startswith(roll + ","):
                return line.strip()
    return None

while True:
    print("\n1.Add  2.View all  3.Search  4.Exit")
    choice = input("Enter your choice: ")
    try:
        if choice == "1":
            roll, name = input("Roll: "), input("Name: ")
            add_student(roll, name, int(input("Marks: ")))
            print("Student record saved.")
        elif choice == "2":
            view_students()
        elif choice == "3":
            print(search_student(input("Roll no: ")) or "Not found.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
    except ValueError:
        print("Marks must be a number.")
