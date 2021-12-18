num = (int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')),
       int(input('Digite um valor: ')))
print(num)
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 foi digitado na posição {num.index(3) + 1}')
else:
    print(f'O valor 3 não foi encontrado.')
print(f'Os valores pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n)
