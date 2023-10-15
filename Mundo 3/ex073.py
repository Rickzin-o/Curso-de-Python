brasileirao = ('Corinthias', 'Bragantino', 'Atlético-MG', 'Coritiba', 'São Paulo',
               'Santos', 'Cuiabá', 'Internacional', 'Avaí', 'América-MG',
               'Palmeiras', 'Flamengo', 'Botafogo', 'Fluminense', 'Ceará SC',
               'Atlético-PR', 'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza')
print('Data: 06/05/2022')
print('=-=' * 25)
print(f'Lista de times do Brasileirão Série A: {brasileirao}')
print('=-=' * 25)
print(f'Os 5 primeiros times são: {brasileirao[:5]}')
print(f'Os 4 últimos são: {brasileirao[-4:]}')
print('=-=' * 25)
print(f'Lista em ordem alfabética: {sorted(brasileirao)}')
print('=-=' * 25)
print(f"O Flamengo está na {brasileirao.index('Flamengo')+1}ª posição")
