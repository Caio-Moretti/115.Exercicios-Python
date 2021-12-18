from time import sleep


def maior(*num):
    mai = total = 0
    print('=-' * 30)
    print('Analisando os valores passados...')
    for n in num:
        total += 1
        print(f'{n} ', end='')
        sleep(0.3)
        if total == 0:
            mai = n
        if n > mai:
            mai = n
    print(f'- Foram informados {total} valores ao todo.')
    print(f'O maior valor informador foi o {mai}')


maior(1, 2, 7, 2, 3, 5)
sleep(3)
maior(4, 7, 0)
sleep(3)
maior(1, 2)
sleep(3)
maior(6)
sleep(3)
maior()
