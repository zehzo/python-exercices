matriz = [[], [], []]
listaPares = []

soma3coluna = 0
maximo2 = -999999999999
for i in range(len(matriz)):
    for j in range(1, 4):
        valor = int(input('Digite um valor para ser adicionado para {}X{}: '.format((i + 1), j)))
        matriz[i].append(valor)
        if valor % 2 == 0:
            listaPares.append(valor)
        if j == 2:
            if valor > maximo2:
                maximo2 = valor
        if j == 3:
            soma3coluna += valor


for i in range(len(matriz)):
    for j in range(3):
        print(f'[ {matriz[i][j]:^5} ]', end='')
    print('\n', end='')


somaPares = 0
for valor in listaPares:
    somaPares += valor

print(f'A soma dos valores pares é: {somaPares}')
print(f'A soma dos valores da ultima coluna é: {soma3coluna}')
print(f'O maior valor digitado da segunda coluna é: {maximo2}')
