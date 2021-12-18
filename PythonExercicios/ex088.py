from random import randint
from time import sleep
total = 1
print('==' * 20)
print('MEGA SENA')
print('==' * 20)
quant = int(input(f'Quantos jogos você quer jogar? '))
lista = []
jogos = []
cont = 0
while total <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
print('==' * 20)
print(f'Sorteando {quant} Jogos')
print('==' * 20)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)

