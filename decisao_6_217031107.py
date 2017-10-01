print("Celsius para Fahrenheit(1)    Fahrenheit para Celsius(2)    Milimetro para Polegadas(3)    Polegada para Milimetro(4)")

operation = input("Insira a operação desejada (1 ou 2 ou 3 ou 4)")
value = float(input("Insira o valor para realizar a operação: "))

def op_r(op):
    return{
        '1': (9/5)*value + 32,
        '2': 5/9*(value -32),
        '3': value/25.4,
        '4': value * 24.4
    }.get(op, "Operação não existente")

print(op_r(operation))
