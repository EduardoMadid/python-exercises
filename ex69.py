# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
#
# B) quantos homens foram cadastrados.
#
# C) quantas mulheres tem menos de 20 anos.

maisdezoito = homem = mulher = menosdezoito = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('[M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maisdezoito += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulher += 1
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('Deseja cadastrar outra pessoa? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maisdezoito}!')
print(f'Ao todo temos {homem} homens cadastrados!')
print(f'E temos {mulher} mulheres com menos de 20 anos')
