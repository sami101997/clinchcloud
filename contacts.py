import json

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load contacts from file (if available)
def load_contacts():
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)
    print("Contacts saved successfully!")

# Add a new contact
def add_contact(contacts):
    name = input("Enter Name: ").strip()
    if name in contacts:
        print("Contact already exists!")
        return
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email (optional): ").strip()
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact {name} added successfully!")
    save_contacts(contacts)

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found!")
        return
    print("\n--- Contact List ---")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}")

# Update an existing contact
def update_contact(contacts):
    name = input("Enter Name of contact to update: ").strip()
    if name not in contacts:
        print("Contact not found!")
        return
    phone = input(f"Enter new Phone Number (leave blank to keep {contacts[name]['Phone']}): ").strip() or contacts[name]["Phone"]
    email = input(f"Enter new Email (leave blank to keep {contacts[name]['Email']}): ").strip() or contacts[name]["Email"]
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact {name} updated successfully!")
    save_contacts(contacts)

# Delete a contact
def delete_contact(contacts):
    name = input("Enter Name of contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
        save_contacts(contacts)
    else:
        print("Contact not found!")

# Main menu
def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-5.")

# Run the program
if __name__ == "__main__":
    main()
