f = str(input('Digite uma frase: '))
f = f.lower().strip()

numero = f.count('a')
primeira = f.find('a')
ultima = f.rfind('a')

print('A letra A aparece {} vezes'.format(numero))
print('A letra A aparece pela primeira vez na posição {}'.format(primeira+1))
print('A letra A aparece pela última vez na posição {}'.format(ultima+1))
