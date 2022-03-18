nome = str(input('Digite o seu nome: '))
if nome == 'José':
    print('Que nome bonito!')
elif nome == 'Pedro' or 'Maria' or 'Paulo':
    print('O seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia, {}'.format(nome))