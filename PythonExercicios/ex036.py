valor = float(input('Qual é o valor da casa? '))
sal = float(input('Qual é o valor do salário? '))
tempo = int(input('Em quantos anos a casa vai ser paga? '))
parcela = valor / (tempo * 12)
print('Cada parcela mensal dessa casa vai custar {:.2f} reais.'.format(parcela))
if parcela > (0.30 * sal):
    print('Empréstimo negado. o valor da parcela excedeu 30% do seu salário.')
else:
    print('Empréstimo feito com sucesso. Você poderá comprar sua casa.')
