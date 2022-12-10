from romano_class import NumeroRomano

def test_crear_funcion_entero_a_romano():
    nr = NumeroRomano(35)
    assert nr.representacion == "XXXV"

def test_crear_funcion_romano_a_entero():
    nr = NumeroRomano("CCCXXXIV")
    assert nr.valor == 334

def test_suma_romanos():
    nr1 = NumeroRomano("XX")
    nr2 = NumeroRomano(30)

    nr3 = nr1 + nr2

    assert isinstance(nr3,NumeroRomano) == True
    assert nr3.valor == 50
    assert nr3.representacion == 'L'

def test_suma_romanos_a_numero():
    nr4 = NumeroRomano("XX")
    nr5 = nr4 + 30
    
    assert isinstance(nr5,NumeroRomano) == True
    assert nr5.valor == 50
    assert nr5.representacion == 'L'

def test_resta_romanos():
    nr6 = NumeroRomano("XX")
    nr7 = NumeroRomano(5)

    nr9 = nr6 - nr7 
    
    assert isinstance(nr9,NumeroRomano) == True
    assert nr9.valor == 15
    assert nr9.representacion == 'XV'    