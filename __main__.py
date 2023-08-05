from bot import Bot
from bot import *
from AddressBook import *


if __name__ == "__main__":
    print('Hello')
    bot = Bot()

#автоматичне завантаження

COMMANDS = {
    add_command: ("add", "+", "2"),
    change_command: ("change", "зміни", "3"),
    exit_command: ("bye", "exit", "end", "0"),
    delete_contact_command:("del","8"),
    find_command: ("find", "4"),
    show_all_command: ("show all", "5"),
    hello_command:("hello", "1"),
    edit_name_command: ("edit", "7"),
    show_address_book: ("page", "**"),
    change_birthday_command: ("bday", "6")   
}

def parser(text: str):
    return unknown_command, []


def main():
    while True:
        user_input = input("enter your choises--->>> ")
        
        cmd, data = parser(user_input)

        result = cmd(*data)

        print(result)
        
        if cmd == exit_command:
            break
 

if __name__ == "__main__":
    address_book = AddressBook()
    main()