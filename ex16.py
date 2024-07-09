# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
numero = float(input("Digite um numero: "))
print('O numero é {}, apenas a parte inteira dele é {}'.format(numero, trunc(numero)))
# pode usar tbm o int(numero)