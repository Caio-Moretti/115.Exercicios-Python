import math
n = int(input('Digite um ângulo para saber seu seno, cosseno e tangente: '))
cos = math.cos(math.radians(n))
sin = math.sin(math.radians(n))
t = math.tan(math.radians(n))
print('Seu ângulo: {}'.format(n))
print('Seno: {:.2f}'.format(sin))
print('Cosseno: {:.2f}'.format(cos))
print('Tangente: {:.2f}'.format(t))
