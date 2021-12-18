lista = list()
pares = list()
impares = list()
while True:
    n = int(input('Digite o número: '))
    resp = str(input('Quer continuar? [S/N] '))
    lista.append(n)
    if resp.upper() in 'N':
        break
for v in lista:  # Não entendi porque o Guanabara usou o enumerate
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
#    if n % 2 == 0:
#        pares.append(n)
#    else:
#        impares.append(n)

print(lista)
print(pares)
print(impares)
