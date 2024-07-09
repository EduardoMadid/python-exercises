# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado
# e as suas respectivas posições na lista.

lista = []
for i in range(1,6):
    lista.append(int(input('Digite um número para ser guardado na lista: ')))

print('-=' * 30)
print(f'A lista completa é {lista}!')
print('-=' * 30)
print(f'O maior valor da lista é {max(lista)} nas posições ', end='')

for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}...', end='')

print()

print(f'O menor valor da lista é {min(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}...', end='')
