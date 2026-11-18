"""
Program 3(a) - Lab Exercise 1 – Contact book using lists and dictionaries
Source: Python Lab Report
"""

# Lab Exercise 1: Contact book using lists and dictionaries

contacts = []   # list of dictionaries, one dictionary per contact

def add_contact(name, phone, email):
    contacts.append({"name": name, "phone": phone, "email": email})

def search_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None

def display_all():
    if not contacts:
        print("Contact book is empty.")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")

while True:
    print("\n1.Add  2.Search  3.Delete  4.Display all  5.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact(input("Name: "), input("Phone: "), input("Email: "))
        print("Contact added.")
    elif choice == "2":
        found = search_contact(input("Enter name to search: "))
        print(found if found else "Contact not found.")
    elif choice == "3":
        found = search_contact(input("Enter name to delete: "))
        if found:
            contacts.remove(found)
            print("Contact deleted.")
        else:
            print("Contact not found.")
    elif choice == "4":
        display_all()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
