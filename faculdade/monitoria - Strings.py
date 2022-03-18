'''palavra = input('Digite algo: ')
tamanho = len(palavra)
palavrarev = ''

for c in range(tamanho - 1, -1, -1):
    print(palavra[c])
    palavrarev += palavra[c]
print(palavrarev)
'''

#Encriptação
nome = input('Digite o seu nome: ')
str_saida = ''

for char in nome:
    str_saida += str(ord(char)) + '-'
print(str_saida)

aux = ''
nomeRecuperado = ''

for char in str_saida:
    if char == '-':
        letra = chr(int(aux))
        nomeRecuperado += letra
        aux = ''
    else:
        aux += char
print(nomeRecuperado)




