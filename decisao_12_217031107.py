v1 = float(input("Insira o primeiro valor: "))
v2 = float(input("Insira o segundo valor: "))
op = input("Inisira a operação +-*/  ")
def operational(o):
    return{
        '+': v1 + v2,
        '-': v1 - v2,
        '*': v1 * v2,
        '/': v1 / v2
    }.get(o, "")
print(operational(op))
