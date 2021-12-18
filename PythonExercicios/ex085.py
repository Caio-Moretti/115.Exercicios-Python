principal = [list(), list()]
n = 0
for c in range(0, 7):
    n = int(input(f'Digite o {c + 1}º valor: '))
    print(n)
    if n % 2 == 0:
        principal[0].append(n)
    else:
        principal[1].append(n)
principal[0].sort()
principal[1].sort()
print('=-' * 30)
print(principal)
print('=-' * 30)
print(f'Pares: {principal[0]}')
print(f'Impares: {principal[1]}')