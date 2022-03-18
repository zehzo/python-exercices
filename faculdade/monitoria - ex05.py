qtdNumeros = int(input('Digite a quantidade de números: '))
somaTotal = somaPesos = 0

for i in range(qtdNumeros):
    numero = float(input('Digite um número: '))
    peso = float(input('Digite o peso: '))

    total = numero * peso
    somaTotal += total
    somaPesos += peso

if (somaPesos == 0):
    somaPesos = 1

media = somaTotal / somaPesos
print(media)