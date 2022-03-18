#Ler 5 números informar o maior entre eles usando o For.

numero1 = int(input('Digite um número: '))
for i in range(1,5):
    numeroTestado = int(input('Digite outro número: '))
    if numeroTestado > numero1:
        numero1 = numeroTestado
print(numero1)
