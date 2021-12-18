print('FLAG = 999')
num = 0
quantidade = 0
soma = 0
num = int(input('Digite um valor: '))
while num != 999:
    quantidade += 1
    soma += num
    num = int(input('Digite um valor: '))

#    if num == 999:
#        quantidade -= 1
#    else:
#        soma += num
print('Foram digitados {} números.'.format(quantidade))
print('A soma entre os números digitados é {}'.format(soma))
