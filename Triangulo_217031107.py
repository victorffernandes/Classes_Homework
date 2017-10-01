p1 = tuple( map(int,input("Insira as coordenadas do ponto 1: ").split()))
p2 = tuple(map(int,input("Insira as coordenadas do ponto 2: ").split()))
p3 = tuple(map(int,input("Insira as coordenadas do ponto 3: ").split()))

dist = lambda p_1, p_2: ((p_1[0] - p_2[0])**2 + (p_1[1] - p_2[1])**2)**0.5

l = [dist(p1,p2), dist(p1,p3), dist(p2,p3)]

if l[0] + l[1] > l[2]:
    print("Esse triângulo existe!")
    if l[0] == l[1] == l[2]:
        print("\n e é um equilátero!")
    elif l[0] != l[1] != l[2]:
        print("\n e é um escaleno!")
    else:
        print("\n e é um isósceles!")
else:
    print("Esse triãngulo não existe! :(")
