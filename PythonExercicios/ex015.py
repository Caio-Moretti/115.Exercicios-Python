d = int(input('Quantos dias alugado? '))
km = int(input('Quantos Km rodados? '))
v = (d * 60) + 0.15 * km
print('O valor a ser pago é de R$: {:.2f}'.format(v))
