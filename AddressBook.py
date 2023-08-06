from collections import UserDict
from rich.console import Console
from rich.table import Table
from rich import box
from datetime import datetime, date
import re
import pickle

# Клас AddressBook, який наслідується від UserDict, 
# та ми потім додамо логіку пошуку за записами до цього класу.
class AddressBook(UserDict):
    def add_record(self,):
        pass


    def delete_record(self,):
        pass

    def add_record(self, record):
        pass


    def delete_record(self, name):
        pass


    def save_to_file(self):
        pass


    def load_from_file(self):
        pass


    def __get_current_week(self):
        pass


    def congratulate(self):
        pass


    # метод iterator, який повертає генератор за записами. Пагінація    
    def __iter__(self, n=5):
        pass


    def __str__(self) -> str:
        pass

# завантажує записи під час ініціалізації
    def __init__(self):
        super().__init__()
        self.load_from_file()



address_book = AddressBook()    

