from Add_Contact import Contact


menu_selection = ""
while menu_selection != '8':
    print('''Hello, welcome to the contact management System!
    Menu:
    1. Add a new contact
    2. Edit an existing contact
    3. Delete a contact
    4. Search for a contact
    5. Display all contacts
    6. Export contacts to a text file
    7. Import contacts from a text file
    8. Quit''')

    menu_selection = input("Please select an option by number: ")

    if menu_selection == '1':
        Contact.add_contact()
    elif menu_selection == '2':
        Contact.edit_contact()
    elif menu_selection == '3':
        Contact.remove_contact()
    elif menu_selection == '4':
        Contact.search()
    elif menu_selection == '5':
        Contact.display()
    elif menu_selection == '6':
        Contact.save_to_file()
    elif menu_selection == '7':
        Contact.import_contacts()
    elif menu_selection == '8':
        print("Goodbye!")
    else:
        print("Invalid option. Please try again.")
