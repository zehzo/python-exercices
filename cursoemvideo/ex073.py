classif = ('Atletico','Flamengo','Corinthians','Palmeiras','Fluminense','America','Sao Paulo','Gremio','Vasco','Internacional',
      'Botafogo','Sport','Cruzeiro','Vitoria','Santos','Chapecoense','Atletico','Bahia','Ceara','Parana')
print('Os 5 primeiros colocados são: ',end='')
for time in classif[:5]:
    print(f'{time}, ', end='') #if classif[5] == True: print('end='\b'))
print('\b\b.')
print('Os últimos 4 colocados são: ',end='')
for time in classif[:-5: -1]:
    print(f'{time}, ', end='')
print('\b\b.')
print('Os times em ordem alfabética: ',end='')
for time in sorted(classif):
    print(f'{time}, ', end='')
print('\b\b.')
#print(f'O time da Chapecoense está no {classif.index('Chapecoense')}')
pos = (classif.index('Chapecoense')) + 1
print(f'Chapecoense é o {pos}º colocado.')