#nomedacidade = input('Digite o nome da sua cidade: ')
# dividir o nome utilizando o split, isolar o primeiro nome,
#print('Começa com santo?: {}'.format(nomedacidade.split()[0].lower().join().find('santo')))

cid = str (input('Em que cidade você nasceu? ')).strip()
print (cid[:5].upper() == 'SANTO')

