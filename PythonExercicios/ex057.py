sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo.upper() not in 'MF':
    sexo = str(input('Valor inválido. Digite novamente: ')).upper()
print('sexo {} registrado com sucesso.'.format(sexo))
