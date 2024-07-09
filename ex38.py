#  Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#
# – O primeiro valor é maior
#
# – O segundo valor é maior
#
# – Não existe valor maior, os dois são iguais

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite um número inteiro: "))
if num1 > num2:
    print(f'O primeiro valor é maior! {num1} > {num2}!')
elif num1 < num2:
    print(f'O segundo valor é maior! {num1} < {num2}!')
else:
    print(f'Eles são iguais! {num1} = {num2}!')