'''termo1 = int(input('Digite o primeiro termo: '))
pa = int(input('Digite a PA: '))
resultado = termo1

#termo1 , termo1 + pa, termo1 + 2 * pa

while resultado < (termo1 + (10 * pa)):
    print(resultado)
    resultado += pa
'''
print('Gerador de PA')
print(10 * '-=')

primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1
print('\b\b\nFIM!')

