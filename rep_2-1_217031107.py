n = int (input("Insira o número: "))
isTri = False
i = 2
while  i < (n//2)+1 and  isTri == False:
    if n == ((i-1) * i * (i+1)):
        isTri = True
    i+= 1
print(isTri)

'''   
for i in range(2, n):
    if n == ((i-1) * i * (i+1)):
        isTri = True
print(isTri)'''

