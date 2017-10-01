import math


class Point:

    def __init__(self, array):
        self.dimensions = array.__len__()
        if array.__len__() >= 1:
            self.x = array[0]
        if array.__len__() >= 2:
            self.y = array[1]
        if array.__len__() == 3:
            self.z = array[2]

    def oned_dist(self, other):
        if self.x >= other.x:
            return self.x - other.x
        else:
            return other.x - self.x

    def twod_dist(self, other):
        return (math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))**0.5

    def threed_dist(self, other):
        return (math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2) + math.pow(self.z - other.z, 2))**0.5

    def calc_dist(self, other):
        if self.dimensions == other.dimensions:
            if self.dimensions == 1:
                return self.oned_dist(other)
            elif self.dimensions == 2:
                return self.twod_dist(other)
            elif self.dimensions == 3:
                return self.threed_dist(other)
            else:
                return "Número de dimensões ainda não implementado"
        else:
            return "Os dois pontos devem ter o mesmo números de dimensões! \n E o máximo de dimensões é 3!"


def string_treater(string):
    str_array = string.split(',')
    float_array = []
    for x in str_array:
        try:
            float_array.append(float(x))
        except ValueError:
            print("Você só pode colocar números e o separador , --> x,y,z . Deve seguir o padrão --> x,y,z ou x,y ou x")
            return []
    return float_array


def accep_loop():
    default_message = "Insira as coordenandas do ponto no padrão x,y,z ou x,y ou x: "
    arg = string_treater(input(default_message))
    if arg:
        return arg
    else:
        return accep_loop()

while True:
    p = Point(accep_loop())
    p2 = Point(accep_loop())
    print("A distância entre os pontos é de: %.2f" % (p.calc_dist(p2)))
