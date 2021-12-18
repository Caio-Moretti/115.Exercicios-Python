v = float(input('Digite a velocidade do carro (Em Km/h): '))
if v > 80:
    print('Carro acima da velocidade permitida! Multa com o valor de {:.2f} reais'.format((v - 80) * 7))
else:
    print('{}Km/h. Carro dentro do limite de velocidade.'.format(v))
