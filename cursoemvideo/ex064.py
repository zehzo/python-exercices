#condicao de parada = 999
soma = contador = 0
n = int(input('Digite um numero: '))

while n != 999:
    soma += n
    contador += 1
    n = int(input('Digite um numero: '))

print('Soma dos Valores: {} e foram digitados {} números'.format(soma, contador))