#Número Primo

n = int(input('Digite um numero: '))
count = 0
div = 2
for c in range(div, n, 1):
    if n % div == 0:
        count += 1
        print(div, end=':')
    div += 1
if count >= 1:
    print('O numero não é primo!')
else:
    print('O número é primo!')


