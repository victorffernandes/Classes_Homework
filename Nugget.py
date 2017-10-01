num = int(input("Nuggets: "))
keep = True


while keep:
    for i in range(0,(num//6)+1):
        for j in range(0, (num//9)+1):
            for n in range (0,(num//20)+ 1):
                if i * 6 + j * 9 + n * 20 == num:
                    keep = False
                    print("%d pacotes de 6, %d pacotes de 9, %d pacotes de 20" % (i,j,n))
