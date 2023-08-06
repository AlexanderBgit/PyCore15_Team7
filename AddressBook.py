from collections import UserDict
from rich.console import Console
from rich.table import Table
from rich import box
from datetime import datetime, date, timedelta
import re
import pickle
from classes import *

# Клас AddressBook, який наслідується від UserDict, 
# та ми потім додамо логіку пошуку за записами до цього класу.
class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[str(record.name)] = record
        return f"Contact {record} add success"


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


    def congratulate(self, period: int):
        current_date = datetime.now().date()

        results = []
        for record in self.data.values():
            if record.birthday:
                next_birthday = datetime(current_date.year, record.birthday.month, record.birthday.day).date()

                if next_birthday < current_date:
                    next_birthday = datetime(current_date.year + 1, record.birthday.month, record.birthday.day).date()

                days_to_bd = (next_birthday - current_date).days
                if 0 <= days_to_bd <= period:
                    results.append(f"{record.name} {next_birthday.strftime('%d.%m')}")

        return results


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

