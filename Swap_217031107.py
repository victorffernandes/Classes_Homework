

try:
    x = int(input("Insira o primeiro valor: "))
    y = int(input("Insira o segundo valor: "))
    print("X: ", x, end="\n")
    print("Y: ", y)

    aux = x
    x = y
    y = aux

    print("\n")
    print("X: ", x, end="\n")
    print("Y: ", y)
except ValueError:
    print("Valor não pode ser convertido para número! Tente novamente!")
