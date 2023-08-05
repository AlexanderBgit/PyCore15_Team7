from AddressBook import *


class Bot:
    def __init__(self):
        self.value = AddressBook()


@input_error
def add_command(*args):
    return 


@input_error
def change_command(*args):
    return


@input_error
def edit_name_command(*args):
    return


@input_error
def delete_contact_command(*args):
    return "Please provide a name to delete the contact."


@input_error
def find_command(*args):
    return


def exit_command(*args):
    return "Good bye!"
        

def unknown_command(*args):
    pass


def show_all_command(*args):
    ...


def hello_command(*args):
    return "How can I help you?"


def show_address_book():
    print('No contacts saved.')


@input_error
def change_birthday_command(*args):
    return 