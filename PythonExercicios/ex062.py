a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
mais = int(input('Quantos termos você quer mostrar inicialmente: '))
termo = a1
contador = 1
total = 0
#mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        contador += 1
        print(termo)
        termo += r
    mais = int(input('Quantos termos a mais você quer mostrar: '))
print('FIM')
print('Você viu {} termos'.format(total))










"""
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
# a10 = a1 + (10 * r)
termo = a1
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        contador += 1
    print('FIM')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
"""