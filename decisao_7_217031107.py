cliente_1 = tuple(
    map( float,input("Cliente, insira seu número de cadastro e o valor da compra: ").split()))
cliente_2 = tuple(
    map( float,input("Cliente, insira seu número de cadastro e o valor da compra: ").split()))
cliente_3 = tuple(
    map( float,input("Cliente, insira seu número de cadastro e o valor da compra: ").split()))

print("Os clientes pagaram juntos o total de "+str(cliente_1[1]+cliente_2[1]+cliente_3[1]))
print("Os clientes pagaram juntos em média "+str((cliente_1[1]+cliente_2[1]+cliente_3[1])/3))

more100 = []
count = 0
if cliente_1[1] > 100:
    more100.append(int(cliente_1[0]))
elif cliente_1[1] < 50:
    count += 1

if cliente_2[1] > 100:
    more100.append(int(cliente_2[0]))
elif cliente_2[1] < 50:
    count += 1

if cliente_3[1] > 100:
    more100.append(int(cliente_1[0]))
elif cliente_3[1] < 50:
    count += 1

print(str(more100)+ " pagaram mais de R$100,00 nas compras.")
print(str(count)+ " clientes pagaram menos de R$50,00 nas compras.")
