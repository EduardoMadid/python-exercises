#  Aprimore o desafio anterior, mostrando no final:
#  A) A soma de todos os valores pares digitados.
#  B) A soma dos valores da terceira coluna.
#  C) O maior valor da segunda linha.

somapar = somacoluna = maior = 0
matriz = []
linhas = int(input('Quantas linhas: '))
colunas = int(input('Quantas colunas: '))
print('-=' * 30)
for i in range(linhas):
    linha = []
    for j in range(colunas):
        n = int(input(f"Numero para {[i, j]}: "))
        if j == 2:
            somacoluna += n
        if i == 1:
            maior = n
        else:
            if i == 1:
                if maior > n:
                    maior = n
        linha.append(n)
    matriz.append(linha)

print('-=' * 30)
for i in range(linhas):
    for j in range(colunas):
        print(matriz[i][j], end='\t')
        if matriz[i][j] % 2 == 0:
            somapar += matriz[i][j]
    print()
print('-=' * 30)

print()
print(f'A soma dos pares é igual a {somapar}!')
print(f'A soma da terceira coluna é igual a {somacoluna}!')
print(f'O maior valor da segunda linha é {maior}!')
