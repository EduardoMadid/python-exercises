#  Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
#  se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
#  do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input("Digite seu ano de nascimento: "))
idade = (date.today().year) - ano
if idade > 18:
    saldo = idade - 18
    print(f'Você esta com {idade} anos! JÁ PASSOU {saldo} anos!')
    print(f'Seu ano de alistamento foi em {ano + 18}')
elif idade < 18:
    saldo = 18 - idade
    print(f'Voce esta com {idade} anos! ESTÁ MUITO CEDO FALTA {saldo} anos!')
    print(f'Seu ano de alistamento vai ser em {ano + 18}')
else:
    print(f'Voce está com {idade} anos! TEMPO PERFEITO PARA SE ALISTAR!')