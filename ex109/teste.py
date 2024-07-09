# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.

# Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.

#Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.


import moeda

p = float(input('Digite o preço? R$'))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.metade(p, True)}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.dobro(p, True)}')
t = int(input('Digite a taxa para mostrar o aumento e a diminuicao do valor: '))
print(f'Aumentando {moeda.moeda(p)} em {t}%, temos R${moeda.aumentar(p, t, True)}')
print(f'Diminuindo {moeda.moeda(p)} em {t}%, temos R${moeda.diminuir(p, t, True)}')