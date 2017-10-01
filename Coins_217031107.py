
coins_values = [100, 50, 25, 10, 5, 1]
coins_count = []
value = int(input("Insira o valor em centavos: "))

for x in range(0, coins_values.__len__()):
    if value % coins_values[x] == 0:
        coins_count.append(value/coins_values[x])
        break
    elif value % coins_values[x] != 0:
        coins_count.append(value//coins_values[x])
        value = value % coins_values[x]

coins_names = ["100", "50", "25", "10", "5", "1"]
for i in range(0, coins_count.__len__()):
    print("%s centavos --> %.2f moedas" % (coins_names[i], coins_count[i]))
