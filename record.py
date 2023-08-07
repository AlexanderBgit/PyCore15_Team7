class Record:
    def __init__(self, name, phone_number, birthday=None):
        self.name = name
        self.phones = [phone_number]
        self.birthday = birthday

    def change_birthday(self, new_birthday):
        self.birthday = new_birthday
        return f"Birthday changed to {new_birthday} for contact {self.name}"
    
    def add_phone(self, phone):
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

    def change_name(self, new_name):
        self.name = new_name
        return f"Name changed to {new_name} for contact {self.name}"

    def __str__(self):
        return f"{self.name}, {', '.join(self.phones)}, {self.birthday}"