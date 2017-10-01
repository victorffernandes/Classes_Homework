num = input("Insira um número de 0 a 99: ")

default = 'Caractere não pode ser convertido pra número!'


def unit(x):
    return {
        '0': '',
        '1': 'um',
        '2': 'dois',
        '3': 'três',
        '4': 'quatro',
        '5': 'cinco',
        '6': 'seis',
        '7': 'sete',
        '8': 'oito',
        '9': 'nove',
    }.get(x, default)


def exceptions(x):
    return {
        '00': 'zero',
        '10': 'dez',
        '11': 'onze',
        '12': 'doze',
        '13': 'treze',
        '14': 'quatorze',
        '15': 'quinze',
        '16': 'dezesseis',
        '17': 'dezessete',
        '18': 'dezoito',
        '19': 'dezenove',
    }.get(x, False)


def dec(x):
    return {
        '0': '',
        '2': 'vinte',
        '3': 'trinta',
        '4': 'quarenta',
        '5': 'cinquenta',
        '6': 'sessenta',
        '7': 'setenta',
        '8': 'oitenta',
        '9': 'noventa',
    }.get(x, default)

if exceptions(num):
    print(exceptions(num))
else:
    if len(num) == 2:
        if num[0] == '0' or num[1] == '0':
            print(dec(num[0]) + " " + unit(num[1]))
        else:
            print(dec(num[0]) + " e " + unit(num[1]))
    elif num[0] == '0':
        print("zero")
    else:
        print(unit(num[0]))
