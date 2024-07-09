#  Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#  O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números
#  entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint

jogos = list()
lista = list()

print('-' * 30)
print('      Jogo da MEGA SENA!      ')
print('-' * 30)
quant = int(input('Quantos jogos gostaria que eu sorteie? '))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f'Sorteando {quant} JOGOS!', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')