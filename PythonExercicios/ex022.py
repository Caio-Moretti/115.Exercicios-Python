n = str(input('Digite seu nome completo: '))
nome = n.strip()
número = len(nome)
esp = nome.count(' ')
quant = número - esp
lista = nome.split()

print('O nome em maiúsculas: {}'.format(nome.upper()))
print('O nome em minúsculas: {}'.format(nome.lower()))
print('Quantidades de letras em seu nome: {}'.format(quant))
print('Quantidade de letras no primeiro nome: {}'.format(len(lista[0])))
