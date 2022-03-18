lista = []
condicao = True
qtdDeNumeros = 0

while condicao == True:
    valor = int(input('Digite um valor para ser adicionado na lista: '))
    lista.append(valor)
    qtdDeNumeros += 1
    continuar = input('Deseja inserir mais valores? (S ou N): ')
    if continuar in 'Nn':
        condicao = False


print(f'Foram digitados {qtdDeNumeros} números')
lista = lista.sort(reverse=True)
print(f'Lista decrescente: {lista}')

if 5 in lista:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
