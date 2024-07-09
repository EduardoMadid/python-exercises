# Faça um programa que tenha uma lista chamada
# números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos
# os valores pares sorteados pela função anterior.

from random import randint

numeros = []
def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(1, 10))
    print(f'A lista ficou: {lista}')
    print('-=' * 30)


def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos pares de {lista}, temos {soma}')
    print('-=' * 30)

sorteia(numeros)
somaPar(numeros)

