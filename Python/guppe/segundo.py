import primeiro

def fun2():
    primeiro.func1()


if __name__ == '__main__':
    fun2()
    print('segundo foi executado diretamente')
else:
    print('Segundo foi importado')
    print(f'{__name__}')