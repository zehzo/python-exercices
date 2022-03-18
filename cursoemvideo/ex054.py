#Ano de nascimento de 7 pessoas

anoAtual = 2020
menor = maior = 0

for i in range(0,7):
    ano = int(input('Digite o ano de nascimento: '))
    if anoAtual - ano >= 21:
        maior += 1
    else:
        menor += 1
print(f'No total {maior} são maiores de idade e {menor} são menores de idade.')

