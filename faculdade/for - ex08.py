numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
mdc = 0

if numero2 > numero1:
    numero2,numero1 = numero1, numero2

for i in range(1,numero2 + 1):
    if (numero1 % i == 0 and numero2 % i == 0):
        mdc = i

print(mdc)

