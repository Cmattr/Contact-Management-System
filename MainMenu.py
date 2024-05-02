import json

contacts = {}

def add_contact(contacts):
    add_name= (input("please add contacts name: "))
    add_number = input("please add contacts phone number: ")
    add_email = (input("please add email address: "))
    new_contact = {
           "name": add_name,
           "phone": add_number,
           "email": add_email,
    }
    contacts[add_name] = new_contact
    print(f"\nNew contact for {add_name} has been added.\n")

def edit_contact(contacts):
    edit_name = input("please enter the name of the contact you would like to edit: ")
    print("please input the new contact information below. ")
    new_name = (input("please add contacts name: "))
    new_number = input("please add contacts phone number: ")
    new_email = (input("please add email address: "))
    new_info = { 
       "name": new_name,
       "phone": new_number,
       "email": new_email,
        }
    if edit_name in contacts:
        contacts[edit_name]["name"] = new_name
        contacts[edit_name]["phone"] = new_number
        contacts[edit_name]["email"] = new_email
    

def remove_contact(contacts):
    remove_name = input("please enter the name of the contact you wish to delete: ")
    contacts.pop(remove_name)
    print (f"\n{remove_name} has been removed from your contacts\n")

def search(contacts):
    search_name = input("please enter the name of the contact you would like to search: ")
    for name, details in contacts.items():
        if (search_name) == name:    
            print(f"\ncontact found:\ncontact:{name}, info: {details}\n")
            break
        else:
            print(f"no contact found for {search_name}")

def display(contacts):
    for key, value in contacts.items():
        print(f"\nContact: {key}, Info: {value}\n")

           

def save_to_new_file(contacts):
    with open('save_file.txt', 'w') as text_file:
        text_file.write(json.dumps(contacts))

def import_contacts(contacts):
    try:
        with open("save_file.txt", 'r') as file:
            for line in file:
                name, number, email = line.strip().split(',')
                contact = {
                    'name': name,
                    'number': number,
                    'email': email
                }
                contacts[name] = contact
                print(f"\nContact: {contact['name']}, Info: {contact['number']}, {contact['email']}\n")
                return contacts
    except FileNotFoundError:
        print("File not found")
        return contacts 

menu_selection = ""
while menu_selection != '8':
    

    print('''Hello, welcome to the contact management System!
    menu:
    1. Add a new contact
    2. Edit an existing contact
    3. Delete a contact
    4. Search for a contact
    5. Display all contacts
    6. Export contacts to a text file
    7. Import contacts from a text file
    8. Quit''')

    menu_selection = input("please select an option by number: ")

    # add contact 
    if menu_selection == '1':
        add_contact(contacts)
        print(f"Contacts Updated:")
        display(contacts)
        #edit contacts
    elif menu_selection == '2':
        edit_contact(contacts)
        print(f"contacts updated:")
        display(contacts)
    # delete contact
    elif menu_selection =='3':
        remove_contact(contacts)
        print(f"contacts updated:")
        display(contacts)
    # search contacts
    elif menu_selection == '4':
        search(contacts)
    # view contact
    elif menu_selection == '5':
        display(contacts)
    elif menu_selection == '6':
        save_to_new_file(contacts)
        print("your contacts have been added to file: exported-contacts.txt")
    elif menu_selection == '7':
        import_contacts(contacts)
    else:
        pass