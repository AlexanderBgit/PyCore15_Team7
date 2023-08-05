from datetime import datetime, date
import re
from abc import ABC, abstractmethod
from AddressBook import *


class Record:
    def __init__(self, name, phone, Birthday, email) -> None:
        pass


    def change_birthday(self, new_birthday):
        pass


    def add_phone(self, phone):
        pass


    def change_phone(self, old_phone, new_phone):
        pass


    def change_name(self, new_name):
        pass


    def days_to_birthday(self):
        pass

    def __str__(self) -> str:
        return

class Field(ABC):
    def __init__(self, value) -> None:
        self.value = value



class Name(Field):
    def __init__(self, first_name, last_name=None) -> None:
        return
    

class Phone(Field):
    def __init__(self, value) -> None:
        return


class Birthday(Field):
    def __init__(self, value) -> None:
        self.value = value


class Email(Field):
    def __init__(self, value) -> None:
        return
    

class Tag(Field):
    def __init__(self, value) -> None:
        return


class Note(Field):
    def __init__(self, title: str) -> None:
        self.title = title    


    