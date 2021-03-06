def fatorial(num, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param num: O número a ser calculado
    :param show: (Opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial do número num
    """
    f = 1
    for c in range(num, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(' = ', end='')
    return f


print(fatorial(5, True))
