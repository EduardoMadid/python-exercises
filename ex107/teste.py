# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from exs.ex107 import moeda

p = float(input('Digite o preço? R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
t = int(input('Digite a taxa para mostrar o aumento e a diminuicao do valor: '))
print(f'Aumentando {p} em {t}%, temos R${moeda.aumentar(p, t)}')
print(f'Diminuindo {p} em {t}%, temos R${moeda.diminuir(p, t)}')