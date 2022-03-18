import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tg = math.tan(math.radians(an))
print("O ângulo de {}º tem SENO: {:.2f}, COS: {:.2f}, TAN: {:.2f}.".format(an, seno, cos, tg))


