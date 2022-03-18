termo1 = int(input('Digite o primeiro termo da PA: '))
pa = int(input('Digite a razao da PA: '))
count = 0
for c in range(termo1, (termo1 + 10 * pa), pa):
    print(termo1, end= (' '))
    termo1 += pa
    count += 1
    print(count)