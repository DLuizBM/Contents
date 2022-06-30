from datetime import date
from utils.helper import date_to_str, str_to_date

class Client:

    count: int = 101

    def __init__(self: object, name: str, email: str, cpf: str, birthday: str) -> None:
        self.__name: str = name
        self.__cpf: str = cpf
        self.__birthday: str = str_to_date(birthday)
        self.__email: str = email
        self.__code: int = Client.count
        self.__register: date = date.today() 
        Client.count += 1

        
    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def name(self: object) -> str:
        return self.__name

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def birthday(self: object) -> str:
        return date_to_str(self.__birthday)

    @property
    def email(self: object) -> str:
        return self.__email

    @property
    def register(self: object) -> str:
        return self.__register

    def __str__(self: object) -> str:
        return f"Código: {self.code} \nName: {self.name}"\
                "\nData de nascimento: {self.birthday} "\
                "\nData de cadastrado: {self.register}"
