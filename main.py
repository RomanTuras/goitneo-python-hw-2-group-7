'''
    HW-2 Contacts assistant bot module
    Entry point
'''

import cmd_handler as handler
from controllers import AddressBook

def main():
    '''
    Main module
    '''
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = handler.parse_input(user_input)

        if command in ["close", "exit", "e"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            handler.add_contact(args, book)
        elif command == "change":
            handler.change_contact(args, book)
        elif command == "phone":
            handler.find_by_phone(args, book)
        elif command == "remove":
            handler.remove_phone(args, book)
        elif command == "all":
            handler.show_all_contacts(book)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
