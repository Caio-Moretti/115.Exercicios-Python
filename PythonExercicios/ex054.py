from datetime import date
atual = date.today().year
maioridade = 0
for c in range(0, 7):
    ano = int(input('Digite o ano de nascimento da pessoa: '))
    idade = atual - ano
    if idade >= 21:
        maioridade += 1
print('{} pessoas são maiores de idade'.format(maioridade))

