# Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome

nome = str(input("Digite seu nome completo: ")).strip()
print("Analisando seu nome........")
print(f'O seu nome em maiusculas fica: {nome.upper()}')
print(f'O seu nome em minusculaa fica: {nome.lower()}')
print(f'O seu nome possui {len(nome) - nome.count(' ')} letras!')
print(f'Seu primeiro nome possui: {nome.find(' ')}')