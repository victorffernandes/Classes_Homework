p = tuple(map(float, input("Insira as coordenadas do ponto: ").split()))

if p[0] * p[1] > 0:
    if p[0] > 0:
        print("Primeiro quadrante " + str(p[0]) + " " + str(p[1]))
    else:
        print("Terceiro quadrante " + str(p[0]) + " " + str(p[1]))
elif p[0] * p[1] < 0:
    if p[0] < 0:
        print("Segundo quadrante " + str(p[0]) + " " + str(p[1]))
    else:
        print("Quarto quadrante " + str(p[0]) + " " + str(p[1]))
else:
    if p[0] == 0 == p[1]:
        print("0 " + str(p[0]) + " " + str(p[1]))
    else:
        print("-1 " + str(p[0]) + " " + str(p[1]))
