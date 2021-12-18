from random import randint
certo = randint(0, 5)
chute = int(input('Adivinhe um número entre 0 e 5: '))
print('Era {}'.format(n))
if chute == certo:
    print('Parabéns! Você acertou.')
else:
    print('Infelizmente, você errou.')
