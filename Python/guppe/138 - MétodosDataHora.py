"""
Métodos de data e hora

import datetime

# com now() podemos especificar um time zone (fuso horário)
agora = datetime.datetime.now()
print(agora)

hoje = datetime.datetime.today()
print(hoje)


import datetime
# mudanças ocorrendo à meia-noite
# método combine()
//timedelta pega a diferença entre 2 datas
// ex: se now() for 11-12-2020 e timedelta days=1
// a soma vai ser 12-12-2020, timedelta está somando 1 dia à data atual
maintenance = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())
# datetime.time(), quando sem argumentos, coloca horas, minutos e segundo como 0
# combine(), combina tudo que foi passado.
print(maintenance)
# 2020-05-13 00:00:00
# vai adicionar 1 dia e contanda a partir da hora 00:00:00


import datetime

# encontrar o dia da semana, weekday()

maintenance = datetime.datetime.combine(datetime.datetime.now() + datetime.timedelta(days=1), datetime.time())
print(maintenance.weekday())
# weekday() retorna o dia em que o evento ocorre, ocorreu, ocorrerá
# a representação é feita por números, sendo Monday = 0 ... Sunday = 6


import datetime


birth = input('Enter the day of your birth (dd/mm/yyyy): ')
birth = birth.split('/')
birth = datetime.datetime(int(birth[2]), int(birth[1]), int(birth[0]))
print(birth)

if birth.weekday() == 0:
    print('You were born on sunday')
elif birth.weekday() == 1:
    print('You were born on monday')
elif birth.weekday() == 2:
    print('You were born on tuesday')
elif birth.weekday() == 3:
    print('You were born on wednesday')
elif birth.weekday() == 4:
    print('You were born on thursday')
elif birth.weekday() == 5:
    print('You were born on friday')
else:
    print('You were born on saturday')


import datetime

# formantando datas/horas com strftime() (string format time)
# dd/mm/yy hora:minuto

today = datetime.datetime.today()
print(today)

new_today = today.strftime('%d/%m/%Y')
# y minúsculo devolve somento os últimos 2 dígitos do ano
# há várias configurações do strftime que podem ser vistas na documentação
print(new_today)


import datetime


def data(data):
    if data.month == 1:
        return f'{data.day} de Janeiro de {data.year}'
    elif data.month == 2:
        return f'{data.day} de Fevereiro de {data.year}'
    elif data.month == 3:
        return f'{data.day} de Março de {data.year}'
    elif data.month == 4:
        return f'{data.day} de Abril de {data.year}'
    elif data.month == 5:
        return f'{data.day} de Maio de {data.year}'


today = datetime.datetime.today()
print(data(today))


import datetime
print(datetime.timedelta(days=1) + datetime.datetime.now())
print(datetime.datetime(year=1995, month=8, day=1))

import datetime

hoje = datetime.datetime.today()
#strftime formata de acordo com a forma desejada
print(hoje.strftime('%d/%m/%Y'))
print(hoje.strftime('%d/%B/%Y')) # B devolve o nome do mês, b apenas as iniciais


from textblob import TextBlob
import datetime

#  o textblob precisa da internet para fazer a tradução


def get_dateformat(today):
    return f"{today.day} de {TextBlob(today.strftime('%B')).translate(to='pt-br')} de {today.year}"


hoje = datetime.datetime.today()
print(get_dateformat(hoje))



# Transformando string em datetime
import datetime
birthday = datetime.datetime.strptime('01/08/1995', '%d/%m/%Y')
print(birthday)

# Trabalhando somente com hora
lunch = datetime.time(12, 00, 00) # H, M, S
print(lunch)

# Marcando tempo de execução do código com timeit

import timeit

tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)

tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)

tempo = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(tempo)

"""
import timeit, functools


def soma(n):
    sum = 0
    for num in range(n * 200):
        sum = sum + num ** num + 4
    return sum

# partial em  functools testa a função com o seu parâmetro, number repete a quantidade de teste
# útil para testar funções e saber se são performáticas
print(timeit.timeit(functools.partial(soma, 2), number=10000))


