from random import randint
certo = randint(0, 10)
chute = int(input('Adivinhe um número entre 0 e 10: '))
contagem = 1
while chute != certo:
    chute = int(input('Tente novamente: '))
    contagem += 1
    if chute == certo:
        print('ACERTOU!')
        print('Você acertou em {} tentativas.'.format(contagem))

''' from random import randint
certo = randint(0, 5)
chute = int(input('Adivinhe um número entre 0 e 5: '))
print('Era {}'.format(certo))
if chute == certo:
    print('Parabéns! Você acertou.')
else:
    print('Infelizmente, você errou.') '''
