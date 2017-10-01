try:
    t = input("Insira o tempo seguindo a notação 00:00:00 --> ")
    t = t.split(":")
    if t.__len__() != 3:
        print("Formato colocado não é compatível!")
    else:
        seconds, minutes, hours = float(t[2]), float(t[1]), float(t[0])
        print("O tempo inserido em segundos é %d " % (seconds+(minutes * 60)+(hours*60**2)))
except ValueError:
    print("O valor colocado não é um número!")
