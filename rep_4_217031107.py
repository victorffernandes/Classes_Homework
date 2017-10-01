restart = 'y'
while(restart=='y'):
    num = int(input("Insira o número: "))
    result = ''
    count = 0
    for i in range(1,(num//2)+1):
        if(num%i == 0):
            result += " %d" % i
            count += 1
    if count == 1:
        print("O número informado é primo")
    else:
        print(result)
    restart = input("Deseja analisar outro número? (y/n)")