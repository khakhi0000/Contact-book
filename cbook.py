import os

contact_file = "file.txt"

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact number: ")
    email = input("Enter contact mail: ")

    with open(contact_file, "a") as f:
        f.write(f"{name},{phone},{email}\n")
        print("Contact added successfully\n")

def view_contact():
    if not os.path.exists(contact_file):
        print("No contact found\n")
        return

    with open(contact_file ,"r")as f:
        contacts = f.readlines()
    print("\n---- Contact list ----")
    for index, contact in enumerate(contacts,1):
        name,phone,email = contact.strip().split(",")
        print(f"{index}.Name: {name},Phone: {phone},Email: {email}")
    print()
def search_contact():
    search_name = input("Enter name to search: ")
    with open(contact_file, 'r') as f:
        contacts = f.readlines()
    found = False
    for contact in contacts:
        name, phone, email = contact.strip().split(",")
        if search_name in name.lower():
            print(f"\n Found:Name: {name},Email: {email},Phone: {phone}")
            found = True
            break
        if not found:
            print("\nNot found! ")
def del_contact():
    search_name =input('Enter name to search: ')
    with open(contact_file, 'r') as f:
        contacts = f.readlines()
    updated_contacts = []
    found = False
    for contact in contacts:
        name, phone, email = contact.strip().split(",")
        if search_name not in name.lower():
            updated_contacts.append(contact)
        else:
            found = True
    if found:
        with open(contact_file,'w') as f:
            f.writelines(updated_contacts)
            print("Contact Deleted! ")
    else:
        print("Contact not  found")
def menu():
    while True:
        print("1: Add Contact")
        print("2: View Contacts")
        print("3: Search Contact")
        print("4: Delete Contact")
        print("5: Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            del_contact()
        elif choice == "5":
            print("Exiting program-----")
            break
        else:
            print("Invalid choice!")
menu()










