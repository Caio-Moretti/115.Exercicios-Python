def área(a, b):
    ar = a * b
    print(f'A área do terreno é {ar:.1f} ({a} x {b})')


comp = float(input('Comprimento: '))
larg = float(input('Largura: '))
área(comp, larg)
