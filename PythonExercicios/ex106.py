from time import sleep
c = ('\033[m',         # 0 - SEM COR
     '\033[0;30;41m',   # 1 - VERMELHO
     '\033[0;30;42m',   # 2 - VERDE
     '\033[0;30;43m',   # 3 - AMARELO
     '\033[0;30;44m',   # 4 - AZUL
     '\033[0;30;45m',   # 5 - ROXO
     '\033[7;30m')     # 6 - BRANCO


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    sleep(1)


def ajuda(com):
    título(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[5], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


while True:
    título('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca: '))
    if comando[0].upper() == 'F':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO', 1)
