numero = int(input('Digite um número entre 0 e 20: '))
tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
         'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while 0 > numero or numero > 20:
    print('O valor digitado não pertence ao intervalo 0 - 20')
    numero = int(input('Digite um número entre 0 e 20: '))
for pos, num in enumerate(tupla):
    if numero == pos:
        print('O valor digitado foi {}'.format(num))
