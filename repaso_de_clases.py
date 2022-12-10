import datetime

class Persona():
    def __init__(self,nombre,email):#self seria una referencia a las variables y funciones de la misma clase
        self.nombre=nombre
        self.email=email
        self.fecha = datetime.datetime.now()

    #metodo magico para mostrar los datos de un objeto en string
    def __str__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Fecha:{self.fecha}"    

    #metodo magico para mostrar la representacion de un objeto en string
    def __repr__(self):
        return f"Nombre: {self.nombre}, Email: {self.email}, Fecha:{self.fecha}"

    #metodo magico para sumar objetos
    def __add__(self,otro):
        #return f"Nombre: {self.nombre}, Email: {self.email}, Fecha:{self.fecha} objeto de afuera: {otro.valor}"
        return f"la suma {10+otro.valor}"           

class Segundo:
    def __init__(self,valor):
        self.valor=valor

class Comida:
    def __init__(self):
        self.valor = 1991

jose = Persona("Jose","jose@email.com")
#print(str(datetime.datetime.now()))
#print(repr(datetime.datetime.now()))
saludar = Persona("rolando","rlopez@email.com")
segundo = Segundo(1988)
comida = Comida()

sumar = saludar + comida

print(sumar)