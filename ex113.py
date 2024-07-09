# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma
# semelhante ‘a função input() do Python, só que fazendo a validação para aceitar
# apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat()
# com a mesma funcionalidade.


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\n\033[31mERRO! Por favor digite um numero inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mEntrada de dados interrompida pelo usuario!\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print(f'\n\033[31mERRO! Por favor digite um numero real válido!\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[31mEntrada de dados interrompida pelo usuario!\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um numero: ')
n2 = leiaFloat('Digite um Real: ')
print(f'Voce acabou de digitar o numero {n1} e o real foi {n2}!')
