from collections import UserList
from datetime import datetime
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


# Клас: Нотатка має: імя, саму нотатку, список тєгів, дату створеня та "wg" для кількості співпадінь.


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

    # Методи додати тег, очистити записати новий тег, змінити текст нотатки, та добавити текст нотатки.
    # Методи використовуются у відповідних функціях бота.

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
        return f"Ім'я: {self.name}. Дата створення:  {self.data.ctime()}\nЗміст: {self.note} \nТєги: {' '.join(str(tg) for tg in self.tegs)}"

    def __repr__(self):
        return repr((self.name, self.note, self.tegs, self.wg))


# Клас нотатки зробив списком, бо так він ітеруется просто за номером і головне немає полів обовязкових а пошук можна зробити за любим полем.


class Notes(UserList):
    def add_note(self, note: Note):  ## Метод який задіяний у функціі make_note(name, note, teg): створеня та запису новоі нотатки.
        self.data.append(note)
        return print(f"Нотатку: {note} \n       було створено та збережено.\n")

    def search_by_tegs(self, teg_input):
        flag = 0  # Шукає за тєгами, теги список може бути купа ціла навіть однакові.
        print(f"Пошук за тегом: {teg_input}")
        for i in range(len(notes_book)):
            notes_book[i].wg = 0
            for n in range(len(notes_book[i].tegs)):
                if teg_input.lower() == notes_book[i].tegs[n].lower():
                    notes_book[i].wg = notes_book[i].wg + 1
            if notes_book[i].wg:
                flag = flag + 1
        if flag:
            print(f"Було знайдено {flag} нотаток:")
            notes_book.sorted_wg()
            print(notes_book)
        else:
            print("\nЗбігів у нотатках немає.\n")
        return None

    def search_by_global(self, word_input):  ## А це пошук глобальний за словом чи навіть буквою по всім полям, можна і по даті зробити.
        flag = 0
        print(f"\nПошук за словом: {word_input}...")
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
            notes_book[i].wg = notes_book[i].wg + n_mach
            if n_mach:
                flag = flag + 1
        if flag:
            print(f"Було знайдено {flag} нотаток:")
            notes_book.sorted_wg()
            print(notes_book)
        else:
            print("\nЗбігів у нотатках немає.\n")
        return None

    def sorted_wg(self):  # Сортує по значенню wg якого набуває нотатка при пошуку збігів.
        self.data = sorted(self.data, key=lambda mach: mach.wg, reverse=True)

    def sorted_data(self):  # Сортуе за часом створення нотатки.
        self.data = sorted(self.data, key=lambda mach: mach.data, reverse=True)
        print("\nНотатки відсортовано за часом створення:")
        print(notes_book)

    def delete_note(self, namber_note):  ##Використовуєтся як метод.  Наприклад: notes_book.delete_note(5)
        namber_note = int(namber_note)
        if (namber_note <= len(notes_book)) and (namber_note > 0):
            self.namber_note = namber_note
            nn = input(f"\nВИ ХОЧЕТЕ ВИДАЛИТИ НОТАТКУ № {namber_note}?  Y/N: ")
            print()
            if (nn == "Y") or (nn == "y"):
                del_note = notes_book.pop(namber_note - 1)
                print(f"НОТАТКУ №: {namber_note}\n{del_note} \n                      БУЛО ВИДАЛЕНО.\n")
            else:
                print(f"Ок. Не видаляємо, принаймні зараз.\n")
        else:
            print(f"\nНотатка №: {namber_note} відсутня. Кількість нотаток = {len(notes_book)}")

    def __str__(self) -> str:
        print()
        return f"\n\n".join("Нотатка № " + str(i + 1) + " " + str(self.data[i])for i in range(len(self.data)))


###############################################################################################################
# Далі пішли функціі бота тоб то функціі які викликають методи класів і з ними працюють.
# Ці функціі знаходятся у файлу бота. Все те що вищще у файлі класів.


