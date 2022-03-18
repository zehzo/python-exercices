'''cateto_oposto = float(input("Informe o valor do cateto oposto: "))
cateto_adjacente = float(input("Informe o valor do cateto adjacente: "))
hipotenusa = ((cateto_adjacente**2)+(cateto_oposto**2))**(1/2)
print ("A hipotenusa do triângulo com os catetos {:.1f} e {:.1f} é {:.1f}".format(cateto_oposto, cateto_adjacente, hipotenusa))'''

import math
cateto_oposto = float(input("Informe o valor do cateto oposto: "))
cateto_adjacente = float(input("Informe o valor do cateto adjacente: "))
hipotenusa = math.hypot(cateto_adjacente, cateto_oposto)
print ("A hipotenusa do triângulo com os catetos {:.1f} e {:.1f} é {:.1f}".format(cateto_oposto, cateto_adjacente, hipotenusa))





