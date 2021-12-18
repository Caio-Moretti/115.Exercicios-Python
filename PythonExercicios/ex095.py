jogadores = list()
while True:
    dados = dict()
    dados['Nome'] = str(input('Nome do jogador: ').title())
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    dados['Gols'] = list()

    for p in range(0, partidas):
        dados['Gols'].append(int(input(f'Quantos gols o {dados["Nome"]} fez na partida {p + 1}? ')))
    #    dados['Total de gols'] += dados['Gols'][p]

    dados['Total de gols'] = sum(dados['Gols'])
    jogadores.append(dados.copy())
    dados.clear()
    while True:
        resp = str(input('Quer continuar? [S/N]: '))
        if resp[0].upper() not in 'SN':
            print('Valor inválido. Digite S ou N')
        else:
            break
    if resp[0].upper() == 'N':
        break
print(jogadores)
print(f'Código   Nome      Gols         Total')
print('--' * 20)
for i, d in enumerate(jogadores):
    print(f'{i:<9}', end='')
    print(f'{d["Nome"]:<9} ', end='')
    print(f'{str(d["Gols"]):<15} ', end='')
    print(f'{str(d["Total de gols"]):>}')
print('--' * 20)

while True:
    while True:
        escolhido = int(input(f'Digite o código de um jogador [999 STOP]: '))
        if 999 != escolhido >= len(jogadores):
            print(f'ERRO! Não existe jogador com código {escolhido}')
        else:
            break
    if escolhido == 999:
        print('<< ENCERRADO >>')
        break

    print('=-' * 30)
    print(f'-- Levantamento do jogador {jogadores[escolhido]["Nome"]} --')
    for i, g in enumerate(jogadores[escolhido]["Gols"]):
        print(f'=>  No jogo {i + 1} fez {g} gol(s). ')
    print(f'Foi um total de {jogadores[escolhido]["Total de gols"]} gol(s).')
    print('=-' * 30)
