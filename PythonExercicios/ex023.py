num = int(input('Digite um número de 0 a 9999: '))
# Pega o número, divide pela grandeza e pega o resto da divisão por 10 (123//1 = 123 % 10 = 12 com resto 3)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(c))
print('Centena: {}'.format(d))
print('Milhar: {}'.format(m))
