lista = list()
total_pessoas = media = 0
while True:
    total_pessoas += 1
    pessoa = dict()
    pessoa['Nome'] = str(input('Nome: ').title())
    while True:
        pessoa['Sexo'] = str(input('Sexo [M/F]: '))
        if pessoa['Sexo'][0].upper() not in 'MF':
            print('Valor inválido. Digite M ou F')
        else:
            break
    pessoa['Idade'] = int(input("Idade: "))
    if total_pessoas == 1:
        media = pessoa['Idade']
    else:
        media = (media + pessoa['Idade']) / 2
    lista.append(pessoa.copy())
    pessoa.clear()
    while True:
        resp = str(input('Quer continuar? [S/N]: '))
        if resp[0].upper() not in 'SN':
            print('Valor inválido. Digite S ou N')
        else:
            break
    if resp[0].upper() == 'N':
        break
print('=-' * 30)
print(lista)
print('=-' * 30)
print(f'Total de pessoas cadastradas: {total_pessoas}')
print(f'Média das idades: {media:.2f}')
print(f'Lista de mulheres:')
for d in lista:
    if d['Sexo'].upper() == 'F':
        print(f'[{d["Nome"]}] ', end='')
print()
print(f'Lista de pessoas com a idade acima da média: ')
for d in lista:
    if d['Idade'] > media:
        print(f'[{d["Nome"]}: {d["Idade"]}] ', end='')
print()
print('=-' * 30)
