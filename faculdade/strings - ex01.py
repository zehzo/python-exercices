# Ler 2 strings e dizer quantas vezes o primeiro aparece no segundo.

string1 = input('Digite uma frase: ')
string2 = input('Digite outra frase: ')
qtd = 0
pos = string2.find(string1)
while pos != -1:
    qtd += 1
    pos = string2.find(string1, pos + 1)

print(qtd)