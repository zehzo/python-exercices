
matriz = [[], [], []]

for i in range(len(matriz)):
    for j in range(1, 4):
        valor = int(input('Digite um valor para ser adicionado para {}X{}: '.format((i + 1), j)))
        matriz[i].append(valor)

for i in range(len(matriz)):
    for j in range(3):
        print(f'[ {matriz[i][j]} ]',end = '')
    print('\n',end='')


