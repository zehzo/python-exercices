
lista = []
dado = []
maior = 0
menor = 99999999999
maisLeve = ''
maisPesado = ''
condicao = True

while condicao == True:
    dado.append(str(input('Digite o nome da pessoa: ')))
    dado.append(float(input('Digite o peso da pessoa: ')))
    lista.append(dado.copy())
    continuar = input('Deseja inserir mais valores? (S ou N): ')
    if continuar in 'Nn':
        condicao = False
    if dado[1] > maior:
        maisPesado = dado[0]
    if dado[1] < menor:
        maisLeve = dado[0]
    dado.clear()

print('Foram cadastradas {} pessoas.'.format(len(lista)))
print(maisLeve, maisPesado)
