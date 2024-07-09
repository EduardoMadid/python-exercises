# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar
# mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('=' * 20)
print('PROGRESSÃO DE UMA P.A.')
print('=' * 20)
primeiro = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
cont = 0
mais = 10
total = 0

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{primeiro} --> ', end='')
        primeiro += razao
        cont += 1
    print('PAUSA!', end='')
    print()
    mais = int(input('Deseja mostrar quantos termos a mais? '))
print(f'Progressão finalizada com {total} termos!')
