"""
Estruturas lógicas
and, or, not, is

Operadores usuários
not, is

Operadores binários
and, or

"""

ativo = True
logado = False

if ativo and logado:
    print(f"Bem-vindo ao sistema")
else:
    print(f"Confirme seu cadastro.")

if not ativo:
    print(f"Não está ativo / {ativo}")
else:
    print(f"Ativo / {ativo}")
    print(f"{not ativo}")

# Is é usado para fazer uma pergunta sobre uma variável
# No print abaixo é pergunta de logado é Falso, como logado é Falso
# Será printado o valor TRUE, pois logado é falso.
print(logado is False)

