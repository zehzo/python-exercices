palavras = ('alo', 'maca', 'banana', 'teste')
contador = 0


for palavra in palavras:
    print('As vogais da palavra {} são: '.format(palavra.upper()))
    for letra in palavra:
        if letra in 'aeiou':
            print(f'{letra} ')
