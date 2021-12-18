sal = float(input('Qual o salário? '))
if sal <= 1250:
    print('O seu salário de R$: {:.2f} com aumento fica R$:{:.2f}'.format(sal, sal * 1.15))
else:
    print('O seu salário de R$: {:.2f} com aumento fica R$:{:.2f}'.format(sal, sal * 1.10))
