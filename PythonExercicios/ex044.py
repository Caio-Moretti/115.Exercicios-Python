valor = float(input('Digite o valor do produto: '))
pagamento = int(input('Selecione a forma de pagamento: '
                      '\n1. À vista no dinheiro, cheque ou débito. '
                      '\n2. À vista no cartão de crédito. '
                      '\n3. 2x no cartão de crédito. '
                      '\n4. 3x no cartão de crédito. '
                      '\n5. Quero parcelar em mais vezes.'
                      '\nResposta: '))
if pagamento == 5:
    parcela = int(input('Em quantas vezes você quer parcelar? '))
elif pagamento == 4:
    print('O seu produto custará 3 parcelas de {:.2f} reais'.format((valor * 1.20) / 3))
elif pagamento == 3:
    print('O seu produto custara 2 parcelas de {:.2f} reais'.format(valor / 2))
elif pagamento == 2:
    print('O seu produto custará {:.2f} reais (5% de desconto)'.format(valor * 0.95))
elif pagamento == 1:
    print('O seu produto custará {:.2f} reais (10% de desconto)'.format(valor * 0.90))
else:
    print('Insira uma opção disponível.')

if pagamento == 5:
    print('Seu produto custará {} parcelas de {} reais'.format(parcela, (valor * 1.20) / parcela))
else:
    print('Obrigado por comprar nosso produto.')
