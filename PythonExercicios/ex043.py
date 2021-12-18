altura = float(input('Digite a altura em metros: '))
peso = float(input('Digite o peso em Kg: '))
imc = peso / (altura ** 2)
print('IMC = {:.2f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
