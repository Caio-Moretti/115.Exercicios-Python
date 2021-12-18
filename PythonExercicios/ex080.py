lista = []
for c in range(0, 5):
    n = int(input('Digite um valor para adicionar na lista: '))

    # Aqui ele verifica se o n é o primeiro número adicionado ou maior que o último.
    # (Para adicionar ao último lugar)
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado ao final da lista')

    else:
        # Aqui começa a varrer a lista a procura de um valor maior que o n (para colocar o n no lugar dele).
        pos = 0  # Começa da posição 0...
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)  # Coloca o n na posição atual (e desloca para a esquerda o resto da lista)
                print(f'Valor adicionado na posição {pos}')
                break
            pos += 1  # Vai para a próxima posição para verificar.
print('=-' * 30)
print(f'Aqui está sua lista: {lista}')
