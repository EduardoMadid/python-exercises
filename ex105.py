#  Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*nota, sit=False):
    boletim = dict()
    boletim['total'] = len(nota)
    boletim['maior'] = max(nota)
    boletim['menor'] = min(nota)
    media = sum(nota)/len(nota)
    boletim['media'] = media
    if sit:
        if media >= 7:
            boletim['situacão'] = 'BOM'
        elif media >= 5:
            boletim['situacão'] = 'RAZOAVEL'
        else:
            boletim['situacão'] = 'RUIM'
    return boletim


resp = notas(8, 6, 10, 6.5, sit=True)
print(resp)
