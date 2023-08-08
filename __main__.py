from bot import Bot
from bot import *
from AddressBook import *
from rich.console import Console
from classes import *


COMMANDS = {
    add_command: ("add", "+", "2","adding","append"),
    change_command: ("change", "зміни", "3"),
    exit_command: ("bye", "exit", "end","GoodBye", "0"),
    delete_contact_command:("del","8", "delete"),
    find_command: ("find", "4"),
    show_all_command: ("show-all", "5", "show","showing"),
    hello_command:("hello", "1"),
    edit_name_command: ("edit", "7","rename"),
    change_birthday_command: ("change-bday", "6","change-birthday", "changebday","changebirthday"),
    change_email_command: ("change-email", "9", "change-mail", "changemail", "changeemail"),
    change_address_command: ("change-address", "10","changeaddress"),
    sort_files: ("sort","sorting"),
    contacts_in_period: ("period", "bdays","congrats"),
    help_command: ("help")
    
}


def parser(text: str):
    text_lst = text.split(" ")
    for cmd, kwds in COMMANDS.items():
        kwd = text_lst[0]
        if len(text_lst) and kwd in kwds:
            data = text[len(kwd):].strip().split()
            return cmd, data
        
        # for kwd in kwds:
        #     if text.lower().startswith(kwd):
        #         data = text[len(kwd):].strip().split()
        #         if cmd in [change_command, edit_name_command]:
        #             if len(data) < 3:
        #                 data.append(None)
        #         return cmd, data
    return unknown_command, []


def main():
    while True:
        user_input = input("enter your choices--->>> ")
        
        cmd, data = parser(user_input)

        if cmd == exit_command:
            break

        result = cmd(*data)

        if isinstance(result, str):
            print(result)
        else:
            console = Console()
            console.print(result)
        
 

if __name__ == "__main__":
    print('Hello. I am your contact-assistant.\nWhat can I do for you?')
    bot = Bot()
    main()