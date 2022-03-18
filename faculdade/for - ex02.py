num = int(input('Digite um numero: '))
if num < 0:
    print('Não é possível realizar o cálculo com um número negativo!')
else:
    fatorial = 1
    for i in range(num, 1, -1):
        fatorial = fatorial * i
    print(fatorial)

