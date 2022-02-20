#DECLARACIÓ DE FUNCIONS
from os import *
from time import sleep

def MenuOpcions():
    print("MENÚ D'OPCIONS:")
    print("1- VERIFICAR NOMBRES PRIMERS ")
    print("2- DIBUIXAR UN TAULELL D'ESCACS")
    print("3- CÀLCUL CONSUM")

#MAIN
MenuOpcions()
tria = input("ESCULL UNA OPCIÓ: ")
while (tria != '0'):
    if (tria == '1'):
        NombresPrimers()
    elif (tria == '2'):
        TaulellEscacs()
    elif (tria == '3'):
        CalculConsum()
    else: 
        print("ERROR, torna a intentar;")
        sleep(1)
    system('cls')
    tria = input("ESCULL UNA OPCIÓ: ")
