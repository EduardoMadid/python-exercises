# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros:
# início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}!')

    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' -> ')
            sleep(0.2)
            cont += p
        print('FIM!')
        print('-=' * 30)
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' -> ')
            cont -= p
            sleep(0.2)
        print('FIM!')
        print('-=' * 30)

contador(1,10,1)
contador(10, 0, 2)

print("Agora é SUA VEZ:")
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo a passo: '))
contador(inicio, fim, passo)
