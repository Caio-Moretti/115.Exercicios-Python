palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO',
            'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO',
            'PROGRAMADOR', 'FUTURO')
for palavra in palavras:
    print(f'\nNa palavra {palavra} temos as vogais ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end='')
