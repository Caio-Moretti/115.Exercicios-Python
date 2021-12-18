from random import randint
cont = jogador = 0
resposta = ''
print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
while True:
    computador = randint(0, 10)
    pi = str(input('Par ou Ímpar? [P/I]: ')).strip().lower()[0]
    jogador = int(input('Digite um número: '))
    print('-' * 40)
    if (jogador + computador) % 2 == 0:
        resposta = 'Par'
        print(f'{jogador} + {computador} = {jogador + computador} (PAR)')
    else:
        resposta = 'Impar'
        print(f'{jogador} + {computador} = {jogador + computador} (ÍMPAR)')
    if pi.lower()[0] == resposta.lower()[0]:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont += 1
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {cont} vezes.')
