# Faca um programa que leia o nome e média de um aluno,
# guardando tambem a situação em um dicionario.
# No final, mostre o conteudo da estrutura na tela!


aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['media'] >= 7:
    print('Voce foi APROVADO!')
elif 5 <= aluno['media'] < 7:
    print('Voce esta em RECUPERAçÂO')
else:
    print('Voce foi REPROVADO!')

print('-=' * 30)

for k, v in aluno.items():
    print(f'{k} = {v}')