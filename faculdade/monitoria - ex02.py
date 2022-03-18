# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número
# Não utilize a função de potência da linguagem

base = int(input('Digite o primeiro número: '))
expoente = int(input('Digite o segundo número: '))
resultado = 1

for contagem in range(expoente):
    resultado = base * resultado

print(resultado)

