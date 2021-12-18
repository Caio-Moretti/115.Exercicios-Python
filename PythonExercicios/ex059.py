n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
opt = int(input('Agora selecione a próxima operação:'
                '\n[1] Somar'
                '\n[2] Multiplicar'
                '\n[3] Mostrar o maior'
                '\n[4] Novos números'
                '\n[5] Sair do programa.'
                '\n RESPOSTA: '))

while opt != 5:
    if opt == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
        opt = int(input('E agora, o que quer fazer?'
                        '\n[1] Somar'
                        '\n[2] Multiplicar'
                        '\n[3] Mostrar o maior'
                        '\n[4] Novos números'
                        '\n[5] Sair do programa.'
                        '\n RESPOSTA: '))
    elif opt == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
        opt = int(input('E agora, o que quer fazer?'
                        '\n[1] Somar'
                        '\n[2] Multiplicar'
                        '\n[3] Mostrar o maior'
                        '\n[4] Novos números'
                        '\n[5] Sair do programa.'
                        '\n RESPOSTA: '))
    elif opt == 3:
        if n1 == n2:
            print('{} e {} são iguais.'.format(n1, n2))
        elif n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
        opt = int(input('E agora, o que quer fazer?'
                        '\n[1] Somar'
                        '\n[2] Multiplicar'
                        '\n[3] Mostrar o maior'
                        '\n[4] Novos números'
                        '\n[5] Sair do programa.'
                        '\n RESPOSTA: '))
    elif opt == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
        opt = int(input('E agora, o que quer fazer?'
                        '\n[1] Somar'
                        '\n[2] Multiplicar'
                        '\n[3] Mostrar o maior'
                        '\n[4] Novos números'
                        '\n[5] Sair do programa.'
                        '\n RESPOSTA: '))
    elif opt == 5:
        print('Saindo do programa.')
    else:
        print('Número inválido, tente novamente.')
        opt = int(input('O que quer fazer?'
                        '\n[1] Somar'
                        '\n[2] Multiplicar'
                        '\n[3] Mostrar o maior'
                        '\n[4] Novos números'
                        '\n[5] Sair do programa.'
                        '\n RESPOSTA: '))
print('Programa encerrado. ')
