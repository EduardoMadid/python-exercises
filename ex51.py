# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

print('=' * 20)
print('PROGRESSÃO DE UMA P.A.')
print('=' * 20)
termo = int(input('PRIMEIRO TERMO: '))
razao = int(input('RAZÃO: '))
decimo =  termo + (10 - 1) * razao

for i in range(termo, decimo + razao, razao):
    print(i, end=' -> ')
print('Acabou!')
