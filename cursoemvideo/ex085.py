#Digitar 7 valores e cadastrar em uma lista única
lista = []
listaPares = []
listaImpares = []

for i in range(7):
    valor = int(input('Digite um valor para ser adicionado na lista: '))
    lista.append(valor)

for i in lista:
    if i % 2 == 0:
        listaPares.append(i)
    else:
        listaImpares.append(i)

listaPares.sort()
listaImpares.sort()

print(f'Lista de Valores Pares em ordem crescente: {(listaPares)}')
print(f'Lista de Valores Impares em ordem crescente: {(listaImpares)}')