# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre
# quantos números foram digitados e qual foi a soma entre eles
# (desconsiderando o flag).

soma = cont = n = 0
while n != 999:
    n = int(input('Digite numero inteiro (para parar digite 999):  '))
    cont += 1
    soma += n
print(f'PROGRAMA PARADO!')
print(f'Foram digitados {cont - 1} numeros!\nA soma dos numeros é de {soma - 999}!')