ano = int(input('Digite um ano: '))
print('Ano bissexto' if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0 else 'Ano não bissexto')
#how to make this works?, if we put a number