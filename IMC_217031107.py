
m = float(input("Insira a sua massa em kg"))
h = float(input("Insira a sua altura em m"))

imc = m/h**2

def switch(string, obj):
    for k, v in obj.items():
        if k == string:
            print(v(imc))

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Saudável")
elif imc < 29.9:
    print("Peso em excesso")
elif imc < 34.9:
    print("Obesidade em grau I")
elif imc < 39.9:
    print("Obesidade em grau II")
else:
    print("Obesidade Grau III")