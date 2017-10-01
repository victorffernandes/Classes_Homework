

#while True:
try:
    r = float(input("Insira o raio da circunferência: "))
    print("O perímetro da circunferência é %.2f" % (2 * 3.14 * r))
except ValueError:
    print("Valor inválido!")
