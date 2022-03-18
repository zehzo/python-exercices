def area(l, c):
    return print(f'A área do terreno de {l} x{c} é: {(l*c):.2f}m².')

l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))

area(l,c)