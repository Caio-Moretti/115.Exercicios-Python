dis = float(input('Digite a distância da sua viagem em Km: '))
if dis <= 200:
    print('O valor da sua passagem será {:.2f} reais'.format(dis * 0.5))
else:
    print('O valor da sua passagem será {:.2f} reais'.format(dis * 0.45))
