# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input("Digite o número inteiro que deseja exibir a tabuada: "))
quant = int(input("Digite até que numero vai ir a tabuada: "))
for i in range(1, quant +1):
    print(f'{tabuada} x {i} = {tabuada*i}')