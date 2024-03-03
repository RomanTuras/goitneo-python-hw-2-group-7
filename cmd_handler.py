'''Commands handler module'''

from exceptoins_handler import input_error, NameExists
from controllers import Record, AddressBook


def parse_input(user_input):
    '''
    Parsing user input
    '''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, book:AddressBook):
    '''
    Add a new contact
    '''
    name, phone = args
    record = Record(name)
    if book.is_has_record(record):
        raise NameExists
    record.add_phone(phone)
    book.add_record(record)
    print("Contact added!")


@input_error
def remove_phone(args, book:AddressBook):
    '''
    Removing phone from contact
    '''
    name, phone = args
    record = Record(name)
    if book.is_has_record(record):
        record.remove_phone(phone)
        book.update_record(record)
        print("Phone removed!")


@input_error
def change_contact(args, book:AddressBook):
    '''
    Change contact number by name
    '''
    name, old_phone = args
    record = book.find_by_name(name)
    if record:
        new_phone = input("Enter a new phone: ")
        record.edit_phone(old_phone, new_phone)
        print("Contact updated!")


@input_error
def find_by_phone(args, book:AddressBook):
    '''
    Getting contact number by name
    '''
    phone = args[0]
    for record in book.values():
        if record.find_phone(phone):
            print(record)
        else:
            raise KeyError


def show_all_contacts(book:AddressBook):
    '''
    Showing all contacts
    '''
    for name, record in book.data.items():
        print(record)
