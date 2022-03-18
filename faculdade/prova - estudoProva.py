tab = {}
qtd = 0

matricula = int(input('Digite o número da matrícula do aluno: '))
while matricula < 1:
    matricula = int(input('Digite um número válido para matrícula do aluno: '))

while matricula > 0 and qtd < 200:
    nome = str(input('Digite o nome do aluno: '))
    idade = int(input('Digite a idade do aluno: '))
    tab[matricula] = (nome, idade)
    qtd += 1
    matricula = int(input('Digite o número da matrícula do aluno: '))
print('Dados importados')
print(tab[1])

n = int(input('Digite quantas vezes você deseja ver os alunos em um intervalo de idades: '))
while n > 0:
    idadeMinima = int(input('Digite a idade mínima: '))
    idadeMaxima = int(input('Digite a idade maxima: '))
    if idadeMaxima < idadeMinima:
        print('Intervalo digitado incorretamente.')
    else:
        if tab['matricula'][1] >= idadeMinima and tab['matricula'][1] <= idadeMaxima:
