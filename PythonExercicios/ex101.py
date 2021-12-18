from datetime import date


# Criar uma função voto(ano_de_nascimento)
def voto(ano):
    if idade < 17:
        return 'Negado'
    elif idade >= 18:
        return 'Obrigatório'
    elif 65 <= idade == 17:
        return 'Opcional'


# Criar um input perguntando o ano
resp = int(input('Data de nascimento: '))
idade = date.today().year - resp
print(f'Com {idade} anos => Voto {voto(resp)}.')
