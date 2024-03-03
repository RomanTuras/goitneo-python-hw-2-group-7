'''Exceptions handler'''


class NameExists(Exception):
    '''Name already exists'''


class IncorrectPhoneNumber(Exception):
    '''Incorrect Phone Number'''


def input_error(func):
    '''
    Error handler decotator
    '''
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Give me name and phone please!")
        except NameExists:
            print("The same name already exists, add another!")
        except KeyError:
            print("Name not found!")
        except IncorrectPhoneNumber:
            print("Incorrect Phone Number!")

    return inner
