

'''
nome = input('Digite seu nome: ')
e1 = nome.find(' ')
e2 = len(nome) - 1

while (e2 >= 0) and (nome[e2] != ' '):
    e2 = e2 - 1

res = nome[:e1].upper() + nome[e1: e2 + 1] + nome[e2 + 1:].upper()
print(res)
'''

'''#Ler o nome do usuário e imprimir somente o primeiro e o ultimo nome em maiúsculas

nome = input('Digite o seu nome: ').upper()
lista = nome.split()

print(lista[0] + ' '+ lista[-1])
'''


#Ler uma lista de N numeros, e depois criar duas outras listas com os numeros pares e impares separados. No final imprimir as 3 listas

'''n = int(input("Digite um valor: "))

lista = []
listaPares = []
listaImpares = []

for i in range(n):
	num = input("Digite o valor de indice %d da lista" % i)
	lista.append(num)

for n in range(len(lista)):
	if int(lista[n])%2 == 0:
		listaPares.append(lista[n])
	else:
		listaImpares.append(lista[n])

print(lista)
print(listaPares)
print(listaImpares)'''

'''#Ler as notas de N alunos (N é informado pelo user), calcular e imprimir a média das notas e depois imprimir as notas que sejam maiores que a média calculada

n = int(input('Digite a quantidade de alunos: '))
somaNotas = 0
listaDeNotas = []

while n > 0:
    nota = float(input('Digite a nota do aluno: '))
    somaNotas += nota
    listaDeNotas += nota
    print(listaDeNotas)
    n += 1

media = somaNotas / n'''

#Solução de Alan
n = int(input("digite o tamanho da lista: "))
while (n<=0):
    n = int(input("digite um valor válido: "))

media = 0
soma = 0
lista = [None]*n
lista_maiores_notas = [None]*n
tamanho = len(lista)

for i in range (n):
    lista[i] = float(input("digite o elemento: "))
    soma += lista[i]

media = soma/n

for j in range (tamanho):
    if lista[j]>media:
        lista_maiores_notas[j] = lista[j]
print ("a média das notas é: ", media)
print ("as notas maiores que a média são: ", lista_maiores_notas)

