num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

lista = [num, num2, num3]
lista.sort()

print('O menor número é {}'.format(lista[0]))
print('O maior número é {}'.format(lista[2]))
