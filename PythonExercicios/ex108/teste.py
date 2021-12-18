from ex108 import moeda
p = float(input('Preço: R$: '))
print(f'O preço {moeda.moeda(p)} dobrado é {moeda.moeda(moeda.dobro(p))}')
print(f'O preço {moeda.moeda(p)} pela metade é {moeda.moeda(moeda.metade(p))}')
print(f'O preço {moeda.moeda(p)} com 10% de aumento é {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'O preço {moeda.moeda(p)} com 30% de desconto é {moeda.moeda(moeda.diminuir(p, 30))}')
