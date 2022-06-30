"""
Parâmetros somento posicionais
"""
def cumprimentar_v1(nome):
    return f"Olá, {nome}!"

print(cumprimentar_v1(nome="Messi"))
# É possível chamar a função passando a chave (nesse caso, nome)


def cumprimentar_v2(nome, /):
    return f"Olá, {nome}!"

# print(cumprimentar_v2(nome="Messi"))
# Esse modo irá gerar um erro, pois a função só aceita argumentos posicionais, isso é, somente o argumento.
print(cumprimentar_v2("Messi"))

def cumprimentar_v3(nome, /, mensagem):
    return f"{mensagem}, {nome}!"
# Dessa forma, somente o parâmetro nome é posicional.
print(cumprimentar_v3("Messi", mensagem="Hola"))

def cumprimentar_v4(nome, mensagem, /): # A barra indica que tudo que está antes dela é posicional
    return f"{mensagem}, {nome}!"
print(cumprimentar_v3("Messi", "Hola"))

# * obriga que todo parâmetro após ele, deve ter a chave informada.
def cumprimentar_v5(*, nome):
    return f"Olá, {nome}!"

print(cumprimentar_v5(nome="Lionel"))

# Juntando tudo
def cumprimentar_v6(nome, /, mensagem, *, fim):
    return f"{mensagem}, {nome}{fim}"
# nome é posicional, mensagem pode ou não receber a chave do parâmetro, fim deve obrigatoriamente receber a chave do parâmetro, fim
print(cumprimentar_v6("Lionel", "Hola", fim="!!!"))