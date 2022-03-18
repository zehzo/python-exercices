lista = []
condicao = True

while condicao:
    valor = int(input('Digite um valor para ser adicionado a lista: '))
    lista.append(valor)
    condicao = str(input('Deseja digitar mais valores? (S ou N): '))
    if condicao not in 'Ss':
        condicao = False

listaPares = []
listaImpares = []

for i in lista:
    if i % 2 == 0:
        listaPares.append(i)
    else:
        listaImpares.append(i)

print('Lista: {}'.format(lista))
print('Lista Pares: {}'.format(listaPares))
print('Lista Impares: {}'.format(listaImpares))

