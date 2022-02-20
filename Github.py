#DECLARACIÓ DE FUNCIONS
import random as rnd
from os import *
from time import sleep

def MenuOpcions():
    print("MENÚ D'OPCIONS:")
    print("0- SORTIR DEL PROGRAMA")
    print("1- VERIFICAR NOMBRES PRIMERS ")
    print("2- DIBUIXAR UN TAULELL D'ESCACS")
    print("3- CÀLCUL CONSUM")
    print("7- JOC D'ENDEVINA EL NUMERO")
    print("8- CONVERSOR FARENHEIT-CELCIUS")
    print("9- VALIDADOR DE DATA")

#Joc d'endevinar un numero amb pistes de si es mes alt o mes baix
def JocEndevinaNumero():
    numeroAleatori= rnd.randint(0, 10)

    numeroIntroduit = int(input("Introdueix un número: "))

    while numeroIntroduit != numeroAleatori:
        if numeroIntroduit > numeroAleatori:
            print("Intenta amb un nombre MÉS PETIT")
            numeroIntroduit= int(input("Introdueix un altre número: "))
        else :
            print("Intenta amb un nombre MÉS GRAN")
            numeroIntroduit= int(input("Introdueix un altre número: ")) 
    if numeroIntroduit == numeroAleatori:
        print("Has endevinat el número")

#Conversor Celcius-Farenheit
def ConversorFarenheitCelcius():
    tipus = input("Introdueixi si introduira Farenheit(f) o Celcius(c) > ")
    temperatura = int(input("introdueix la tempreratura"))
    if tipus == "f":
        temperatura = (temperatura - 32) / 1.8000
        print("La tempreratura anterior en celcius es ", temperatura)
    elif tipus == "c":
        temperatura = (temperatura * 1.8000) + 32
        print("La tempreratura anterior en farenheit es ", temperatura)
    else:
        print("Error parametre no valid")

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
    elif (tria == '4'):
        DiesPassats()
    elif (tria == '5'):
        OrdenarNumeros()
    elif (tria == '6'):
        CalculadorsBasica()
    elif (tria == '7'):
        JocEndevinaNumero()
    elif (tria == '8'):
        ConversorFarenheitCelcius()
    elif (tria == '9'):
        ValidaData()
    else: 
        print("ERROR")
        sleep(1)
        
    #RETORN AL MENÚ
    print("TORNANT AL MENÚ PRINCIPAL")
    #NETEJA DE PANTALLA
    sleep(0.7)
    system('cls')
    #TRIA D'OPCIÓ
    tria = input("ESCULL UNA OPCIÓ: ")
