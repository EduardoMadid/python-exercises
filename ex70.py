# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:
#
# A) qual é o total gasto na compra.
#
# B) quantos produtos custam mais de R$1000.
#
# C) qual é o nome do produto mais barato.

print('-' * 20)
print('LOJA SUPER BARATÃO')
print('-' * 20)
total = totmil = cont = menor = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 20)
print('FIM DO PROGRAMA')
print('-' * 20)
print(f'O total da compra foi {total:.2f}!')
print(f'Temos {totmil} produtos custando mais que R$1000,00!')
print(f'O produto mais barato foi {barato} que custa {menor}!')

