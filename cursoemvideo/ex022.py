nome = input("Digite o seu nome: ")

print('Maiúsculo: {}' .format(nome.upper()))
print('Minúsculo: {}' .format(nome.lower()))
print('Quantidade de caracteres: {}' .format(len(''.join(nome.split()))))
print('Quantidade de caracteres do primeiro nome: {}'.format(len(nome.split()[0])))

