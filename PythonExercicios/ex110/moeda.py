def aumentar(preço, taxa, formato=False):
    res = preço + (preço * taxa/100)
    return res if not formato else moeda(res)


def diminuir(preço, taxa, formato=False):
    res = preço - (preço * taxa/100)
    return res if not formato else moeda(res)


def dobro(preço, formato=False):
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço, formato=False):
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}: {preço:.2f}'.replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=10):
    print('-' * 50)
    print(f'Preço analisado: {moeda(preço)}'.center(50))
    print('-' * 50)
    print(f'Dobro do preço analisado: \t{dobro(preço, True)}')
    print(f'Metade do preço analisado: \t{metade(preço, True)}')
    print(f'Aumento de {taxaa}% no preço: \t{aumentar(preço, taxaa, True)}')
    print(f'Redução de {taxar}% no preço: \t{diminuir(preço, taxar, True)}')
    print('-' * 50)

