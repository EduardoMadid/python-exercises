#  Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#  Depois disso, mostre a listagem de números gerados e também indique o menor e o maior
#  valor que estão na tupla.

from random import randint
numeros = (randint(1, 10), randint(1, 10),
randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: ')
for n in numeros:
    print(f'{n}', end=' -> ')
print('final')
print(f'O maior valor sorteado foi {max(numeros)} e o menor foi {min(numeros)}!')