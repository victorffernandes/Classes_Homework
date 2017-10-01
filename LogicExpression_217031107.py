try:
    value = float(input("Insira um valor: "))

    print(str(10.0 <= value <= 50.0))
except ValueError:
    print("Valor inserido é inválido!")
