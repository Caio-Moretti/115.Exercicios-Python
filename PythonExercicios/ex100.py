from random import randint
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores: ', end='')
    for c in range(0, 6):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('FIM')


def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somandos os valores pares de {lista}, temos {soma}')


numbers = []
sorteia(numbers)
somaPar(numbers)
