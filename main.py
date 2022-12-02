'''
1 - Crea una función que pase de entero > 0 y < 4000 a romano

2 - Cualquier otra entrada debe dar error

Casos

a) 1994 -> MCMXCIV
b) 4000 -> RomanNumberError("el valor debe ser menor que 4000")
c) "unacadena" -> RomanNumberError("debe ser un entero")
d) 0 -> RomanNumberError("el valor debe ser mayor a cero")
e) -3 -> RomanNumberError("el valor debe ser mayor a cero")
f) 4.5 -> RomanNumberError("debe ser un entero")
'''


class RomanNumberError(Exception):
    pass


unidades = {
    1: 'I',
    2: 'II',
    3: "III",
    4: 'IV',
    5: 'V',
    6: "VI",
    7: 'VII',
    8: 'VIII',
    9: "IX"
}

decenas = {
    10: 'X',
    20: 'XX',
    30: 'XXX',
    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC'
}

centenas = {
    100: 'C',
    200: 'CC',
    300: 'CCC',
    400: 'CD',
    500: 'D',
    600: 'DC',
    700: 'DCC',
    800: 'DCCC',
    900: 'CM'
}

millares = {
    1000: 'M',
    2000: 'MM',
    3000: 'MMM',
    }


def romanos(num):
    num = str(num)
    lista = []
    
    if len(num) < 4:
        num = '{:0>4s}'.format(num)

    lista = list(num)

    indice = 0
    for cifra in lista:
        lista[indice] = cifra + '0' * (len(lista) - 1 - indice)
        indice += 1

    numeros_romanos = ""
    for i in range(len(lista)):
        if int(lista[i]) > 0:
            if i == 0:
                numeros_romanos += millares.get(int(lista[i]))
            elif i == 1:
                numeros_romanos += centenas.get(int(lista[i]))
            elif i == 2:
                numeros_romanos += decenas.get(int(lista[i]))
            elif i == 3:
                numeros_romanos += unidades.get(int(lista[i]))

    return numeros_romanos


