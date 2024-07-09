#  Crie um programa onde o usuário possa digitar sete valores numéricos
#  e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#  No final, mostre os valores pares e ímpares em ordem crescente.

num = [[], []]
valor = 0
for i in range(1, 8):
    valor = int(input(f'Digite o {i}o. valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=' * 30)
print(f'Todos os valores: {num}')
print(f'Os valores pares são: {sorted(num[0])}')
print(f'Os valores impares são: {sorted(num[1])}')
