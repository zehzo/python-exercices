#
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))

operacao = int(input('Digite ->\n1 para somar os valores\n2 para multiplicar\n3 para mostrar o maior valor'
      '\n4 para pedir novos números\n5 para sair do programa\n'))

while operacao != 5:
    if (operacao == 1):
        resultado = valor1 + valor2
        print('A soma dos valores digitados é: {}'.format(resultado))
    if (operacao == 2):
        resultado = valor1 * valor2
        print('O produto digitado dos valores é: {}'.format(resultado))
    if operacao == 3:
        if valor1 > valor2:
            print('O maior valor digitado foi: {}'.format(valor1))
        else:
            print('O maior valor digitado foi: {}'.format(valor2))
    if operacao == 4:
        valor1 = int(input('Digite novamente um valor: '))
        valor2 = int(input('Digite novamente outro valor: '))
    operacao = int(input('Digite ->\n1 para somar os valores\n2 para multiplicar\n3 para mostrar o maior valor'
      '\n4 para pedir novos números\n5 para sair do programa\n'))
print('FIM!')



