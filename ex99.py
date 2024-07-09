# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*num):
    maior = cont = 0
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print('Analisando os valores passados.........')
    print(f'Foram informados {cont} valores ao todo!')
    print(f'O maior valor encontrado foi {maior}!')

maior(2, 9, 4, 5, 7 , 1)
