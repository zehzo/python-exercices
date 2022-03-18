velocidade = int(input('Digite a velocidade do carro: '))
print('Você recebeu uma multa no valor de R${:.2f}.'.format((velocidade-80)*7) if velocidade > 80 else 'Você não foi multado')