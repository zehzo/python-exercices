lista = []
maior = menor =  0

for pos in range(5):
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    if pos == 0:
        maior = lista[pos]
        menor = lista[pos]
    else:
        if valor > maior:
            maior = valor
        if valor < menor:
            menor = valor


print(lista)
print(f'O maior valor digitado foi {maior} na(s) posição(ões): ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {menor} na(s) posição(ões): ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f'{i}... ', end='')
print()