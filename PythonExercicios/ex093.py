dados = dict()
dados['Nome'] = str(input('Nome do jogador: ').title())
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
dados['Gols'] = list()

for p in range(0, partidas):
    dados['Gols'].append(int(input(f'Quantos gols o {dados["Nome"]} fez na partida {p + 1}? ')))
#    dados['Total de gols'] += dados['Gols'][p]
dados['Total de gols'] = sum(dados['Gols'])
print('=-' * 30)
for k, v in dados.items():
    print(f'{k}: {v}')
print('=-' * 30)
print(f'O jogador {dados["Nome"]} jogou {partidas} partidas: ')
for i, v in enumerate(dados['Gols']):
    print(f' => Na partida {i + 1} ele fez {v} gols.')
"""for p in range(0, partidas):
    print(f' => Na partida {p + 1} ele fez {dados["Gols"][p]} gols.')"""
print(f'Foi um total de {dados["Total de gols"]} gols.')
print('--' * 30)
