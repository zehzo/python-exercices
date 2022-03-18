tupla = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
         int(input('Digite outro valor: ')), int(input('Digite outro valor: ')))
contador9 = 0
for i in tupla:
    if i == 9:
        contador9 += 1
print(contador9)

if 3 not in tupla:
    print('O valor 3 não foi digitado')
else:
    posicao = tupla.index(3)
    print('O valor 3 foi digitado na posição {}'.format(posicao))

contador = 0
print('-=-' * 30)
for i in tupla:
    if i % 2 == 0:
        if contador ==0:
            print('Os números pares digitados são: ')
        print('{} '.format(i))
        contador += 1
if contador == 0:
    print('Não foi digitado nenhum número par')
