l1 = int(input('Digite o valor de um lado: '))
l2 = int(input('Digite o valor de outro lado: '))
l3 = int(input('Digite o valor de mais um lado: '))
if l1 >= l2 + l3 and l2 >= l3 + l1 and l3 >= l1 + l2:
    print("Triângulo inexistente.")
else:
    print("Triângulo existente")
