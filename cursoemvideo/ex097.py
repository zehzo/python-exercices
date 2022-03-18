def printbonito(texto):
    l = len(texto) + 4
    print('~'* (l))
    print(f'{texto:^{l}}')
    print('~' * (l))

text = 'Qualquer coisa'
printbonito(text)
printbonito('Teste')
printbonito('Agora vamos ver se deu certo mesmo!')
