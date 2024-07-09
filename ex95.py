# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do JOGADOR: '))
    tot = int(input(f'Quantas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(1, tot+1):
        partidas.append(int(input(f'   Quantos gols na partida {c}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S] [N]: ')).upper()[0]
        if resp in 'NS':
            break
        print('ERRO!')
    if resp == "N":
        break

print('-=' * 30)
print('cod        ', end='')
for i in jogador.keys():
    print(f'{i:<18}', end='')
print()
print('-' * 60)
for k, v in enumerate(time):
    print(f'{k:>3}   ', end='')
    for d in v.values():
        print(f'{str(d):<22}', end='')
    print()
print('-' * 60)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 interrompe!):  '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRRO! N existe jogador com esse codigo!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}!')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols!')
    print('-' * 40)
print('<<<VOLTE SEMPRE!>>>')
