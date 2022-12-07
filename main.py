'''
1-Crear una funcion que pase de entero > 0 y < 4000 a romano
2-Cualquier otra entrada debe dar error
'''
class RomanNumberError(Exception):
    pass

dic_entero_a_romano={
    1:'I',2:'II',3:'III',
    4:'IV',5:'V',6:'VI',
    7:'VII',8:'VIII',9:'IX',
    10:'X',20:'XX',30:'XXX',
    40:'XL',50:'L',60:'LX',
    70:'LXX',80:'LXXX',90:'XC',
    100:'C',200:'CC',300:'CCC',
    400:'CD',500:'D',600:'DC',
    700:'DCC',800:'DCCC',900:'CM', 
    1000:'M',2000:'MM',3000:'MMM'
}

dic_romano_a_entero={

 'I':1, 'V':5, 'X':10,'L':50, 'C':100, 'D':500, 'M':1000 , '':0
}

restas = {
    'I':('V','X'),
    'X':('L','C'),
    'C':('D','M')   
}


'''
Reglas a cumplir con romano_a_entero
- Los símbolos se suman y ordenan de mayor a menor
- Si un símbolo de menor valor antecede a uno de mayor, el de menor valor se resta al de mayor
- Solo se puede restar un símbolo de valor pequeño de cualquier símbolo de valor grande.
- Los símbolos "I", "X", "C" y "M" se pueden repetir tres veces seguidas, pero no más. (Pueden aparecer más de tres veces si no aparecen secuencialmente, como en XXXIX.) "D", "L" y "V" no se pueden repetir.

Restas:
- "I" solo se puede restar de "V" y "X".
- "X" se puede restar de "L" y "C" solamente. 
- "C" se puede restar de "D" y "M" solamente. 
- "V", "L" y "D" nunca se pueden restar.

- Si se ha producido repetición de “I”, “X” o “C” ya no pueden restarse de sus digitos respectivos. Esto IIX es incorrecto, IX es correcto
Las restas correctas solo pueden realizarse una vez
'''


def romano_a_entero(rom:str) -> int: 
    print("valor romano: ", rom)

    valor_entero = 0
    caracter_anterior = ""
    cont_repes = 0

    for caracter in rom:

        if caracter == caracter_anterior:
            if caracter_anterior == "L" or caracter_anterior == "D" or caracter_anterior == "V":
                raise RomanNumberError("No se puede repetir estos valores: L,D,V")
            cont_repes += 1
        else:
            cont_repes = 1

        if cont_repes > 3:
            raise RomanNumberError("No se puede repetir el valor más de tres veces")

        if dic_romano_a_entero.get(caracter_anterior) < dic_romano_a_entero.get(caracter):
            if caracter_anterior == "V" or caracter_anterior=="L" or caracter_anterior=="D":
                raise RomanNumberError(f"El simbolo romano {caracter_anterior} no se puede restar")
            if caracter_anterior and (caracter not in restas[caracter_anterior]):
                raise RomanNumberError(f"El simbolo romano {caracter_anterior} solo se puede restar de {restas[caracter_anterior][0]} y {restas[caracter_anterior][1]}")
         
            #if caracter_anterior not in restas.keys():
            #    raise RomanNumberError(f"El simbolo romano {caracter_anterior} no se puede restar")
            #    print("Ingresa aqui")
          
            valor_entero -=  dic_romano_a_entero.get(caracter_anterior) * 2
            
        caracter_anterior = caracter
        valor_entero += dic_romano_a_entero.get(caracter)
  
    return valor_entero


print("Romano a entero:", romano_a_entero("VX"))


def entero_a_romano(num:int) -> str:

    num = "{:0>4d}".format(num)
    lista = list(num) 
    longitud = len(lista)
    numero_romano=""

    for i in range(longitud):
        longitud -=1
        lista[i] += "0"*longitud
        numero_romano += dic_entero_a_romano.get( int(lista[i]),'')

    return numero_romano


#print("funcion en accion",entero_a_romano(336))