# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

from ex108 import moeda
p = float(input('Digite o preço? R$'))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}')
t = int(input('Digite a taxa para mostrar o aumento e a diminuicao do valor: '))
print(f'Aumentando {moeda.moeda(p)} em {t}%, temos R${moeda.moeda(moeda.aumentar(p, t))}')
print(f'Diminuindo {moeda.moeda(p)} em {t}%, temos R${moeda.moeda(moeda.diminuir(p, t))}')