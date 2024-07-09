# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for i in range(1, 7):
    numero = int(input(f'Digite  o {i} número inteiro: '))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print(f'Tem {cont} numeros PARES e a soma dos pares é {soma}!')


