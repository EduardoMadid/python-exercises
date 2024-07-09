# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
tabuada = int(input("Digite o número inteiro que deseja exibir a tabuada: "))
for i in range(1,11):
    print(f'{tabuada} x {i} = {tabuada*i}')