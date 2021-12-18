def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mERRO! Entrada de dados interrompida.\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mERRO! Entrada de dados interrompida.\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Número Inteiro: ')
n2 = leiaFloat('Número Real: ')
print(f'Valor inteiro: {n1}'
      f'\nValor Real: {n2}')
