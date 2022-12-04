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

dict_entero_a_romano = {
    1: 'I',
    2: 'II',
    3: "III",
    4: 'IV',
    5: 'V',
    6: "VI",
    7: 'VII',
    8: 'VIII',
    9: "IX",
    10: 'X',
    20: 'XX',
    30: 'XXX',
    40: 'XL',
    50: 'L',
    60: 'LX',
    70: 'LXX',
    80: 'LXXX',
    90: 'XC',
    100: 'C',
    200: 'CC',
    300: 'CCC',
    400: 'CD',
    500: 'D',
    600: 'DC',
    700: 'DCC',
    800: 'DCCC',
    900: 'CM',
    1000: 'M',
    2000: 'MM',
    3000: 'MMM',
}

dict_romano_a_entero = {
    'I': 1,
    'II': 2,
    "III": 3,
    'IV': 4,
    'V': 5,
    "VI": 6,
    'VII': 7,
    'VIII': 8,
    "IX": 9,
    'X': 10,
    'XX': 20,
    'XXX': 30,
    'XL': 40,
    'L': 50,
    'LX': 60,
    'LXX': 70,
    'LXXX': 80,
    'XC': 90,
    'C': 100,
    'CC': 200,
    'CCC': 300,
    'CD': 400,
    'D': 500,
    'DC': 600,
    'DCC': 700,
    'DCCC': 800,
    'CM': 900,
    'M': 1000,
    'MM': 2000,
    'MMM': 3000,
}


def entero_a_romanos(num: int) -> str:
    num = '{:0>4d}'.format(num)
    lista = list(num)
    longitud = len(lista)
    numeros_romanos = ""

    for i in range(longitud):

        longitud -= 1
        lista[i] += '0' * longitud

        numeros_romanos += dict_entero_a_romano.get(int(lista[i]), '')

    return numeros_romanos


def romano_a_entero(rom:str)->int: #M < D->C->C->X->I->I->I
    print("valor romano: ",rom)
    lista = list(rom)  # convertirmos en lista el romano recibido #['M','D','C','C','X','I','I','I']
    print("lista romano: ",lista)
    
    valor_entero=0

    for i in rom:
  
        #if i != len(lista)-1:
            """
            if dic_romano_a_entero.get(lista[i]) < dic_romano_a_entero.get(lista[i+1]):
                # si es I and V  or I and X
                #   restar si
                #  
                valor_entero += dic_romano_a_entero.get(lista[i+1]) - dic_romano_a_entero.get(lista[i])
            else:
                valor_entero +=dic_romano_a_entero.get(lista[i])    
            """
            valor_entero +=dict_romano_a_entero.get(i) 
    return valor_entero
    
print("Romano a entero: ",romano_a_entero("MDCCXIII"))#MMXIX
