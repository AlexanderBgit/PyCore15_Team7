

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
        return f"Incorrect birthday: {self.value}. Date of birth must be one of the formats: '11-11-1111', '11.11.1111' or '11/11/11'"


class EmailError(Exception):
    def __init__(self, value, *args: object) -> None:
        super().__init__(*args)
        self.value = value

    def __str__(self) -> str:
        return f"Incorrect email: {self.value}. Email must match a pattern: 'email@domain.dom'."


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError as ex:
            return ex
        except ValueNeedEnterError as ex:
            return ex
        except FindRecordError as ex:
            return ex
        except PhoneError as ex:
            return ex
        except BirthdayError as ex:
            return ex
        except EmailError as ex:
            return ex
    
    return wrapper
