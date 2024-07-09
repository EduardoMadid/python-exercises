# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

galera = list()
pessoa = dict()
media = soma = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Nome: "))
    while True:
        pessoa['sexo'] = str(input('Digite seu sexo: [M] [F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
    pessoa['idade'] = int(input('Digite sua idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar cadastrando? [S] [N]: ')).upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Responda APENAS S ou N!")
    if resp == 'N':
        break

print('-=' * 30)
print(f'A) Foram cadastrados no total: {len(galera)} pessoas!')
media = soma/len(galera)
print(f'B) A media da idade das pessoas: {media:5.2f} anos!')
print(f'C) A lista de mulheres:', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p['nome']}', end='')
print(f'A lista de pessoas com idade acima da media:')
for p in galera:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print("ENCERRADO!")

