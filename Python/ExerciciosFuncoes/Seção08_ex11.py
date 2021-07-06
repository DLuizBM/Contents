def media_das_notas(*args):
    total = 0
    media_final = 0

    for num in range(0, len(args) - 1):
        total = total + args[num]
    if args[len(args) - 1] == 'a':
        media_final = total / 3
    elif args[len(args) - 1] == 'p':
        media_final = total / 2
    print(f'A média final é: {media_final}.')


media = 'a'
lista = [7, 8, 9]

media_das_notas(*lista, media)
# Passando a *lista e média, o args irá transformar tudo em uma tupla que será a seguinte:
# (7, 8, 9, 'a')



