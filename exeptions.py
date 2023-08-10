

class FindRecordError(Exception):
    def __init__(self, value, *args: object) -> None:
        super().__init__(*args)
        self.value = value

    def __str__(self) -> str:
        return f"Operation impossible. Can't find record with name {self.value}."


class ValueNeedEnterError(Exception):
    def __init__(self, value, *args: object) -> None:
        super().__init__(*args)
        self.value = value

    def __str__(self) -> str:
        return f"Operation impossible. You must enter {self.value}."


class PhoneError(Exception):
    def __init__(self, value, *args: object) -> None:
        super().__init__(*args)
        self.value = value

    def __str__(self) -> str:
        return f"Incorrect phone: {self.value}. Phone must match a pattern: '+[country][town][number]' (for exemple: '+380661234567' or '+442012345678')"


class BirthdayError(Exception):
    def __init__(self, value, *args: object) -> None:
        super().__init__(*args)
        self.value = value

    def __str__(self) -> str:
        return f"Incorrect birthday: {self.value}. Date of birth must be one of the formats: '11-11-1111'"


class EmailError(Exception):
    def __init__(self, value, *args: object) -> None:
        super().__init__(*args)
        self.value = value

    def __str__(self) -> str:
        return f"Incorrect email: {self.value}. Email must match a pattern: 'email@domain.dom'."

class UnknownFieldError(Exception):
    def __init__(self, value, *args: object) -> None:
        super().__init__(*args)
        self.value = value

    def __str__(self) -> str:
        return f"Unknown field: {self.value}"

class TypeError(Exception):
    def __init__(self, value, *args: object) -> None:
        super().__init__(*args)
        self.value = value

    def __str__(self) -> str:
        return f"Unknown: {self.value}"


# def input_error(func):
#     def wrapper(*args,**kwars):
#         try:
#             return func(*args)
#         except IndexError as ex:
#             return ex
#         except ValueNeedEnterError as ex:
#             return ex
#         except FindRecordError as ex:
#             return ex
#         except PhoneError as ex:
#             return ex
#         except BirthdayError as ex:
#             return ex
#         except EmailError as ex:
#             return ex
#         except UnknownFieldError as ex:
#             return ex
#         except TypeError as ex:
#             if "takes" in str(ex) and "positional arguments but" in str(ex):
#                 print("Помилка: Неправильна кількість аргументів.")
#             return ex
#         except ValueError as ex:
#             return ex
    
#     return wrapper


class MaxArgumentError(ValueError):
    pass

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, FindRecordError, PhoneError, BirthdayError, EmailError, UnknownFieldError, MaxArgumentError) as ex:
            return ex
        except TypeError as ex:
            if "takes from 1 to 3 positional arguments but" in str(ex):
                raise MaxArgumentError("Приймає максимум 3 аргументи: name, note та teg.")
            return ex
    return wrapper