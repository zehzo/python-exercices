numero = int(input('Digite um número: '))
soma = 0
divisor = 1

while numero > divisor:
	if numero % divisor == 0: 
		soma += divisor
	divisor += 1

if soma == numero:
	print('Número Perfeito!')
