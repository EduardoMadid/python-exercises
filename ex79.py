# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
while True:
    n = int(input("Digite um valor: "))
    if n not in lista:
        print('Valor adicionado com sucesso!')
        lista.append(n)
    else:
        print(f'O numero {n} já está presente na lista digite outro!')
    resp = str(input('Quer continuar? [S] [N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print(f'A lista organizada em valores crescentes fica assim: {sorted(lista)}!')