from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Número da carteira de trabalho [não tem: 0]: '))
dados['idade'] = datetime.now().year - nasc
if dados['ctps'] != 0:
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = (dados['ano de contratação'] + 35) - nasc
print('=-' * 30)
for k, v in dados.items():
    print(f' {k} = {v}')
