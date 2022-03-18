quilometros_rodados = int(input('Digite quantos quilômetros serão percorridos: '))
print('O valor da sua viagem será de R${:.2f}'.format(quilometros_rodados * 0.50) if quilometros_rodados < 200
      else 'O valor de sua viagem será de R${:.2f}'.format(quilometros_rodados * 0.45))
