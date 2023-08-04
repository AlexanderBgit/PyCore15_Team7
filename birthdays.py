from datetime import datetime, timedelta


# додаємо метод класу AddressBook():
def bd_in_period(self, period: int):
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

# додаємо функцію виклику команди "period [n]", задекорована
@input_error
def contacts_in_period(period: int) -> str:
    result = ab.bd_in_period(int(period)) #ab = AddressBook()
    if result:
        return "\n".join(str(record) for record in result)
    else:
        return f"No birthdays in {period} days"
    
# не забуваємо додати команду 'period' в словник команд 
# обовʼязково додаємо інструкцію до команди 'period' в наш help

