idade = quant_homens = quant_mulheres_20 = quant_maiores = 0
while True:
    sexo = ' '
    idade = int(input('Digite a idade: '))
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        quant_maiores += 1
    if sexo == 'F' and idade < 20:
        quant_mulheres_20 += 1
    else:  # se não for F vai ser M.
        quant_homens += 1
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'Você cadastrou {quant_maiores} pessoas maiores de 18 anos')
print(f'Você cadastrou {quant_homens} homens.')
print(f'Você cadastrou {quant_mulheres_20} mulheres menores de 20 anos')
print('FIM DO PROGRAMA')
print('--' * 20)
