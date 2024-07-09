# Exercício Python 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input("Digite um numero inteiro: "))
if num % 2 == 0:
    print(f'O número {num} é par!')
else:
    print(f'O numéro {num} é impar!')