invest = float (input("Insira seu investimento: "))
tax = float(input("Insira a taxa em porcentagem. Ex: 20"))
tot = 0
rep = "S"
year = 1
while rep.upper()=="S":
    for i in range(0,12):
        tot += tot*(tax/100) + invest
    print("O ano é %d e o saldo do investimento é R$ %.2f" % (year, tot))
    year += 1
    rep = input("Deseja calcular mais um ano ? (S/N)")

