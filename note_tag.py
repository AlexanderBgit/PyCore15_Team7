from datetime import datetime
from collections import UserList
import re


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