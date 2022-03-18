produtos = ('Leite', 12.50, 'Pão', 5.00, 'Manteiga', 10.00)


print(f'{"Listagem de produtos":^40}')
for pos in range(len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')