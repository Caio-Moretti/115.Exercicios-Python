num = int(input('Digite um número e descubra se ele é par ou ímpar: '))
if num // 1 % 2 == 0:
    print('O número {} é par.'.format(num))
else:
    print('O número {} é ímpar.'.format(num))
