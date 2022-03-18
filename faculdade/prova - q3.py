'''
matricula = []
nome = []
idade = []
tabela = {'matricula': matricula ,'nome': nome , 'idade': idade}
nMatricula = 1
contador = 1

while nMatricula > 0 and contador <= 200:
    nMatricula = int(input('Digite o número da matrícula: '))
    if nMatricula > 0:
        tabela['matricula'].append(nMatricula)
        nomeAluno = str(input('Digite o nome do aluno: '))
        tabela['nome'].append(nomeAluno)
        idadeAluno = int(input('Digite a idade do aluno: '))
        tabela['idade'].append(idadeAluno)

print(tabela)
idadeMinima = int(input('Digite um valor de idade mínima para buscar: '))
idadeMaxima = int(input('Digite um valor de idade máxima para buscar: '))

for i in tabela['nome']:
    print(tabela[i])
'''

'''tabela = {}
max = 0

matricula = int(input("digite a matricula: "))
while matricula > 0 and max < 200:
    nome = input("digite o nome: ")
    idade = int(input("digite a idade: "))
    tabela[matricula]  = (nome, idade)
    matricula = int(input("digite a matricula: "))

n = int(input("digite um valor para n: "))
while n < 0:
    n = int(input("digite um valor para n: "))

for vezes in range(n):
    idade_minima = int(input("digite a idade minima: "))
    idade_maxima = int(input("digite a idade máxima: "))
    if idade_minima > idade_maxima:
        print("ERRO")

    quantidade_intervalo = 0
    for codigo in tabela:
        if idade_minima <= tabela[codigo][1] <= idade_maxima:
                print(tabela[codigo])
                quantidade_intervalo += 1
    print(f"{quantidade_intervalo} pessoa(s) nesse intervalo")'''

tab = {}
qtd = 0
matr = int(input("Digite a matrícula do aluno: "))
while matr <= 0 :
    matr = int(input("Digite pelo menos uma matrícula válida: "))
while (matr > 0) and (qtd < 200) :
    qtd = qtd + 1
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    tab[matr] = (nome, idade)
    matr = int(input("Digite outra matricula, <=0 para parar: "))
if matr > 0 :
    print("Quantidade máxima de alunos atingida, último valor foi descartado!")

n = int(input("Digite o número de consultas: "))
while n <= 0 :
    n = int(input("O número de consultas deve ser positivo: "))

for i in range(n) :
    idadeMin = int(input("Digite a idade mínima desejada: "))
    idadeMax = int(input("Digite a idade máxima desejada: "))
    if (idadeMin < 1) or (idadeMin > idadeMax) :
        print("Intervalo inválido, descartado!")
    else:
        qtd = 0
for matr in tab :
    if (idadeMin <= tab[matr][1]) and ( tab[matr][1] <= idadeMax) :
        print("Aluno", matr, tab[matr])
        qtd = qtd + 1
    if qtd > 0 :
        print("Selecionado(s)", qtd, "aluno(s) nesse intervalo.")
    else:
        print("Não existe nenhum aluno neste intervalo.")