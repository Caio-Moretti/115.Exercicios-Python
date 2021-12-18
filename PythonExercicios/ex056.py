media = 0
nome_do_mais_velho = ''
menos_de_20 = 0
velho = 0
for c in range(0, 4):
    nome = str(input('Digite o nome: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('digite o sexo: '))
    media = (media + idade) / 2
    if sexo.lower() == 'feminino' and idade < 20:
        menos_de_20 += 1
    elif sexo.lower() == 'masculino' and idade > velho:
        velho = idade
        nome_do_mais_velho = nome
print('A média das idades é: {:.2f}'.format(media))
print('O nome do homem mais velho é: {}'.format(nome_do_mais_velho))
print('Número de mulheres que tem menos de 20 anos: {}'.format(menos_de_20))
