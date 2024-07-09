#  Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
#  a maioridade e quantas já são maiores.

from datetime import date

ano = date.today().year
contmaior = 0
contmenor = 0

for i in range(1, 7):
    pessoa = int(input(f'Em que ano a {i} pessoa nasceu?'))
    idade = ano - pessoa
    if idade >= 21:
        contmaior += 1
    else:
        contmenor += 1
print(f'Existem {contmenor} pessoas MENORES de idade!\nE {contmaior} pessoas MAIORES!')