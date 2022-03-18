#Dada uma frase qualquer em uma string, print a frase sem as vogais

fraseQualquer = str(input('Digite uma frase: '))

vogais = 'aeiou'
final = ''

for letra in fraseQualquer:
    if letra not in vogais:
        final += letra
print(final)