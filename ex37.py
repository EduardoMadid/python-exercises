# Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um numero inteiro: "))
print('''
MENU - Escolha uma das opções abaixo:
1 - binário
2 - octal
3 - hexadecimal
''')

opcao = int(input("Escolha uma das opcções acima: "))

if opcao == 1:
    print(f'Em binário, o número {num}, ficaria {bin(num)[2:]}!')
elif opcao == 2:
    print(f'Em octal, o número {num}, ficaria {oct(num)[2:]}!')
elif opcao == 3:
    print(f'Em hexadecimal, o número {num}, ficaria {hex(num)[2:]}!')
else:
    print(f'OPCAO INVÁLIDA!\nEscolha um número presente no menu!')