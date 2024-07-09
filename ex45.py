# Crie um programa que faça o computador jogar Jokenpô com você.1

from random import randint
from time import sleep

cores = {'vermelho': '\033[1;31m', 'verde': '\033[1;32m', 'amarelo': '\033[1;33m'}

itens = ['pedra', 'papel', 'tesoura']
computador = randint(0,2)
print('''SUAS OPÇÕES:
0 - PEDRA
1 - PAPEL
2- TESOURA''')
jogador = int(input("Qual a sua jogada? "))
if jogador > 2:
    print(f'ERRO DIGITE UM NUMERO VALIDO!')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!!')
    sleep(1)
    print('-=' * 11)
    print(f'COMPUTADOR jogou {itens[computador]}!')
    print(f'JOGADOR jogou {itens[jogador]}!')
    print('-=' * 11)
    print(f'ANALISANDO JOGADA.....')
    sleep(2)
    if computador == 0:
        if jogador == 0:
            print(f'{cores['amarelo']}EMPATE!')
        elif jogador == 1:
            print(f'{cores['verde']}JOGADOR GANHOU!')
        elif jogador == 2:
            print(f'{cores['vermelho']}JOGADOR PERDEU!')

    elif computador == 1:
        if jogador == 0:
            print(f'{cores['vermelho']}JOGADOR PERDEU!')
        elif jogador == 1:
            print(f'{cores['amarelo']}EMPATE!')
        elif jogador == 2:
            print(f'{cores['verde']}JOGADOR GANHOU!')

    elif computador == 2:
        if jogador == 0:
            print(f'{cores['verde']}JOGADOR GANHOU!')
        elif jogador == 1:
            print(f'{cores['vermelho']}JOGADOR PERDEU!')
        elif jogador == 2:
            print(f'{cores['amarelo']}EMPATE!')