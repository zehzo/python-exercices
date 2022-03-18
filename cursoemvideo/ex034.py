salario = float(input("Digite o valor do seu salário: "))
aumento = salario * 1.1 if salario >= 1250 else salario * 1.15
print('O novo valor do seu salário é de R${:.2f}'.format(aumento))