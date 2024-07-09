# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o
# usuário venceu ou perdeu.

from random import randint
from time import sleep
numero = randint(1,5)
print('-=-' * 20)
print('Vou pensar em um numero de 1 a 5. Tente adivinhar...')
print('-=-' * 20)
chute = int(input("Chute um número inteiro entre 1 a 5: "))
print('Analisando....')
sleep(3)
if numero == chute:
        print(f'PARABÉNS!Voce me venceu!')
else:
    print(f'Ganhei! Eu pensei no numero {numero} e nao no {chute}!')