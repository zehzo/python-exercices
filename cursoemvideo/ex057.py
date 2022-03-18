#Programa que só aceita M ou F como sexo de uma pessoa
sexo = str(input('Digite o sexo (M ou F): ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo corretamente! (M ou F): ')).upper()
print(sexo)