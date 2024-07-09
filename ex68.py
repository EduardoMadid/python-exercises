# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
print('-=' * 30)
print('Vamos jogar PAR ou IMPAR!')
print('-=' * 30)
v = 0
while True:
    computador = randint(0,10)
    jogador = int(input('Diga um valor: '))
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}! Total de {soma}', end=' ')
    print('DEU PAR!' if soma % 2 == 0 else 'DEU IMPAR!')
    print('-=' * 30)
    if tipo == 'P':
        if soma % 2 == 0:
            print(f'Você \033[32m VENCEU!\033[m')
            v += 1
        else:
            print('Voce \033[31mPERDEU!\033[m')
            break
    elif tipo == 'I':
        if soma % 2 == 1:
            print(f'Voce \033[32m VENCEU!\033[m')
            v += 1
        else:
            print('Voce \033[31mPERDEU!\033[m')
            break
    print('-=' * 30)
    print('VAMOS JOGAR NOVAMENTE!')
    print('-=' * 30)
print('-=' * 30)
print(f'\033[31mGAME OVER!\033[m Voce venceu {v} vezes!')