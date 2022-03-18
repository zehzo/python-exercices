#Calcular o valor de S, onde S é:• S = 1 + 3/2 + 5/3 + 7/4 + ... + 99/50

'''numeroDePassos = float(input('Digite um número de passos: '))
S = 1
soma = 0
for i in range(1,numeroDePassos/2):
    numerador = S + 2
    denominador = S + 1
    soma += numerador / denominador
print(soma)

numeromax = int(input('Digite o último número a ser dividido na sequencia: '))
dividendo = 1
divisor = 1
soma = 0
for i in range(1,numeromax+1):
    soma += dividendo/divisor
    dividendo += 2
    divisor += 1
print(soma)'''

#Calcular o valor de S com N termos, onde N é informado pelo usuário e S é:•
#S = 2/500 - 5/490 + 2/480 - 5/470 + ...

denominador = 500
n = int(input('Digite o numero de iteracoes:'))
aux1 = aux2 = soma = 0

for i in range(1, n + 1):
    if (denominador > 0):
        aux1 = -5 /denominador
        aux2 = 2 / denominador
        if (i%2 == 0):
            soma = soma + aux1
        else:
            soma = soma + aux2
        print('Soma = {} Denominador = {} Aux1 = {} Aux2 = {} i = {}'.format(soma, denominador, aux1, aux2, i))
    else:
        print('Erro')
    denominador = denominador - 10
