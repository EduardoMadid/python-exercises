# Crie um programa que leia nome,
# ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

pessoa = dict()

pessoa['nome'] = str(input('Digite seu NOME: '))
nasc = int(input('ANO de NASCIMENTO: '))
pessoa['idade'] = datetime.now().year - nasc
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if pessoa['ctps'] == 0:
    print('-=' * 30)
    for k, v in pessoa.items():
        print(f' - {k} tem o valor {v}!')
else:
    pessoa['cont'] = int(input('Ano de Contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['cont'] + 35) - datetime.now().year)
    print('-=' * 30)
    for k, v in pessoa.items():
        print(f' - {k} tem o valor {v}!')
