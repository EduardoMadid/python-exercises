# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que a cada litro de tinta, pinta um aárea de 2m².

largura = float(input("Digite a largura da sua parede: "))
altura = float(input("Digite a altura da sua parede: "))
area = largura * altura
print(f'Será necessario de {area / 2:.1f} litros de tinta, para pintar uma parede de {largura:.1f}m x {altura:.1f}m, cuja area equivale a {area:.2f}m²!')