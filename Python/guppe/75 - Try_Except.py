"""
TRY EXCEPT
Usamos try e except para tratar erros que podem ocorrer no nosso código. Previnindo
assim que o programa pare de funcionar e o usuário receba mensagens de erro inesperadas.

A forma geral mais simples é:

try:
    // execução problemática
except:
    // o que deve ser feito em caso de problema


# Exemplo1 - Tratando erro genérico

try:
    soma()
    # a função soma não foi definida, NameError.
except:
    print("OPS! Um problema foi encontrado, por favor contate o suporte.")
# Tente executar a função, caso encontre algum problema. Trate o erro.
# OBS: Tratar erro de forma genérica não é a melhor forma, o ideal é tratar de forma
específica

# Exemplo 2 - Tratando erro de forma específica

try:
    soma()
except NameError:
    print("Você está usando uma função inexistente.")

# Exemplo 3 - Tratando erro de forma específica

try:
    len(5) # Type erro
except TypeError: # NameError como foi especificado que é um TypeError e em except NameError, o erro não vai ser tratado
                  # deve mudar para TypeError
    print("Função len não funciona com o tipo int.")


# Exemplo 4 - Tratando erro de forma específica

try:
    len(5)
except TypeError as err:
    print(f"A aplicação gerou o seguinte erro: {err}")
    # mensagem que vai aparecer por causa de err -> object of type 'int' has no len()


try:
    dic = {'a': 1}
    print(dic['b'])
except NameError as erra:
    print(f"A aplicação gerou o seguinte erro: {erra}")
except TypeError as errb:
    print(f"A aplicação gerou o seguinte erro: {errb}")
except IndexError as errc:
    print(f"A aplicação gerou o seguinte erro: {errc}")
except:
    print("Um erro diferente foi gerado.")
# É possível colocar diversas excessões de erro.

"""
# Exemplo com função


def pega_valor(dicionario, a):
    try:
        return f"{dicionario[a]}"
    except KeyError:
        return None
    # Tente impŕimir com a chave passada, caso não consiga, retorne None
    except TypeError:
        return None
    # Tente imprimir esse dicionário, se não for dicionário, retorne None


dic = {'a': 10}
print(pega_valor(dic, 'b'))
# print(dic['b'])
# KeyError: a chave que estamos tentando acessar no dicionário,não existe
