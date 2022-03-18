#Palindromo

frase = input('Digite a frase: ').upper().strip()
fraseSplit = frase.split()
fraseJunta = ''.join(fraseSplit)
fraseInvertida = ''

for char in range (len(fraseJunta) - 1 , -1 , -1):
    fraseInvertida += str(fraseJunta[char])

if fraseInvertida == fraseJunta:
    print('A frase digitada é um palíndromo!!')