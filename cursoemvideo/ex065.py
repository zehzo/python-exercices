
condicao = 'SIM'
nDetermos = 0
soma = 0

while condicao == 'SIM':
    nDetermos += 1
    n = int(input('Digite um número: '))
    if nDetermos == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    soma += n
    condicao = input('Deseja continuar? (SIM ou NAO): ').upper()


media = soma / nDetermos
print('Media: {}, Maior termo: {}, Menor termo: {}'.format(media, maior, menor))
