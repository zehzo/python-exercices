
listaNegativos = []
negativo = -1
while negativo < 0 and len(listaNegativos) != 2:
    negativo = int(input('Digite um número negativo: '))
    if negativo < 0:
        listaNegativos.append(negativo)
    if len(listaNegativos) == 2:
        print('Essa foi a ultima iteração, o programa será finalizado.')

multiplosDe5 = []
for numero in listaNegativos:
    if numero % 5 == 0:
        multiplosDe5.insert(0, numero)

print('Os múltiplos de 5 que foram digitados, em ordem inversa, são:', end='')
for num in multiplosDe5:
    print(' {},'.format(num),end='')
print('\b.')

maior = 0 #Essa variável vai ser substituída na primeira iteração do programa
for i in range(len(listaNegativos)):
    if i == 0:
        maior = listaNegativos[i]
    else:
        if (listaNegativos[i] % 11) == 0 and listaNegativos[i] > maior:
            maior = listaNegativos[i]
if maior % 11 != 0: #para evitar que valor maior fique como o valor do primeiro item da lista
    #caso não haja outros números divisíveis por 11.
    print('Não foi digitado nenhum número divisível por 11.')
else:
    print('O maior valor digitado múltiplo de 11 foi: {}'.format(maior))


