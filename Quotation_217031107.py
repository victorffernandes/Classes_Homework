
try:
    brl = float(input("Insira o quanto de dinheiro você tem em reais: "))
    dollar_quotation = float(input("Insira a cotação do dolar: "))

    print("Você tem %.2f doláres!" % (brl/dollar_quotation))
except ValueError:
    print("Os valores requisitados não conseguiram ser convertidos! Tente novamente!")
