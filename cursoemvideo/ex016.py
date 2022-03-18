'''x = float(input("Digite um número: "))
y = int (x)
print("A porção inteira do número {} é: {}".format(x, y))'''

from math import trunc
num = float(input("Digite o valor: "))
print('A porção inteira do número {} é {}'.format(num, trunc(num)))