def passo(inicio, fim, passo):
    soma = 0
    if passo == 0:
        passo = 1
    if inicio > fim:
        for i in range(inicio, fim, passo):
            soma += i
    else:
        for i in range(fim, inicio, passo):
            soma += i
    return print(soma)

passo()