'''Construir uma tabela de conversão de graus Fahrenheit para Celsius, para todos os Fahrenheit
em um intervalo informado pelo usuário.'''

valorInicial = int(input('Digite um valor em Fahrenheit: '))
valorFinal = int(input('Digite outro valor em Fahrenheit: '))

if valorInicial > valorFinal:
    valorInicial, valorFinal = valorFinal, valorInicial

for i in range(valorInicial, valorFinal + 1):
    C = (i - 32) * 5 / 9
    print(f'Fahrenheit = {i} | Celsius = {C}')

