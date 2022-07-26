import random

def cargar():
    retun int(input("ingrese numero"))

def cargaraleatorio():
    return random.randint( 1 ,40)

def adivinanumero():
    numero= cargaraleatorio()
    esnumero= False
    while esnumero == False :
        x=cargar()
        if numero == x :
            print("has encontrdo el umero")
        elif numero > x :
            print("el numero es mayor")
        else numero < x :
            print("el numero es menor")