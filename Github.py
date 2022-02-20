from tkinter import *
def MenuOpcions():
    print("MENÚ D'OPCIONS:")
    print("1- VERIFICAR NOMBRES PRIMERS ")
    print("2- DIBUIXAR UN TAULELL D'ESCACS")
    print("3- CÀLCUL CONSUM")

def NombresPrimers():
    print("EXECUTANT VERIFICADOR DE NOBRES PRIMERS:")
    primer = True
    divisor = 2

            
    numero = int(input("ENTRA UN NOMBRE"))
    numero = int(numero)
    while divisor < numero:
        if ((numero % divisor) == 0):primer = False
        divisor = divisor + 1

    if primer == True:print("EL NOMBRE ",numero," ÉS PRIMER")
    else:print("EL NOMBRE ",numero," NO ÉS PRIMER")