from collections import UserList
from datetime import datetime
# from classes import Field, Name_teg, Note, Teg  Розкоментити потім для імпорту класів з файлу класів. 
import re, os, pickle


def bot_add_teg(teg_text, number_note):  # Додає тег teg_text до нотатки № number_note з перевіркою номера нотатки.
    try:  # Не потребуе декоратора помилок.
        int(number_note)
    except ValueError:
        return print(
            "\nБуло введено не розпізнане число. Введіть будь ласка вірний номер нотатки.")
    if (number_note <= len(notes_book)) and (number_note > 0):
        notes_book[number_note - 1].add_teg(teg_text)
        print(f"\nТег: {teg_text} було добавлено до нотатки №: {number_note}")
    if (number_note > len(notes_book)) or (number_note <= 0):
        print(f"\nНотатка №: {number_note} не існуе. У Вас всього {len(notes_book)} нотаток.")


def bot_change_teg(teg_text, number_note):  # Записує тег teg_text замість існуючих тегів до нотатки № number_note
    try:  #  з перевіркою номера нотатки. Не потребуе декоратора помилок.
        int(number_note)
    except ValueError:
        return print("\nБуло введено не розпізнане число. Введіть будь ласка вірний номер нотатки.")
    if (number_note <= len(notes_book)) and (number_note > 0):
        notes_book[number_note - 1].change_teg(teg_text)
        print(f"\nТег нотатки №: {number_note} було замінено тегом {teg_text}.")
    if (number_note > len(notes_book)) or (number_note <= 0):
        print(f"\nНотатка №: {number_note} не існуе. У Вас всього {len(notes_book)} нотаток.")


def bot_add_text_note(note_text, number_note):  # Додає текст note_text до нотатки № number_note
    try:  # з перевіркою номера нотатки. Не потребуе декоратора помилок.
        int(number_note)
    except ValueError:
        return print("\nБуло введено не розпізнане число. Введіть будь ласка вірний номер нотатки.")
    if (number_note <= len(notes_book)) and (number_note > 0):
        notes_book[number_note - 1].add_text_note(note_text)
        print(f"\nТекст: {note_text} було добавлено до тексту нотатки №: {number_note}")
    if (number_note > len(notes_book)) or (number_note <= 0):
        print(f"\nНотатка №: {number_note} не існуе. У Вас всього {len(notes_book)} нотаток.")


def bot_change_text_note(note_text, number_note):  # Записує текст note_text до нотатки № number_note  але видаляє попередній, тобто змінює.
    try:  # з перевіркою номера нотатки. Не потребуе декоратора помилок.
        int(number_note)
    except ValueError:
        return print("\nБуло введено не розпізнане число. Введіть будь ласка вірний номер нотатки.")
    if (number_note <= len(notes_book)) and (number_note > 0):
        notes_book[number_note - 1].change_text_note(note_text)
        print(f"\nТекст нотатки №: {number_note} було замінено текстом: {note_text}.")
    if (number_note > len(notes_book)) or (number_note <= 0):
        print(f"\nНотатка №: {number_note} не існуе. У Вас всього {len(notes_book)} нотаток.")


def make_note(name, note, teg):  # Робить нову нотатку та додає у кінець списка. Поля не обов'язкові.
    notatca = Note(name, note, teg)  # Використовує метод .add_note(name, note, teg)
    notes_book.add_note(notatca)


def show_notes(n_str=None):
    try:  #  з перевіркою номера нотатки. Не потребуе декоратора помилок.
        int(str(n_str))
    except ValueError:
        print("\nВаш список нотаток:\n")
        for i in range(len(notes_book)):
            print("Нотатка №:", i + 1, " ", notes_book[i], "\n")
    else:
        n_str = int(
            n_str
        )  # Показуе або усі або по декілька нотаток на один раз. Не потребує декоратора помилок.
        if n_str > 0:  # Використовуе функцію  print_one_page(n_str)
            long = len(notes_book)
            if long <= n_str:
                print("\nВаш список нотаток:\n")
                for i in range(len(notes_book)):
                    print("Нотатка №:", i + 1, " ", notes_book[i], "\n")
            else:
                print_one_page(n_str)
        else:
            print("\nВаш список нотаток:\n")
            for i in range(len(notes_book)):
                print("Нотатка №:", i + 1, " ", notes_book[i], "\n")


