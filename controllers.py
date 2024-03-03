'''Main Controllers'''

from collections import UserDict
from exceptoins_handler import input_error, NameExists, IncorrectPhoneNumber


class Field:
    '''Base class for record fields'''
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    '''A class for storing a contact name. Required field.'''
    def __init__(self, name):
        super().__init__(name)


class Phone(Field):
    '''A class for storing a phone number. Has format validation (10 digits).'''
    def __init__(self, phone_number):
        if phone_number.isdigit() and len(phone_number)==10:
            super().__init__(phone_number)
        else:
            raise IncorrectPhoneNumber


class Record:
    '''A class for storing information about a contact, including name and phone list.'''
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        '''Adding phone'''
        phone = Phone(phone_number)
        self.phones.append(phone)

    def edit_phone(self, old_phone, new_phone):
        '''Edit phone number'''
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return

    def remove_phone(self, phone):
        '''Removing phone number'''
        if phone in self.phones:
            self.phones.remove(phone)

    def find_phone(self, phone_number):
        '''Finding phone number'''
        for phone in self.phones:
            if phone.value == phone_number:
                return phone_number

    def __str__(self):
        return f"Contact: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"




class AddressBook(UserDict):
    '''A class for storing and managing records.'''

    def is_has_record(self, record:Record):
        '''Check is record exists'''
        return record.name.value in self.data.keys()

    @input_error
    def add_record(self, record:Record):
        '''Storing record'''
        if self.is_has_record(record):
            raise NameExists
        else:
            self.data.update({record.name.value:record})

    @input_error
    def update_record(self, record:Record):
        '''Updating record'''
        if self.is_has_record(record):
            self.data.update({record.name.value:record})

    @input_error
    def delete(self, record:Record):
        '''Deleting record'''
        self.data.pop(record)

    @input_error
    def find_by_name(self, name):
        '''Finding record by user name'''
        record = self.data.get(name)
        if record:
            return record
        raise KeyError



if __name__ == "__main__":
    print("")
    print("******************")
    print("Start Testing...")
    print("******************")
    print("")

    book = AddressBook()

    # Створення запису для John
    print("--> Creating John with two phones:")
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    print("--> Creating Jane with two phones:")
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_phone("5555555553")
    book.add_record(jane_record)

    print("--> Show all book records:")

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    print("--> Finding John:")
    # Знаходження та редагування телефону для John
    print(book.find_by_name("John"))
    book.find_by_name("Johneree") # Incorrect name

    print("--> Change John phone number:")
    john_record.edit_phone("1234567890", "1112223333")
    john_record.remove_phone("1112223333")

    print(book.find_by_name("John"))  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    print("--> Find certain John number:")
    # # Пошук конкретного телефону у записі John
    found_phone = john_record.find_phone("5555555555")
    print(f"{john_record.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    print("--> Deleting Jane:")
    book.delete("Jane")
    for name, record in book.data.items():
        print(record)

