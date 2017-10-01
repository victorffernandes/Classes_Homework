n = int(input("Numero lá"))

for i in range (1,n):
     a = i
     b = i + 1
     c = i + 2
     d = a * b * c
     if d == n:
         print('o número',n,'é triangular' )
     else:
         print('O número',n,'não é triangular.')
