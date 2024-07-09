# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
numero = int(input("Digite um número: "))
n = str(numero)
print(f'Analisando o numero {numero}...')
print(f'A unidade desse número é {n[3]}')
print(f'A dezena desse número é {n[2]}')
print(f'A centena desse número é {n[1]}')
print(f'A milhar desse número é {n[0]}')