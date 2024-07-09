# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre:
#
# a) Os 5 primeiros times.
#
# b) Os últimos 4 colocados.
#
# c) Times em ordem alfabética.
#
# d) Em que posição está o time da Chapecoense.

times = (
    "Flamengo",
    "Bahia",
    "Botafogo FR RJ",
    "São Paulo FC SP",
    "CA Paranaense PR",
    "Red Bull Bragantino SP",
    "Palmeiras SP",
    "Internacional RS",
    "Cruzeiro",
    "Atletico Mineiro MG",
    "Fortaleza CE",
    "EC Juventude RS",
    "Gremio",
    "Vasco Gama",
    "Fluminense RJ",
    "Criciúma",
    "Corinthians SP",
    "AC Goianiense GO",
    "EC Vitória BA",
    "Cuiabá Esporte Clube MT"
)
print('-=' * 30)
print('INFORMAÇÕES SOBRE O BRASILEIRÃO!')
print('-=' * 30)
print(f'Os 5 primeiros times são: {times[:5]}!')
print('-=' * 30)
print(f'Os últimos 4 times são: {times[-4:]}!')
print('-=' * 30)
print(f'Times em ordem alafbética: {sorted(times)}!')
print('-=' * 30)
print(f'O time de Ciciúma está na posição: {times.index("Criciúma") + 1}!')

