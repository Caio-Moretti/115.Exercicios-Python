lista = list()
c = 0
while True:
    n = int(input('Digite o número: '))
    resp = str(input('Quer continuar? [S/N] '))
    lista.append(n)
    c += 1
    lista.sort(reverse=True)
    if resp.upper() in 'N':
        break
print(lista)
if 5 in lista:
    print('O 5 se encontra na lista.')
else:
    print('O 5 não está na lista.')
