frase = str(input('Digite uma frase: ')).strip()
print ('A letra A aparece {} vezes' .format(frase.upper().count('A')))
print ('A primeira vez que a letra A aparece está na posição {}'.format(frase.upper().find('A')+1))
print ('A ultima vez que a letra A aparece está na posição {}'.format(frase.upper().rfind('A')+1))
