# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que
# vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []

while True:
    num = (int(input('Digite um valor: ')))
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = str(input('Deseja continuar : [S] [N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print('-=' * 30)
print(f'A lista completa é de {lista}!')
print(f'A lista dos PARES é {pares}!')
print(f'A lista dos IMPARES é {impares}!')