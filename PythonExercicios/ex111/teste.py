from ex111.UtilidadesCeV import moeda
p = float(input('Preço: R$: '))
#print(f'O preço {moeda.moeda(p)} dobrado é {moeda.dobro(p, True)}')
#print(f'O preço {moeda.moeda(p)} pela metade é {moeda.metade(p, True)}')
#print(f'O preço {moeda.moeda(p)} com 10% de aumento é {moeda.aumentar(p, 10, True)}')
#print(f'O preço {moeda.moeda(p)} com 30% de desconto é {moeda.diminuir(p, 30, True)}')
moeda.resumo(p, 12, 30)
