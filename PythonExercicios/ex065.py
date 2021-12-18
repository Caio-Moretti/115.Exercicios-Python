resposta = 's'
soma = contador = maior = menor = media = 0
while resposta.lower() not in 'n':
    n = int(input('Digite um número: '))
    soma += n
    contador += 1
    media = (media + n) / 2
    if contador == 1:
        maior = menor = media = n
    else:
        if n < menor:
            menor = n
        if n > maior:
            maior = n
    resposta = str(input('Quer continuar [S/N]? ')).strip().lower()

print('A soma entre os valores é {}'.format(soma))
print('Você digitou {} números'.format(contador))
print('A média entre eles é {}'.format(media))
print('O maior valor foi o {}'.format(maior))
print('O menor valor foi o {}'.format(menor))
print('FIM')
