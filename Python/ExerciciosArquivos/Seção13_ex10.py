from operator import itemgetter

# Separando os nomes das cidades
with open('arquivo_teste.txt', 'r') as arquivo:
    cidades = []
    linha = arquivo.readline()
    while linha:
        cidade = ''
        i = 0
        while linha[i] != ':' and linha[i] != '\n':
        # Por que é necessário o '\n' para não ter erro????
        # o cursor sempre da um '\n' no fim no arquivo (após uma leitura), lembrar que '\n' é um caractere
            cidade = cidade + linha[i]
            i = i + 1
        cidades.append(cidade)
        linha = arquivo.readline()

res = list(filter(lambda cidade: cidade != '', cidades))
print(res)

# Separando o número de habitantes das cidades
with open('arquivo_teste.txt', 'r') as arquivo:
    habitantes = []
    linha = arquivo.readline()
    while linha:
        num = ''
        for carac in linha:
            if carac == ':':
                for i in range(linha.index(carac) + 2, len(linha)):
                    if linha[i] != '.' and linha[i] != '\n':
                    # saída sem linha[i] != '\n' : ['12000000\n', '3000000\n', '6320000\n', '9237000\n', '21000000\n', '', '', '', '']
                        num = num + linha[i]
        linha = arquivo.readline()
        habitantes.append(num)

res2 = list(filter(lambda num: num != '', habitantes))
res2 = list(map(lambda num: float(num), res2))
print(res2)

# Criando um dicionário para agrupar cada cidade com seu número de habitantes

cid_hab = {}

for i in range(0, len(res)):
    novo = {res[i]: res2[i]}
    cid_hab.update(novo)

max_chave = ''
for chave, valor in cid_hab.items():
    if valor == max(cid_hab.values()):
        max_chave = chave

print(f'A cidade com mais habitantes é {max_chave} com {cid_hab[max_chave]} habitantes.')
cidades = sorted(cid_hab.items(), key=itemgetter(1), reverse=False)
# itemgetter faz o sorted organizar por chave ou valor, se for 0, chave, se um valor
cidades = dict(cidades)

for chave, valor in cidades.items():
    print(f'{chave} : {valor}')
