from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade <= 9:
    print('CATEGORIA MIRIM')
elif idade <= 14:
    print('CATEGORIA INFANTIL')
elif idade <= 19:
    print('CATEGORIA JÚNIOR')
elif idade <= 20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')
print('IDADE: {}'.format(idade))
