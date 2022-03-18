frase = '  Curso em Video Python  '
print (frase[8:])
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[::2])
print("""Texto muito grande utilizando 3 aspas""")
print(frase.count('o'))
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.strip().replace('Python','Android'))

frase.replace('Python','Android')
print (frase)

frase = frase.strip().replace('Python','Android')
print (frase)

print ('Curso' in frase)

print(frase.find('Curso'))

dividido = frase.split()
print(dividido[0])
print(dividido[0][2])

