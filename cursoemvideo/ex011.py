largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = altura * largura
tintas = (area //2)
print('A parede de {:.2f}m x {:.2f}m tem {:.2f}m² de área e serão necessários {:.1f} baldes de tinta para pintá-la'.format(largura, altura, area, tintas))