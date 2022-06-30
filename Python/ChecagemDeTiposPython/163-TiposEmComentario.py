def cabecalho1(texto):
    # type: (str) -> str
    # forma de especificar o tipo de entrada e tipo de retorno, type: (str) -> str, não um comentário comum
    return texto

print(cabecalho1("Hello"))

def cabecalho2(texto, centralizar):
    # type: (str, bool) -> str
    return f"{texto} {centralizar}"

print(cabecalho2("Hello", True))


def cabecalho3(
    texto, # type: str
    alinhamento=True, # type: bool
    teste="" # type: str 
): # type: (...) -> str
    # o ultimo parâmetro não precisa de vírgula separando o parâmetro do type
    if alinhamento: 
        return 'a ' + texto + " " + teste
    else: 
        return 'b ' + texto + " " + teste

print(cabecalho3("Hello", False, "Teste"))

# Declaração de variável, type hinting e comentário de

nome = "Lionel Messi" # type: str