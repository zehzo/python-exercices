nome = str(input('Digite o seu nome: '))
if nome == 'José':
    print('Que nome lindo você tem!')
else:
    print("Que nome normal!")
print("Bom dia {}!".format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('A sua média foi {:.2}'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
print ('Parabéns!' if m>= 6 else 'Estude mais!')
