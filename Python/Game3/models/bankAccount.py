from models.client import Client
from utils.helper import format_float_str_coin

class Account:

    code: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__account_number: int = Account.code
        self.__client: Client = client
        self.__bank_balance: float = 0.0
        self.__limit: float = 100.00
        self.__total_balance: float = self.__calculate_total_balance
        Account.code += 1
    
    @property
    def account_number(self: object) -> int:
        return self.__account_number
    
    @property
    def client(self: object) -> Client:
        return self.__client
    
    @property
    def bank_balance(self: object) -> float:
        return self.__bank_balance
    
    @bank_balance.setter
    def bank_balance(self: object, value: float) -> None:
        self.__bank_balance = value

    @property
    def limit(self: object) -> float:
        return self.__limit

    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value

    @property
    def total_balance(self: object) -> float:
        return self.__total_balance

    @total_balance.setter
    def total_balance(self: object, value: float) -> None:
        self.__total_balance = value

    @property
    def __calculate_total_balance(self: object) -> float:
        return self.__limit + self.__bank_balance  

    def __str__(self: object) -> str:
        return f"Número da conta: {self.account_number}\n" \
               f"Cliente: {self.client.name}\n" \
               f"Saldo total: {format_float_str_coin(self.total_balance)}\n" \
                      
    def deposit_money(self: object, value: float) -> None:
        if value > 0:
            self.bank_balance = self.bank_balance + value
            self.total_balance = self.__calculate_total_balance
            print("Depósito efetuado com sucesso!")
        else:
            print("Erro ao efetuar depósito. Tente novamente.")

    def withdraw_money(self: object, value: float) -> None:
        if value > 0 and self.total_balance >= value: 
            if self.bank_balance >= value: 
                self.bank_balance = self.bank_balance - value
                self.total_balance = self.__calculate_total_balance
            else:
                rest: float = self.bank_balance - value
                self.limit = self.limit + rest
                self.bank_balance = 0
                self.total_balance = self.__calculate_total_balance
            print("Saque efetuado com sucesso!")
        else:
            print("Saque não realizado. Tente novamente.")

    def transfer_money(self: object, destination_account: object,  value: float) -> None:
        if value > 0 and self.total_balance >= value: 
            if self.bank_balance >= value: 
                self.bank_balance = self.bank_balance - value
                self.total_balance = self.__calculate_total_balance
                destination_account.bank_balance = destination_account.bank_balance + value
                destination_account.total_balance = destination_account.__calculate_total_balance
                print("Transferência realizada com sucesso.")
            else: 
                rest: float = self.bank_balance - value
                self.limit = self.limit + rest
                self.bank_balance = 0
                self.total_balance = self.__calculate_total_balance
                destination_account.bank_balance = destination_account.bank_balance + value
                destination_account.total_balance = destination_account.__calculate_total_balance
                print("Transferência realizada com sucesso.")
        else:
            print("Transferência não realizada. Tente novamente.")

