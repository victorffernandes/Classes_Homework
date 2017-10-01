
try:
    name = input("Insira o nome do produto: ")
    qunt = int(input("Insira a quantidade comprada: "))
    value = float(input("Insira o valor da unidade: "))
    percent = float(input("Insira a porcentagem do desconto (entre 0 e 100): "))

    print("Você comprou %s e gastou R$%.2f " % (name, qunt*value*(percent/100)))
except ValueError:
    print("Os valores requisitados não conseguiram ser convertidos! Tente novamente!")
