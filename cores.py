'''
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m!!!')
'''
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

nome = 'Eduardo'
print(f'Olá! Muito prazer em te conhecer {cores['azul']}{nome} !!')



