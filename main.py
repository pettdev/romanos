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


diccionario = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        "I": 1,
}

unidades = {
    'I': 1,
    'II': 2,
    "III": 3,
    'IV': 4,
    'V': 5,
    "VI": 6,
    'VII': 7,
    'VIII': 8,
    "IX": 9
}

decenas = {
    'X': 10,
    'XX': 20,
    'XXX': 30,
    'XL': 40,
    'L': 50,
    'LX': 60,
    'LXX': 70,
    'LXXX': 80,
    'XC': 90
}

centenas = {
    'C': 100,
    'CC': 200,
    'CCC': 300,
    'CD': 400,
    'D': 500,
    'DC': 600,
    'DCC': 700,
    'DCCC': 800,
    'CM': 900
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

    return lista