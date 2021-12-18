"""a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
a10 = a1 + (10 * r)
for c in range(a1, a10, r):
    print(c)"""

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
a10 = a1 + (10 * r)
termo = a1
contador = 1
while contador <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    contador += 1
print('FIM')
