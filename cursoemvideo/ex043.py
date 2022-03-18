peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura (em metros) : '))
imc = peso/(altura**2)
if imc <= 18.5:
    print ('Abaixo do peso!')
elif 18.5 < imc <= 25:
    print('Peso Ideal!')
elif 25 < imc <= 30:
    print('Sobrepeso')
elif 30 < imc <= 40:
    print('Obesidade')
elif 40 < imc:
    print('Obesidade mórbida')
