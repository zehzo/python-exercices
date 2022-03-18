nota1 = int(input('Digite a sua primeira nota: '))
nota2 = int(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Sua média é {:.2f}'.format(media))
if media < 5:
    print('Você foi reprovado!')
elif 5 <= media < 7:
    print('Você está em recuperação!')
else:
    print('Você foi aprovado!')
