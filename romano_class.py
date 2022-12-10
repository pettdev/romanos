from main import RomanNumberError

class NumeroRomano():

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



    def __init__(self,valor):

        if isinstance(valor,str):
            self.representacion = valor#expresiones o simbolo romanos
            self.valor = self.romano_a_entero(valor)#valores en numeros y llama a la funcion romano a entero
        elif isinstance(valor,int):
            self.valor = valor#valor en numero
            self.representacion = self.entero_a_romano(valor)#valor o simbolo romano llama a la funcion entero a romano
        else:
            raise RomanNumberError("El valor debe ser cadena o entero")

    def entero_a_romano(self,num):
        if num > 3999 or num < 0:
            raise RomanNumberError("El limite de valor es de 0 a 3999")

        num = "{:0>4d}".format(num)
        lista = list(num) 
        longitud = len(lista)
        numero_romano=""

        for i in range(longitud):       
            longitud -=1
            lista[i] += "0"*longitud        
            numero_romano += self.dic_entero_a_romano.get( int(lista[i]),'')

        return numero_romano

    def romano_a_entero(self,rom):
        valor_entero=0
        caracter_anterior=""
        cont_repes=0
        caracter_ante_anterior=""

        for caracter in rom:     
            if caracter == caracter_anterior:
                cont_repes +=1
            else:
                cont_repes =1

            if cont_repes > 3:
                raise RomanNumberError("No se puede repetir el valor más de tres veces")

            if cont_repes == 2 and caracter in "LDV":  
                raise RomanNumberError(f"No se puede repetir estos valores: L,D,V, su valor repetido es {caracter}")  
        
            if caracter_anterior and self.dic_romano_a_entero.get(caracter_anterior) < self.dic_romano_a_entero.get(caracter):
                
                if caracter_anterior == "V" or caracter_anterior=="L" or caracter_anterior=="D":
                    raise RomanNumberError(f"El simbolo romano {caracter_anterior} no se puede restar")

                if caracter not in self.restas[caracter_anterior]:
                    raise RomanNumberError(f"El simbolo romano {caracter_anterior} solo se puede restar de {self.restas[caracter_anterior][0]} y {self.restas[caracter_anterior][1]}")
            
                if caracter_anterior not in self.restas.keys():
                    raise RomanNumberError(f"El simbolo romano {caracter_anterior} no se puede restar 2")

                if caracter_anterior == caracter_ante_anterior:
                    raise RomanNumberError("Si hay repeticiones no se resta")    

                valor_entero -=  self.dic_romano_a_entero.get(caracter_anterior)*2
        
            caracter_ante_anterior = caracter_anterior
            caracter_anterior = caracter
            valor_entero += self.dic_romano_a_entero.get(caracter)

        return valor_entero


    def __repr__(self):
        return self.representacion

    def __add__(self,otro):
        if isinstance(otro,NumeroRomano):
            return NumeroRomano(self.valor+otro.valor)#recoge el valor del otro objeto en int
        elif isinstance(otro,int):
            return NumeroRomano(self.valor+otro)#recibe el valor del otro objeto 
        elif isinstance(otro,float):
            return NumeroRomano(self.valor+int(otro))

    def __sub__(self,otro):
        if isinstance(otro,NumeroRomano):
            return NumeroRomano(self.valor-otro.valor)#recoge el valor del otro objeto en int
        elif isinstance(otro,int):
            return NumeroRomano(self.valor-otro)#recibe el valor del otro objeto 
        elif isinstance(otro,float):
            return NumeroRomano(self.valor-int(otro))


"""
obj1= NumeroRomano(50)
print("valor: ",obj1.valor)
print("representacion: ",obj1.representacion) 
obj2 = NumeroRomano('XX')
print("valor: ",obj2.valor)
print("representacion: ",obj2.representacion) 
        
sumaObjetos = obj1 - obj2
print("v: ",sumaObjetos.valor)
print("r: ",sumaObjetos.representacion)
"""