lista = []

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        contador = 0
        while pos < len(lista):
            if n <= lista[pos] and contador == 0:
                lista.insert(pos, n)
                contador += 1
            pos += 1
print(lista)