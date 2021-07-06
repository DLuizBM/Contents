"""
Decoradores(decorators)
- Decorators são funções;
- Decorators envolvem outras funções e aprimoram seus comportamentos;
- Decorators são funções de HOF
- Decorator tem uma sintaxe própria, usando @ (syntact sugar / açucar sintático)



# Exemplo (sintaxe não recomendada / sem syntact sugar)


def seja_educado(funcao): # seja_educado é a função decorator, estamos decorando a função saudação
    def sendo():
        print('Foi um prazer conhecer você')
        funcao()
        # notar que o funcao, vai receber o nome da função passada
        print('Tenha um ótimo dia')
    return sendo
    # passando a função e não a execução


def saudacao():
    print('Seja bem vindo(a).')
# decorando a função saudação com educação, aprimorando a função saudação

teste = seja_educado(saudacao)
teste()

# Exemplo 2 - Decorando a função raiva

def raiva():
    print("Que raiva!!!")

teste = seja_educado(raiva)
teste()


# Com sintaxe recomendada

def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente mesmo')
    return sendo

@seja_educado # indica que seja_educado está decorando o função apresentando
def apresentando():
    print('Meu nome é Hamilton!!')

# Testando 1
apresentando()

# Testando 2

@seja_educado
def dormir():
    print('Quero dormir!!')

dormir()

Exemplo de uso em web (não funcional):

def checa_login(): #decorator function
    if not request.usuário:
        redirect('http://www.suaempresa.com/login')

def home(request):
    return 'Pode acessar a home'

@checa_login #decorator
def admin(request):
    return 'Pode acessar admin'

- Quando chegar em admin, será executado o decorator para saber se o quem está tentando acessar
admin é administrador ou usuário, se for administrador terá acesso, se não será enviado para o site
especificado



"""


def colocar(funcao):
    def colocando(*args, **kwargs):
        funcao(args[0])
        print('Vamos colocar a cor vermelha no seu carro.')
    return colocando


@colocar
def carro(cor):
    print(f'Quero colocar a cor {cor} no meu carro.')


carro('vermelha')



