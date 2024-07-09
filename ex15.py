# Escreva um programa que pergunta a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa 60 reais por dia e 0.15 por km rodado

km = float(input("Digite quantos quilometros foram percorridos: "))
dias = float(input("Digite por quantos dias o carro foi usado: "))
km_novo = km * 0.15
dias_novo = dias * 60
print(f'O carro percorreu por {dias} dias, andando {km} quilometros!\nCustando assim pelos km R${km_novo:.2f}, pelos dias R${dias_novo}!\nO total a ser pago é de R${km_novo + dias_novo:.2f}')