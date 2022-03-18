'''string = str(input('Digite a expressao: '))
if string.count('(') == string.count(')'):
    print('A expressão foi digitada corretamente')
else:
    print('A expressão não foi digitada corretamente')'''

expressao = str(input('Digite a expressão matemática: '))
lista = []
for i in expressao:
    if i == '(':
        lista.append(')')
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')


if len(lista) == 0:
    print('Lista válida!')
