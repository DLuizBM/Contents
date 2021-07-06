"""
Set comprehensions

Sintaxe:
{num for num in iterável}

"""

print({num for num in range(0, 5)})
print({print(f'par {str(num)} ', end='') if num % 2 == 0 else print(f'impar {str(num)} ', end='') for num in range(10)})