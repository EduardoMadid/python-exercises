def aumentar(preco=0, taxa=0, formato=False):
    """
    Aumenta o preço de acordo com a taxa!
    :param preco: Preço que vai ser aumentado!
    :param taxa: Taxa que vai aumentar o preço!
    :param formato: Se falso não estará formatado!
    :return: Retorna o resultado!
    """
    res = preco + (preco * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco - (preco * taxa / 100)
    return res if formato is False else moeda(res)


def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco/2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0, taxamais=0, taxamenos=0):
    print('-='*30)
    print(f'{'RESUMO DO VALOR':^60}')
    print('-='*30)
    print(f'Preço Analisado: {moeda(preco)}')
    print(f'Dobro do Preço: {dobro(preco, True)}')
    print(f'Metade do Preço: {metade(preco, True)}')
    print(f'{taxamais}% de aumento: {aumentar(preco,taxamais, True)}')
    print(f'{taxamenos}% de redução: {diminuir(preco, taxamenos, True)}')
    print('-=' * 30)


