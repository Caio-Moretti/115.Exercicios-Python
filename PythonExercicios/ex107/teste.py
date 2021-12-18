from ex107 import moeda
p = float(input('Preço: '))
print(f'O preço {p:.2f} dobrado é {moeda.dobro(p):.2f}')
print(f'O preço {p:.2f} pela metade é {moeda.metade(p):.2f}')
print(f'O preço {p:.2f} com 10% de aumento é {moeda.aumentar(p, 10):.2f}')
print(f'O preço {p:.2f} com 30% de desconto é {moeda.diminuir(p, 30):.2f}')
