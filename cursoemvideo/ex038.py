num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
if num1 == num2:
    print('Os dois números são iguais!')
elif num1 > num2:
    print('O número {} é maior do que {}'.format(num1, num2))
else:
    print('O número {} é menor do que {}'.format(num1, num2))
