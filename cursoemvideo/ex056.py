# Nome, idade e sexo de 4 pessoas: Média de idade, nome do homem mais velho, quantidade de mulheres com menos de 20 anos

somaIdade = 0
nomeVelho = ''
idadeAnt = 0
somaJovens = 0

for i in range (0,4):
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo (M ou F): ').upper()
    if sexo != 'M' and sexo != 'F':
        sexo = input('Digite M ou F para informar o sexo da pessoa: ')
    somaIdade += idade
    if idade >= idadeAnt:
        idadeAnt = idade
        nomeVelho = nome
    if (idade < 20) and (sexo == 'F'):
        somaJovens += 1

media = somaIdade / 4
print(f'Média das Idades: {media}, Nome do homem mais velho: {nomeVelho}, Quantidade de mulheres com menos de 20 anos: {somaJovens}')



