#Calcular o valor de S com N termos, onde N é informado pelo usuário e S é: S = 37*38/1 + 36*37/2 + 35*36/3 + ...

n = int(input('Digite o número de termos: '))
somaTotal = 0
num1 = 37
num2 = 38

for i in range(1, n+1):
    somaAtual = (num1 * num2)/i
    print(f'({num1} * {num2})/{i}')
    num1 -= 1
    num2 -= 1
    print(somaAtual)
    somaTotal += somaAtual
    print(f'Para N = {n}| S = {somaTotal}')