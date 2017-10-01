number = input("Insira o número")


def unit(num):
    return{
        '1': 'I',
        '2': 'II',
        '3': 'III',
        '4': 'IV',
        '5': 'V',
        '6': 'VI',
        '7': 'VII',
        '8': 'VIII',
        '9': 'IX',
    }.get(num, "")


def dec(num):
    return{
        '1': 'X',
        '2': 'XX',
        '3': 'XXX',
        '4': 'XL',
        '5': 'L',
        '6': 'lX',
        '7': 'lXX',
        '8': 'LXXX',
        '9': 'XC',
    }.get(num, "")


def cent(num):
    return{
        '1': 'C',
        '2': 'CC',
        '3': 'CCC',
        '4': 'CD',
        '5': 'D',
        '6': 'DC',
        '7': 'DCC',
        '8': 'DCCC',
        '9': 'CM',
    }.get(num, "")


def mil(num):
    return{
        '1': 'M',
        '2': 'MM',
        '3': 'MMM'
    }.get(num, "")

defs = [mil, cent, dec, unit]
result = ''
for i in range(0, len(number)):
    result += defs[i](number[i])
print(result)
