frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso != junto:
    print('NÃO É UM PALÍNDROMO')
else:
    print('PALÍNDROMO')

"""from unidecode import unidecode
x = 'palíndromo'
frase = str(input('Digite uma frase: '))
frase = frase.replace(" ", "")
frase2 = frase[::-1]
frase = unidecode(frase).lower()
frase2 = unidecode(frase2).lower()
print(frase)
print(frase2)
if frase == frase2:
    print('Essa frase é um palíndromo')
else:
    print('Essa frase não é um palíndromo')"""
