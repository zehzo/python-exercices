#Ler um número inteiro N e imprimir o valor do n-ésimo termo da sequência [-1, 0, 5, 6, 11, 12, 17, 18, ...]

n = int(input('Digite a quantidade de termos da sequencia: '))
termo1 = -1
termo2 = 0
for i in range(1, n + 1):
    if (i % 2 != 0):
        termoFinal = termo1
        termo1 = termo1 + 6
    else:
        termoFinal = termo2
        termo2 = termo2 + 6
print(f'Termo {n} da sequencia: {termoFinal}')

'''nDeTermos = int(input('Digite a quantidade de termos da sequencia: '))
termo1 = -1
termo2 = 0
for i in range(1, nDeTermos + 1):
    print (i, end= ' ')
    if (i % 2 != 0):
        print(termo1)
        termoFinal = termo1
        termo1 = termo1 + 6
    else:
        print(termo2)
        termoFinal = termo2
        termo2 = termo2 + 6
print(f'Termo {nDeTermos} da sequencia: {termoFinal}')'''