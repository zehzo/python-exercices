# Peso de 5 pessoas, mostrar maior peso e menor

'''import math
pesoAnt = 0
maior = - (math.inf)
menor = (math.inf)

for i in range(0,5):
    peso = int(input('Digite o peso: '))
    if peso >= pesoAnt:
        maior = peso
    elif peso <= pesoAnt:
        menor = peso
    pesoAnt = peso

print(f'O maior peso digitado foi: {maior} e o menor: {menor}')
'''

maior = menor = 0

for p in range(1, 6):
    peso = float(input('Digite o peso da {}º pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}kg'.format(maior))
print('O menor peso lido foi de {}kg'.format(menor))