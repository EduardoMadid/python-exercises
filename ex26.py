# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input("Digite uma frase: ")).strip().upper()
primeiraletra = frase[0]
print(f'A letra {primeiraletra}, aparece {frase.count(primeiraletra)} vezes! ')
print(f'A letra {primeiraletra}, aparece a primeira vez na posição {frase.find(primeiraletra)+1}!')
print(f'A letra {primeiraletra}, aparece a ultima vez na posição {frase.rfind(primeiraletra)+1}!')
