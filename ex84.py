# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
nomeepeso = []
principal = []
mai = men = 0
while True:
    nomeepeso.append(str(input('Digite seu nome: ')).strip().upper())
    nomeepeso.append(float(input('Digite seu peso: ')))
    if len(principal) == 0:
        mai = men = nomeepeso[1]
    else:
        if nomeepeso[1] > mai:
            mai = nomeepeso[1]
        if nomeepeso[1] < men:
            men = nomeepeso[1]
    principal.append(nomeepeso[:])
    nomeepeso.clear()
    resp = str(input('Quer continuar? [S] [N]: ')).strip().upper()[0]
    if resp in 'N':
        print('-=' * 30)
        print('Lista terminada!')
        break
print(f' Os dados foram {principal}!')
print(f'-=' * 30)
print(f'Ao todo voce cadastrou {len(principal)} pessoas!')
print(f'O maior peso foi de {mai} quilos! Peso de ', end='')
for p in principal:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men} quilos! Peso de ', end='')
for p in principal:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()
print('-=' * 30 + 'FIM!')

