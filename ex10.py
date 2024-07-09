# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere 1 dolar = 3,27 reais
carteira = float(input("Digite quantos reais voce possui na sua carteira: R$"))
print(f'Voce pode comprar {carteira / 3.27:.2f} dolares!')
