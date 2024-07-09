# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import radians, sin, cos, tan
angulo = int(input("Digite um valor de angulo: "))
cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))
print(f'O angulo é {angulo:.2f}\nO seno dele é {seno:.2f}\nO seu cosseno é {cosseno:.2f}\nA sua tangente é {tangente:.2f}!')