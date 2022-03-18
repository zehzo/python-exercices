n_termos = ''
numeradorImpar = 150
numeradorPar = 156
denominador = 20
soma = 0

while not n_termos.isnumeric():
    n_termos = input('Digite o número de termos da série: ')
    while n_termos[0] == '-':
        n_termos = input('Digite o número de termos da série: ')
n_termos = int(n_termos)

for n in range(1, n_termos + 1):
    if n % 2 == 0:
        print(f'{numeradorPar}, {denominador}')
        soma -= (numeradorPar / denominador)
        numeradorPar += 14
    else:
        print(f'{numeradorImpar}, {denominador}')
        soma += (numeradorImpar / denominador)
        numeradorImpar += 12
    denominador += 10 * n


print('O valor da série com {} termos é {}'.format(n_termos, soma))