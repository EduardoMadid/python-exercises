'''pessoas = {'nome':'gustavo', 'sexo':'masculino', 'idade': 22}

print(f'O {pessoas['nome']} tem {pessoas['idade']} anos')

print(pessoas.keys())
print(pessoas.values())
print()

print(pessoas.items())

for k in pessoas.keys():
    print(k)
print()

for k in pessoas.values():
    print(k)
print()

for k, v in pessoas.items():
    print(f'{k} = {v}')


# dicionario dentro da lista
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
'''
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
