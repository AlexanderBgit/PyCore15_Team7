from collections import UserDict, UserList
from datetime import datetime
from datetime import datetime
from classes import Field, Name, Phone, Birthday, Record, AddressBook
import re, os, pickle

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

## Нотатка має імя саму нотатку список тєгів дату створеня та "wg" для кількості співпадінь  #####################

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


## Клас нотатки зробив списком, бо так він ітеруется просто за номером і головне немає полів обовязкових а пошук можна зробити за любим полем  ##

class Notes(UserList):

    def add_note(self, note: Note):
        self.data.append(note)
        return print(f"Нотатка: {note.name} було добавлено.")  # Чи виводити подумаю бо може бути багато.
    
    def search_by_tegs(self, teg_input):        ## Шукає за тєгами, теги список може бути купа ціла навіть однакові, але це поправимо 
        print(f"Пошук за тегом: {teg_input}\n")
        for i in range(len(notes_book)):
            notes_book[i].wg = 0
            for n in range(len(notes_book[i].tegs)):
                #print(i+1,"  ",notes_book[i].tegs[n],"  ",n)
                if teg_input.lower() == notes_book[i].tegs[n].lower():
                    notes_book[i].wg = notes_book[i].wg + 1
                    #print(f"Нотатка номер: {i+1} має збіг: {teg_input}")
            if notes_book[i].wg:        
                print(f"Нотатка №: {i+1} має {notes_book[i].wg} збігів: {teg_input}")
                print(notes_book[i],"\n")        
        return None
    
    def search_by_global(self, word_input):     ## А це пошук глобальний за словом чи навіть буквою по всім полям, можна і по даті зробити
        print(f"Пошук за словом: {word_input}\n")
        for i in range(len(notes_book)):
            notes_book[i].wg = 0
            for n in range(len(notes_book[i].tegs)):
                #print(i+1,"  ",notes_book[i].tegs[n],"  ",n)
                if word_input.lower() == notes_book[i].tegs[n].lower():
                    notes_book[i].wg = notes_book[i].wg + 1
                    #print(f"Нотатка номер: {i+1} має збіг: {word_input}")
            n_mach = 0
            if notes_book[i].note:        
                n_mach = n_mach + len(re.findall(word_input.lower(), notes_book[i].note.lower()))
            if notes_book[i].name:
                n_mach = n_mach + len(re.findall(word_input.lower(), notes_book[i].name.lower()))

            notes_book[i].wg =  notes_book[i].wg + n_mach
            if notes_book[i].wg:
                print(f"Нотатка №: {i+1} має {notes_book[i].wg} збігів: {word_input}")
                print(notes_book[i],"\n")
        #notes_book.sorted_wg() 
        #for i in range(len(notes_book)):
        #    if notes_book[i].wg:
        #        print(f"Нотатка №: {i+1} має {notes_book[i].wg} збігів: {word_input}")
                       
        return None
    
    def sorted_wg(self):
        self.data = (sorted(self.data, key=lambda mach: mach.wg, reverse=True))
        #return self.data
    
    def delete_note(self, namber_note):
        self.namber_note = namber_note
        nn = input(f"\nВИ ХОЧЕТЕ ВИДАЛИТИ НОТАТКУ № {namber_note}?  Y/N: ")
        print()
        if (nn == "Y") or (nn == "y"):
            del_note = notes_book.pop(namber_note-1)
            print(f"\nНОТАТКУ №: {namber_note}\n{del_note} \n                      БУЛО ВИДАЛЕНО.\n")
        #print(del_note)
    
    #def __str__(self) -> str:
        #return "\n".join(str(nt) for nt in self.data)
        #return "\n".join(str(rec) for rec in self.data.values())
        #return f"Ім'я: {self.name} Телефон: {' '.join(str(rec) for rec in self.phones)} День народження: {self.birthday}" 
 

    
    def __str__(self) -> str:
        return (f"\n\n".join("Нотатка № "+str(i+1)+" "+str(self.data[i]) for i in range(len(self.data))))

    

###############################################################################################################

def show_notes(n_str = -1):  # Це показуе або усі або по декілька
    if n_str > 0:
        long = len(notes_book)
        if long <= n_str:
            print("Ваш список нотаток:\n")
            for i in range(len(notes_book)):
                print("Нотатка №:",i+1," ",notes_book[i],"\n")
        else:
            print_one_page(n_str) 
    elif n_str == -1:
        print("Ваш список нотаток:\n")
        for i in range(len(notes_book)):
            #print(i+1," ",notes_book[i])
            print("Нотатка №:",i+1, " ", notes_book[i], "\n")

def print_one_page(n):
    f = 0
    fn = 0
    for i in range(len(notes_book)):
        f = f + 1
        fn = fn + 1
        print("Нотатка №:",fn, " ", notes_book[i], "\n")
        if f == n:
            f = 0
            nn = True
            while nn:
                nn = input(f"Щоб подивитися наступні {n} нотаток натисніть Enter.")
                print()
                nn = False
    print("Всі нотаткии показано.\n")

## Загрузка та збереження. Потім можна доробити та  зберігати після кожного редактування    

def load_note_book():
    path_note_book = ("save_note_book.bin")
    if os.path.exists(path_note_book):
        with open(path_note_book,"br") as fbr:
            fbr_list = pickle.load(fbr)
        return fbr_list
    else:
        return None 

def save_note_book(list):
    path_note_book = ("save_note_book.bin")
    with open(path_note_book,"bw") as fwb:
        pickle.dump(list, fwb)
    print("\nНотатки збережено.\n")

notes_book = Notes()


##   Далі просто тестова прога під коментом.  ##############################################################################################


if load_note_book():
    notes_book = load_note_book()
    print("\nНотатки загружено.\n")
else:
    print("\nНотатки відсутні.\n")


name = "nina"
note = "Полюбляє катосити велосипедом, не вживає спіртного"
teg = "Car"
#notatca = Note(name, note, teg)
#notes_book.add_note(notatca)


name = "viktor"
note = "Полюбляє бухати, тільки рідко та мало"
teg = "Drinc"
#notatca = Note(name, note, teg)
#notes_book.add_note(notatca)


rec: Note = notes_book[0]
#rec.change_text_note("Почав пиячити(((((")
#rec.change_teg("Music")
#rec.add_teg("Car")
#notes_book.add_note(rec)



#show_notes()


notes_book.search_by_tegs("Car")





notes_book.search_by_global("вело")

notes_book.sorted_wg()

print(notes_book)

print("print(notes_book)\n")
print(notes_book)

#notes_book.delete_note(1)
print("print(notes_book)\n")
print(notes_book)
save_note_book(notes_book)

# Приклад з интернет просторів
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
#print(sorted(student_objects, key=lambda student: student.age))  # sort by age
#[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
#print(student_objects)

# Сортування за значенням WG 
# значення WG набувають значень під час:  
#  notes_book.search_by_global("текст")  та  notes_book.search_by_tags("тег")

#notes_book = (sorted(notes_book, key=lambda mach: mach.wg, reverse=True))

#notes_book.sorted_wg()

#print(notes_book)

#for i in range(len(notes_book)):
#    print("Нотатка №:",i+1,notes_book[i],"\n")
