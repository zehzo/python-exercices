from time import strftime,localtime
ano = int(strftime('%Y', localtime()))
anouser = int(input('Qual o seu ano de nascimento?: '))
dif = ano - anouser
if dif <= 9:
    print('Categoria MIRIM')
elif 9 < dif < 14:
    print('Categoria INFANTIL')
elif 14 <= dif < 19:
    print ('Categoria JUNIOR')
elif 19 <= dif < 20:
    print ('Categoria SÊNIOR')
else:
    print ('Categoria MASTER')
