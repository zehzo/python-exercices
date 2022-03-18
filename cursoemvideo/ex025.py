#nome = str(input('Digite o nome: ')).strip()
#print (('Seu nome tem silva? {}' .format(nome.upper().find('SILVA'))))

nome = str(input('Qual é o seu nome completo? ')).strip()
print ('Seu nome tem silva? {}'.format('SILVA' in nome.upper()))