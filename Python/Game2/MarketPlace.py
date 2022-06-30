from typing import List, Dict
from time import sleep
from models.product import Product
from utils.helper import format_float_str_coin

products: List[Product] = []
cart: List[Dict[Product, int]] = []

def main() -> None: 
    menu()

def menu() -> None: 
    print("================")
    print("==Bem-vindo(a)==")
    print("======Shop======")

    print("Selecione uma das seguintes opções:")

    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Comprar produtos")
    print("4 - Visualizar carrinho")
    print("5 - Fechar pedido")
    print("6 - Sair")

    option: int = int(input())

    if option == 1:
        register_product()
    elif option == 2:
        list_products()
    elif option == 3:
        buy_product()
    elif option == 4:
        view_cart()
    elif option == 5:
        close_order()
    elif option == 6:
        print("Saindo do sistema")
        print("Volte sempre :)!")
        exit(0)
    else:
        print("Opção inválida.")
        menu()

def register_product() -> None: 
    print("Cadastro de Produto")
    print("===================")

    name: str = input("Informe o nome do produto: ")
    price: float = float(input("Informe o valor do produto: "))

    product: Product = Product(name, price)

    products.append(product)

    print(f"Produto {product.name} cadastrado com sucesso!")
    menu()

def list_products() -> None: 
    if len(products) > 0:
        print("Listagem de produtos")
        for product in products:
            print(product)
    else:
        print("Não existem produtos cadastrados.")
    menu()

def buy_product() -> None: 
    if len(products) > 0:
        print("Informe o código do produto que deseja adicionar.")
        print("=================================================")
        for product in products:
            print(product)
            print("================================================")

        code: int = int(input())
        product: Product = get_product_by_code(code)
        if product:
            if len(cart) > 0:
                is_in_cart: bool = False
                for item in cart:
                    if product in item:
                        is_in_cart = True
                        for product, quantity in item.items():
                            item[product] = quantity + 1
                        break
                    
                if not is_in_cart:
                    newProduct = {product: 1}
                    cart.append(newProduct)
                    print(f"O produto {product.name} foi adicionado com sucesso")
                    menu()
            else:
                item = {product: 1}
                cart.append(item)
                print(f"O produto {product.name} for adicionado ao carrinho.")
                menu()
        else:
            print("O produto com código {code} não foi encontrado")
            menu()

    else:
        print("Não existem produtos cadastrados.")
    menu()

def view_cart() -> None: 
    if len(cart) > 0:
        print("Produtos no carrinho")
        for item in cart:
            for data in item.items():
                print(data[0])
                print(f"Quantidade: {data[1]}")
                print("===============================")
                sleep(1)
    else:
        print("Não exitem produtos no carrinho")
    menu()

def close_order() -> None: 
    if len(cart) > 0:
        total_value: float = 0
        print(cart)
        for item in cart:
            for productName, numberOfProducts in item.items():
                print(productName)
                print(f'Quantidade: {numberOfProducts}')
                total_value += productName.price * numberOfProducts

        print(f"Sua fatura é {format_float_str_coin(total_value)}")
        cart.clear()
    else:
        print("Não existem produtos no carrinho")
    menu()

def get_product_by_code(code: int) -> None: 
    productFound: Product = None

    for product in products:
        if product.code == code:
            productFound = product
            break
    return productFound

if __name__ =='__main__':
    main()