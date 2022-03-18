totalemprestimo = float(input('\033[1:32mDigite o valor total do imóvel: \033[m'))
salario = float(input('\033[1:32mDigite o valor do seu salário: \033[m'))
anos = int(input('\033[1:32mEm quantos anos você pretende pagar o empréstimo? \033[m'))
mensalidade = totalemprestimo/ (anos * 12)

if mensalidade <= (salario * 0.3):
    print('\033[1:32mSeu empréstimo foi aprovado com parcelas mensais no valor de: R${:.2f}\033[m'.format(mensalidade))
else:
    print('\033[1:31mEmpréstimo negado!\033[m')


