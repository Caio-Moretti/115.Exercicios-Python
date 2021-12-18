v = float(input('Digite um valor em metros: '))
cm = v * 100
mm = v * 1000
print(('O valor que você digitou é {}m\nEsse valor equivale a {:.0f}cm e {:.0f}mm'.format(v, cm, mm)))
