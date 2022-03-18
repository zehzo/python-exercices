
# Incompleto
termo1 = int(input('Digite o primeiro termo: '))
pa = int(input('Digite a PA: '))
resultado = termo1
total = 0
mais = 10
cont = 1

while mais != 0:
    total += mais
    while cont <= total:
        print(resultado)
        resultado += pa
        cont += 1
    mais = int(input('Quantos termos a mais você quer mostrar? '))

maistermos = int(input('Quer mostrar mais quantos termos? '))
