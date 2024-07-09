# Faça um algoritmo que leia um preco de um produto e mostre seu novo preço com 5% de desconto.
produto = float(input("Digite o valor do produto: "))
desconto = produto - (produto*0.05) 
print(f'O produto com valor de {produto} ficará custando {desconto} reais!')