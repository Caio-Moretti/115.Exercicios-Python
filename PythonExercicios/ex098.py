from time import sleep


def lin():
    print('-' * 30)


def contador(i, f, p):
    if p == 0:
        p = 1
    if inicio < fim:
        if p < 0:
            print('ERRO. (PASSO NEGATIVO)')
        print(f'Contando de {i} até {f} de {p} em {p}')
        for c in range(i, f + 1, p):
            print(f'{c} ', end='')
            sleep(0.3)
        print('FIM')
    else:
        if p < 0:
            p *= -1
        print(f'Contando de {i} até {f} de {p} em {p}')
        for c in range(i, f - 1, -p):
            print(f'{c} ', end='')
            sleep(0.3)
        print('FIM')


# Programa Principal
print('CONTAGEM DE 1 ATÉ 10 DE 1 EM 1')
for c in range(1, 11, 1):
    print(f'{c} ', end='')
    sleep(0.3)
print(f'FIM.')
lin()
print('CONTAGEM DE 10 ATÉ 10 DE 2 EM 2')
for c in range(10, -1, -2):
    print(f'{c} ', end='')
    sleep(0.3)
print(f'FIM.')
lin()
print('=-' * 30)
print('Crie uma contagem personalizada')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
lin()
print('FIM DO PROGRAMA')
