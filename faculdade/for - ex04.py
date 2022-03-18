#Somar os inteiros ímpares entre dois valores inteiros informados pelo usuário.
'''o contador deve pegar os números entre o número inicial e o final, logo, é necessário iniciar a contagem do número
    inicial + 1 e ir até o número final que no python é um número que não entra na interação.'''
inicial = int(input('Digite o número inicial: '))
final = int(input('Digite o número final: '))
soma = 0
if inicial < final:
    for i in range (inicial + 1, final):
        if (i%2 != 0): #condição para testar se o número é impar
            soma += i
    print(soma)
elif final < inicial:
    for i in range (inicial, final - 1, -1):
        if (i%2 != 0):
            soma += i
    print(soma)
else:
    print('Os dois numeros sao iguais!')