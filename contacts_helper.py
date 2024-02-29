'''HW-2 Contacts assistant bot module'''

def input_error(func):
    '''
    Error handler decotator
    '''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner

def parse_input(user_input):
    '''
    Parsing user input
    '''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    '''
    Add a new contact
    '''
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    '''
    Change contact number by name
    '''
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def get_phone(args, contacts):
    '''
    Getting contact number by name
    '''
    name = args[0]
    if name in contacts.keys():
        return contacts[name]
    else:
        return "Name not found!"

def show_all_contacts(contacts):
    '''
    Showing all contacts
    '''
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def main():
    '''
    Main module
    '''
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "e"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            show_all_contacts(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
