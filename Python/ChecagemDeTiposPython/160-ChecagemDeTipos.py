"""
instalando o mypy
py -3 -m pip install mypy
Usar o comando py -3 -m pip install package, no windows.
"""

def cabecalho(text: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "#")
        # center coloca a string text no centro e completa com # até chegar a 50 carcteres

print(cabecalho("It is a little text"))
print(cabecalho("It is a little text", alinhamento=False))

# para executar o mypy
# & C:\Users\bbcar\AppData\Local\Programs\Python\Python39\Scripts\mypy.exe .\160-ChecagemDeTipos.py