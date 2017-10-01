

try:
    celsius = float(input("Insira a temperatura em Celsius: "))
    print("Essa temperatura corresponde a %.2f Fahreinheit" % (celsius * 9/5 + 32))
except ValueError:
    print("Valor não pode ser convertido para número! Tente novamente!")
