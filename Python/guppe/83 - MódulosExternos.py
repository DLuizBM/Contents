"""
Módulos externos

Utilizamos o Pip - Python installer package
Para instalar basta entrar no terminal e digitar: pip install pacote
pacotes oficiais do python - acessa o site pypi.org

Como exemplo, importei o pacote colorama, que permite mudar a cor do terminal
"""
from colorama import init
init()
from colorama import Fore

print(Fore.RED, "Olá mundo")