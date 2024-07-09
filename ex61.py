# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('=' * 20)
print('PROGRESSÃO DE UMA P.A.')
print('=' * 20)
primeiro = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
cont = 0
while cont <= 10:
    print(f'{primeiro} --> ', end='')
    primeiro += razao
    cont += 1
print('FIM!')