def print_one_page(n):  # У функціі show_notes(n_str) виводить n нотаток за один виклик.
    f = 0  # Не потребує декоратора бо викликаєтся функцією яка має перевірку.
    fn = 0
    for i in range(len(notes_book)):
        f = f + 1
        fn = fn + 1
        print("Нотатка №:", fn, " ", notes_book[i], "\n")
        if f == n:
            f = 0
            nn = True
            while nn:
                nn = input(f"Щоб подивитися наступні {n} нотаток натисніть Enter.")
                print()
                nn = False
    print("Всі нотаткии показано.\n")


######   Загрузка та збереження. #############################################################################################

def load_note_book():
    global notes_book
    path_note_book = "save_note_book.bin"
    if os.path.exists(path_note_book):
        with open(path_note_book, "br") as fbr:
            notes_book = pickle.load(fbr)
            print("\nНотатки загружено.\n")
    else:
        print("\nНотатки відсутні.\n")

def save_note_book():
    path_note_book = "save_note_book.bin"
    with open(path_note_book, "bw") as fwb:
        pickle.dump(notes_book, fwb)
    print("\nНотатки збережено.\n")


###############################################################################################################################
##   Далі просто тестова прога.  ##############################################################################################

notes_book = Notes()

load_note_book() # Загрузка.

###### Приклади синтаксису створення  та редагування нотаток.##################################################################

name = "nina"
note = "Полюбляє катосити велосипедом, не вживає спіртного"
teg = "Car"
make_note(name, note, teg)

make_note(None, " Були були на селі", "Літак")    # Зробив нову нотатку.
make_note("Вова", " Гуляли на селі", "Гуляли")   # Зробив нову нотатку.
make_note("Оля", " Жили у селі", "Жили")         # Зробив нову нотатку.
make_note(None, " Були були у славному місті Тернопіль", "Тернопіль")  # Зробив нову нотатку.

notes_book.search_by_tegs("Літак")  # Пошук за тегом "Літак". Виведе усі нотатки але спершу відсортує по кількості збігів.
notes_book.search_by_global("були")  # Пошук за текстом "були" по всіх полях. Виведе усі нотатки але спершу відсортує по кількості збігів.

print(notes_book)           # Просто розпечатає форматом весь список нотаток. У методі описано вже формат виводу.

notes_book.delete_note(6)   # Видалить нотатку № 6, якщо номера нема напише про це, якщо ввести не число буде помилка потребує декоратора.
notes_book.delete_note(6)   # Також видалить бо вони змістяться, якщо номера нема напише про це.

show_notes()      # Якщо нічого не ввести, 
show_notes('qwe') # або не число то тоді виведе усі ноатки за один раз.

show_notes(5)     # Виводить по 5 нотаток за раз.
show_notes('5')   # Виводить по 5 нотаток за раз.

bot_add_teg("teg_text TEST", 3)             # Добавить тег "teg_text TEST" до нотатки номер 3
bot_change_teg("teg_text_rewrite_TEST", 3)  # Замінить теги новим тегом "teg_text_rewrite_TEST" у нотатки номер 3

bot_change_text_note("note_text change_text_note", 10)  # Замінить текст нотатки на текст  note_text change_text_not.
bot_add_text_note("+ add text note TEST", 10)           # Добавить текст "+ add text note TEST" до тексту "note_text change_text_note"  
                                                        # та отримаємо "note_text change_text_note + add text note TEST".

notes_book.sorted_data() # Відсортує за часом створення. Спочатку останні а в кінці ті що давно створені.

show_notes()     # Покаже усі нотатки.

save_note_book() # Збереження словника.

###############################################   ВСЕ ГОТОВО   ################################################################################