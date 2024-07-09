# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique
# o número
# a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela
# o processo de cálculo do fatorial.

def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número!
    :param n: Numero que vai ser calculado!
    :param show: Mostrar ou nao a conta(opcional)!
    :return: O valor do fatorial de um numero n!
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f


print(fatorial(5, show=True))
help(fatorial)

