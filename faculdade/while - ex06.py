numero = float(input('Digite um número: '))
numeroDeTermos = 1
soma = 0

while numero >= 0:
	soma += numero
	numeroDeTermos += 1

	numero = float(input('Digite outro número: '))

media = soma/numeroDeTermos

print(media)