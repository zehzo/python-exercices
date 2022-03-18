#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números impares e de numeros pares

par = impar = 0

for i in range (10):
    numero = int(input('Digite um número inteiro: '))
    if (numero % 2 == 0):
        par += 1
    else:
        impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')
