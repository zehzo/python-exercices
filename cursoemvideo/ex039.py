from datetime import date
yel = '\033[33m'
red = '\033[31m'
red2 = '\033[1:4:7m'
green = '\033[32m'
stop = '\033[m'
ano = int(input('{}Digite o seu ano de nascimento: {}'.format(yel,stop)))
atual = date.today().year
diferenca = (atual - ano)

if diferenca == 18:
    print ('{}Está na hora de se alistar!{}'.format(green,stop))
elif diferenca > 18:
    print ('{}Você passou {}{}{}{}{} anos do seu alistamento!{}'.format(red,stop,red2,(diferenca-18),stop,red,stop))
else :
    print('Faltam {} anos para o seu alistamento'.format(18-diferenca))

