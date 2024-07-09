# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu sálario atual: "))
anos = int(input("Digite quantos anos você ira pagar: "))
prestacao = casa / (anos * 12)
min = salario * 0.3
print(f'Para pagar uma casa de R${casa} em {anos}, ', end='')
print(f'a prestação será de R${prestacao}!')
if prestacao <= min:
    print(f'Emprestimo pode ser CONCEDIDO!')
else:
    print(f'Emprestimo NEGADO!')
