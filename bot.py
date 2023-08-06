from AddressBook import *
from exeptions import *


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
    if address_book.data:
        console = Console()
        table = Table(show_header=True, header_style="bold", box=box.ROUNDED)
        table.add_column("Name")
        table.add_column("Phone number")
        table.add_column("Birthday", style="dim")

        for record in address_book.data.values():
            name = str(record.name)
            phone_numbers = ', '.join([str(phone) for phone in record.phones])
            birthday = str(record.birthday) if record.birthday else "N/A"
            table.add_row(name, phone_numbers, birthday)

        console.print(table)
    else:
        print('No contacts saved.')


def hello_command(*args):
    return "How can I help you?"


def show_address_book():
    print('No contacts saved.')


@input_error
def change_birthday_command(*args):
    return 