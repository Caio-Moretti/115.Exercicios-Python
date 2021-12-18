x = 'Número primo'
n = int(input('digite um número inteiro para saber se ele é primo: '))
for c in range(2, n):
    if n % c == 0:
        x = 'Número normal'
print(x)
