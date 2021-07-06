"""
Trabalhando com deltas de data e hora
Delta é a diferença entre a data final e a data inicial


import datetime
data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2020, 8, 1, 0)

delta = aniversario - data_hoje
print(type(delta))
print(repr(delta))
print(delta)
print(delta.days)

# horas
horas = delta.seconds / 3600
min = horas - int(horas)
print(int(horas - min))

# minuto
min = min * 60
seg = min - int(min)
print(int(min - seg))

# segundo
seg = seg * 60
print(round(seg))
# round arredonda para cima

"""
import datetime

data_compra = datetime.datetime.now()
print(data_compra)
regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)
vencimento = data_compra + regra_boleto
print(vencimento)