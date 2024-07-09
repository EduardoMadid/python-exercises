# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input("Digite sua velocidade em km: "))
if velocidade > 80:
    multa = (velocidade - 80)*7
    print(f'Voce foi MULTADO!\nSua multa irá custar R${multa},00!')
else:
    print(f'Tá de boa! Só não passa dos 80 hein!')