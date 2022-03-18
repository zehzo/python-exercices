# Mostrar fatorial do numero

numero = int(input('Digite um número: '))
fatorial = numero
print('Fatorial de {} ('.format(numero), end='')

while numero > 1:
    print('{} x '.format(numero), end='')
    fatorial = fatorial * (numero - 1)
    numero -= 1
print('1) = {}'.format(fatorial))