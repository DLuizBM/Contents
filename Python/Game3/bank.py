from typing import List
from models.client import Client
from models.bankAccount import Account

accounts: List[Account] = []

def main() -> None:
    menu()

def menu() -> None:
    print("================")
    print("==Bem-vindo(a)==")
    print("======ATM======")

    print("Selecione uma das seguintes opções:")

    print("1 - Criar conta")
    print("2 - Efetuar saque")
    print("3 - Efetuar depósito")
    print("4 - Efetuar transferância")
    print("5 - Listar contas")
    print("6 - Sair")

    option: int = int(input())

    if option == 1:
        create_account()
    elif option == 2:
        withdraw()
    elif option == 3:
        deposit()
    elif option == 4:
        transfer()
    elif option == 5:
        list_accounts()
    elif option == 6:
        print("Saindo do sistema")
        print("Volte sempre :)!")
        exit(0)
    else:
        print("Opção inválida.")
        menu()

def create_account() -> None:
    print("Informe os dados do cliente.")

    name: str = input("Nome do cliente: ")
    email: str = input("Email do cliente: ")
    cpf: str = input("CPF do cliente: ")
    birthday: str = input("Data de nascimento do cliente: ")

    client: Client = Client(name, email, cpf, birthday)

    account: Account = Account(client)

    accounts.append(account)

    print("Conta criada com sucesso.")
    print("Dados da conta: ")
    print(account)
    menu()


def withdraw() -> None:
    if len(accounts) > 0:
        account_number: int = int(input("Informe o número da conta: "))

        account: Account = search_account_by_number(account_number)

        if account:
            value: float = float(input("Informe o valor do saque: "))
            account.withdraw_money(value)
        else:
            print(f"Não foi encontrada a conta com número {account_number}")
    else:
        print("Ainda não existem contas cadastradas.")
    menu()


def deposit() -> None:
    if len(accounts) > 0:
        account_number: int = int(input("Informe o número da conta para depósito: "))

        account: Account = search_account_by_number(account_number)

        if account:
            value: float = float(input("Informe o valor do depósito: "))
            account.deposit_money(value)
        else:
            print(f"Não foi encontrada a conta com número {account_number}")

    else:
        print("Ainda não existem contas cadastradas.")
    menu()

def transfer() -> None:
    if len(accounts) > 0:
        origin_account_number: int = int(input("Informe o número da sua conta: "))
        origin_account: Account = search_account_by_number(origin_account_number)

        if origin_account:
            destination_account_number: int = int(input("Informe o número da conta de destino: "))
            destination_account: Account = search_account_by_number(destination_account_number)

            if destination_account:
                value: float = float(input("Informe o valor da transferância: "))
                origin_account.transfer_money(destination_account, value)
            else:
                print(f"Não foi encontrada a conta de destino com número {origin_account_number}")
                menu()
        else:
            print(f"A sua conta, com número {origin_account_number},  não foi encontrada.")
            menu()

    else:
        print("Ainda não existem contas cadastradas.")
    menu()

def list_accounts() -> None:
    if len(accounts) > 0:
        for account in accounts:
            print(account)
    else:
        print(f"Não existem contas cadastradas.")
    menu()

def search_account_by_number(number: int) -> Account:
    wanted_account: Account = None

    if len(accounts) > 0:
        for account in accounts:
            if account.account_number == number:
                wanted_account = account
                break
    return wanted_account


if __name__ == '__main__':
    main()