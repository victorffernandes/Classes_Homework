n = int(input("Insira o número de números perfeitos: "))
sum = 0
count = 0
actual = 1

while count < n:
    for i in range(1,(actual//2)+1):
        if actual % i == 0:
            sum += i
    if actual == sum:
        print(actual)
        count += 1
    actual += 1
    sum = 0
