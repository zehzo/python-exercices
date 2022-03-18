from random import randint

n = int(input('Digite quantos jogos serão gerados: '))
palpites = []
jogos = []

for i in range(n):
    palpites.clear()
    for j in range(6):
        valor = randint (1,60)
        if valor in palpites:
            valor = randint(1,60)
        palpites.append(valor)
    jogos.append(palpites.copy())

print(jogos)
