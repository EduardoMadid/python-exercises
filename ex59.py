# Crie um programa que leia dois valores e mostre um menu na tela:
#
# [ 1 ] somar
#
# [ 2 ] multiplicar
#
# [ 3 ] maior
#
# [ 4 ] novos números
#
# [ 5 ] sair do programa
#
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
opcao = 0
while opcao != 5:
    print('''
    [ 1 ] somar

    [ 2 ] multiplicar

    [ 3 ] maior

    [ 4 ] novos números

    [ 5 ] sair do programa''')
    print()
    opcao = int(input("Qual é sua opção: "))

    if opcao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif opcao == 2:
        print(f'{num1} x {num2} = {num1*num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'{num1} > {num2}')
        elif num1 < num2:
            print(f'{num1} < {num2}')
        else:
            print(f'{num1} = {num2}')
    elif opcao == 4:
        num1 = int(input("Digite o primeiro numero:"))
        num2 = int(input("Digite o segundo numero:"))
    elif opcao == 5:
        print('SAINDO DO PROGRAMA!')
    else:
        print(f'OPCAO INVALIDA!')
    print('-=' * 20)
print('FIM! Volte sempre!')



