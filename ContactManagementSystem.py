import re
import json

contacts = {}

def display_welcome_message():
    # Task: Display welcome message
    print("Welcome to the Contact Management System!")

def display_menu():
    # Task: Display the menu options
    print("\nMenu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file (BONUS)")
    print("8. Quit")

def validate_phone(phone):
    # Task: Validate phone number format
    return re.match(r'^\+?\d{10,15}$', phone)

def validate_email(email):
    # Task: Validate email format
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email)

def add_contact():
    # Task: Add a new contact
    print("Adding a new contact...")
    name = input("Enter name: ")
    phone = input("Enter phone number (+<country code>XXXXXXXXXX): ")
    if not validate_phone(phone):
        print("Invalid phone number format. Please try again.")
        return
    email = input("Enter email address: ")
    if not validate_email(email):
        print("Invalid email format. Please try again.")
        return
    
    additional_info = input("Enter additional information (address, notes, etc.): ")

    contacts[phone] = {
        'name': name,
        'email': email,
        'additional_info': additional_info
    }
    print(f"Contact '{name}' added successfully!")

def edit_contact():
    # Task: Edit an existing contact's information
    phone = input("Enter the phone number of the contact to edit: ")
    if phone not in contacts:
        print("Contact not found.")
        return

    print("Editing contact...")
    name = input("Enter new name (leave blank to keep current): ")
    email = input("Enter new email address (leave blank to keep current): ")
    additional_info = input("Enter new additional information (leave blank to keep current): ")

    if name:
        contacts[phone]['name'] = name
    if email and validate_email(email):
        contacts[phone]['email'] = email
    if additional_info:
        contacts[phone]['additional_info'] = additional_info

    print("Contact updated successfully!")

def delete_contact():
    # Task: Delete a contact
    phone = input("Enter the phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def search_contact():
    # Task: Search for a contact
    phone = input("Enter the phone number of the contact to search: ")
    if phone in contacts:
        contact = contacts[phone]
        print(f"Name: {contact['name']}")
        print(f"Phone: {phone}")
        print(f"Email: {contact['email']}")
        print(f"Additional Info: {contact['additional_info']}")
    else:
        print("Contact not found.")

def display_all_contacts():
    # Task: Display all contacts
    if not contacts:
        print("No contacts available.")
        return

    for phone, details in contacts.items():
        print(f"Name: {details['name']}, Phone: {phone}, Email: {details['email']}, Additional Info: {details['additional_info']}")

def export_contacts():
    # Task: Export contacts to a file
    filename = input("Enter filename to export contacts (e.g., contacts.json): ")
    try:
        with open(filename, 'w') as f:
            json.dump(contacts, f, indent=4)
        print(f"Contacts exported to {filename} successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def import_contacts():
    # Task: Import contacts from a file
    filename = input("Enter filename to import contacts from (e.g., contacts.json): ")
    try:
        with open(filename, 'r') as f:
            imported_contacts = json.load(f)
            contacts.update(imported_contacts)
        print(f"Contacts imported from {filename} successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Task: Main program execution
    display_welcome_message()

    while True:
        display_menu()
        choice = input("Please choose an option (1-8): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Thank you for using the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

