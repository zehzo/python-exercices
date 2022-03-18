
nomes = []
nota1 = []
nota2 = []
notas = [nota1, nota2]
lista = [nomes, notas]
condicao = True

while condicao == True:
    nome = str(input('Digite o nome do aluno: '))
    nomes.append(nome)
    nota_1 = float(input('Digite a primeira nota: '))
    nota1.append(nota_1)
    nota_2 = float(input('Digite a segunda nota: '))
    nota2.append(nota_2)
    print(notas)
    print(lista)
    c = input('Deseja continuar? (S ou N): ')
    if c in 'Nn':
        condicao = False

print('Programa finalizado')

for i in range(len(nomes)):
    media = (lista[1][0][i] + lista[1][1][i]) / 2
    aluno = lista[0][i]
    print('Nº: {} / Aluno: {} / Média: {}'.format(i, aluno, media))

n = int(input('Digite o número do Aluno que você deseja buscar: '))
print('As notas de {}, são {} e {}'.format(lista[0][n], lista[1][0][n], lista[1][1][n]))