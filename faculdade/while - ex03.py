N = int(input('Digite o número de termos: '))
soma = 1
numerador = 1
denominador = 1
contador = 1

while contador < N :
	numerador += 2
	denominador += 1
	contador += 1
	termoStr = print(f'{numerador}/{denominador}')
	termoAtual = numerador/denominador
	soma += termoAtual

print(soma)