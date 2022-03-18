red = '\033[31m'
green = '\033[32m'
yel = '\033[33m'
stop = '\033[m'

num = int(input('Digite um número inteiro: '))
op = int(input('Digite 1 para converter o número para binário, 2 para octal e 3 para hexadecimal: '))

if op == 1:
    print('O valor convertido para binário é: {} '.format(bin(num)[2:]))
elif op == 2:
    print('O valor convertido para octal é: {} '.format(oct(num)[2:]))
elif op == 3:
    print('O valor convertido para hexadecimal é: {}'.format(hex(num)[2:]))
else:
    print('{}Digite uma opção válida!{}'.format(red, stop))
