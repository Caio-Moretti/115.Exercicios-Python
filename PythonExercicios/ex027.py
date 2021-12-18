nome = str(input('Digite um nome completo: '))
quant = nome.count(' ')
nomes = nome.split()
print('Seu nome completo é {}'.format(nome))
print('Seu primeiro nome é {}'.format(nomes[0]))
print('Seu último nome é {}'.format(nomes[0 + quant]))
print(len(nomes)) #A função "len" em uma lista mostra a quantidade de elementos dentro dela.
