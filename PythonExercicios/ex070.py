menor = mais_que_mil = total = 0
mais_barato = ' '
cont = 1
print('-=' * 20)
print('SUPER MERCADO')
print('-=' * 20)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$: '))
    if cont == 1 or preco < menor:
        menor = preco
        mais_barato = produto
    if preco > 1000:
        mais_que_mil += 1
    total += preco
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
    else:
        cont += 1
print('=-' * 20)
print('------CHECK OUT------')
print(f'Quantidade: {cont} produtos')
print(f'Produto mais barato: {mais_barato} ({menor})')
print(f'Total gasto na compra: R$: {total:.2f}')
print(f'Quantidade de produtos acima de R$:1000.00: {mais_que_mil}')
print('=-' * 20)
print('FIM DO PROGRAMA')
print('=-' * 20)
