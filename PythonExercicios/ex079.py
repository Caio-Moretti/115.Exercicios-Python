lista = []
while True:
    n = int(input('Digite um valor para adicionar na lista: '))
    if n not in lista:
        lista.append(n)
    else:
        print('Valor já adicionado.')
    resp = str(input('Quer continuar? [S/N]: '))
    if resp[0].upper() in 'N':
        break
print('=-' * 30)
lista.sort()
print(f'Você adicionou os valores: {lista}')
