resp = ''
resp2 = ''
lista = list()
alunos = list()
media = 0
while True:
    alunos.append(str(input('Nome: ')))
    alunos.append(float(input('Nota 1: ')))
    alunos.append(float(input('Nota 2: ')))
    resp = str(input('Quer continuar? [S/N] '))
    lista.append(alunos[:])
    alunos.clear()
    if resp[0].upper() in 'N':
        break
for a in lista:
    media = (a[1] + a[2]) / 2
    print('-'*26)
    print(f'{"NOME":<10}{"MÉDIA":>13}')
    print(f'{a[0].title():<10} -> {media:>8.1f}')
print('-' * 26)
while True:
    resp2 = str(input('Qual aluno você quer ver a nota [FLAG 999] ?  '))
    if resp2 == '999':
        break
    else:
        for a in lista:
            if resp2.lower() == a[0].lower():
                print(f'Notas do(a) {a[0].title()}: {a[1:3]}')
