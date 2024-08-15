import json


class Contact:
    contacts = {}

    def __init__(self, name, number, email):
        self.name = name
        self.number = number
        self.email = email

    @classmethod
    def add_contact(cls):
        try:
            name = input("Please add contact's name: ")
            if name in cls.contacts:
                print(f"Contact with name {name} already exists.")
                return
            
            number = input("Please add contact's phone number: ")
            email = input("Please add email address: ")
            contact_info = {
                "name": name,
                "phone": number,
                "email": email,
            }
            cls.contacts[name] = contact_info
            print(f"\nNew contact for {name} has been added.\n")
        except Exception as e:
            print(f"An error occurred while adding the contact: {e}")

    @classmethod
    def edit_contact(cls):
        try:
            edit_name = input("Please enter the name of the contact you would like to edit: ")
            if edit_name not in cls.contacts:
                print(f"No contact found with the name {edit_name}.")
                return
            
            print("Please input the new contact information below.")
            name = input("Please add contact's name: ")
            number = input("Please add contact's phone number: ")
            email = input("Please add email address: ")
            contact_info = { 
                "name": name,
                "phone": number,
                "email": email,
            }
            cls.contacts[name] = contact_info
            if edit_name != name:
                del cls.contacts[edit_name]
            print(f"\nContact for {edit_name} has been updated.\n")
        except Exception as e:
            print(f"An error occurred while editing the contact: {e}")

    @classmethod
    def remove_contact(cls):
        try:
            remove_name = input("Please enter the name of the contact you wish to delete: ")
            if remove_name not in cls.contacts:
                print(f"No contact found with the name {remove_name}.")
                return
            
            del cls.contacts[remove_name]
            print(f"\n{remove_name} has been removed from your contacts.\n")
        except Exception as e:
            print(f"An error occurred while removing the contact: {e}")

    @classmethod
    def search(cls):
        try:
            search_name = input("Please enter the name of the contact you would like to search: ")
            if search_name in cls.contacts:
                print(f"\nContact found:\nContact: {search_name}, Info: {cls.contacts[search_name]}\n")
            else:
                print(f"No contact found for {search_name}.")
        except Exception as e:
            print(f"An error occurred while searching for the contact: {e}")

    @classmethod
    def display(cls):
        try:
            if not cls.contacts:
                print("No contacts to display.")
                return
            
            for key, value in cls.contacts.items():
                print(f"\nContact: {key}, Info: {value}\n")
        except Exception as e:
            print(f"An error occurred while displaying contacts: {e}")

    @classmethod
    def save_to_file(cls):
        try:
            with open('save_file.txt', 'w') as file:
                json.dump(cls.contacts, file)
            print("Your contacts have been saved to file: save_file.txt")
        except Exception as e:
            print(f"An error occurred while saving contacts to file: {e}")

    @classmethod
    def import_contacts(cls):
        try:
            with open('save_file.txt', 'r') as file:
                cls.contacts = json.load(file)
            print("Contacts have been imported.")
        except FileNotFoundError:
            print("File not found.")
        except json.JSONDecodeError:
            print("Error decoding the JSON data from the file.")
        except Exception as e:
            print(f"An error occurred while importing contacts: {e}")


