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

## Нотатка має імя саму нотатку список тєгів дату створеня та "wg" для кількості співпадінь. 
 
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

## Методи додати тег, очистити записати новий тег, змінити текст нотатки, та добавити текст нотатки.
## Методи використовуются у відповідних функціях бота.

    def add_teg(self, teg_input):
        self.tegs.append(teg_input)

    def change_teg(self, teg_input):
        if teg_input:
            self.tegs = []
            self.tegs.append(teg_input)

    def change_text_note(self, note_input):
        self.note = note_input

    def add_text_note(self, note_input):
        self.note_input = note_input
        self.note = self.note + " " + self.note_input    

    def __str__(self):
        return f"Ім'я: {self.name}. Дата створення:  {self.data.ctime()}\nЗміст: {self.note} \nТєги: {' '.join(str(tg) for tg in self.tegs)}"# wg:={self.wg}"

    def __repr__(self):
        return repr((self.name, self.note, self.tegs, self.wg))


## Клас нотатки зробив списком, бо так він ітеруется просто за номером і головне немає полів обовязкових а пошук можна зробити за любим полем.  

class Notes(UserList):

    def add_note(self, note: Note):## Метод який задіяний у функціі  def make_note(name, note, teg): створеня та запису новоі нотатки.
        self.data.append(note)
        return print(f"Нотатку: {note} \n       було створено та збережено.\n")  # Чи виводити подумаю бо може бути багато.
    
    def search_by_tegs(self, teg_input):
        flag = 0        ## Шукає за тєгами, теги список може бути купа ціла навіть однакові. 
        print(f"Пошук за тегом: {teg_input}")
        for i in range(len(notes_book)):
            notes_book[i].wg = 0
            for n in range(len(notes_book[i].tegs)):
                if teg_input.lower() == notes_book[i].tegs[n].lower():
                    notes_book[i].wg = notes_book[i].wg + 1
            if notes_book[i].wg:
                flag = flag + 1
            # Якщо виводити невідсортовані   нотатки а тільки ті що мають збіг без сортування.   
            #if notes_book[i].wg:        
            #    print(f"Нотатка №: {i+1} має {notes_book[i].wg} збігів: {teg_input}")
            #    print(notes_book[i],"\n") 
        if flag:
            print(f"Було знайдено {flag} нотаток:")
            notes_book.sorted_wg()
            print(notes_book)
        else:
            print("\nЗбігів у нотатках немає.\n")
        #notes_book.sorted_wg()
        #print(notes_book,"\n")               
        return None
    
    def search_by_global(self, word_input):     ## А це пошук глобальний за словом чи навіть буквою по всім полям, можна і по даті зробити.
        flag = 0
        print(f"Пошук за словом: {word_input}...")
        for i in range(len(notes_book)):
            notes_book[i].wg = 0
            for n in range(len(notes_book[i].tegs)):
                if word_input.lower() == notes_book[i].tegs[n].lower():
                    notes_book[i].wg = notes_book[i].wg + 1
                    flag = flag + 1
            n_mach = 0
            if notes_book[i].note:        
                n_mach = n_mach + len(re.findall(word_input.lower(), notes_book[i].note.lower()))
            if notes_book[i].name:
                n_mach = n_mach + len(re.findall(word_input.lower(), notes_book[i].name.lower()))

            notes_book[i].wg =  notes_book[i].wg + n_mach
            if n_mach:
                flag = flag + 1
            ## Це якщо виводити не відсортовані нотатки а тільки ті що мають збіг без сортування.
            #if notes_book[i].wg:
            #    print(f"Нотатка №: {i+1} має {notes_book[i].wg} збігів: {word_input}")
            #    print(notes_book[i],"\n")
        if flag:
            print(f"Було знайдено {flag} нотаток:")
            notes_book.sorted_wg()
            print(notes_book)
        else:
            print("\nЗбігів у нотатках немає.\n")
        ## Це якщо виводити тільки ті що мают збіг. 
        #for i in range(len(notes_book)):
        #    if notes_book[i].wg:
        #        print(f"Нотатка №: {i+1} має {notes_book[i].wg} збігів: {word_input}")
        #        print(notes_book[i])      
        return None
    
    def sorted_wg(self):
        self.data = (sorted(self.data, key=lambda mach: mach.wg, reverse=True))
        #return self.data

    def sorted_data(self):
        self.data = (sorted(self.data, key=lambda mach: mach.data, reverse=True))
        print("Нотатки відсортовано за часом створення:")
        print(notes_book)

    
    def delete_note(self, namber_note): ##Використовуєтся як метод.  Наприклад: notes_book.delete_note(5)
        namber_note = int(namber_note)
        if (namber_note <= len(notes_book)) and (namber_note > 0):
            self.namber_note = namber_note
            nn = input(f"\nВИ ХОЧЕТЕ ВИДАЛИТИ НОТАТКУ № {namber_note}?  Y/N: ")
            print()
            if (nn == "Y") or (nn == "y"):
                del_note = notes_book.pop(namber_note-1)
                print(f"НОТАТКУ №: {namber_note}\n{del_note} \n                      БУЛО ВИДАЛЕНО.\n")
            else:
                print(f"Ок. Не видаляємо, принаймні зараз.\n")
        else:
            print(f"\nНотатка №: {namber_note} відсутня. Кількість нотаток = {len(notes_book)}")    
        #print(del_note)
    
    #def __str__(self) -> str:
        #return "\n".join(str(nt) for nt in self.data)
        #return "\n".join(str(rec) for rec in self.data.values())
        #return f"Ім'я: {self.name} Телефон: {' '.join(str(rec) for rec in self.phones)} День народження: {self.birthday}" 
    
    def __str__(self) -> str:
        print()
        return (f"\n\n".join("Нотатка № "+str(i+1)+" "+str(self.data[i]) for i in range(len(self.data))))

