#S = 37*38/1 + 36*37/2

N = int(input('Digite o número de termos: '))
num = 37
den = 1
soma = 0
contador = 1

while contador < N: 
	termo = (num * (num + 1))/den
	num -= 1
	den += 1
	contador += 1
	soma += termo 
	print(termo)
	print(f'{num}/{den}')
	print(soma)