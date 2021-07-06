"""
Teste de velocidade

# Generators

def nums():
    for num in range(1, 10):
        yield num

ge1 = nums()
print(ge1)
print(next(ge1))
print(next(ge1))

# Generator expression
ge2 = (num for num in range(1, 10))

print(ge2)
print(next(ge2))
print(next(ge2))

"""
# Realizando teste de velocidade
import time

# Generators
gen_ini = time.time()
print(sum(num for num in range(1000000)))
gen_tempo = time.time() - gen_ini

# List Comprehension
list_ini = time.time()
print(sum([num for num in range(1000000)]))
list_tempo = time.time() - list_ini

print(f'Generator: {gen_tempo}')
print(f'List comprehension: {list_tempo}')

# O tempo gasto pelo Generator é menor do que o tempo do List comprehension



