# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
#
# – à vista no cartão: 5% de desconto
#
# – em até 2x no cartão: preço formal
#
# – 3x ou mais no cartão: 20% de juros

produto = float(input("Digite o valor do produto: R$"))
print('''
Para comprar o produto escolha uma das opções abaixo: 

1 - à vista dinheiro/cheque: 10% de desconto
2 - à vista no cartão: 5% de desconto
3 - em até 2x no cartão: preço formal 
4 - 3x ou mais no cartão: 20% de juros
''')
opcao = int(input("Escolha o metodo de pagamento: "))
if opcao == 1:
    print(f'O valor a ser pago sobre o produto de R${produto}, será de R${produto - (produto * 0.1)}, com o desconto de 10% aplicado!')
elif opcao == 2:
    print(f'O valor a ser pago sobre o produto de R${produto}, será de R${produto - (produto * 0.05)}, com o desconto de 5% aplicado!')
elif opcao == 3:
    print(f'O valor a ser pago sobre o produto de R${produto} parcelando 2 vezes, será duas parcelas de R${produto/2}')
elif opcao == 4:
    parcelas = int(input("Quantas parcelas? "))
    total = produto + (produto * 0.2)
    print(f'O valor a ser pago sobre o produto de R${produto} parcelando {parcelas} vezes, será de R${total}, na qual cada parcela saira por R${total/parcelas:.2f}!')
else:
    print(f'\033[1;31mERRO!')
