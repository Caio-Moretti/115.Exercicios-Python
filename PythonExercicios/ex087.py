matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = 0
soma3c = 0
maior2l = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite o valor [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            somap += matriz[linha][coluna]
        elif linha == 1:
            if matriz[linha][coluna] >= maior2l:
                maior2l = matriz[linha][coluna]
for l in range(0, 3):
    soma3c += matriz[l][2]
print('==' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é {somap}')
print(f'A soma dos valores da terceira coluna é {soma3c}')
print(f'O maior valor da segunda linha é {maior2l}')
print('==' * 20)
