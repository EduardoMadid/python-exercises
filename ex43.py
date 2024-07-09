# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC)
# e mostre seu status, de acordo com a tabela abaixo:
#
# – IMC abaixo de 18,5: Abaixo do Peso
#
# – Entre 18,5 e 25: Peso Ideal
#
# – 25 até 30: Sobrepeso
#
# – 30 até 40: Obesidade
#
# – Acima de 40: Obesidade Mórbida

peso = float(input("Digite seu peso em KG: "))
altura = float(input("Digite sua altura: "))
IMC = peso / (altura ** 2)
print(f'O seu IMC equivale a: {IMC:.1f}!')
if IMC < 18.5:
    print(f'ABAIXO DO PESO!')
elif 18.5 <= IMC < 25:
    print(f'PESO IDEAL!')
elif 25 <= IMC < 30:
    print(f'SOBREPESO!')
elif 30 <= IMC <= 40:
    print(f'OBESIDADE!')
elif IMC >= 40:
    print(f'OBESIDADE MORBIDA!')