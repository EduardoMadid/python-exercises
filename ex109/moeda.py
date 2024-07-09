def aumentar(preco=0, taxa=0, formato=False):
    """
    Aumenta o preço de acordo com a taxa!
    :param preco: Preço que vai ser aumentado!
    :param taxa: Taxa que vai aumentar o preço!
    :param formato: Se falso não estará formatado!
    :return: Retorna o resultado!
    """
    res = int(preco + (preco * taxa/100))
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = int(preco - (preco * taxa / 100))
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = int(preco/2)
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')



