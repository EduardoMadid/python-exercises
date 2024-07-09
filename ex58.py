#  Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#  Só que agora o jogador vai tentar adivinhar até acertar,
#  mostrando no final quantos palpites foram necessários para vencer.

from random import randint

tent = 1
numero = randint(0,10)
print('-=-' * 20)
print('Vou pensar em um numero de 0 a 10. Tente adivinhar...')
print('-=-' * 20)
acertou = False
while not acertou:
    chute = int(input("Chute um número inteiro entre 0 a 10: "))
    if numero == chute:
        acertou = True
    else:
        tent += 1
        if numero > chute:
            print(f'Tente um numero MAIOR....')
        else:
            print(f'Tente um numero MENOR...')
print(f'PARABÉNS!Voce VENCEU! Com {tent} tentativas!')
