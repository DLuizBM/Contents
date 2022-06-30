"""
Type hinting - Forma para tipar um valor em python

# Vantagens
1 - Facilita o processo de descoberta de errros
2 - Melhora a documentação do código
3 - Programação python avançada

# Desvantagens
1 - Recurso totalmente completo somente a partir da versão 3.7
2 - Queda da performance do python


# variável: tipo -> tipo de retorno
def salute(salute: str) -> str:
    return f"Hello, {salute}"


print(salute("World"))
"""
def cabecalho(text: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f" {text.title()} ".center(50, "#")
        # center coloca a string text no centro e completa com # até chegar a 50 carcteres

print(cabecalho("It is a little text"))
print(cabecalho("It is a little text", False))