
try:
    num1 = float(input("Insira o primeiro valor: "))
    num2 = float(input("Insira o segundo valor: "))
    num3 = float(input("Insira o terceiro valor: "))
    print("A soma dos inversos é %.2f" % ((1/num1)+(1/num2)+(1/num3)))
except ValueError:
    print("Valor não pode ser convertido para número! Tente novamente!")
