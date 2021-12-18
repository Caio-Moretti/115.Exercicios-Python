from random import choice
from time import sleep

jokenpo = ['Pedra', 'Papel', 'Tesoura']
jokenposter_stainger = choice(jokenpo)
jogador = int(input('Qual a sua jogada?'
                    '\n1. Pedra'
                    '\n2. Papel'
                    '\n3. Tesoura'
                    '\nEscolha: '))

print('\nJO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!'
      '\n ')

if jogador == 1:
    print('Você: Pedra')
elif jogador == 2:
    print('Você: Papel')
elif jogador == 3:
    print('Você: Tesoura')
else:
    print('Escolha uma opção válida.')

print('Jokenposter Stainger: {}'.format(jokenposter_stainger))

sleep(2)

print('--' * 20)

if jokenposter_stainger == 'Pedra' and jogador == 1:
    print('Empate!')
    w = 0
elif jokenposter_stainger == 'Pedra' and jogador == 2:
    print('Você ganhou!')
    w = 2
elif jokenposter_stainger == 'Pedra' and jogador == 3:
    print('Você perdeu!')
    w = 1

elif jokenposter_stainger == 'Papel' and jogador == 1:
    print('Você perdeu!')
    w = 1
elif jokenposter_stainger == 'Papel' and jogador == 2:
    print('Empate!')
    w = 0
elif jokenposter_stainger == 'Papel' and jogador == 3:
    print('Você ganhou!')
    w = 2

elif jokenposter_stainger == 'Tesoura' and jogador == 1:
    print('Você ganhou!')
    w = 2
elif jokenposter_stainger == 'Tesoura' and jogador == 2:
    print('Você perdeu!')
    w = 1
elif jokenposter_stainger == 'Tesoura' and jogador == 3:
    print('Empate!')
    w = 0

if w == 0:
    print('Jokenposter Stainger: Vamo de novo! Ta com medinho?')
elif w == 1:
    print('Jokenposter Stainger: OTÁRIO ')
elif w == 2:
    print('Jokenposter Stainger: TAAAVA DEMORAANDO! Revanche!')
else:
    print(' ')

print('--' * 20)