###############################################################################################################
'''
try:
        int(list_input[2])
    except ValueError:
        list_input[2]=-1

try:
        return datetime.strptime(str_date, "%d-%m-%Y").date()
    except ValueError:
        print("Введіть коректну дату. Формат: dd-mm-yyyy")
        return None  
'''
###############################################################################################################
def  bot_add_teg(teg_text, number_note):
    try:
        int(number_note)
    except ValueError:
        return print("Було введено не розпізнане число. Введіть будь ласка вірний номер нотатки.")
    if (number_note <= len(notes_book)) and (number_note > 0):
        notes_book[number_note-1].add_teg(teg_text)



def make_note(name, note, teg): # Робить нову нотатку та додає у кінець списка. Поля не обов'язкові.
    notatca = Note(name, note, teg)
    notes_book.add_note(notatca)



def show_notes(n_str = -1):  # Це показуе або усі або по декілька нотаток на один раз.
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
            print("Нотатка №:",i+1, " ", notes_book[i], "\n")

def print_one_page(n): # Належить до функціі show_notes(n_str)
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

## Загрузка та збереження. Також можна доробити та  зберігати після кожного редактування, просто написати у коді  save_note_book()  

def load_note_book():
    path_note_book = ("save_note_book.bin")
    if os.path.exists(path_note_book):
        with open(path_note_book,"br") as fbr:
            fbr_list = pickle.load(fbr)
        return fbr_list
    else:
        return None 

def save_note_book():
    path_note_book = ("save_note_book.bin")
    with open(path_note_book,"bw") as fwb:
        pickle.dump(notes_book, fwb)
    print("\nНотатки збережено.\n")

###############################################################################################################################

notes_book = Notes()

##   Далі просто тестова прога.  ##############################################################################################

if load_note_book():
    notes_book = load_note_book()
    print("\nНотатки загружено.\n")
else:
    print("\nНотатки відсутні.\n")

name = "nina"
note = "Полюбляє катосити велосипедом, не вживає спіртного"
teg = "Car"
make_note(name, note, teg)

make_note( None," Були були на селі", "Село") # Зробив нову нотатку.
make_note( "Вова"," Гуляли на селі", "Гуляли") # Зробив нову нотатку.
make_note( "Оля"," Жили у селі", "Жили") # Зробив нову нотатку.
make_note( None," Були були у славному місті Тернопіль", "Тернопіль") # Зробив нову нотатку.

# Приклад роботи функцій як методів класу нотатка. Кожен єлемент notes_book[] є клас нотатка class Note:

notes_book[4].change_text_note("QWERTY") # Замінить текст нотатки на текст "QWERTY".
notes_book[4].add_text_note(" 12345") # Добавить текст " 12345" до тексту "QWERTY" нотатки та отримаємо "QWERTY 12345".
notes_book[2].add_teg("Літак") # Добавить у нотатку №2 тег "Літак". Якщо не буде номера нотатки буде помилка.
notes_book[3].change_teg("QWERTYUIOP") # Очистить усе поле з тегами та запише туди "QWERTYUIOP"

notes_book.search_by_tegs("Літак") # Пошук за тегом "Літак".
notes_book.search_by_global("були") # Пошук за текстом "були" по всіх полях.

print(notes_book) # Просто розпечатає форматом весь список нотаток.

notes_book.delete_note(6) # Видалить нотатку № 6, якщо номера нема напише про це, якщо ввести не число буде помилка потребує декоратора.
notes_book.delete_note(6) # Також видалить бо вони змістяться, якщо номера нема напише про це.

show_notes()  # Якщо нічого не ввести виведе усі ноатки за один раз.
show_notes(5) # Виводить по 5 нотаток за раз.

notes_book.sorted_data() # Відсортує за часом створення. Спочатку останні а в кінці ті що давно створені.

save_note_book()

#Приклад з интернет просторів сортування по полю списків у спискуна прикладі класу.##############
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
#####################################################################################################
