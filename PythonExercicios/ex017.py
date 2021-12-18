from math import hypot
c1 = float(input('Digite o valor do primeiro cateto: '))
c2 = float(input('Digite o valor do segundo cateto: '))
h = hypot(c1, c2)
print('Com os catetos {} e {} o valor da Hipotenusa é {}'.format(c1, c2, h))
