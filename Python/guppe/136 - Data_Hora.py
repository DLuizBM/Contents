"""
Manipulando Data e Hora
Python tem um módulo built-in chamado datetime



import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)

# retorno de data e hora atual
# dentro de datetime temos a classe datetime
# dentro dessa classe temos o método now()
print(datetime.datetime.now())
# 2020-05-11 20:41:24.858353

# Representação com o método repr
print(repr(datetime.datetime.now()))
# datetime.datetime(2020, 5, 11, 20, 50, 29, 836296)

# replace() para fazer ajustes na data e hora
init = datetime.datetime.now()
print(init.replace(year=1995, month=8, day=1, hour=16, minute=7, second=45, microsecond=1))



import datetime

evento = datetime.datetime(2020, 1, 1)
print(evento)

nascimento = input("Informe o nascimento (dd/mm/yy): ")
nascimento = nascimento.split('/')
print(nascimento)
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)

"""
# Acesso individual dos elementos de data e hora

import datetime

evento = datetime.datetime.now()
print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)