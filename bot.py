from AddressBook import *
from classes import *
from exeptions import *
from rich.console import Console
from rich.table import Table
from rich import box
import subprocess

ab = AddressBook()

class Bot:
    def __init__(self):
        self.value = AddressBook()


@input_error
def add_command(*args):
    if not len(args):
        raise ValueNeedEnterError("Name")
    
    name = None
    phone = None
    birthday = None
    email = None
    adress = None
    
    count = 1
    for value in args:
        if count == 1:
            name = Name(value)
        if count == 2:
            phone = Phone(value)
        if count == 3:
            birthday = Birthday(value)
        if count == 4:
            email = Email(value)
        if count == 5:
            adress = Adress(value)
                
        count += 1

    record = address_book.get(name.value)

    if record:
        if phone:
            record.add_phone(phone)
        if birthday:
            record.change_birthday(birthday)
        if email:
            record.change_email(email)
        if adress:
            record.change_adress(adress)
        return f"Contact {name.value} updated successfully."
    
    record = Record(name, phone, birthday, email, adress)
    address_book.save_to_file()
    return address_book.add_record(record)

    
    # //////////////////////////
    # name = args[0]
    # last_name = ""
    # phone_number = None
    # birthday = None

    # # При більше ніж одному аргументі, другий це прізвище, третій - телефон
    # # четвертий аргумент - день народження
    # if len(args) > 1:
    #     # чи є прийнятним номер телефону
    #     if len(args[-1]) == 10 and args[-1].isdigit():
    #         phone_number = Phone(args[-1])
    #         if len(args) >= 3:
    #             last_name = args[1]
    #         if len(args) >= 4:
    #             birthday = Birthday(args[2])
    #     else:
    #         last_name = args[1]
    #         if len(args) >= 3:
    #             phone_number = Phone(args[2])
    #             if len(args) >= 4:
    #                 birthday = Birthday(args[3])

    #  # Чи існує контакт
    # record_name = f"{name} {last_name}".strip()
    # rec = address_book.get(record_name)
    # if rec:
    #     if phone_number:
    #         return rec.add_phone(phone_number)
    #     if birthday:
    #         return rec.change_birthday(birthday)
    #     return f"Contact {record_name} already exists in the address book."

    # # Створюємо name, phone number, and birthday
    # name_field = Name(f"{name} {last_name}".strip())
    # rec = Record(name_field, phone_number, birthday)
    # address_book.save_to_file()
    # return address_book.add_record(rec)


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

@input_error
def contacts_in_period(period: int) -> str:
    result = ab.congratulate(int(period)) #ab = AddressBook()
    if result:
        return "\n".join(str(record) for record in result)
    else:
        return f"No birthdays in {period} days"

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
def change_birthday_command(name: str, birthday: str) -> str:
    rec: Record = ab.get(str(name))
    if rec:
        return rec.change_birthday(birthday)
    return f"No {name} in contacts"

@input_error
def sort_files(path):
    try:
        result = subprocess.run(["python3", "sort.py", path], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e) 