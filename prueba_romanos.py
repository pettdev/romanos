from romano_class import NumeroRomano


continuar=True
deseo=True
valor=''

while continuar:

    operacion = input("Convertir Entero a Romano:ingrese X\nConvertir Romano a Entero:ingrese Y: ")


    if operacion == 'X':
            valor = int(input("por favor ingrese valor numerico: "))

            obj = NumeroRomano(valor)
            print(f"El valor de {obj.valor} es igual a {obj.representacion} ")

    elif operacion =='Y':
            valor = input("por favor ingrese valor romano: ")

            obj = NumeroRomano(valor)
            print(f"El valor de {obj.valor} es igual a {obj.representacion} ")

    else:
            print("Ingrese X o Y por favor")

    v = input("Deseas continuar s/n")
    if v == "n" :
        continuar=False
        print("Fin del programa")