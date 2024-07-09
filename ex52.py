# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
tot = 0
num = int(input('Digite um numero para verificação de numeros primos: '))
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print(c, end=' ')
print()
print(f'O numero {num} foi divisivel {tot} vezes!')
if tot == 2:
    print(f'E por isso ele é PRIMO!')
else:
    print(f'E por isso ele NÃO É PRIMO!')