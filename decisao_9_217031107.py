sig = [((20,1),(18,2)),((19,2),(20,3)),((21,3),(19,4)),
     ((20,4),(20,5)),((21,5),(20,6)),((21,6),(22,7)),
     ((23,7),(22,8)),((23,8),(22,9)),((23,9),(22,10)),
     ((23,10),(21,11)),((22,11),(21,12)),((22,12),(19,1))]

n_sig = ['Aquário','Peixes','Áries','Touro','Gêmeos',
         'Câncer', 'Leão','Virgem', 'Libra','Escorpião',
         'Sargitário','Capricórnio']

date = tuple(map(int,input("Insira o dia e o mẽs").split()))

possible_date = []
possible_sign = []

for sign in range(0,len(sig)):
    for d in sig[sign]:
        if d[1] == date[1]:
            possible_date.append(d)
            possible_sign.append(n_sig[sign])

if possible_date[0][0] >= date[0]:
    print(possible_sign[0])
else:
    print(possible_sign[1])
