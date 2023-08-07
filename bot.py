from AddressBook import *
from classes import *
from exeptions import *
# from rich.console import Console
from rich.table import Table
from rich import box
import subprocess



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
    if not len(args):
        raise ValueNeedEnterError("Name")
    
    if len(args) < 3:
        raise ValueNeedEnterError("Old Phone and New Phone")
    
    name = None
    old_phone = None
    new_phone = None
    birthday = None
    email = None
    adress = None
    
    count = 1
    for value in args:
        if count == 1:
            name = Name(value)
        if count == 2:
            old_phone = Phone(value)
        if count == 3:
            new_phone = Phone(value)
        if count == 4:
            birthday = Birthday(value)
        if count == 5:
            email = Email(value)
        if count == 6:
            adress = Adress(value)
                
        count += 1

    record = address_book.get(name.value)

    if record:
        record.change_phone(old_phone, new_phone)
        
        if birthday:
            record.change_birthday(birthday)
        if email:
            record.change_email(email)
        if adress:
            record.change_adress(adress)
        return f"Contact {name.value} updated successfully."
    else:
        raise FindRecordError(name.value)


@input_error
def edit_name_command(*args):
    if len(args) < 3:
        raise ValueNeedEnterError("Old Name and New Name")
    
    old_name = Name(args[0])
    new_name = Name(args[1])
    
    record = address_book.get(old_name.value)

    if record:
        return record.change_name(new_name)
    else:
        raise FindRecordError(new_name)


@input_error
def delete_contact_command(*args):
    if not len(args):
        raise ValueNeedEnterError("Name")
    
    name = Name(args[0])
    
    record = address_book.get(name.value)

    if record:
        return address_book.delete_record(name.value)
    else:
        raise FindRecordError(name)


@input_error
def find_command(*args):
    if not len(args):
        raise ValueNeedEnterError("Name")
    
    name = Name(args[0])
    
    record = address_book.get(name.value)

    if record:
        return f"Successfuly find record: {record}"
    else:
        raise FindRecordError(name)


def exit_command(*args):
    return "Good bye!"
        

def unknown_command(*args):
    return f"Operation isn't possible. Can't recognized command. Use command 'help' for instructions."


@input_error
def contacts_in_period(period: int) -> str:
    result = address_book.congratulate(int(period))
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
        table.add_column("Email")
        table.add_column("Adress")

        for record in address_book.data.values():
            name = str(record.name)
            phone_numbers = ', '.join([str(phone) for phone in record.phones])
            birthday = str(record.birthday) if record.birthday else "N/A"
            email = str(record.email) if record.email else "N/A"
            adress = str(record.adress) if record.adress else "N/A"
            table.add_row(name, phone_numbers, birthday, email, adress)

        # console.print(table)
        return table
    else:
        # print('No contacts saved.')
        return "No contacts saved."


def hello_command(*args):
    return "How can I help you?"


@input_error
def change_birthday_command(name: str, birthday: str) -> str:
    rec: Record = address_book.get(str(name))
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

@input_error
def help_command() -> str:
    return "Available commands:\n" \
           "- hello\n" \
           "- add [name] [phone in format +380xxxxxxx]\n" \
           "- change [name] [phone]\n" \
           "- find [name]\n" \
           "- show_all\n" \
           "- edit [name]\n" \
           "- birthday [name] [date in format dd.mm.yyyy]\n" \
           "- period [number of days]\n" \
           "- help \n" \
           "- del [name] \n" \
           "- sort [path] \n" \
           "- bday [name] for birthday change \n" \
           "- period [n] (n = days of period for Bdays) \n" \
           "- bye, end, exit"