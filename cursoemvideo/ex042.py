a = int(input('Digite o lado do triângulo: '))
b = int(input('Digite outro lado do triângulo: '))
c = int(input('Digite outro lado do triângulo: '))
if abs(a-c) < b < a+c and abs(a-b) < c < a+c and abs (b-c) < a < b+c:
    print('O triângulo com os lados {}, {} e {} existe!'.format(a,b,c))
    if a == b == c:
        print('Esse triângulo é equilátero.')
    elif a != b != c:
        print('Esse triângulo é escaleno')
    else:
        print('Esse triângulo é isósceles')
else:
    print('O triângulo com os lados {}, {} e {} não existe!'.format(a, b, c))