# Desenvolva um programa que leia quatro valores pelo teclado
# e guarde-os em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
#
# B) Em que posição foi digitado o primeiro valor 3.
#
# C) Quais foram os números pares.

n = (int(input('Digite um número: ')), int(input('Digite outro número: '))
     ,int(input('Digite mais um número: ')), int(input('Digite o último número: ')))

print('-=' * 30)
print(f'Os valores digitados foram:\n{n}')
print('-=' * 30)
print(f'O valor 9 apareceu {n.count(9)} vezes!')

if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3) + 1} posição!')
else:
    print(f'O valor 3 nao foi digitado!')

print(f'Os valores PARES digitados foram ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end=' ')
