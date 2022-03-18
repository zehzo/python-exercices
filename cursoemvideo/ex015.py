km = float(input('Digite a quantidade de quilômetros rodados: '))
dias = int(input('Digite a quantidade de dias: '))
valor = (km * 0.15) + (dias * 60)
print('O total a pagar foi R${:.2f} por {} quilômetros rodados em {} dias'.format(valor, km, dias))
