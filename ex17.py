# Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triangulo retandulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjascente: "))
h = hypot(co, ca)
print(f'A hipotenusa mede {h:.2f}, o c.a  mede {ca} e o c.o mede {co}!')