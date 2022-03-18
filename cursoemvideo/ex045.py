#pedra, papel ou tesoura
from random import randint
escolhadojogador = str(input('Escolha uma das opcoes: Pedra, Papel ou Tesoura: ')).strip()

if escolhadojogador.upper() == 'PEDRA':
    escolha = 1
elif escolhadojogador.upper() == 'PAPEL':
    escolha = 2
elif escolhadojogador.upper() == 'TESOURA':
    escolha = 3

maquina = randint(1,3)

if escolha == 1:
    if maquina == 2:
        print('Voce Perdeu!')
    elif maquina == 3:
        print('Voce Ganhou!')
    else:
        print('Empate')
elif escolha == 2:
    if maquina == 1:
        print('Voce ganhou!')
    elif maquina == 3:
        print('Voce perdeu!')
    else:
        print('Empate!')
elif escolha == 3:
    if maquina == 1:
        print('Voce perdeu!')
    elif maquina == 2:
        print('Voce ganhou!')
    else:
        print('Empate!')
else:
    print('Digite Pedra, Papel ou Tesoura corretamente!')

if maquina == 1:
    maquina = 'Pedra'
elif maquina == 2:
    maquina = 'Papel'
elif maquina == 3:
    maquina = 'Tesoura'
print ('Voce escolheu {} e a maquina escolheu {}' .format(escolhadojogador, maquina))
