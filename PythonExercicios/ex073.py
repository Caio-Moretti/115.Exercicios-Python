times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Fortaleza',
         'Bragantino', 'Fluminense', 'Internacional', 'Ceará', 'América-MG',
         'Cuiabá', 'Athletico-PR', 'Santos', 'São Paulo', 'Atlético-GO',
         'Juventude', 'Bahia', 'Grêmio', 'Sport', 'Chapecoense',)
print(f'Lista dos 5 primeiros colocados: {times[0:5]}')
print(f'lista dos últimos 4 colocados: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'A posição da Chape é: {times.index("Chapecoense") + 1}ª')
