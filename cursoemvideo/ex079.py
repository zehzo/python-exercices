condicao = True
lista = []
cont = 0

while condicao == True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('O valor não será adicionado.')
    else:
        lista.append(valor)
    continuar = input('Deseja continuar adicionando valores? S ou N: ')
    if continuar in 'Ss':
        condicao = True
    else:
        condicao = False

listaOrdenada = sorted(lista)
print(f'A lista em ordem crescente é : {listaOrdenada}')
