from datetime import date
ano = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
if idade < 18:
    print('Ainda vai se alistar.')
    print('Ainda faltam {} anos pro seu alistamento'.format(18 - idade))
elif idade == 18:
    print('Hora de se alistar.')
else:
    print('Já passou do tempo do seu alistamento.')
    print('Já se passaram {} anos do seu alistamento.'.format(idade - 18))
