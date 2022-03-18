from random import randint

computador = randint(1,10)

usuario = int(input('Digite um valor de 1 a 10: '))

while usuario != computador:
    usuario = int(input('Você errou, tente novamente: '))

print('Parabéns! {} é o número aleatório!'.format(usuario))