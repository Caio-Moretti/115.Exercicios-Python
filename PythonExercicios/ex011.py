h = float(input('Qual é a altura da parede (Em metros.)? Resposta: '))
c = float(input('Qual é o comprimento dessa parede (Em metros.)? Resposta: '))
a = h * c
L = a / 2
print("A área da sua parede é de {} m2 e precisará de {} Litros de tinta para pintá-la".format(a, L))
