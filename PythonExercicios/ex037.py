num = int(input('Digite um número inteiro: '))
opt = int(input('Escolha uma das opções:'
                  '\n1. Transformar para binário.'
                  '\n2. Transformar para octal. '
                  '\n3. Transformar para hexadecimal.'
                  '\nResposta: '))
if opt != 1 and opt != 2 and opt != 3:
    print('Escolha um número válido.')
elif opt == 1:
    print('{} em binário é igual a {}'.format(num, bin(num)))
elif opt == 2:
    print('{} em octal é igual a {}'.format(num, oct(num)))
else:
    print('{} em hexadecimal é igual a {}'.format(num, hex(num)))
