numero = int(input('Digite um numero: '))
divisor = 1
condicao = 0

while numero <= divisor:
	numero = int(input('Digite um numero válido: '))

while numero > divisor:
	if (numero % divisor == 0) :
		condicao += 1
	divisor += 1

if condicao >= 2:
	print('Numero não é Primo!')
else:
	print('Numero Primo!')
