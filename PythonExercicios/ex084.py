maior_peso = menor_peso = 0
pessoas = list()
dados = list()
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resposta = str(input('Quer continuar? [S/N] '))
    if resposta.upper() in 'N':
        break
print('=-' * 30)
print(pessoas)
print(f'Total de pessoas: {len(pessoas)}')
print(f'Maior peso: {maior_peso}. Pessoas: ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0].title()}] ', end='')
print()
print(f'Menor peso: {menor_peso}. Pessoas: ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0].title()}] ', end='')
print()
print('=-' * 30)
