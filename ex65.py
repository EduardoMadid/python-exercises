# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
soma = quant = media = 0
resp = 'S'
maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite numero inteiro: '))
    soma += n
    quant += 1
    resp = str(input('Quer continuar? [S] [N]: ')).strip().upper()[0]
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma/quant
print(f'A media de {quant} valores mostrados é {media:.2f}!')
print(f'O menor valor lido é {menor} e o maior é {maior}!')