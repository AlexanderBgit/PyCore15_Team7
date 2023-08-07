from datetime import datetime, date
import re
from AddressBook import *
from exeptions import *
from collections import UserDict, UserList

class Field:
    def __init__(self, value: str) -> None:
        self.value = value
    
    def __str__(self) -> str:
        return self.value


class Name(Field):
    def __init__(self, first_name, last_name=None) -> None:
        if last_name:
            self.value = f"{first_name} {last_name}"
        else:
            self.value = first_name
    

class Phone(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value:str):
        if self.is_correct_phone(value):
            self.__value = value
        else:
            raise PhoneError(value)
        
    def is_correct_phone(self, value) -> bool:
        pattern = re.compile(r"\+\d{11,13}")
        result = re.fullmatch(pattern, value)
        
        return True if result else False


class Birthday(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value:str):
        if re.fullmatch(r"\d{1,2}-\d{1,2}-\d{4}", value):
            self.__value = datetime.strptime(value, "%d-%m-%Y")
        elif re.fullmatch(r"\d{1,2}\.\d{1,2}\.\d{4}", value):
            self.__value = datetime.strptime(value, "%d.%m.%Y")
        elif re.fullmatch(r"\d{1,2}/\d{1,2}/\d{4}", value):
            self.__value = datetime.strptime(value, "%d/%m/%Y")
        else:
            raise BirthdayError(value)
        
    def is_empty_date(self) -> bool:
        return self.__value == datetime(1, 1, 1)
    
    def __str__(self):
        return self.__value.strftime("%d-%m-%Y") if not self.is_empty_date() else ""


class Email(Field):
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value:str):
        if self.is_correct_email(value):
            self.__value = value.lower()
        else:
            raise EmailError(value)
        
    def is_correct_email(self, value) -> bool:
        pattern = re.compile(r"([a-zA-Z]{1}[a-zA-Z0-9_.]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,})")
        result = re.fullmatch(pattern, value)
        
        return True if result else False
    

class Adress(Field):
    def __init__(self, value):
         self.value = value


class Field:
    def __init__(self, value):
         self.value = value
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return str(self)

class Name_teg(Field):
    pass

class Note(Field):
    pass

class Teg(Field):
    pass

## Нотатка має імя саму нотатку список тєгів дату створеня та "wg" для кількості співпадінь  
class Note:
    def __init__(self, name: Name_teg = None, note: Note = None, teg: Teg = None):
        self.wg = 0
        self.data = datetime.now()
        self.tegs = []
        self.note = note
        if teg:
            self.tegs.append(teg)
        if name:
            self.name = name.title()
        else:
            self.name = name

    def add_teg(self, teg_input):
        self.tegs.append(teg_input)

    def change_teg(self, teg_input):
        if teg_input:
            self.tegs = []
            self.tegs.append(teg_input)

    def change_text_note(self, note_input):
        self.note = note_input

    def __str__(self):
        return f"Ім'я: {self.name}. Дата створення:  {self.data.date()}\nЗміст: {self.note} \nТєги: {' '.join(str(tg) for tg in self.tegs)} wg:={self.wg}"

    def __repr__(self):
        return repr((self.name, self.note, self.tegs, self.wg))


## Клас нотатки зробив списком, бо так він ітеруется просто за номером 
# і головне немає полів обовязкових а пошук можна зробити за будь-яким полем  ##
class Notes(UserList):

    def add_note(self, note: Note):
        self.data.append(note)
        return print(f"Нотатка: {note.name} було добавлено.")  # Чи виводити подумаю бо може бути багато.
    
    def search_by_tegs(self, teg_input):        ## Шукає за тєгами, теги список може бути купа ціла навіть однакові, але це поправимо 
        print(f"Пошук за тегом: {teg_input}")
        for i in range(len(notes_book)):
            notes_book[i].wg == 0
            for n in range(len(notes_book[i].tegs)):
                #print(i+1,"  ",notes_book[i].tegs[n],"  ",n)
                if teg_input.lower() == notes_book[i].tegs[n].lower():
                    notes_book[i].wg =+ 1
                    print(f"Нотатка номер: {i+1} має збіг: {teg_input}")
        return None
    
    def search_by_global(self, word_input):     ## А це пошук глобальний за словом чи навіть буквою по всім полям, можна і по даті зробити
        print(f"Пошук за словом: {word_input}")
        for i in range(len(notes_book)):
            notes_book[i].wg == 0
            for n in range(len(notes_book[i].tegs)):
                #print(i+1,"  ",notes_book[i].tegs[n],"  ",n)
                if word_input.lower() == notes_book[i].tegs[n].lower():
                    notes_book[i].wg =+ 1
                    print(f"Нотатка номер: {i+1} має збіг: {word_input}")
            n_mach = 0
            if notes_book[i].note:        
                n_mach =+ len(re.findall(word_input.lower(), notes_book[i].note.lower()))
            if notes_book[i].name:
                n_mach =+ len(re.findall(word_input.lower(), notes_book[i].name.lower()))
            notes_book[i].wg =+ n_mach
            if n_mach:
                print(f"Нотатка номер: {i+1} має {n_mach} збігів: {word_input}")
        return None
    
    def __str__(self) -> str:
        return "\n".join(str(nt) for nt in self.data)
    

notes_book = Notes()
###############################################################################################################


class Record:
    def __init__(self, name: Name, phone: Phone = None, birthday: Birthday = None, email: Email = None, adress: Adress = None) -> None:
        self.name = name
        self.phones = []
        if phone:
            self.phones.append(phone)
        self.birthday = birthday
        self.email = email
        self.adress = adress


    def change_birthday(self, new_birthday: Birthday):
        self.birthday = new_birthday
        return f"Birthday changed to {new_birthday} for contact {self.name}"

    def change_email(self, new_email:Email):
        self.email = new_email

    
    def change_adress(self, new_adress:Adress):
        self.adress = new_adress

    
    def add_phone(self, phone: Phone):
        if phone not in self.phones:
            self.phones.append(phone)
            return f"Phone {phone} added to contact {self.name}"
        return f"{phone} is already present in the contact {self.name}"

    def change_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            self.phones.remove(old_phone)
            self.phones.append(new_phone)
            return f"Phone {old_phone} changed to {new_phone} for contact {self.name}"
        return f"{old_phone} is not present in the contact {self.name}"


    def change_name(self, new_name: Name):
        self.name = new_name
        return f"Name changed to {new_name} for contact {self.name}"

        
    def __str__(self) -> str:
        result = ""
        if self.name:
            result = result + str(self.name)
        if len(self.phones):
            result = result + ", " + ",".join([str(p) for p in self.phones])
        if self.birthday:
            result = result + ", " + str(self.birthday)
        if self.email:
            result = result + ", " + str(self.email)
        if self.adress:
            result = result + ", " + str(self.adress)

        return result
