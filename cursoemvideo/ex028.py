#import random
#random = random.randint(1,4)
#numero = int(input('Digite um número entre 0 e 5: '))
#print('Você acertou' if numero == random else 'Você errou')

from random import randint
from time import sleep
computador = randint (0,5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5, tente adivinhar..')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}'.format(computador,jogador))