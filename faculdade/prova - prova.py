
'''nDeTermos = int(input('Digite o número de termos: '))
while nDeTermos <= 0:
    nDeTermos = int(input('Digite um número de termos válido: '))

numerador = 10
denominadorImpar = 1
denominadorPar = 5
contador = 1
somaAcumulada = 0
denominador = 1

while contador <= nDeTermos:
    if contador == 2:
        denominador = -denominadorPar
    if contador > 2:
        if contador % 2 == 0 and contador > 2:
            denominadorPar += 6
            denominador = -denominadorPar
        else:
            denominadorImpar += 7
            denominador = denominadorImpar
    soma = numerador / denominador
    somaAcumulada += soma
    numerador += 2
    contador += 1

print('O valor da série com {} termos é {}'.format(nDeTermos, somaAcumulada))'''

'''
n_termos = ''
numerador = 10
denominador_impar = 1
denominador_par = 5
soma = 0

while not n_termos.isnumeric():
    n_termos = input('Digite o número de termos a serem aplicados à série: ')
n_termos = int(n_termos)

for n in range(n_termos):
    if n%2 == 0:
        soma += (numerador/denominador_impar)
        denominador_impar += 7
    else:
        soma -= (numerador/denominador_par)
        denominador_par += 6
    numerador += 2
    
print('O valor da série com {} termos é {}'.format(n_ter
não tem espaço pra colocar até o finnal do print
print('O valor da série com {} termos é {}'.format(n_termos, soma))
'''

qtdDeNumeros = 0
lista = []
numeroDigitado = int(input('Digite um número: '))
while numeroDigitado != 0:
    lista.append(numeroDigitado)
    numeroDigitado = int(input('Digite outro número: '))
for qtd in lista:
    qtdDeNumeros += 1
print(qtdDeNumeros)
tresDigitos = []
tresDigitosPositivo = []
tresDigitosNegativo = []
print('Numeros de 3 digitos significativos: ', end='')
for numero in lista:
    if numero < -99 and numero > -1000:
        tresDigitosNegativo.append(numero)
    if numero > 99 and numero < 1000:
        tresDigitosPositivo.append(numero)
tresDigitos = tresDigitosNegativo + tresDigitosPositivo

soma = 0
quantidade = 0
for numero in tresDigitos:
    print(f'{numero} ', end='')
    soma += numero
    quantidade += 1
if quantidade != 0:
    media = soma / quantidade
print(f'\nMédia: {media}')

contador7 = 0:
for numero in lista:
    if numero % 7 == 0:
        if contador7 == 0:
            maior = numero
        if maior >= numero:
        maior = numero

print('Maior número digitado multiplo de 7: {}'.format(maior))


'''
num = 1
cont = 0
listan = []
listap = []
maior = 0
soma = 0
while num != 0:
    num = int(input('Digite um número: '))
    cont += 1
    if num < 1 and num / -100 > 1 and num / -1000 < 1:
        listan += [num]
        soma += num
    elif num > 1 and num / 100 > 1 and num / 1000 < 1:
        listap += [num]
        soma += num
    if num > maior and num % 7 == 0:
        maior = num
média = soma / cont

'''