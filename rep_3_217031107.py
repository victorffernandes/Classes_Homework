num = int(input("Insira o número: "))

actual = 0
previous = 0
result = ''
count = 0
while(count != num+1 ):
    if count == 0:
        result +=str(actual+previous)+' ,'
        previous = 0
        actual = 1
    elif count == 1:
        result +=str(actual+previous)+' ,'
    else:
        result += str(actual+previous)+", "

        temp = previous
        previous = actual
        actual = actual+temp
    count+=1
print(result)