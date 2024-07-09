# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’,
# o programa se encerrará.
# Importante: use cores.

from time import sleep


c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[0;30m')


def titulo(txt, cor=0):
    print(c[cor], end='')
    print('-=' * 20)
    print(f'{txt:^40}')
    print('-=' * 20)
    print(c[0], end='')
    sleep(1)


def pulaLinha():
    print('-=' * 30)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'!', 4)
    print(c[5], end='')
    print(help(com))
    print(c[0], end='')
    sleep(2)


while True:
    titulo('SISTEMA DE AJUDA PYHTON', 2)
    msg = str(input('FUNÇÃO OU BIBLIOTECA > '))
    ajuda(msg)
    resp = str(input('Quer pesquisar outro comando? [S] [N]: ')).strip().upper()[0]
    if resp in 'N':
        titulo('TCHAU! Obrigado por Utilizar do programa de AJUDA!', 1)
        break
